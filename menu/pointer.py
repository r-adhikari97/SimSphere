import pygame


class CustomCursor:
    """
    Class For handling Mouse Pointer behaviours
    """
    def __init__(self):
        self.size = (30,30)
        self.image = None

    def set_image(self, image_urL:str):
        """
        Responsible for setting image 
        """
        self.image = pygame.image.load(image_urL).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)


    def draw(self, surface):
        """
        Draws customer pointer object
        """
        ## Phase 1: clsoe mouse pointer
        pygame.mouse.set_visible(False)

        ## Phase 2: Extract x and y for mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        ## Phase 3: Draw the image
        surface.blit(self.image, (mouse_x+15, mouse_y+15))