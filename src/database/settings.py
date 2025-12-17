from sqlalchemy import create_engine

from .enviroment import DatabaseEnviroment


engine = create_engine(DatabaseEnviroment().POSTGRESQL_URL_INTERNAL)
