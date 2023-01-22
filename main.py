# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                           #
#                    Python Pixel Editor                    #
#                     Developer: Carbon                     #
#                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Imports: #

import pygame
import random

# Editor: #

class Editor():
    def __init__(self, init_screen_width, init_screen_height, board_width, board_height):

        # Properties:

        self.screen_width, self.screen_height = init_screen_width, init_screen_height
        self.board_width, self.board_height = board_width, board_height
        self.window_running = True
        self.fps_handler = pygame.time.Clock()

        # Board Properties:

        self.rows = self.board_width // 16
        self.columns = self.board_width // 16
        self.pixel_size = (self.board_width // self.columns)

        # Grid Properties:

        self.grid = []
        self.grid_ready = False

        # Color Properties:

        self.color_picker_rectangle = pygame.Rect(self.board_width // 16, self.board_height - (self.board_height // 6), self.board_width // 4.6, self.board_height // 16)
        self.color_picker_image = pygame.Surface((self.board_width // 3, self.board_height // 16))
        self.color_picker_image.fill((40, 42, 53))
        self.rad = (self.board_height // 16) // 2
        self.color_length = (self.board_width // 4) - self.rad * 4
        self.color = 0.5

        for i in range(self.color_length):
            color = pygame.Color(0)
            color.hsla = (int(360 * i / self.color_length), 100, 50, 100)
            pygame.draw.rect(self.color_picker_image, color, (i + self.rad -  int(self.board_width / self.board_height) * 16, (self.board_height // 16) // 3, int(self.board_width / self.board_height) * 32, (self.board_height // 16) - 2 * (self.board_height // 16) // 3))

        self.current_color = self.get_current_color()

    def start_window(self):
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        self.board = pygame.Surface((self.board_width, self.board_height))
        pygame.display.set_caption('Pixel Editor: ')

    def draw_tool_bar(self):
        pygame.draw.rect(self.board, (40, 42, 53), (0, (self.board_height // 2) + self.board_height // 3.33, self.board_width, self.board_height // 5))
        pygame.draw.rect(self.board, (0, 0, 0), (0, (self.board_height // 2) + self.board_height // 3.25, self.board_width, self.board_height // 5.3), int(self.board_width / self.board_height * 10))

    def get_current_color(self):
        color = pygame.Color(0)
        color.hsla = (int(self.color * self.color_length), 100, 50, 100)
        return color

    def draw_colors(self):
        self.board.blit(self.color_picker_image, self.color_picker_rectangle)
        pygame.draw.rect(self.board, (0, 0, 0), self.color_picker_rectangle, int(self.board_width / self.board_height * 12), border_radius = self.board_width // 8)
        pygame.draw.circle(self.board, self.get_current_color(), (self.color_picker_rectangle.left + self.rad + self.color * self.color_length, self.color_picker_rectangle.centery), self.color_picker_rectangle.height // 3)

    def update_colors(self):
        position = pygame.mouse.get_pos()
        ratio_x = (self.screen_width / self.board_width)
        ratio_y = (self.screen_height / self.board_height)
        position = (position[0] / ratio_x, position[1] / ratio_y)
        if(pygame.mouse.get_pressed()[0] and self.color_picker_rectangle.collidepoint(position)):
            self.color = (position[0] - self.color_picker_rectangle.left - self.rad) / self.color_length
            self.color = (max(0, min(self.color, 1)))

        self.current_color = self.get_current_color()

    def init_grid(self):
        if(not self.grid_ready):
            for i in range(self.rows):
                self.grid.append([])
                for j in range(self.columns):
                    self.grid[i].append((255, 255, 255))

            for i, row in enumerate(self.grid):
                for j, pixel in enumerate(row):
                    pygame.draw.rect(self.board, (pixel), (j * self.pixel_size, i * self.pixel_size, self.pixel_size, self.pixel_size))

            self.grid_ready = True

    def update_editor(self):
        self.init_grid()
        self.draw_tool_bar()
        self.draw_colors()
        self.update_colors()
        self.start_drawing()
        self.window.blit(pygame.transform.smoothscale(self.board, (self.screen_width, self.screen_height)), (0, 0))

    def get_mouse_position(self, position):
        ratio_x = (self.screen_width / self.board_width)
        ratio_y = (self.screen_height / self.board_height)
        position = (position[0] / ratio_x, position[1] / ratio_y)
        if(position[1] < self.board_height - (self.board_height // 5)):
            row, column = int(position[1] // self.pixel_size), int(position[0] // self.pixel_size)
            return row, column
        else:
            return -1, -1

    def start_drawing(self):
        if(pygame.mouse.get_pressed()[0]):
            row, column = self.get_mouse_position(pygame.mouse.get_pos())
            if(self.grid[row][column] != self.current_color):
                self.grid[row][column] = self.current_color
                pygame.draw.rect(self.board, (self.current_color), (column * self.pixel_size, row * self.pixel_size, self.pixel_size, self.pixel_size))

        if(pygame.mouse.get_pressed()[2]):
            row, column = self.get_mouse_position(pygame.mouse.get_pos())
            if(self.grid[row][column] != (255, 255, 255)):
                self.grid[row][column] = (255, 255, 255)
                pygame.draw.rect(self.board, (255, 255, 255), (column * self.pixel_size, row * self.pixel_size, self.pixel_size, self.pixel_size))

    def update_window(self, fps):
        self.fps_handler.tick(fps)
        print(self.fps_handler)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.window_running = False
                quit()
            if(event.type == pygame.VIDEORESIZE):
                self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

        pygame.display.update()

# Pixel Editor: #

editor = Editor(800, 600, 1920, 1080)
editor.start_window()

while(editor.window_running):
    editor.update_editor()
    editor.update_window(120)