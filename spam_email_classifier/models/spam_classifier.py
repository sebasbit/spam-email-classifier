import pandas as pd
from pycaret.classification import predict_model, load_model

from spam_email_classifier.core.config import MODEL_DIR
from spam_email_classifier.models.base_classifier import BaseClassifier
from spam_email_classifier.models.dto import Message, MessageClassification
from spam_email_classifier.models.featurize_email import featurize_message


class SpamClassifier(BaseClassifier):
    COL_NAMES = [
        "pain",
        "private",
        "bank",
        "money",
        "drug",
        "spam",
        "prescription",
        "creative",
        "height",
        "featured",
        "differ",
        "width",
        "other",
        "energy",
        "business",
        "message",
        "volumes",
        "revision",
        "path",
        "meter",
        "memo",
        "planning",
        "pleased",
        "record",
        "out",
        "semicolon",
        "dollar",
        "sharp",
        "exclamation",
        "parenthesis",
        "square_bracket",
        "ampersand"
    ]
    CLASS_SPAM = 1

    def classify(self, message: Message) -> MessageClassification:
        model = load_model(MODEL_DIR)
        feature_vector, word_freq = featurize_message(message)
        input_df = pd.DataFrame([feature_vector], columns=self.COL_NAMES)
        predictions = predict_model(model, data=input_df, verbose=False)
        pred_label = predictions['prediction_label'].iloc[0]
        pred_score = predictions['prediction_score'].iloc[0]

        is_spam = (pred_label == self.CLASS_SPAM)
        probability_spam = pred_score if is_spam else (1.0 - pred_score)

        return MessageClassification(
            message=message,
            is_spam=bool(is_spam),
            probability=float(probability_spam),
            found_words=[word for word in word_freq.keys() if word in self.COL_NAMES],
        )
