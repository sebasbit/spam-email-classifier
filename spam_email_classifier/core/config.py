import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


UI_TEXTS = {
    "window_title": "CLASIFICADOR DE CORREOS SPAM",
    "app_title": "CLASIFICADOR DE CORREOS SPAM",
    "subject_group": "Asunto",
    "message_group": "Mensaje",
    "btn_classify": "Clasificar",
    "validation_error": "Error de Validación",
    "validation_min_chars": "El {field} debe tener al menos {n_chars} caracteres.",

    "analysis_result": "RESULTADO DEL ANÁLISIS",
    "classification_group": "Clasificación",
    "classification_result": "{cls_text} ({prob_percent}% de probabilidad de ser SPAM)",
    "word_classification_group": "Relación 'Palabra vs Clasificación'",
    "no_words_found": "No se encontraron palabras clave relevantes.",
    "no_graph": "[Sin Gráfico]",
    "spam_ham_group": "SPAM vs HAM"
}
WINDOW_SIZE = "500x500"
MIN_CHARS_SUBJECT = 8
MIN_CHARS_MESSAGE = 16
ASSETS_DIR = resource_path(os.path.join("assets", "bar_plots"))
FAVICON = resource_path(os.path.join("assets", "favicon.ico"))
