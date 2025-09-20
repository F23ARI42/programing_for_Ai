from sqlalchemy import create_engine, text
engine = create_engine('sqlite:///case_study.sqlite')
update_query = text("UPDATE census SET state = 'New York' WHERE state = 'California'")
verify_query = text("SELECT state FROM census")
with engine.connect() as conn:
    result = conn.execute(verify_query)
    for row in result:
        print(row)
