from sqlalchemy import create_engine
from models import Base

# Database setup
DATABASE_URL = "sqlite:///bank.db"  # Using SQLite for simplicity

def init_db():
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()
