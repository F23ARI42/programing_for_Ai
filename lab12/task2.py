from sqlalchemy import create_engine,inspect,Table,MetaData
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')
inspector = inspect(engine)
meta = MetaData()
Album = Table('Album', meta,autoload_with=engine)
print(repr(Album))