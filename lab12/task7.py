from sqlalchemy import create_engine, MetaData, Table, select, func

engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')

with engine.connect() as connection:
    metadata = MetaData()
    media_type = Table('MediaType', metadata, autoload_with=engine)
    track = Table('Track', metadata, autoload_with=engine)
    stmt = (
        select(media_type.c.Name, func.avg(track.c.Milliseconds).label("AvgLengthMs"))
        .select_from(media_type.join(track, media_type.c.MediaTypeId == track.c.MediaTypeId))
        .group_by(media_type.c.Name)
        .order_by(media_type.c.Name)
    )
    results = connection.execute(stmt).fetchall()
    for row in results:
        print(row)
