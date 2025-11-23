from spam_email_classifier.models.base_classifier import BaseClassifier
from spam_email_classifier.models.dto import Message
from spam_email_classifier.views.result_view import ResultView


class ResultController:
    def __init__(self, classifier: BaseClassifier):
        self.classifier = classifier
        self.view = None

    def show(self, message: Message):
        msg_classification_dto = self.classifier.classify(message)
        self.view = ResultView(msg_classification_dto)
        self.view.grab_set()
