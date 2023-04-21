from sqlalchemy import create_engine,MetaData

engine = create_engine("mysql+pymysql://localhost:3306/client_radar_dev_db")

meta = MetaData()

conn = engine.connect()