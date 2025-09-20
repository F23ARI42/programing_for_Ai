from sqlalchemy import *
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')
inspector = inspect(engine)
print(inspector.get_table_names())