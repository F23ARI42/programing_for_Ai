from sqlalchemy import create_engine, text
engine = create_engine('sqlite:///case_study.sqlite')
delete_query = text("DELETE FROM census WHERE sex = 'M'")
with engine.connect() as conn:
    result = conn.execute(delete_query)
    print("All rows where deleted.")
