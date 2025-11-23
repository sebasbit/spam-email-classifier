import ttkbootstrap as ttk
from spam_email_classifier.controllers.result_controller import ResultController
from spam_email_classifier.models.dto import Message
from spam_email_classifier.models.dummy_classifier import DummyClassifier
from spam_email_classifier.views.main_view import MainView
from spam_email_classifier.core.config import UI_TEXTS, WINDOW_SIZE


class AppController:
    def __init__(self):
        self.root = ttk.Window(themename="darkly")

        self.root.title(UI_TEXTS["window_title"])
        self.root.geometry(WINDOW_SIZE)
        self.root.resizable(False, False)

        self.view = MainView(self.root, controller=self)

        self.classifier = DummyClassifier()  # TODO: implement real classifier.

    def run(self):
        self.root.mainloop()

    def handle_classify(self, subject: str, message_body: str):
        message_dto = Message(subject=subject, body=message_body)
        result_ctrl = ResultController(self.classifier)
        result_ctrl.show(message_dto)
