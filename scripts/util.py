

import pygame
import os

# Automatically get base directory
BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "images")

def load_image(image_path):
    """Loads a single image from the data/images directory."""
    full_path = os.path.join(BASE_PATH, image_path)
    print('one')
    print(os.path.exists(full_path))
    if not os.path.isfile(full_path):
        print(f"File not found: {full_path}")
        return None
    return pygame.image.load(full_path).convert_alpha()

def load_images(folder_name):
    """Loads all images from a folder inside data/images and returns a list."""
    full_path = os.path.join(BASE_PATH, folder_name)
    
    if not os.path.isdir(full_path):
        print(f"Directory not found: {full_path}")
        return []
    
    images = []
    for image_file in sorted(os.listdir(full_path)):
        if image_file.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder_name, image_file)
            image_surface = load_image(image_path)
            if image_surface:
                images.append(image_surface)

    return images

