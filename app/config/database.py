# import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from decouple import config

ssl_args = {'ssl_ca': '/etc/ssl/cert.pem'}
db_host = config("DB_HOST")
db_user = config("DB_USER")
db_pass = config("DB_PASS")
db_name = config("BD_NAME")

database_url = "mysql+pymysql://" + db_user + \
    ":" + db_pass+"@"+db_host+"/" + db_name

# sqlite_file_name = "../database.sqlite"
# base_dir = os.path.dirname(os.path.realpath(__file__))

# database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(database_url, connect_args=ssl_args, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

# meta = MetaData()

# conn = engine.connect()
