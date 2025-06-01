"""
Models represent different sphere objects for the user to choose from
Options
1. Plastic ball
2. Rubber ball
3. Tennis Ball
4. Steel Ball
"""

import pygame
from constants.constant import *

class Sphere:
    """
    Sphere Class
    """
    def __init__(self, radius:int=20, weight:int=10, x:int=100,y:int=100, color=(255,0,0)):
        self.x = x
        self.y = y
        self.name = None 
        self.radius = radius
        self.color = color
        self.weight = weight
        self.image = None


    def __repr__(self):
        return f"Sphere(name={self.name}, image={self.image}, weight={self.weight}, radius={self.radius})"

    ## SETTERS
    def set_radius(self, radius:int):
        self.radius = radius

    def set_weight(self, weight:int):
        self.weight = weight

    def set_image(self, image_url:str):
        """
        Converts image_url to a surface object
        """
        self.image = image_url

    def set_color(self, object_color:tuple):
        self.color = object_color

    def set_name(self, object_name:str):
        self.name = object_name

    ## ACTION
    def draw(self, screen):
        """
        Draws the sphere surface on surface
        """
        if self.image:
            image = pygame.image.load(self.image)
            screen.blit(image, (self.x, self.y))
        else:
            pygame.draw.circle(surface=screen, color=self.color, center=(self.x, self.y), radius=self.radius)




class SphereBuilder:
    """
    SphereBuilder class is responsible for building custom spheres on basis of attributes provided
    """
    def __init__(self):
        self.sphere = Sphere()

    ## BASE METHODS
    def addName(self, object_name:str):
        self.sphere.set_name(object_name=object_name)
        return self 

    def addWeight(self, weight:int):
        self.sphere.set_weight(weight=weight)
        return self 
    
    def addRadius(self, radius:int):
        self.sphere.set_radius(radius=radius)
        return self

    def addImage(self, image_url:str):
        self.sphere.set_image(image_url=image_url)
        return self
    
    def addColor(self, object_color:tuple):
        self.sphere.set_color(object_color=object_color)
        return self
    
    def build(self):
        return self.sphere
