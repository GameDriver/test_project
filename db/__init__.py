# from .base_config import engine
from .base_db import BaseDAO, engine

db_dao = BaseDAO(engine)
