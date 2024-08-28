from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

url = URL(
    drivername='postgresql',
    username="postgres",
    password="postgres",
    host="localhost",
    database="postgres",
    port="5432",
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
