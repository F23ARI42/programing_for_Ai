from sqlalchemy import create_engine, MetaData, Table, select, func
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')
with engine.connect() as connection:
    metadata = MetaData()
    genre = Table('Genre', metadata, autoload_with=engine)
    track = Table('Track', metadata, autoload_with=engine)
    stmt = (
        select(genre.c.Name, func.count(track.c.TrackId).label("TotalTracks"))
        .select_from(genre.join(track, genre.c.GenreId == track.c.GenreId))
        .group_by(genre.c.Name)
        .order_by(genre.c.Name)
    )
    results = connection.execute(stmt).fetchall()
    for row in results:
        print(row)
