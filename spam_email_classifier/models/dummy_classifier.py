import random
from spam_email_classifier.models.base_classifier import BaseClassifier
from spam_email_classifier.models.dto import Message, MessageClassification


class DummyClassifier(BaseClassifier):
    CLASS_SPAM = 1
    CLASS_HAM = 0

    def load_model(self, path: str):
        pass

    def classify(self, message_obj: Message) -> MessageClassification:
        is_spam_bool = random.choice([True, False])

        if is_spam_bool:
            prob = random.uniform(0.6, 0.99)
        else:
            prob = random.uniform(0.01, 0.4)

        words = message_obj.full_text.split()
        found_words = random.sample(words, min(len(words), 3)) if words else []

        return MessageClassification(
            message=message_obj,
            is_spam=is_spam_bool,
            probability=prob,
            found_words=found_words
        )
