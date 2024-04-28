import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name =  "text_summarizer"

list_files = [
    ".github.workflows.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/utils/common.py",
    "config/config.yaml"
    "params.yaml"
    "app.py"
    "main.py"
    "setup .py"
    "Dockerfile"
    "requirements.txt"
    "research/trials.ipynb"
]

for filepath in list_files:
    path = Path(filepath)
    filedir, filepath = os.path.split(path)

    if filedir  != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory: {filedir} for file")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    
    else:
        logging.info(f"file already exists: {filepath}")