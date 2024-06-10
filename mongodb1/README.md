# Projeto 2

Uso dos arquivos .sql para fazer a inserção no mongodb, para a inserção foi feito a mão todas as collections podendo ser vista no arquivo txt jsonmongodb.txt

Foram feitas pesquisas no banco para inserção melhor dos dados, tais como:

- Collection Section: 
``` 
Select distinct s.semester , s.year , c.title , s.room_number, i.name from bd2.section s
left join bd2.teaches t on t.sec_id = s.sec_id and t.semester = s.semester and t.year = s.year and s.course_id = t.course_id
left join bd2.course c on c.course_id = s.course_id
inner join bd2.instructor i on i.ID = t.ID
order by s.semester 
```
- Collection Departmant:
```
select c.course_id, c.dept_name from bd2.course c
order by c.dept_name
```
- Collection Course:
```
select s.name,t.course_id, c.title, t.semester, t.year from  bd2.student as s
join bd2.takes t on t.ID = s.id 
join bd2.course c on c.course_id = t.course_id
where t.ID = s.id and c.course_id = t.course_id
order by s.name
```
- As outras colections foram feitas convertendo queries de inserção do sql para o formato json

A resolução está feita das 10 queries pedidas está contida em consulta.py cada uma em uma função, basta descomentar


