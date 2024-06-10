import psycopg2
from time import sleep
from neo4j import GraphDatabase
import os

instructor = "select * from bd2.instructor;"
student = "select * from bd2.student;"
course = "select * from bd2.course;"
section = "select * from bd2.section;"
teaches = "select * from bd2.teaches;"
takes = "select * from bd2.takes;"
advisor = "select * from bd2.advisor;"
prereq = "select * from bd2.prereq;"
department = "select * from bd2.department;"
classroom = "select * from bd2.classroom;"

def inserir(querysql, driver):

    conn = psycopg2.connect(
			host="motty.db.elephantsql.com",
			database="aakuknty",
			user="aakuknty",
			password="urFy-riYIFUDDQmIaENzvOkIyJLqUzsf"
		)
    cursor = conn.cursor()
    cursor.execute(querysql)
    print("inserindo: ", querysql)
    for i in cursor.fetchall():
        print(i)
        if "instructor" in querysql:
            driver.execute_query("CREATE (:instructor { id: '" + i[0] + "', name: '" + i[1] + "', dept_name: '" + i[2] + "', salary: " + str(i[3]) + "});")
        elif "student" in querysql:
            driver.execute_query("CREATE (:student { id: '" + i[0] + "', name: '" + i[1] + "', dept_name: '" + i[2] + "', tot_cred: " + str(i[3]) + "});")
        elif "course" in querysql:
            driver.execute_query("CREATE (:course { course_id: '" + i[0] + "', title: '" + i[1] + "', dept_name: '" + i[2] + "', credits: " + str(i[3]) + "});")
        elif "section" in querysql:
            driver.execute_query("CREATE (:section { course_id: '" + i[0] + "', sec_id: '" + i[1] + "', semester: '" + i[2] + "', year: " + str(i[3]) + ", building: '" + i[4] + "', room_number: " + str(i[5]) + ", time_slot_id: '" + str(i[6]) + "'});")
        elif "department" in querysql:
            driver.execute_query("CREATE (:department { dept_name: '" + i[0] + "', building: '" + i[1] + "', budget: " + str(i[2]) + "});")
        elif "classroom" in querysql:
            driver.execute_query("CREATE (:classroom { building: '" + i[0] + "', room_number: '" + i[1] + "', capacity: " + str(i[2]) + "});")
        elif "teaches" in querysql:
            driver.execute_query("MATCH (i:instructor { id: '" + i[0] + "'}), (s:section { course_id: '" + i[1] + "', sec_id: '" + i[2] + "', semester: '" + i[3] + "', year: " + str(i[4]) + "}) CREATE (i)-[:TEACHES]->(s);")
        elif "takes" in querysql:
            driver.execute_query("MATCH (s:student { id: '" + i[0] + "'}), (t:section { course_id: '" + i[1] + "', sec_id: '" + i[2] + "', semester: '" + i[3] + "', year: " + str(i[4]) + "}) CREATE (s)-[:TAKES]->(t);")
        elif "advisor" in querysql:
            driver.execute_query("MATCH (s:student { id: '" + i[0] + "'}) set s.advisor = '" + i[1] + "'")
        elif "prereq" in querysql:
            driver.execute_query("MATCH (c:course { course_id: '" + i[0] + "'}), (p:course { course_id: '" + i[1] + "'}) CREATE (c)-[:PREREQ]->(p);")
        
        sleep(3)
    
    cursor.close()

def inserirdepois(querysql, driver):
    conn = psycopg2.connect(
            host="motty.db.elephantsql.com",
            database="aakuknty",
            user="aakuknty",
            password="urFy-riYIFUDDQmIaENzvOkIyJLqUzsf"
            )
    cursor = conn.cursor()
    cursor.execute(querysql)
    print("inserindo: ", querysql)
    for i in cursor.fetchall():
        if "section" in querysql:
            driver.execute_query("MATCH (c:classroom { building: '" + i[4] + "', room_number: " + str(i[5]) + "}) MATCH (s:section { sec_id: " + str(i[1]) + ", course_id: '" + i[0] + "', semester: '" + i[2] + "', year: " + str(i[3]) + " }) CREATE (c)-[:CLASSROOM_SECTION]->(s);")
            sleep(4)
            driver.execute_query("MATCH (s:section { sec_id: " + str(i[1]) + ", course_id: '" + i[0] + "', semester: '" + i[2] + "', year: " + str(i[3]) + " }) MATCH (c:course { course_id: '" + i[0] + "' }) CREATE (s)-[:SECTION_COURSE]->(c);")
        elif "instructor" in querysql:
            driver.execute_query("MATCH (i:instructor { id: '" + i[0] + "' }) MATCH (d:department { dept_name: '" + i[2] + "' }) CREATE (i)-[:INSTRUCTOR_DEPARTMENT]->(d);")
        elif "student" in querysql:
            driver.execute_query("MATCH (s:student { id: '" + i[0] + "' }) MATCH (d:department { dept_name: '" + i[2] + "' }) CREATE (s)-[:STUDENT_DEPARTMENT]->(d);")
        elif "course" in querysql:
            driver.execute_query("MATCH (c:course { course_id: '" + i[0] + "', title: '" +i[1]+"' }) MATCH (d:department { dept_name: '" + i[2] + "' }) CREATE (c)-[:COURSE_DEPARTMENT]->(d);")
        sleep(1)

with GraphDatabase.driver("neo4jLink", auth=("neo4jUSer", "neo4jPassword")) as driver:
    driver.verify_connectivity()
    print("Conectado ao banco de dados Neo4j")
    sleep(1)
    inserir(instructor, driver)
    inserir(student, driver)
    inserir(course, driver)
    inserir(section, driver)
    inserir(department, driver)
    inserir(classroom, driver)
    inserir(teaches, driver)
    inserir(takes, driver)
    inserir(advisor, driver)
    driver.execute_query("MATCH (ins:instructor), (s:student) where ins.id = s.advisor CREATE (ins)-[:ADVISOR]->(s);")
    inserir(prereq, driver)
    inserirdepois(section, driver)
    inserirdepois(instructor, driver)
    inserirdepois(student, driver)
    inserirdepois(course, driver)
    sleep(1)
    print("Inserção de dados no banco de dados Neo4j concluída")
