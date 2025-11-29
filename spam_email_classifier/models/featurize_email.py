import re
from collections import defaultdict

from spam_email_classifier.models.dto import Message


def freq_pain_feature(text, freq):
    return float(freq['pain'])


def freq_private_feature(text, freq):
    return float(freq['private'])


def freq_bank_feature(text, freq):
    return float(freq['bank'])


def freq_money_feature(text, freq):
    return float(freq['money'])


def freq_drug_feature(text, freq):
    return float(freq['drug'])


def freq_spam_feature(text, freq):
    return float(freq['spam'])


def freq_prescription_feature(text, freq):
    return float(freq['prescription'])


def freq_creative_feature(text, freq):
    return float(freq['creative'])


def freq_height_feature(text, freq):
    return float(freq['height'])


def freq_featured_feature(text, freq):
    return float(freq['featured'])


def freq_differ_feature(text, freq):
    return float(freq['differ'])


def freq_width_feature(text, freq):
    return float(freq['width'])


def freq_other_feature(text, freq):
    return float(freq['other'])


def freq_energy_feature(text, freq):
    return float(freq['energy'])


def freq_business_feature(text, freq):
    return float(freq['business'])


def freq_message_feature(text, freq):
    return float(freq['message'])


def freq_volumes_feature(text, freq):
    return float(freq['volumes'])


def freq_revision_feature(text, freq):
    return float(freq['revision'])


def freq_path_feature(text, freq):
    return float(freq['path'])


def freq_meter_feature(text, freq):
    return float(freq['meter'])


def freq_memo_feature(text, freq):
    return float(freq['memo'])


def freq_planning_feature(text, freq):
    return float(freq['planning'])


def freq_pleased_feature(text, freq):
    return float(freq['pleased'])


def freq_record_feature(text, freq):
    return float(freq['record'])


def freq_out_feature(text, freq):
    return float(freq['out'])


# Features that look for certain characters
def freq_semicolon_feature(text, freq):
    return text.count(';')


def freq_dollar_feature(text, freq):
    return text.count('$')


def freq_sharp_feature(text, freq):
    return text.count('#')


def freq_exclamation_feature(text, freq):
    return text.count('!')


def freq_para_feature(text, freq):
    return text.count('(')


def freq_bracket_feature(text, freq):
    return text.count('[')


def freq_and_feature(text, freq):
    return text.count('&')


def generate_feature_vector(text, freq) -> list:
    feature = []
    feature.append(freq_pain_feature(text, freq))
    feature.append(freq_private_feature(text, freq))
    feature.append(freq_bank_feature(text, freq))
    feature.append(freq_money_feature(text, freq))
    feature.append(freq_drug_feature(text, freq))
    feature.append(freq_spam_feature(text, freq))
    feature.append(freq_prescription_feature(text, freq))
    feature.append(freq_creative_feature(text, freq))
    feature.append(freq_height_feature(text, freq))
    feature.append(freq_featured_feature(text, freq))
    feature.append(freq_differ_feature(text, freq))
    feature.append(freq_width_feature(text, freq))
    feature.append(freq_other_feature(text, freq))
    feature.append(freq_energy_feature(text, freq))
    feature.append(freq_business_feature(text, freq))
    feature.append(freq_message_feature(text, freq))
    feature.append(freq_volumes_feature(text, freq))
    feature.append(freq_revision_feature(text, freq))
    feature.append(freq_path_feature(text, freq))
    feature.append(freq_meter_feature(text, freq))
    feature.append(freq_memo_feature(text, freq))
    feature.append(freq_planning_feature(text, freq))
    feature.append(freq_pleased_feature(text, freq))
    feature.append(freq_record_feature(text, freq))
    feature.append(freq_out_feature(text, freq))
    feature.append(freq_semicolon_feature(text, freq))
    feature.append(freq_dollar_feature(text, freq))
    feature.append(freq_sharp_feature(text, freq))
    feature.append(freq_exclamation_feature(text, freq))
    feature.append(freq_para_feature(text, freq))
    feature.append(freq_bracket_feature(text, freq))
    feature.append(freq_and_feature(text, freq))
    return feature


def featurize_message(message: Message) -> tuple[list, defaultdict]:
    text = message.full_text
    text = text.replace('\r\n', ' ')
    words = re.findall(r'\w+', text)
    word_freq = defaultdict(int)
    for word in words:
        word_freq[word] += 1
    return generate_feature_vector(text, word_freq), word_freq
