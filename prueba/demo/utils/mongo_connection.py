from pymongo import MongoClient
from urllib.parse import quote
from django.conf import settings
 
class MongoConn(object):
    _conn = None
    _db = None
 
    def __new__(cls, *args, **kwargs):
        len_args = len(args)
        if not cls._conn or len_args != 0:
            if len_args == 2:
                db_ = args[1]
            else:
                db_ = settings.MONGO_DB
            conn = MongoClient(
                'mongodb://%s:%s@%s' % (
                    settings.MONGO_USER,
                    quote(settings.MONGO_SECRET),
                    settings.MONGO_HOST
                )
            )
            db = db_
            cls._conn = conn
            cls._db = getattr(conn, db)
        return cls
    
    """
    
    # Para conectar con Mongo
    from demo.utils.mongo_connection import MongoConn
    conn = MongoConn(True)
    db = conn._db

    # Ya haces la consulta
    db."Profesores".find({'ID_Profesor': 1})
    
    """