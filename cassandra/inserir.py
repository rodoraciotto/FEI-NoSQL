import psycopg2
from time import sleep
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv

load_dotenv()

session = Cluster(
    cloud={
			"secure_connect_bundle": 'Caminho/para/o/Secure/.zip',
			'connect_timeout': 30
		},
    auth_provider=PlainTextAuthProvider("Token", 'AstraTokenPassword'),
).connect()

print(f"Cassandra: {session}")

dept = """create table default_keyspace.department(
	dept_name		text, 
	 building		text, 
	 budget		    int,
     curso_id   text,
	 ctitle 	text,
	 primary key ((dept_name), curso_id)
);"""

secass = """create table default_keyspace.section
	(curso_id		text, 
	 ctitle 	text,
	 dept_name 		text,
	 semester		text,
	 year			int, 
	 building		text,
	 room_number	int,
	 prof_name 		text,
	 primary key ((curso_id), semester, year)
	);"""

coursestdcass = """create table default_keyspace.studdentcourse
	(curso_id		text, 
	 ctitle			text,
	 credits		int,
	 name 			text,
	 primary key ((curso_id), name)
);"""

profcass = """create table default_keyspace.instructor
	(ID 			text,
	 name			text, 
	 dept_name		text, 
	 salary			int,
	 orienta 		text,
	 primary key ((ID), orienta)
	);"""

stdcass = """create table default_keyspace.student
	(ID			text, 
	 name			text, 
	 dept_name		text, 
	 tot_cred		int,
	 primary key (ID)
	)"""

classcass = """create table default_keyspace.classroom
	(building		text,
	 room_number	text,
	 capacity		int,
	 primary key (building, room_number)
	);"""

coursecass = """create table default_keyspace.course
	(curso_id		text, 
	 title			text, 
	 credits		int,
	 prereq_id 		text,
	 primary key ((curso_id), prereq_id),
	);"""

tabelascass = [secass, coursestdcass, profcass, stdcass, classcass, coursecass]

dept = """select d.dept_name, d.building, d.budget , c.title , c.course_id from bd2.department d inner join bd2.course c on d.dept_name = c.dept_name;"""
section = """Select distinct c.course_id,  c.title, c.dept_name,  s.semester , s.year , cl.building,  cl.room_number, i.name  from bd2.section s
left join bd2.teaches t on t.sec_id = s.sec_id and t.semester = s.semester and t.year = s.year and s.course_id = t.course_id
left join bd2.course c on c.course_id = s.course_id
left join bd2.instructor i on i.ID = t.ID
inner join bd2.classroom cl on cl.room_number = s.room_number
order by s.semester, s.year """
stdcourse = """Select t.course_id , c.title, c.credits , s.name from bd2.student s
left join bd2.takes t on t.id = s.id
left join bd2.course c on c.course_id = t.course_id
where t.course_id is not NULL"""
inst = """select i.id, i.name, i.dept_name, i.salary, s.name from bd2.instructor i
left join bd2.advisor a on a.i_id = i.id
left join bd2.student s on s.id = a.s_id"""
stud = """select s.id, s.name, s.dept_name, s.tot_cred from bd2.student s"""
clas = """select c.building, c.room_number, c.capacity from bd2.classroom c"""
course = """select c.course_id, c.title, c.credits, p.prereq_id from bd2.course c
left join bd2.prereq p on p.course_id = c.course_id"""

def criartables():
	try:
		for i in tabelascass:
			session.execute(i)
		# session.execute(tabelascass[-1])
		print(f"Tabelas criadas")
	except Exception as e:
		print(f"erro: {e}")

def Inserir(sql , cass):
	try:
		conn = psycopg2.connect(
			host="motty.db.elephantsql.com",
			database="aakuknty",
			user="aakuknty",
			password="urFy-riYIFUDDQmIaENzvOkIyJLqUzsf"
		)
		cursor = conn.cursor()
		
		cursor.execute(sql)
		count = 0
		session.execute(f"truncate default_keyspace.{cass};")
		print(cursor)
		for i in cursor.fetchall():
			print(count, i)
			if "department" == cass:
				values = f"insert into default_keyspace.department(dept_name, building, budget, ctitle, curso_id) values ('{i[0]}', '{i[1]}', {int(i[2])}, '{i[3]}', '{i[4]}');"			
			elif "section" == cass:
				values = f"insert into default_keyspace.section(curso_id, ctitle, dept_name, semester, year, building, room_number, prof_name) values ('{i[0]}', '{i[1]}', '{i[2]}' , '{i[3]}', {int(i[4])}, '{i[5]}', {int(i[6])}, '{i[7]}');"
			elif "studdentcourse" == cass:
				values = f"insert into default_keyspace.studdentcourse(curso_id, ctitle, credits, name) values ('{i[0]}', '{i[1]}', {int(i[2])}, '{i[3]}');"
			elif "instructor" == cass:
				values = f"insert into default_keyspace.instructor(ID, name, dept_name, salary, orienta) values ('{i[0]}', '{i[1]}', '{i[2]}', {int(i[3])}, '{i[4]}');"
			elif "student" == cass:
				values = f"insert into default_keyspace.student(ID, name, dept_name, tot_cred) values ('{i[0]}', '{i[1]}', '{i[2]}', {int(i[3])});"
			elif "classroom" == cass:
				values = f"insert into default_keyspace.classroom(building, room_number, capacity) values ('{i[0]}', '{i[1]}', {int(i[2])});"
			elif "course" == cass:
				values = f"insert into default_keyspace.course(curso_id, title, credits, prereq_id) values ('{i[0]}', '{i[1]}', {int(i[2])}, '{i[3]}');"

			resposta = session.execute(values)
			print(resposta)
			count += 1
			sleep(1)
			# print(type(float(i[2])))
		# result = 

	except Exception as e:
		print(f"erro: {e}")
        
# criartables()
#Inserir(dept, "department")
#Inserir(section, "section")
# Inserir(stdcourse, "studdentcourse")
# Inserir(inst, "instructor")
# Inserir(stud, "student")
# Inserir(course, "course")
Inserir(clas, "classroom")



