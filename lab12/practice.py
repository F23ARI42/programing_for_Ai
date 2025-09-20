from sqlalchemy import *
import pandas as pd
engine = create_engine('sqlite:///books.sqlite')
inspector = inspect(engine)
with engine.connect() as connection:
    metadata = MetaData()
    census=Table('census',metadata,
                 Column('id',Integer),
                 Column('name',String(50)),
                 Column('capital',String(50)),
                 Column('population',Integer),
                 Column('education',String(50)),
                 )
    metadata.create_all(engine)
    inspector=inspect(engine)
    print(inspector.get_table_names())
columns =['id','name','capital','papulation','education']
df=pd.read_csv('../../p_for_Ai/lab13/census.csv', names=columns)
print(df.head())
df.to_sql('census',con=engine,if_exists='replace',index=False)
