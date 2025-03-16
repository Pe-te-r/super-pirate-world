import pygame
from os import path,listdir


BASE_PATH='/data/images'


def load_image(path_):
    full_path=path.join(BASE_PATH,path_)
    if path.isfile(full_path):
        return pygame.image.load(path.join(BASE_PATH,path_)).convert()


def load_images(path_):
    full_path= path.join(BASE_PATH,path_)
    if path.isdir(full_path):
        for image in listdir():
            print(image)