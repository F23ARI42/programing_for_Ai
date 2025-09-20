from sqlalchemy import create_engine, MetaData, Table, select
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')
with engine.connect() as connection:
    metadata = MetaData()
    album = Table('Album', metadata, autoload_with=engine)
    stmt = select(album).where(album.c.Title.like('T%'))
    results = connection.execute(stmt).fetchall()
    print(results)
