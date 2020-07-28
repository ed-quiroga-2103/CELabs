from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Text
from sqlalchemy import ForeignKey

file = open('CELabs.db', 'w+')
file.close()

engine = create_engine('sqlite:///D:\\Documents\\Espe\\CELabs\\Web Service\\CELabs.db')
meta = MetaData()



User_Type = Table(
    'User_Type', meta,
    Column('id_user_type', Integer, primary_key = True),
    Column('user_type', String(15), nullable = False)
)

User = Table(
   'User', meta, 
   Column('id_user', Integer, primary_key = True), 
   Column('public_id_user', String(50), unique = True), 
   Column('name', String(50), nullable = False),
   Column('lastname1', String(50), nullable = False),
   Column('lastname2', String(50), nullable = False),
   Column('id_number', String(50), nullable = False),
   Column('password', String(50), nullable = False),
   Column('email', String(50), nullable = False, unique = True),
   Column('phone_number', String(50), nullable = False),
   Column('active', Boolean, nullable = False),
   Column('university_id', String(50), nullable = False),
   Column('user_type', Integer, ForeignKey('User_Type.id_user_type'), nullable = False)

)
    
Reservation = Table(
    'Reservation', meta,
    Column('id_reservation', Integer, primary_key = True),
    Column('public_id_reservation', String(50), unique = True),
    Column('request_date', Text(50), nullable = False),
    Column('requested_date', Text(50), nullable = False),
    Column('init_time', Text(50), nullable = False),
    Column('final_time', Text(50), nullable = False),
    Column('last_mod_id', Text(50), nullable = False),
    Column('last_mod_date', Text(50), nullable = False),
    Column('subject', String(50), nullable = False),
    Column('description', Text(50), nullable = False),
    Column('operator', String(50), nullable = True),
    
)

AllNighter = Table(
    'AllNighter', meta,
    Column('id_allnighter', Integer, primary_key = True),
    Column('public_id_allnighter', String(50), unique = True),
    Column('request_date', Text(50), nullable = False),
    Column('reserved_date', Text(50), nullable = False),
    Column('last_mod_id', Text(50), nullable = False),
    Column('last_mod_date', Text(50), nullable = False),
    Column('subject', String(50), nullable = False),
)

InventoryReport = Table(
    'InventoryReport', meta,
    Column('id_report', Integer, primary_key = True),
    Column('public_id_report', String(50), unique = True),
    Column('date', Text(50), nullable = False),
    Column('complete_computers', Integer, nullable = False),
    Column('incomplete_computers', Integer, nullable = False),
    Column('number_projectors', Integer, nullable = False),
    Column('number_chairs', Integer, nullable = False),
    Column('number_projectors', Integer, nullable = False),
    Column('number_fire_extinguishers', Integer, nullable = False),

)

FaultStatus = Table(
    'FaultStatus', meta,
    Column('id_status', Integer, primary_key = True),
    Column('status', String(50), nullable= False),
)

FaultReport = Table(
    'FaultReport', meta,
    Column('id_report', Integer, primary_key = True),
    Column('public_id_report', String(50), unique = True),
    Column('date_time', Text(50), nullable = False),
    Column('id_faulty_part', String(50), nullable = False),
    Column('description', Text(50), nullable = False),
    Column('id_status', Integer, ForeignKey('FaultStatus.id_status'), nullable = False),
    
)

Worklog = Table(
    'Worklog', meta,
    Column('id_worklog', Integer, primary_key = True),
    Column('public_id_worklog', String(50), unique = True),
    Column('date_time', String(50), nullable = False),
    Column('init_time', String(50), nullable = False),
    Column('final_time', String(50), nullable = False),
    Column('description', Text(50), nullable = False),
 
)

Lab = Table(
    'Lab', meta,
    Column('id_lab', Integer, primary_key = True),
    Column('public_id_lab', String(50), unique = True),
    Column('name', String(50), nullable = False),
    Column('capacity', Integer, nullable = False),
)

