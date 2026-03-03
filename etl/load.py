from sqlalchemy import create_engine
from config.config import DB_URI

def load(df):

    engine = create_engine(DB_URI)

    df.to_sql(
        name="fact_products",
        con=engine,
        if_exists="replace",
        index=False
    )