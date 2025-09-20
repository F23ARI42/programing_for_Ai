from sqlalchemy import create_engine, MetaData, Table, select, func, inspect

# Connect to the database
engine = create_engine('sqlite:///chinook_Sqlite.sqlite')
inspector = inspect(engine)
print(inspector.get_table_names())

with engine.connect() as connection:
    metadata = MetaData()

    # Reflect the tables
    tracks = Table('Track', metadata, autoload_with=engine)
    genre = Table('Genre', metadata, autoload_with=engine)

    # Corrected Query
    stmt = (
        select(genre.c.Name, func.count(tracks.c.Name).label('count'))
        .select_from(tracks.join(genre, tracks.c.GenreId == genre.c.GenreId))
        .where(genre.c.Name == "Rock")
        .group_by(genre.c.Name)
    )

    result = connection.execute(stmt).fetchall()
    for row in result:
        print(row)
