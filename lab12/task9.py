import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')
metadata = MetaData()
track = Table('Track', metadata, autoload_with=engine)
with engine.connect() as connection:
    stmt = select(track)
    df = pd.read_sql(stmt, connection)
print("Null values per column:")
print(df.isnull().sum())
