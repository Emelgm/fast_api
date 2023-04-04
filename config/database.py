import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# almacenar el nombre de la db
sqlite_file_name = '../database.sqlite'
# leer el directorio actual del archivo database
base_dir = os.path.dirname(os.path.realpath(__file__))
# url de conexión
database_url = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'
# motor de la db
engine = create_engine(database_url, echo=True)
# sesion de conexión
Session = sessionmaker(bind=engine)
# manipular tablas de la db
Base = declarative_base()