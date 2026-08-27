import json
from datetime import date
import logging


def load_path():
    file_path = f"./data/YT_data_{date.today()}.json"
    try:
        logeer.info(f"Processing file: YT_date{date.today()}")
        with open(file_path, "r", encoding="uf8") as raw_data:
            data = json.load(raw_data)
        return data
    except FileExistsError:
        logger.error(f"File not found:{file_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
        raise