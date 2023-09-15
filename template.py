import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
#will show in terminal

project_name = "Resume_Screener"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
   "templates/index.html"


]
import sys
sys.path.append("D:/Project/RESUME_SCREENER/src/Resume_Screener")
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")