# spam-email-classifier

Aplicación de escritorio para clasificar correos SPAM usando modelos de Machine Learning

## Configuración del entorno virtual

Asegúrate de tener instalado Miniforge, Miniconda o Anaconda para utilizar el
gestor de paquetes conda. Crea el entorno usando el archivo de configuración `environment.yml`:

```bash
conda env create -f environment.yml
```

Activa el nuevo entorno de Python:

```bash
conda activate spam_email_classifier_env
```

Con el entorno spam_email_classifier_env activado, puedes iniciar la aplicación ejecutando el script principal:

```bash
python main.py
```

## Generación del ejecutable para Windows

Asegúrate de tener el entorno spam_email_classifier_env activado. Si no lo está, ejecútalo:

```bash
conda activate spam_email_classifier_env
```

Navega a la carpeta raíz del proyecto y utiliza el siguiente comando. Este comando incluye todos los archivos
necesarios y dependencias en un solo archivo.

```bash
pyinstaller --noconsole --onefile --name spam_email_classifier --windowed --icon=assets\favicon.ico --add-data "assets;assets" --collect-all ttkbootstrap main.py
```
