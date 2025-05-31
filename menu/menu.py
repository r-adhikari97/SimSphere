import pygame
from constants.constant import *

class SelectionMenu:
    """
    Selection Menu class allowing to choose from options
    """
    def __init__(self):
        self.x = 850
        self.y = 10
        self.width = 300
        self.height = 400
        self.color = DEFAULT_COLOR
        self.menu_font = pygame.font.SysFont(r'sphere_simulations\constants\fonts\Bangers-Regular.ttf', 40)
        self.general_font = pygame.font.SysFont(r'sphere_simulations\constants\fonts\Bangers-Regular.ttf', 28)
        self.text_font = pygame.font.SysFont(r'sphere_simulations\constants\fonts\Bangers-Regular.ttf', 20)

    def draw(self, surface):

        ## Menu Box (Outer: Border + Inner:Main Menu)
        border_rect = pygame.Rect(self.x-1, self.y-1, self.width+2, self.height+2)
        pygame.draw.rect(surface, (0, 0, 0), border_rect) 

        inner_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, self.color, inner_rect) 

        ## Text Box: TITLE
        text_surface = self.menu_font.render("Sphere Simulator!", True, (50,50,50))
        surface.blit(text_surface, (inner_rect.x+25, inner_rect.y+10 ))

        ## Text Box: H2
        text_surface = self.general_font.render("Choose object", True, (50,50,50))
        surface.blit(text_surface, (inner_rect.x+75, inner_rect.y+50))

        ## Image Box : Ball/Sphere
        ball_image = pygame.image.load(BALL_META['tennis_ball']['image']).convert_alpha()
        ball_image = pygame.transform.scale(ball_image,(50,50))
        surface.blit(ball_image, (inner_rect.x+125, inner_rect.y+85))

        ## Text Box : H3
        text_surface = self.text_font.render("tennis ball", True, (50,50,50))
        surface.blit(text_surface, (inner_rect.x+115, inner_rect.y+140))


