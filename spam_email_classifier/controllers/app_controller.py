import ttkbootstrap as ttk
from spam_email_classifier.views.main_view import MainView
from spam_email_classifier.core.config import UI_TEXTS, WINDOW_SIZE


class AppController:
    def __init__(self):
        self.root = ttk.Window(themename="darkly")

        self.root.title(UI_TEXTS["window_title"])
        self.root.geometry(WINDOW_SIZE)
        self.root.resizable(False, False)

        self.view = MainView(self.root)

    def run(self):
        self.root.mainloop()