Evaluation = Table(
    'Evaluation', meta,
    Column('id_evaluation', Integer, primary_key = True),
    Column('date', String(50), nullable = False),
    Column('score', Integer, nullable = False),
    Column('comment', String(50), nullable = False),

)

Event = Table(
    'Event', meta,
    Column('id_event', Integer, primary_key = True),
    Column('description', Text(50), nullable = False),
    Column('init_time', String(50), nullable = False),
    Column('final_time', String(50), nullable = False),
    Column('week_day', String(10), nullable = False),
    Column('is_repeatable', Boolean, nullable = False),
)

Course = Table(
    'Course', meta,
    Column('id_course', Integer, primary_key = True),
    Column('code', String(50), nullable = False),
    Column('name', String(50), nullable = False),
    Column('group', String(50), nullable = False),
)

User_Reservation = Table(
    'User_Reservation', meta,
    Column('id_reservation', Integer, ForeignKey('Reservation.id_reservation'), nullable = False),
    Column('id_user', Integer, ForeignKey('User.id_user'), nullable = False)
)                               

Reservation_Lab = Table(
    'Reservation_Lab', meta,
    Column('id_reservation', Integer, ForeignKey('Reservation.id_reservation'), nullable = False),
    Column('id_lab', Integer, ForeignKey('Lab.id_lab'), nullable = False)
)

User_Operator = Table(
    'User_Operator', meta,
    Column('id_user', Integer, ForeignKey('User.id_user'), nullable = False),
    Column('approved_hours', Integer, nullable = False)
)

FaultReport_Lab = Table(
    'FaultReport_Lab', meta,
    Column('id_report', Integer, ForeignKey('FaultReport.id_report'), nullable = False),
    Column('id_lab', Integer, ForeignKey('Lab.id_lab'), nullable = False)
)

User_Worklog = Table(
    'User_Worklog', meta,
    Column('id_worklog', Integer, ForeignKey('Worklog.id_worklog'), nullable = False),
    Column('id_user', Integer, ForeignKey('User.id_user'), nullable = False)
)

InventoryReport_Lab = Table(
    'InventoryReport_Lab', meta,
    Column('id_report', Integer, ForeignKey('InventoryReport.id_report'), nullable = False),
    Column('id_lab', Integer, ForeignKey('Lab.id_lab'), nullable = False)
)

User_FaultReport = Table(
    'User_FaultReport', meta,
    Column('id_report', Integer, ForeignKey('FaultReport.id_report'), nullable = False),
    Column('id_user', Integer, ForeignKey('User.id_user'), nullable = False)
)

AllNighter_Lab = Table(
    'AllNighter_Lab', meta,
    Column('id_lab', Integer, ForeignKey('Lab.id_lab'), nullable = False),
    Column('id_allnighter', ForeignKey('AllNighter.id_allnighter'), nullable = False)
)

User_AllNighter = Table(
    'User_AllNighter', meta,
    Column('id_user', Integer, ForeignKey('User.id_user'), nullable = False),
    Column('id_allnighter', ForeignKey('AllNighter.id_allnighter'), nullable = False) 
)

User_InventoryReport = Table(
    'User_InventoryReport', meta,
    Column('id_user', Integer, ForeignKey('User.id_user'), nullable = False),
    Column('id_report', Integer, ForeignKey('InventoryReport.id_report'), nullable = False)
)

meta.create_all(engine)

conn = engine.connect()

conn.execute(User_Type.insert(),
    [
   {'id_user_type':'1','user_type':'Administrator'},
   {'id_user_type':'2','user_type':'Admin. Assistant'},
   {'id_user_type':'3','user_type':'Operator'},
   {'id_user_type':'4','user_type':'Professor'},
   {'id_user_type':'5','user_type':'Administrative'}
   ])

conn.close()

print("The database was successfully created")