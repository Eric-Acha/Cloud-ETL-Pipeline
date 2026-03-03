from etl.extract import extract
from etl.transform import transform
from etl.load import load
from etl.logger import get_logger

logger = get_logger()

def run():
    logger.info("Starting Fake Store ETL Pipeline")

    df = extract()
    logger.info("Extraction complete")

    df = transform(df)
    logger.info("Transformation complete")

    load(df)
    logger.info("Load complete")

    logger.info("Pipeline finished successfully")

if __name__ == "__main__":
    run()