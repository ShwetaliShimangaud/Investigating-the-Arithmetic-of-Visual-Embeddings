import torch
import clip

from PIL import Image
import os

device = "cuda" if torch.cuda.is_available() else "cpu"


def get_image_embedding(image):
    preprocessed_image = preprocess(image).unsqueeze(0).to(device)
    with torch.no_grad():
        image_features = model.encode_image(preprocessed_image)
        return image_features


def get_images_from_folder(folder_path):
    images = []

    for filename in os.listdir(folder_path):
        # Check if the file is an image file
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            # Open the image using PIL
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            # Append the image to the list
            images.append(get_image_embedding(image))

    return images


model, preprocess = clip.load("ViT-B/32", device=device)
crown_image_embeddings = get_images_from_folder("Dataset/GoldRatings-10a/crown_royalty__smoke_fire__/crown")
print(crown_image_embeddings)