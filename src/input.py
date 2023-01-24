# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                           #
#                    Python Pixel Editor                    #
#                     Developer: Carbon                     #
#                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Imports: #

from src.modules import *

# Input: #

class Input():
    def __init__(self, editor, x, y, width, height):

        # Editor:

        self.editor = editor

        # Text Input: 

        self.input_zone = pygame.Rect(x, y, width, height)
        self.written_text = "Untitled"

        # Properties:

        self.active = False
        self.rect_colors = [(59, 61, 71), (176, 177, 181)]
        self.text_colors = [(255, 255, 255), (0, 0, 0)]

        # Keys Timer:

        self.keys_timer = pygame.time.get_ticks()
        self.keys_cooldown = 50

    def render(self):
        pygame.draw.rect(self.editor.board, self.rect_colors[self.active], self.input_zone, border_radius = self.editor.board_width // 64)
        pygame.draw.rect(self.editor.board, (0, 0, 0), self.input_zone, self.editor.board_width // 128, border_radius = self.editor.board_width // 64)
        self.text_surface = self.editor.font.render(self.written_text, True, self.text_colors[self.active])
        self.editor.board.blit(self.text_surface, (self.input_zone.x + 30, self.input_zone.y + 35))

    def write(self, event):
        if(self.active and len(self.written_text) < 16):
            if(event.type == pygame.KEYDOWN):
                if event.key == pygame.K_BACKSPACE:
                    self.written_text = self.written_text[:-1]
  
                else:
                    self.written_text += event.unicode

    def check_for_collision(self):
        if(pygame.mouse.get_pressed()[0]):
            position = self.editor.get_proper_mouse_position()
            if(self.input_zone.collidepoint(position)):
                self.active = True
            else:
                self.active = False

    def update(self):
        self.render()
        self.check_for_collision()