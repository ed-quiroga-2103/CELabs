from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Text, BigInteger
from sqlalchemy import ForeignKey
import uuid


file = open('D:\\Documents\\Espe\\CELabs\\Web Service\\CELabs.db', 'w+')
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
    Column('request_date', BigInteger, nullable = False),
    Column('requested_date', BigInteger, nullable = False),
    Column('init_time', BigInteger, nullable = False),
    Column('final_time', BigInteger, nullable = False),
    Column('last_mod_id', Text(50), nullable = False),
    Column('last_mod_date', BigInteger, nullable = False),
    Column('subject', String(50), nullable = False),
    Column('description', Text(50), nullable = False),
    Column('operator', Integer, ForeignKey('User.id_user'), nullable = False),
)

AllNighter = Table(
    'AllNighter', meta,
    Column('id_allnighter', Integer, primary_key = True),
    Column('public_id_allnighter', String(50), unique = True),
    Column('request_date', BigInteger, nullable = False),
    Column('requested_date', BigInteger, nullable = False),
    Column('last_mod_id', Text(50), nullable = False),
    Column('last_mod_date', BigInteger, nullable = False),
    Column('subject', String(50), nullable = False),
    Column('state', Integer, nullable = False)
)

InventoryReport = Table(
    'InventoryReport', meta,
    Column('id_report', Integer, primary_key = True),
    Column('public_id_report', String(50), unique = True),
    Column('date', BigInteger, nullable = False),
    Column('complete_computers', Integer, nullable = False),
    Column('incomplete_computers', Integer, nullable = False),
    Column('number_projectors', Integer, nullable = False),
    Column('number_chairs', Integer, nullable = False),
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
    Column('date_time', BigInteger, nullable = False),
    Column('id_fault_part', String(50), nullable = False),
    Column('description', Text(50), nullable = False),
    Column('id_status', Integer, ForeignKey('FaultStatus.id_status'), nullable = False),
    
)

Worklog = Table(
    'Worklog', meta,
    Column('id_worklog', Integer, primary_key = True),
    Column('public_id_worklog', String(50), unique = True),
    Column('date_time', BigInteger, nullable = False),
    Column('init_time', BigInteger, nullable = False),
    Column('final_time', BigInteger, nullable = False),
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
    Column('init_time', BigInteger, nullable = False),
    Column('final_time', BigInteger, nullable = False),
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
    Column('approved_hours', Integer, nullable = False),
    Column('pending_hours', Integer, nullable = False)
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
    ]
)


conn.execute(Lab.insert(),
    [
        {
            'id_lab': '1', 'public_id_lab': str(uuid.uuid4()), 'name': 'F2-09', 'capacity': 25
        },
        {
            'id_lab': '2', 'public_id_lab': str(uuid.uuid4()), 'name': 'F2-10', 'capacity': 25
        }
    ]
)

conn.execute(User.insert(),
    [
        {'id_user': 1, 'public_id_user': str(uuid.uuid4()), 'name': 'Op', 'lastname1': 'Op', 'lastname2':'Op', 'id_number':'Op',
        'password':'Op', 'email':'Op', 'phone_number':'Op', 'active': 1, 'university_id':'Op', 'user_type':3},
        {'id_user': 2, 'public_id_user': str(uuid.uuid4()), 'name': 'Prof', 'lastname1': 'Prof', 'lastname2':'Prof', 'id_number':'Prof',
        'password':'Prof', 'email':'Prof', 'phone_number':'Prof', 'active': 1, 'university_id':'Prof', 'user_type':4}
    ]
)

conn.close()

print("The database was successfully created")