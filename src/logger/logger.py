import os
import yaml

import logging.config
from src.logger.custom_json_formatter import CustomJSONFormatter

# import logging

def setup_logger():
    logger_config_path: str = os.path.join(os.path.dirname(__file__),"logger_config.yaml")
    with open(logger_config_path, "r") as f:
        config = yaml.safe_load(f.read())

    logging.config.dictConfig(config)

