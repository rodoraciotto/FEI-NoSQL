from time import sleep
from neo4j import GraphDatabase
import os

def q1(driver, dept):
    print("1. Listar todos os cursos oferecidos por um determinado departamento\n")
    query = "MATCH (:department {dept_name: 'Comp. Sci.'})--(c:course) RETURN c.title;"
    result, summary, keys = driver.execute_query(query)
    for item in result:
        print(f"Departamento: {dept} - Curso: {item[0]}")

def q2(driver, dept, semester, year):
    print("2. Recuperar todas as disciplinas de um curso específico em um determinado semestre")
    query = "MATCH (n:section{ year: "+str(year)+", semester: '"+semester+"' }) RETURN n.course_id;"
    result, summary, keys = driver.execute_query(query)
    for item in result:
        query = "MATCH (n:course{course_id: '"+item[0]+"'}) RETURN n.dept_name;"
        result, summary, keys = driver.execute_query(query)
        if result[0][0] == dept:
            print(f"Departamento: {dept} - Curso: {item[0]} - Semestre: {semester} - Ano: {year}")

def q3(driver, cursoid):
    print("3. Encontrar todos os estudantes que estão matriculados em um curso específico")
    query = "MATCH p=(a:student)-[:TAKES]->(s:section) where s.course_id = '"+cursoid+"' RETURN a.name;"
    result, summary, keys = driver.execute_query(query)
    for item in result:
        print(f"Curso: {cursoid} - Estudante: {item[0]}")

def q4(driver, dept):
    print("4. Listar a média de salários de todos os professores em um determinado departamento")
    query = "MATCH (n:instructor{dept_name: '"+dept+"'}) RETURN avg(n.salary);"
    result, summary, keys = driver.execute_query(query)
    print(f"Departamento: {dept} - Média de salários: {result[0][0]}")

def q5(driver, student):
    print("5. Recuperar o número total de créditos obtidos por um estudante específico")
    query = "MATCH (n:student{name: '"+student+"'}) RETURN n.tot_cred;"
    result, summary, keys = driver.execute_query(query)
    print(f"Estudante: {student} - Total de créditos: {result[0][0]}")

def q6(driver, prof, semester, year):
    print("6. Encontrar todas as disciplinas ministradas por um professor em um semestre específico")
    query = "MATCH p=(i:instructor)-[:TEACHES]->(s:section) where i.name = '"+prof+"' and s.semester='"+semester+"' and s.year = "+str(year)+" RETURN s.course_id ;"
    result, summary, keys = driver.execute_query(query)
    for item in result:
        print(f"Professor: {prof} - Disciplina: {item[0]} - Semestre: {semester} - Ano: {year}")

def q7(driver, prof):
    print("7. Listar todos os estudantes que têm um determinado professor como orientador")
    query = "MATCH p=(i:instructor {name: '"+prof+"'})-[:ADVISOR]->(s:student) RETURN s.name;"
    result, summary, keys = driver.execute_query(query)
    print(f"Professor: {prof}")
    for item in result:
        print(f"Orienta: {item[0]}")

def q8(driver):
    print("8. Recuperar todas as salas de aula sem um curso associado")
    query = "MATCH (n:classroom) RETURN n.room_number;"
    salas =[]
    result, summary, keys = driver.execute_query(query)
    for item in result:
        salas.append(item[0])
    print(f"Salas de aula: {salas}")
    query = "MATCH (n:section) RETURN DISTINCT n.room_number;"
    for item in result:
        salas.remove(item[0])
    print(f"Salas de aula sem curso associado: {salas}")

def q9(driver,cursoid):
    print("9. Encontrar todos os pré-requisitos de um curso específico")
    query = "MATCH p=(c:course {course_id: '"+cursoid+"'})-[:PREREQ]->(r:course) RETURN r.title LIMIT 25;"
    result, summary, keys = driver.execute_query(query)
    print(f"Curso: {cursoid}")
    for item in result:
        print(f"Pré-requisito: {item[0]}")

def q10(driver):
    print("10. Recuperar a quantidade de alunos orientados por cada professor")
    query = "MATCH p=(i:instructor)-[:ADVISOR]->(s:student) RETURN i.name, count(s);"
    result, summary, keys = driver.execute_query(query)
    for item in result:
        print(f"Professor: {item[0]} - Orienta: {item[1]}")

with GraphDatabase.driver("neo4jLink", auth=("neo4jUser", "neo4jPassword")) as driver:
    driver.verify_connectivity()
    print("Conectado ao banco de dados Neo4j")
    q1(driver, "Comp. Sci.")
    q2(driver, 'Comp. Sci.' ,'Fall', 2017 )
    q3(driver, "CS-347")
    q4(driver, "Comp. Sci.")
    q5(driver, "Zhang")
    q6(driver, "Srinivasan", "Fall", 2017)
    q7(driver, "Einstein")
    q8(driver)
    q9(driver ,"CS-347")
    q10(driver)
