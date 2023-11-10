import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent
BOT_TOKEN = os.getenv('BOT_TOKEN')
DATEFORMAT = '%Y-%m-%d_%H-%M-%S '
LOG_COUNT = 5
LOG_SIZE = 10**6
PROBABILITIES_LIST = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 97, 99]
