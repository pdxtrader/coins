import sqlalchemy
from sqlalchemy import Table, Column, Integer, String


def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

def create_tables(meta, con):
    coins = Table(
        'coins', meta,
        Column('id', String, primary_key=True),
        Column('symbol', String),
        Column('name', Integer),
        Column('webpage', String),
        Column('github', String)
    )
