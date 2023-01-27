# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                           #
#                    Python Pixel Editor                    #
#                     Developer: Carbon                     #
#                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Imports: #

try:
    import pygame
    import random
    import os
    import numpy
    import PySimpleGUI

except ImportError:
    raise ImportError("Pixel Editor couldn't import all of the necessary packages.")

# Pygame Initialization: #

pygame.init()
