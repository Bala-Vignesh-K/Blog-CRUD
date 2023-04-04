from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from sqlalchemy import create_engine

# user = 'root'
# password = 'Admin@2022'
# host = 'localhost'
# port = 3306
# DB_NAME = 'mydb'
# This engine just used to query for list of databases
# db_engine = create_engine('mysql://{0}:{1}@{2}:{3}'.format(user, password, host, port))


# Go ahead and use this engine
# db_engine = create_engine('mysql://{0}:{1}@{2}:{3}/{4}'.format(user, password, host, port, DB_NAME))
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False}) 
# "mysql+mysqlconnector://root:Admin@2022@localhost:3306//dbname"



# user = 'root'
# password = 'Admin@2022'
# host = 'localhost'
# port = 3306
# DB_NAME = 'mydb'

# engine = create_engine(f"mysql+mysqlconnector://{username}:Admin\@2022@localhost:{port}")

# from sqlalchemy_utils import create_database, database_exists
# url = 'mysql://{0}:{1}@{2}:{3}'.format(user, password, host, port)
# if not database_exists(url):
#     create_database(url)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# with engine.connect() as conn:
#     # Do not substitute user-supplied database names here.
#     conn.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


