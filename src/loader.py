import pandas as pd
from sqlalchemy import create_engine
from .config import DBConfig

class DataLoader:
    def __init__(self):
        pass

    def load_data(self, table_name):
        db_config = DBConfig.load()
        connection_string = f"postgresql+psycopg2://{db_config['DATABASE_USER']}:{db_config['DATABASE_PASSWORD']}@{db_config['DATABASE_HOST']}:{db_config['DATABASE_PORT']}/{db_config['DATABASE_NAME']}"
        engine = create_engine(connection_string)
        sql_query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(sql_query, con=engine)
        return df
