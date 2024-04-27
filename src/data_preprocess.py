import pandas as pd
import os
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from .loader import DataLoader
from .config import DBConfig

class DataPreProcessor:
    def __init__(self):
        self.table_name = 'xdr_data'
        self.pre_processed_table = 'preprocessed_data'
        self.loader = DataLoader()
        self.db_config = DBConfig.load()
        self.df = self.loader.load_data(self.table_name)
        self.connection_string = f"postgresql+psycopg2://{self.db_config['DATABASE_USER']}:{self.db_config['DATABASE_PASSWORD']}@{self.db_config['DATABASE_HOST']}:{self.db_config['DATABASE_PORT']}/{self.db_config['DATABASE_NAME']}"
        self.engine = create_engine(self.connection_string)
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
    
    def analyze_data(self):
        print("Data shape:", self.df.shape)
        print("Data description:", self.df.describe())
        print("Data info:")
        print(self.df.info())
        print("First 5 rows:")
        print(self.df.head())
    
    def handle_duplicates(self):
        self.df.drop_duplicates(inplace=True)

    def handle_missing_values(self):
        numeric_cols = self.df.select_dtypes(include=['float64']).columns
        numeric_imputer = SimpleImputer(strategy='mean')
        self.df[numeric_cols] = numeric_imputer.fit_transform(self.df[numeric_cols])

        categorical_cols = self.df.select_dtypes(include=['object']).columns
        self.df[categorical_cols] = self.df[categorical_cols].fillna('Unknown')

    def split_data(self, test_size=0.2, random_state=None):
        X = self.df.drop(columns=['Satisfaction_Score'])
        y = self.df['Satisfaction_Score']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    def save_preprocessed_data_to_db(self):
        self.df.to_sql(self.pre_processed_table, self.engine, index=False, if_exists='replace')

    def fetch_preprocessed_data(self):
        df = pd.read_sql_table(self.pre_processed_table, con=self.engine)
        return df
