from sqlalchemy import create_engine, MetaData, Table, select, func
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')
with engine.connect() as connection:
    metadata = MetaData()
    invoice = Table('Invoice', metadata, autoload_with=engine)
    stmt = (
        select(invoice.c.BillingCountry, func.max(invoice.c.Total).label("MaxInvoiceAmount"))
        .group_by(invoice.c.BillingCountry)
        .order_by(invoice.c.BillingCountry)
    )
    results = connection.execute(stmt).fetchall()
    for row in results:
        print(row)
