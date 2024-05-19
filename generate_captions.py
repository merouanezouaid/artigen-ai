# !pip install transformers

from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer


feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

from PIL import Image
import clip
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
clip_model, preprocess = clip.load("ViT-B/32", device=device)

image = Image.open("data/thuya.jpeg")
pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
output_ids = model.generate(pixel_values, max_length=50, num_beams=4, early_stopping=True)
captions = tokenizer.batch_decode(output_ids, skip_special_tokens=True)

image = preprocess(image).unsqueeze(0).to(device)
with torch.no_grad():
    image_features = clip_model.encode_image(image)

text_inputs = torch.cat([clip.tokenize(caption).to(device) for caption in captions]).to(device)
with torch.no_grad():
    text_features = clip_model.encode_text(text_inputs)

similarity_scores = image_features @ text_features.T
best_caption_idx = similarity_scores.argmax().item()
product_description = captions[best_caption_idx]
print(product_description)