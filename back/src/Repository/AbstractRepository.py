from sqlalchemy import Table, Column, MetaData, Integer, Computed
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

class AbstarctRepository:
    def __init__(self) -> None:
        try:
            self.engine = create_engine("postgresql+psycopg2://web:web@localhost:5432/web")
            Base = declarative_base()
            Base.metadata.create_all(self.engine)
        except:
            e = sys.exc_info()[1]
            print(e.args[0])