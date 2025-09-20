from sqlalchemy import create_engine, MetaData, Table, select
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')
with engine.connect() as connection:
    metadata = MetaData()
    album = Table('Album', metadata, autoload_with=engine)
    track = Table('Track', metadata, autoload_with=engine)
    customer = Table('Customer', metadata, autoload_with=engine)
    invoice = Table('Invoice', metadata, autoload_with=engine)

    print("a. Albums where ArtistId is 90:")
    a_stmt = select(album).where(album.c.ArtistId == 90)
    print(connection.execute(a_stmt).fetchall())

    print("\nb. Tracks longer than 6 minutes:")
    b_stmt = select(track).where(track.c.Milliseconds > 6 * 60 * 1000)
    print(connection.execute(b_stmt).fetchall())

    print("\nc. Tracks where name starts with 'Love':")
    c_stmt = select(track).where(track.c.Name.like('Love%'))
    print(connection.execute(c_stmt).fetchall())

    print("\nd. Customers from USA:")
    d_stmt = select(customer).where(customer.c.Country == 'USA')
    print(connection.execute(d_stmt).fetchall())

    print("\ne. Invoices with Total between 10 and 20:")
    e_stmt = select(invoice).where(invoice.c.Total.between(10, 20))
    print(connection.execute(e_stmt).fetchall())

    print("\nf. Tracks with GenreId in (1, 2, 3):")
    f_stmt = select(track).where(track.c.GenreId.in_([1, 2, 3]))
    print(connection.execute(f_stmt).fetchall())

    print("\ng. Customers whose last name contains 'son':")
    g_stmt = select(customer).where(customer.c.LastName.like('%son%'))
    print(connection.execute(g_stmt).fetchall())
