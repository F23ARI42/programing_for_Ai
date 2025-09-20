from sqlalchemy import inspect, create_engine, MetaData, Table, String, Numeric, Column
import pandas as pd

engine = create_engine('sqlite:///case_study.sqlite')

with engine.connect() as connection:
    meta = MetaData()
    census = Table('census', meta,
                   Column('state', String(30)),
                   Column('sex', String(1)),
                   Column('age', Numeric),
                   Column('pop2000', Numeric),
                   Column('pop2008', Numeric))
    meta.create_all(engine)
    inspector = inspect(engine)
    print(inspector.get_table_names())
columns = ['state', 'sex', 'age', 'pop2000', 'pop2008']
df = pd.read_csv("census.csv", names=columns)
print(df.head())
df.to_sql("census", con=engine, if_exists="replace", index=False)