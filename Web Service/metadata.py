from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Text


engine = create_engine('sqlite:///C:\\CELabs\\userdb.db')
meta = MetaData()

User = Table(
   'User', meta, 
   Column('id', Integer, primary_key = True), 
   Column('public_id', String(50), unique = True), 
   Column('name', String(50)),
   Column('password', String(50)),
   Column('admin', Boolean),
)

Reservation = Table(
    'Reservation', meta,
    Column('id', Integer, primary_key = True),
    Column('public_id', String(50), unique = True),
    Column('lab_id', Integer, nullable = False),
    Column('date_time', Text(50), nullable = False),
    Column('duration_minutes', Integer, nullable = False),
)

meta.create_all(engine)
