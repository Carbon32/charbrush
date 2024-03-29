# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                           #
#                    Python Pixel Editor                    #
#                     Developer: Carbon                     #
#                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Imports: #

from src.modules import *

# Buttons: #

class Button():
    def __init__(self, editor, text, x, y, width, height, elevation):

        # Editor:

        self.editor = editor

        # Top Rectangle:

        self.top_rect = pygame.Rect((x, y), (width, height))
        self.original_top_rect_y = y
        self.top_color = (203, 92, 100)

        # Bottom Rectangle:

        self.bottom_rect = pygame.Rect((x, y), (width, height))
        self.bottom_color = (160, 68, 93)

        # Properties:

        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.clicked = False
        self.action = False
        self.button_cooldown = 100
        self.button_timer = pygame.time.get_ticks()
        self.click_time = pygame.time.get_ticks()

        # Text:

        self.text_surface = self.editor.font.render(text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

    def render(self):
        self.top_rect.y = self.original_top_rect_y - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        pygame.draw.rect(self.editor.board, self.bottom_color, self.bottom_rect, border_radius = self.editor.board_width // 16)
        pygame.draw.rect(self.editor.board, self.top_color, self.top_rect, border_radius = self.editor.board_width // 16)
        self.editor.board.blit(self.text_surface, self.text_rect)
        position = pygame.mouse.get_pos()
        position = pygame.mouse.get_pos()
        ratio_x = (self.editor.screen_width / self.editor.board_width)
        ratio_y = (self.editor.screen_height / self.editor.board_height)
        position = (position[0] / ratio_x, position[1] / ratio_y)
        if(not self.action):
            if self.top_rect.collidepoint(position):
                self.top_color = (215, 75, 75)
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    if(pygame.time.get_ticks() - self.button_timer >= self.button_cooldown):
                        self.dynamic_elevation = 0
                        self.action = True
                        self.clicked = True
                        self.button_timer = pygame.time.get_ticks()
            else:
                self.top_color = (203, 92, 100)
                self.bottom_color = (160, 68, 93)

        if pygame.mouse.get_pressed()[0] == 0:
            self.dynamic_elevation = self.elevation
            if(self.clicked):
                self.click_time = pygame.time.get_ticks()

            self.clicked = False
            if(self.action):
                if(pygame.time.get_ticks() - self.click_time > 100):
                    self.action = False
                    return True

    def change_color(self, first_color, second_color):
        self.top_color = first_color
        self.bottom_color = second_color