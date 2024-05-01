from src.text_summarizer.components.data_ingestion import DataIngestion
from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.logging import logger


class DataIngestiontTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config =  ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config) #####  data_ingestion
        data_ingestion.download_file()
        data_ingestion.unzip_file()
