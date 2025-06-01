import sys
import pygame
from constants.constant import *
from menu.menu import SelectionMenu
from menu.pointer import CustomCursor



class SphereSimulator:
    """
    Class responsible for managing game state
    """
    simulation_instance = None

    def __init__(self):
        pygame.init()

        ## SIMULATOR STATE
        self.state = True

        ## SCREEN SETTINGS
        pygame.display.set_caption("Sphere Simulator!")
        self.screen = pygame.display.set_mode(SIMULATOR_SCREEN_SIZE)
        self.screen.fill(DEFAULT_COLOR)
        # TODO : Add a custom screen manager to update backgrounds

        ## CLOCK OBJECT for FPS
        self.clock = pygame.time.Clock()

        ## MENU SETTINGS
        self.selection_menu = SelectionMenu()

        ## CUSTOM CURSOR SETTIBGS
        self.cursor = CustomCursor()
        self.cursor.set_image(image_urL=self.selection_menu.current_object.value.image)

    
    def run_simulator(self):
        """
        Main function/ Method responsible for running simulator
        """
        while self.state:
            self.screen.fill(DEFAULT_COLOR)
            """
            Object Motion and Management Section
            """
            self.selection_menu.draw(surface=self.screen)
            self.cursor.draw(surface=self.screen)
            #self.sphere.draw(screen=self.screen)


            """
            User input evdnt loop
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    adjusted_pos = (event.pos[0] + 15, event.pos[1] + 15)

                    ## Checking if Mouse clicked the Object ---> change object
                    if self.selection_menu.image_rect.collidepoint(adjusted_pos):
                        print("COLLIDED")
                        if self.selection_menu.current_object.next_node is None:
                            self.selection_menu.current_object = self.selection_menu.sphere_list.head_node
                        else:
                            self.selection_menu.current_object = self.selection_menu.current_object.next_node

                        self.cursor.set_image(image_urL=self.selection_menu.current_object.value.image)

                    else:
                        mouse_x, mouse_y = (event.pos[0], event.pos[1])
                        print(f"CURRENTLY PRESSED AT : {mouse_x, mouse_y}")
                        


                    

            pygame.display.update()
            self.clock.tick(60)


    

    @staticmethod
    def get_state():
        if SphereSimulator.simulation_instance is None:
            SphereSimulator.simulation_instance = SphereSimulator()
        return SphereSimulator.simulation_instance
    


## DRIVER ##
simulator = SphereSimulator().get_state()
simulator.run_simulator()