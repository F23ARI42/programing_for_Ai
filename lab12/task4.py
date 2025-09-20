from sqlalchemy import create_engine, MetaData, Table, select
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')
with engine.connect() as connection:
    metadata = MetaData()
    album = Table('Album', metadata, autoload_with=engine)
    stmt = select(album).order_by(album.c.Title.asc())
    results = connection.execute(stmt).fetchall()
    print(results)
