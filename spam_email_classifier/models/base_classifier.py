from abc import ABC, abstractmethod

from spam_email_classifier.models.dto import Message, MessageClassification


class BaseClassifier(ABC):
    @abstractmethod
    def classify(self, message: Message) -> MessageClassification:
        pass
