import pandas as pd
cars_data_path = "data/cars.csv"
from sqlalchemy import create_engine


def load_data():
    engine = create_engine('sqlite:///CarStore3000.db', echo=True)
    sqlite_connection = engine.connect()

    cars_df = pd.read_csv(cars_data_path)
    cars_df = cars_df[cars_df.maker.notnull()
                      & cars_df.model.notnull()
                      & cars_df.mileage.notnull()
                      & cars_df.manufacture_year.notnull()
                      & cars_df.price_eur.notnull()
                      & cars_df.body_type.notnull()]

    sqlite_table = "Cars"
    cars_df.to_sql(sqlite_table, sqlite_connection, if_exists='replace')

    return True
