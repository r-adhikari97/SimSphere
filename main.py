import sys
import pygame
from constants.constant import *
from models.model import SphereBuilder
from menu.menu import SelectionMenu



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

        ## SPHERE SETTINGS
        self.sphere = SphereBuilder().rubber_ball()


    
    def run_simulator(self):
        """
        Main function/ Method responsible for running simulator
        """
        while self.state:
            #self.screen.fill(DEFAULT_COLOR)
            """
            User input evdnt loop
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            """
            Object Motion and Management Section
            """
            self.selection_menu.draw(surface=self.screen)
            self.sphere.draw(screen=self.screen)

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