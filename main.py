# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                           #
#                    Python Pixel Editor                    #
#                     Developer: Carbon                     #
#                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Imports: #

from src.editor import *
from src.file_browser import *

# Pixel Editor: #

editor = Editor(800, 600, 1920, 1080)

# File Browser: #

file_browser = FileBrowser(editor)

# Window: #

editor.start_window(file_browser)

# Editor Loop: #

while(editor.window_running):
    editor.update_editor()
    editor.update_window(120)