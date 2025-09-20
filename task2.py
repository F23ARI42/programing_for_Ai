from sqlalchemy import create_engine, text

# Connect to the SQLite database
engine = create_engine('sqlite:///case_study.sqlite')

# SQL query to calculate average age grouped by sex
query = text("""
    SELECT sex, AVG(age) as avg_age
    FROM census
    GROUP BY sex
""")

with engine.connect() as conn:
    result = conn.execute(query)
    for row in result:
        print(f"Sex: {row.sex}, Average Age: {row.avg_age:.2f}")
