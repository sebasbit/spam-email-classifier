import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from spam_email_classifier.core.config import UI_TEXTS, ASSETS_DIR, IMG_EXTENSION, FAVICON
from spam_email_classifier.models.dto import MessageClassification


class ResultView(ttk.Toplevel):
    def __init__(self, classification: MessageClassification):
        super().__init__(title=UI_TEXTS["app_title"])
        self.geometry("600x600")
        self.resizable(True, True)
        self.iconbitmap(FAVICON)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.data = classification

        self.main_frame = ttk.Frame(self, padding=20)
        self.main_frame.pack(fill=BOTH, expand=YES)

        self.create_header()
        ttk.Separator(self.main_frame, orient=HORIZONTAL).pack(fill=X, pady=(0, 20))

        self.create_classification_fieldset()
        self.create_words_fieldset()
        self.create_chart_fieldset()

    def create_header(self):
        lbl = ttk.Label(self.main_frame, text=UI_TEXTS["analysis_result"], font=("Arial", 16, "bold"))
        lbl.pack(pady=(0, 10))

    def create_classification_fieldset(self):
        frame = ttk.Labelframe(self.main_frame, text=UI_TEXTS["classification_group"], padding=10)
        frame.pack(fill=X, pady=10)

        if self.data.is_spam:
            cls_text = "SPAM"
            color = "danger"
        else:
            cls_text = "HAM"
            color = "success"

        prob_percent = round(self.data.probability * 100, 2)

        res_label = ttk.Label(
            frame,
            text=UI_TEXTS["classification_result"].format(cls_text=cls_text, prob_percent=prob_percent),
            bootstyle=color,
            font=("Arial", 12, "bold")
        )
        res_label.pack(anchor=W, pady=(0, 10))

        msg_lbl = ttk.Label(frame, text=self.data.message.full_text, wraplength=540)
        msg_lbl.pack(anchor=W)

    def create_words_fieldset(self):
        frame = ttk.Labelframe(self.main_frame, text=UI_TEXTS["word_classification_group"], padding=10)
        frame.pack(fill=X, pady=10)

        if not self.data.found_words:
            ttk.Label(frame, text=UI_TEXTS["no_words_found"]).pack()
            return

        for i, word in enumerate(self.data.found_words):
            img_path = os.path.join(ASSETS_DIR, f"{word}.{IMG_EXTENSION}")

            item_frame = ttk.Frame(frame)
            item_frame.pack(side=LEFT, padx=10)

            ttk.Label(item_frame, text=word, font=("Consolas", 10, "bold")).pack()

            try:
                pil_img = Image.open(img_path)
                pil_img = pil_img.resize((100, 100), Image.LANCZOS)
                tk_img = ImageTk.PhotoImage(pil_img)

                img_lbl = ttk.Label(item_frame, image=tk_img)
                img_lbl.pack()
            except Exception:
                ttk.Label(item_frame, text=UI_TEXTS["no_graph"], bootstyle="secondary").pack()

    def create_chart_fieldset(self):
        frame = ttk.Labelframe(self.main_frame, text=UI_TEXTS["spam_ham_group"], padding=10)
        frame.pack(fill=BOTH, expand=YES, pady=10)

        prob_spam = self.data.probability
        prob_ham = 1.0 - prob_spam

        labels = ['SPAM', 'HAM']
        sizes = [prob_spam, prob_ham]
        colors = ['#d9534f', '#5cb85c']

        fig, ax = plt.subplots(figsize=(4, 3), dpi=100)
        fig.patch.set_facecolor('#303030')
        ax.set_facecolor('#303030')

        text_props = {'color': 'white'}

        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, textprops=text_props)
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=YES)

    def on_close(self):
        plt.close('all')
        self.destroy()
