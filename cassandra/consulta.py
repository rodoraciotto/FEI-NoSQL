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

def q1(dept):
    print("1. Listar todos os cursos oferecidos por um determinado departamento\n")
    query = f"select ctitle from default_keyspace.department where dept_name = '{dept}' ALLOW FILTERING;"
    print(f"Cursos do departamento de {dept}:\n")
    for row in session.execute(query):
        print(row[0])

def q2(dept, semester, year):
    print("2. Recuperar todas as disciplinas de um curso específico em um determinado semestre")
    query = f"select ctitle from default_keyspace.section where dept_name = '{dept}'  and semester = '{semester}' and year = {year} ALLOW FILTERING;"

    print(f"Disciplinas do curso de {dept} no semestre de {semester} de {year}:\n")
    for row in session.execute(query):
        print(row[0])

def q3(titulo):
    print("3. Encontrar todos os estudantes que estão matriculados em um curso específico")
    query = f"select name from default_keyspace.studdentcourse where ctitle = '{titulo}' ALLOW FILTERING;"
    print(f"Estudantes do curso de {titulo}:\n")
    for row in session.execute(query):
        print(row[0])

def q4(dept):
    print("4. Listar a média de salários de todos os professores em um determinado departamento")
    query = f"select avg(salary) from default_keyspace.instructor where dept_name = '{dept}' ALLOW FILTERING;"

    print(f"Média de salários dos professores de {dept}:\n")
    for row in session.execute(query):
        print(row[0])

def q5(student):
    print("5. Recuperar o número total de créditos obtidos por um estudante específico")
    query = f"select tot_cred from default_keyspace.student where name = '{student}' ALLOW FILTERING;"
    print(f"Total de créditos do estudante {student}:\n")
    for row in session.execute(query):
        print(row[0])

def q6(prof, semester, year):
    print("6. Encontrar todas as disciplinas ministradas por um professor em um semestre específico")
    query = f"select ctitle from default_keyspace.section where semester = '{semester}' and year = {year} and prof_name = '{prof}' ALLOW FILTERING;"
    print(f"Disciplinas ministradas pelo professor {prof} no {semester} de Fall de {year}:\n")
    for row in session.execute(query):
        print(row[0])
    
def q7(prof):
    print("7. Listar todos os estudantes que têm um determinado professor como orientador")
    
    query = f"select orienta from default_keyspace.instructor where name = '{prof}' ALLOW FILTERING;"

    print(f"Estudantes orientados pelo professor {prof}:\n")
    for row in session.execute(query):
        if(row[0] != None):
            print(row[0])

def q8():
    print("8. Recuperar todas as salas de aula sem um curso associado")
    query = f"select room_number from default_keyspace.classroom"
    salas = []
    print(f"Salas de aula sem curso associado:\n")
    for row in session.execute(query):
        salas.append(int(row[0]))
    query = f"select room_number from default_keyspace.section"
    for row in session.execute(query):
        if row[0] not in salas:
            print(row[0])

    print("não possui salas de aula sem curso associado")
def q9(cursoid):
    print("9. Encontrar todos os pré-requisitos de um curso específico")
    query = f"select prereq_id from default_keyspace.course where curso_id = '{cursoid}';"
    print(f"Pré-requisitos do curso {cursoid}:\n")
    for row in session.execute(query):
        print(row[0])

def q10():
    print("10. Recuperar a quantidade de alunos orientados por cada professor")
    query = f"select name, count(orienta) from default_keyspace.instructor group by id;"
    print(f"Quantidade de alunos orientados por cada professor:\n")
    for row in session.execute(query):
        print(row[0], row[1])

q1('Comp. Sci.')
q2('Comp. Sci.' ,'Fall', 2017 )
q3('Database System Concepts')
q4('Comp. Sci.')
q5('Zhang')
q6('Srinivasan','Fall', 2017)
q7('Einstein')
q8()
q9('CS-347')
q10()

