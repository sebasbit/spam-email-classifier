import pandas as pd
import scipy.io
import numpy as np
import os
from pycaret.classification import (
    setup, compare_models, pull, finalize_model,
    save_model, tune_model, evaluate_model
)


class TrainModel:
    def __init__(self):
        self.df = None
        self.final_pipeline = None
        self.COL_NAMES = [
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

    def load_dataset(self, file_path):
        print(f"\n[INFO] Cargando dataset desde: {file_path}")

        try:
            data = scipy.io.loadmat(file_path)

            if "training_data" not in data or "training_labels" not in data:
                raise ValueError("Faltan claves 'training_data' o 'training_labels'.")

            X_train = data["training_data"]
            y_train = np.squeeze(data["training_labels"])

            print(f"[INFO] Dimensiones X: {X_train.shape}")
            self.df = pd.DataFrame(X_train, columns=self.COL_NAMES)
            self.df["label"] = y_train

            count = self.df['label'].value_counts()
            print(f"[INFO] Dataset cargado. Distribución:\n{count}")

        except Exception as e:
            print(f"[ERROR] Fallo al cargar el dataset: {e}")
            self.df = None

    def train_model(self):
        if self.df is None:
            print("[ERROR] No hay datos cargados.")
            return

        print("\n[INFO] Configurando PyCaret (SMOTE activo)...")

        setup(
            data=self.df,
            target='label',
            session_id=123,
            fix_imbalance=True,
            normalize=True,
            normalize_method='minmax',
            verbose=False
        )

        print("[INFO] Comparando modelos base (ordenados por F1)...")
        best_model = compare_models(sort='F1', n_select=1)
        print(f"[INFO] Mejor modelo base encontrado: {best_model}")

        print("\n[INFO] Iniciando optimización de hiperparámetros (Tuning)...")
        tuned_model = tune_model(best_model, optimize='F1', n_iter=10)

        print("\n--- Resultados del Modelo Afinado ---")
        print(pull().head(1))

        print("\n[INFO] Generando evaluación del modelo...")
        evaluate_model(tuned_model)

        print("\n[INFO] Finalizando el modelo con el dataset completo...")
        self.final_pipeline = finalize_model(tuned_model)

        print(f"[EXITO] Modelo finalizado y listo para guardar.")

    def save_trained_model(self, dest_path=None):
        if self.final_pipeline is None:
            print("[ERROR] No hay modelo para guardar.")
            return

        if not dest_path:
            dest_path = "spam_classifier_model"
            print(f"[INFO] Guardando como '{dest_path}.pkl' por defecto.")
        else:
            if dest_path.endswith('.pkl'):
                dest_path = dest_path[:-4]

        try:
            save_model(self.final_pipeline, dest_path)
            print(f"[EXITO] Modelo guardado en: {dest_path}.pkl")
        except Exception as e:
            print(f"[ERROR] Error al guardar: {e}")


if __name__ == "__main__":
    trainer = TrainModel()

    dataset_input = input("Ruta del archivo .mat (Enter para 'spam_data.mat'): ").strip()
    if not dataset_input:
        dataset_input = "spam_data.mat"

    if os.path.exists(dataset_input):
        trainer.load_dataset(dataset_input)

        if trainer.df is not None:
            trainer.train_model()

            save_input = input("\nRuta de destino para guardar el modelo (Enter para local): ").strip()
            trainer.save_trained_model(save_input if save_input else None)
    else:
        print(f"[ERROR] Archivo no encontrado: {dataset_input}")
