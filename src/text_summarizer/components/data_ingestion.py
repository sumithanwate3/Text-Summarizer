import os
import urllib.request as request
import zipfile
from pathlib import Path

from src.text_summarizer.entity import DataIngestionConfig
from src.text_summarizer.logging import logger
from src.text_summarizer.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
            url = self.config.source_URL,
            filename = self.config.local_data_file,
            )
            logger.info(f"{filename} downloaded with the info: \n {header}")
        else:
            logger.info(f"{self.config.local_data_file} already exists od size {get_size(Path(self.config.local_data_file))}")
    
    def unzip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)