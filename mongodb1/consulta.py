from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

url = "linkDoMongo"

client = MongoClient(url, server_api=ServerApi('1'))
db = client.projeto2

# semestres disponíveis: Fall, Spring, Summer
# anos disponíveis: 2017, 2018
# departamentos disponíveis: "Comp. Sci.", "History", 
# "Physics", "Biology", "Music", "Elec. Eng.", "Finance"

# Send a ping to confirm a successful connection
try:
	client.admin.command('ping')
	print("Pinged your deployment. You successfully connected to MongoDB!\n")
except Exception as e:
	print(e)


def q1(dept):
	try:
		print("1) Listar todos os cursos oferecidos por um determinado departamento")

		# busca no mongodb o departamento
		departamento = db.department.find_one({"dept_name": dept})
		# print(departamento)
		print("DEPARTAMENTO: ", departamento["dept_name"])
		for cursoId in departamento["courseid"]:
				cursos = db.course.find_one({ '_id': cursoId })
				print("curso: ", cursos['title'])
	except Exception as e:
		print(f"F: {e}")

def q2(dept, year, semester):
	print("2) Recuperar todas as disciplinas de um curso específico em um determinado semestre")

	# busca no mongodb o section
	sections = db.section.find_one({ "semester": semester, "year": year})

	print(f"Cursos do departamento {dept} no semestre {semester} de {year}:")
	# print("semestre: ", sections["classcourse"])
	for turma in sections["classcourse"]:
		curso = db.course.find_one({ '_id': turma["course_id"] })
		if curso["deptname"] == dept:
			print("curso: ", curso["title"])
		
def q3(título):

	print("3) Encontrar todos os estudantes que estão matriculados em um curso específico")

	curso = db.course.find_one({ "title": título })

	print(f"Alunos matriculados no curso de {título}")
	for alunos in curso["alunosid"]:
		student = db.student.find_one({ '_id': alunos })
		print(student["name"])

def q4(dept):
	print("4) Listar a média de salários de todos os professores em um determinado departamento")
	salarios = []

	professores = db.instructor.find({"dept_name": dept})

	for p in professores:
		# print(p['salary'])
		salarios.append(p['salary'])

	print(f"Média de salários od professores do departamento de {dept}: {sum(salarios)/len(salarios)}")

def q5(aluno):
	print("5) Recuperar o número total de créditos obtidos por um estudante específico")

	student = db.student.find_one({ "name": aluno })
	

	#a mesma forma funciona para o object id pensando em uma base de dados maior
	#student = db.student.find_one({ "_id": ObjectId('6621b810da2ac8848438cd13') })
	print(f"Créditos obtidos por {student['name']}: {student['tot_cred']}")

def q6(prof, semester, year):
	print("6) Encontrar todas as disciplinas ministradas por um professor em um semestre específico")

	section = db.section.find_one({ "semester": semester, "year": year })

	print(f"Disciplinas ministradas pelo professor {prof} no semestre {semester} de {year}:")
	for turma in section["classcourse"]:
		# print(turma['prof_id'])
		professor = db.instructor.find_one({ '_id': turma['prof_id'] })
		curso = db.course.find_one({ '_id': turma["course_id"] })
		if professor["name"] == prof:
			print("curso: ", curso["title"])

def q7(prof):
	print("7) Listar todos os estudantes que têm um determinado professor como orientador")


	professor = db.instructor.find_one({ "name":  prof})
	
	print(f"Orientandos do professor {prof}:")
	for aluno in professor["orientandos"]:
		student = db.student.find_one({ '_id': aluno })
		print(student["name"])

def q8():
	print("8) Recuperar todas as salas de aula sem um curso associado")

	section = db.section.find()
	salas = db.classroom.find()

	cursosala = []
	semcurso = []
	for s in section:
		for turma in s["classcourse"]:
			cursosala.append(turma["class_id"])

	for c in salas:
		semcurso.append(c["_id"])

	for k in semcurso:
		if k in cursosala:
			semcurso.remove(k)
	
	
	print("Salas sem curso associado:")

	for i in semcurso:
		sala = db.classroom.find_one({ '_id': i })
		print(sala["name"])
	
def q9(tit):
	print("9) Encontrar todos os pré-requisitos de um curso específico")

	curso = db.course.find_one({"title": tit})

	print(f"Pré-requisitos do curso {curso['title']}:")

	for i in curso["prereq_id"]:
		c = db.course.find_one({"_id": i})
		print(c["title"])

def q10():
	print("10) Recuperar a quantidade de alunos orientados por cada professor")

	profs = db.instructor.find()

	for p in profs:
		print(f"O professor {p['name']} tem {len(p['orientandos'])} alunos orientados")


q1("Biology")
print()
q2("Comp. Sci.", 2018, "Spring")
print()
q3("Intro. to Computer Science")
print()
q4("Comp. Sci.")
print()
q5("Zhang")
print()
q6("Katz", "Spring", 2018)
print()
q7("Katz")
print()
q8()
print()
q9("Intro. to Digital Systems")
print()
q10()
