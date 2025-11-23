from dataclasses import dataclass
from typing import List


@dataclass
class Message:
    subject: str
    body: str

    @property
    def full_text(self):
        return f"{self.subject}\n-----\n{self.body}"


@dataclass
class MessageClassification:
    message: Message
    is_spam: bool
    probability: float
    found_words: List[str]
