from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data.json')
current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
