# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                           #
#                    Python Pixel Editor                    #
#                     Developer: Carbon                     #
#                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Imports: #

from src.modules import *

# File Browser: #

class FileBrowser():
    def __init__(self, editor):

        # Editor:

        self.editor = editor

        # Status:

        self.browser_running = False

        # Properties:

        self.loaded_grid = []

    def init_file_browser(self):
        self.layout = [
            [PySimpleGUI.Text("Choose a project file: ")],
            [PySimpleGUI.InputText(key = "-FILE_PATH-"),
            PySimpleGUI.FileBrowse(initial_folder = os.getcwd(), file_types = [("Pixel Files", "*.pix")])],
            [PySimpleGUI.Button("Submit"), PySimpleGUI.Exit()]
        ]
        if(self.browser_running == False):
            self.window = PySimpleGUI.Window("Load Files: ", icon = 'logo.ico').Layout(self.layout)
            self.browser_running = True

    def clean_grid(self, line):
        lines = line.split('||')
        a = []
        b = []
        for i in lines:
            a.append(i.split('#'))

        del a[0]
        for j in a:
            for k in j:
                if(k == ''):
                    del a[a.index(j)][j.index(k)]

        for l in a:
            for h in l:
                x = h.split()
                p = []
                for w in x:
                    if(w.isnumeric):
                        w = w.replace('(', '')
                        w = w.replace(')', '')
                        w = w.replace(',', '')
                        p.append(int(w))

                a[a.index(l)][l.index(h)] = (p[0], p[1], p[2])

        return a

    def handle_events(self):
        if(self.browser_running):
            file_event, file = self.window.read()
            if(file_event in (PySimpleGUI.WIN_CLOSED, 'Exit')):
                self.browser_running = False
                self.window.close()

            elif(file_event == "Submit"):
                self.loaded_file = file["-FILE_PATH-"]
                if(self.loaded_file == ''):
                    self.browser_running = False
                    self.window.close()
                else:
                    with open(self.loaded_file, "r") as file:
                        line = file.readline()
                        self.loaded_grid = self.clean_grid(line)
                        self.editor.grid = self.loaded_grid
                        self.editor.draw_board()
                        file_name = self.loaded_file.split("/")
                        self.editor.save_name_input.written_text = (file_name[len(file_name) - 1][0:len(file_name[len(file_name) - 1]) - 4])
                        self.browser_running = False
                        self.window.close()