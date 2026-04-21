from db.connect import engine
from db.tables import Base

print("Creating tables in PostgreSQL...")

try:
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")
except Exception as e:
    print(f"Error creating tables: {e}")

    