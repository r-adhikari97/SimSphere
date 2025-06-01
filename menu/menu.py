import pygame
from pathlib import Path
from models.model import SphereBuilder
from models.data_structure import LinkedList
from constants.constant import *

class SelectionMenu:
    """
    Selection menu for the users to choose items from
    - tenis ball
    - bowling ball
    """

    def __init__(self):
        ## MENU POSITIONING
        self.x = OUTER_BOX_POSITION[0]
        self.y = OUTER_BOX_POSITION[1]
        self.width = OUTER_BOX_DIMENSIONS[0]
        self.height = OUTER_BOX_DIMENSIONS[1]
        self.color = DEFAULT_COLOR

        ## Sphere object Management
        self.sphere_list = self.__get_items()
        self.current_object = self.sphere_list.head_node

        ## FONT management
        self.menu_font = pygame.font.SysFont(r'sphere_simulations\constants\fonts\Bangers-Regular.ttf', 40)
        self.general_font = pygame.font.SysFont(r'sphere_simulations\constants\fonts\Bangers-Regular.ttf', 28)
        self.text_font = pygame.font.SysFont(r'sphere_simulations\constants\fonts\Bangers-Regular.ttf', 20)

    def __get_items(self):
        """
        Method to extract all items from items json to add it to linkedlist and returns latest node
        """
        Sphere_list = LinkedList()

        for ball in BALL_META.keys():
            #print(f"ball: {ball}")
            #print(f"IMG URL : {BALL_META[ball]['image']}")
            spb = SphereBuilder()
            sphere = spb.addName(object_name=BALL_META[ball]['display_name']).addImage(image_url=BALL_META[ball]['image']).build()
            #print(f"SPHERE: {sphere}")
            Sphere_list.add(value=sphere)

        print(Sphere_list)
        return Sphere_list
    

    def draw(self, surface):
        """
        Draws the whole menu onto the screen
        """
        ## CONTAINER : to hold the menu
        border_rect = pygame.Rect(self.x-1, self.y-1, self.width+2, self.height+2)
        pygame.draw.rect(surface=surface, color=(0,0,0), rect=border_rect)

        inner_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, self.color, inner_rect) 

        ## TEXT : Main
        text_surface = self.menu_font.render("Sphere Simulator!", True, (50,50,50))
        surface.blit(text_surface, (inner_rect.x+25, inner_rect.y+10 ))

        ## Text Box: H2
        text_surface = self.general_font.render("Choose object", True, (50,50,50))
        surface.blit(text_surface, (inner_rect.x+75, inner_rect.y+50))

        ## IMAGE : ball
        #print(f"IMG: {self.current_object.value.image}"
        ball_coord_x = inner_rect.x+125
        ball_coord_y = inner_rect.y+85

        self.image_rect = pygame.Rect(ball_coord_x, ball_coord_y, 50,50)

        ball_image = pygame.image.load(self.current_object.value.image).convert_alpha()
        ball_image = pygame.transform.scale(ball_image, (50, 50))
        surface.blit(ball_image,(ball_coord_x, ball_coord_y))
        #pygame.draw.rect(surface, (255, 0, 0), self.image_rect, 2)

    
        ## TEXT : Ball name
        text_surface = self.text_font.render(self.current_object.value.name, True, (50,50,50))
        surface.blit(text_surface, (inner_rect.x+115, inner_rect.y+140))