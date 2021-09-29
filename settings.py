import os
from pathlib import Path
from dotenv import dotenv_values


BASE_DIR = Path(__file__).resolve().parent.parent

ENV_PATH = os.path.join(BASE_DIR.parent, '.env')
env = dotenv_values(ENV_PATH)

DB_ENGINE=env.get('DB_ENGINE')
DB_NAME=env.get('DB_NAME')
# DB_USER=env.get('DB_USER')
# DB_PASS=env.get('DB_PASS')
