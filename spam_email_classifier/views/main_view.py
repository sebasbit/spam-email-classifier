import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.scrolledtext import ScrolledText
from spam_email_classifier.core.config import UI_TEXTS


class MainView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)
        self.subject_entry = None
        self.parent = parent
        self.pack(fill=BOTH, expand=YES)

        self.create_header()
        ttk.Separator(self, orient=HORIZONTAL).pack(fill=X, pady=(0, 20))
        self.create_form()
        self.create_actions()

    def create_header(self):
        title_label = ttk.Label(
            self,
            text=UI_TEXTS["app_title"],
            font=("Arial", 16, "bold"),
            bootstyle="success"
        )
        title_label.pack(pady=(0, 10))

    def create_form(self):
        subject_frame = ttk.Labelframe(
            self,
            text=UI_TEXTS["subject_group"],
            padding=10,
        )
        subject_frame.pack(fill=X, pady=10)

        self.subject_entry = ttk.Entry(subject_frame)
        self.subject_entry.pack(fill=X)

        message_frame = ttk.Labelframe(
            self,
            text=UI_TEXTS["message_group"],
            padding=10,
        )
        message_frame.pack(fill=BOTH, expand=YES, pady=10)

        self.message_text = ScrolledText(
            message_frame,
            height=10,
        )
        self.message_text.pack(fill=BOTH, expand=YES)

    def create_actions(self):
        classify_btn = ttk.Button(
            self,
            text=UI_TEXTS["btn_classify"],
            bootstyle="success-outline",
            width=20,
            command=self.on_classify_click
        )
        classify_btn.pack(pady=20)

    def on_classify_click(self):
        pass
