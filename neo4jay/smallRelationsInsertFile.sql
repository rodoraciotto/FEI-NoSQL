delete from bd2.prereq;
delete from bd2.time_slot;
delete from bd2.advisor;
delete from bd2.takes;
delete from bd2.student;
delete from bd2.teaches;
delete from bd2.section;
delete from bd2.instructor;
delete from bd2.course;
delete from bd2.department;
delete from bd2.classroom;

--(building, num, capacity)
insert into bd2.classroom values ('Packard', '101', '500');
insert into bd2.classroom values ('Painter', '514', '10');
insert into bd2.classroom values ('Taylor', '3128', '70');
insert into bd2.classroom values ('Watson', '100', '30');
insert into bd2.classroom values ('Watson', '120', '50');

--(deptname, building, bugdet)
insert into bd2.department values ('Biology', 'Watson', '90000');
insert into bd2.department values ('Comp. Sci.', 'Taylor', '100000');
insert into bd2.department values ('Elec. Eng.', 'Taylor', '85000');
insert into bd2.department values ('Finance', 'Painter', '120000');
insert into bd2.department values ('History', 'Painter', '50000');
insert into bd2.department values ('Music', 'Packard', '80000');
insert into bd2.department values ('Physics', 'Watson', '70000');

--(course_id, title, deptname, credit)
insert into bd2.course values ('BIO-101', 'Intro. to Biology', 'Biology', '4');
insert into bd2.course values ('BIO-301', 'Genetics', 'Biology', '4'); --introbio
insert into bd2.course values ('BIO-399', 'Computational Biology', 'Biology', '3'); --introbio
insert into bd2.course values ('CS-101', 'Intro. to Computer Science', 'Comp. Sci.', '4');
insert into bd2.course values ('CS-190', 'Game Design', 'Comp. Sci.', '4'); --introcs
insert into bd2.course values ('CS-315', 'Robotics', 'Comp. Sci.', '3'); --introcs
insert into bd2.course values ('CS-319', 'Image Processing', 'Comp. Sci.', '3'); --introcs
insert into bd2.course values ('CS-347', 'Database System Concepts', 'Comp. Sci.', '3'); --introcs
insert into bd2.course values ('EE-181', 'Intro. to Digital Systems', 'Elec. Eng.', '3'); --phypri
insert into bd2.course values ('FIN-201', 'Investment Banking', 'Finance', '3');
insert into bd2.course values ('HIS-351', 'World History', 'History', '3');
insert into bd2.course values ('MU-199', 'Music Video Production', 'Music', '3');
insert into bd2.course values ('PHY-101', 'Physical Principles', 'Physics', '4');

--(i_id, name, dept_name, salary)
insert into bd2.instructor values ('10101', 'Srinivasan', 'Comp. Sci.', '65000'); 
insert into bd2.instructor values ('12121', 'Wu', 'Finance', '90000');
insert into bd2.instructor values ('15151', 'Mozart', 'Music', '40000');
insert into bd2.instructor values ('22222', 'Einstein', 'Physics', '95000');
insert into bd2.instructor values ('32343', 'El Said', 'History', '60000');
insert into bd2.instructor values ('33456', 'Gold', 'Physics', '87000');
insert into bd2.instructor values ('45565', 'Katz', 'Comp. Sci.', '75000');
insert into bd2.instructor values ('58583', 'Califieri', 'History', '62000');
insert into bd2.instructor values ('76543', 'Singh', 'Finance', '80000');
insert into bd2.instructor values ('76766', 'Crick', 'Biology', '72000');
insert into bd2.instructor values ('83821', 'Brandt', 'Comp. Sci.', '92000');
insert into bd2.instructor values ('98345', 'Kim', 'Elec. Eng.', '80000');

--(course_id, sec_id, semester, year, building, room_num,time_slot_id)
insert into bd2.section values ('BIO-101', '1', 'Summer', '2017', 'Painter', '514', 'B');
insert into bd2.section values ('BIO-301', '1', 'Summer', '2018', 'Painter', '514', 'A');
insert into bd2.section values ('CS-101', '1', 'Fall', '2017', 'Packard', '101', 'H');
insert into bd2.section values ('CS-101', '1', 'Spring', '2018', 'Packard', '101', 'F');
insert into bd2.section values ('CS-190', '1', 'Spring', '2017', 'Taylor', '3128', 'E');
insert into bd2.section values ('CS-190', '2', 'Spring', '2017', 'Taylor', '3128', 'A');
insert into bd2.section values ('CS-315', '1', 'Spring', '2018', 'Watson', '120', 'D');
insert into bd2.section values ('CS-319', '1', 'Spring', '2018', 'Watson', '100', 'B');
insert into bd2.section values ('CS-319', '2', 'Spring', '2018', 'Taylor', '3128', 'C');
insert into bd2.section values ('CS-347', '1', 'Fall', '2017', 'Taylor', '3128', 'A');
insert into bd2.section values ('EE-181', '1', 'Spring', '2017', 'Taylor', '3128', 'C');
insert into bd2.section values ('FIN-201', '1', 'Spring', '2018', 'Packard', '101', 'B');
insert into bd2.section values ('HIS-351', '1', 'Spring', '2018', 'Painter', '514', 'C');
insert into bd2.section values ('MU-199', '1', 'Spring', '2018', 'Packard', '101', 'D');
insert into bd2.section values ('PHY-101', '1', 'Fall', '2017', 'Watson', '100', 'A');

--(student_id, name, dept_name, tot_cred)
insert into bd2.student values ('00128', 'Zhang', 'Comp. Sci.', '102');
insert into bd2.student values ('12345', 'Shankar', 'Comp. Sci.', '32');
insert into bd2.student values ('19991', 'Brandt', 'History', '80');
insert into bd2.student values ('23121', 'Chavez', 'Finance', '110');
insert into bd2.student values ('44553', 'Peltier', 'Physics', '56');
insert into bd2.student values ('45678', 'Levy', 'Physics', '46');
insert into bd2.student values ('54321', 'Williams', 'Comp. Sci.', '54');
insert into bd2.student values ('55739', 'Sanchez', 'Music', '38');
insert into bd2.student values ('70557', 'Snow', 'Physics', '0');
insert into bd2.student values ('76543', 'Brown', 'Comp. Sci.', '58');
insert into bd2.student values ('76653', 'Aoi', 'Elec. Eng.', '60');
insert into bd2.student values ('98765', 'Bourikas', 'Elec. Eng.', '98');
insert into bd2.student values ('98988', 'Tanaka', 'Biology', '120');

(st_id, i_id)
insert into bd2.advisor values ('00128', '45565'); 
insert into bd2.advisor values ('76543', '45565'); 
insert into bd2.advisor values ('12345', '10101'); 
insert into bd2.advisor values ('23121', '76543'); 
insert into bd2.advisor values ('44553', '22222'); 
insert into bd2.advisor values ('45678', '22222');
insert into bd2.advisor values ('76653', '98345'); 
insert into bd2.advisor values ('98765', '98345'); 
insert into bd2.advisor values ('98988', '76766'); 

(course_id, prereq_id)
insert into bd2.prereq values ('BIO-301', 'BIO-101');
insert into bd2.prereq values ('BIO-399', 'BIO-101');
insert into bd2.prereq values ('CS-190', 'CS-101');
insert into bd2.prereq values ('CS-315', 'CS-101');
insert into bd2.prereq values ('CS-319', 'CS-101');
insert into bd2.prereq values ('CS-347', 'CS-101');
insert into bd2.prereq values ('EE-181', 'PHY-101');


insert into bd2.teaches values ('10101', 'CS-101', '1', 'Fall', '2017');
insert into bd2.teaches values ('10101', 'CS-315', '1', 'Spring', '2018');
insert into bd2.teaches values ('10101', 'CS-347', '1', 'Fall', '2017');
insert into bd2.teaches values ('12121', 'FIN-201', '1', 'Spring', '2018');
insert into bd2.teaches values ('15151', 'MU-199', '1', 'Spring', '2018');
insert into bd2.teaches values ('22222', 'PHY-101', '1', 'Fall', '2017');
insert into bd2.teaches values ('32343', 'HIS-351', '1', 'Spring', '2018');
insert into bd2.teaches values ('45565', 'CS-101', '1', 'Spring', '2018');
insert into bd2.teaches values ('45565', 'CS-319', '1', 'Spring', '2018');
insert into bd2.teaches values ('76766', 'BIO-101', '1', 'Summer', '2017');
insert into bd2.teaches values ('76766', 'BIO-301', '1', 'Summer', '2018');
insert into bd2.teaches values ('83821', 'CS-190', '1', 'Spring', '2017');
insert into bd2.teaches values ('83821', 'CS-190', '2', 'Spring', '2017');
insert into bd2.teaches values ('83821', 'CS-319', '2', 'Spring', '2018');
insert into bd2.teaches values ('98345', 'EE-181', '1', 'Spring', '2017');

insert into bd2.takes values ('00128', 'CS-101', '1', 'Fall', '2017', 'A');
insert into bd2.takes values ('00128', 'CS-347', '1', 'Fall', '2017', 'A-');
insert into bd2.takes values ('12345', 'CS-101', '1', 'Fall', '2017', 'C');
insert into bd2.takes values ('12345', 'CS-190', '2', 'Spring', '2017', 'A');
insert into bd2.takes values ('12345', 'CS-315', '1', 'Spring', '2018', 'A');
insert into bd2.takes values ('12345', 'CS-347', '1', 'Fall', '2017', 'A');
insert into bd2.takes values ('19991', 'HIS-351', '1', 'Spring', '2018', 'B');
insert into bd2.takes values ('23121', 'FIN-201', '1', 'Spring', '2018', 'C+');
insert into bd2.takes values ('44553', 'PHY-101', '1', 'Fall', '2017', 'B-');
insert into bd2.takes values ('45678', 'CS-101', '1', 'Fall', '2017', 'F');
insert into bd2.takes values ('45678', 'CS-101', '1', 'Spring', '2018', 'B+');
insert into bd2.takes values ('45678', 'CS-319', '1', 'Spring', '2018', 'B');
insert into bd2.takes values ('54321', 'CS-101', '1', 'Fall', '2017', 'A-');
insert into bd2.takes values ('54321', 'CS-190', '2', 'Spring', '2017', 'B+');
insert into bd2.takes values ('55739', 'MU-199', '1', 'Spring', '2018', 'A-');
insert into bd2.takes values ('76543', 'CS-101', '1', 'Fall', '2017', 'A');
insert into bd2.takes values ('76543', 'CS-319', '2', 'Spring', '2018', 'A');
insert into bd2.takes values ('76653', 'EE-181', '1', 'Spring', '2017', 'C');
insert into bd2.takes values ('98765', 'CS-101', '1', 'Fall', '2017', 'C-');
insert into bd2.takes values ('98765', 'CS-315', '1', 'Spring', '2018', 'B');
insert into bd2.takes values ('98988', 'BIO-101', '1', 'Summer', '2017', 'A');
insert into bd2.takes values ('98988', 'BIO-301', '1', 'Summer', '2018', null);


insert into bd2.time_slot values ('A', 'M', '8', '0', '8', '50');
insert into bd2.time_slot values ('A', 'W', '8', '0', '8', '50');
insert into bd2.time_slot values ('A', 'F', '8', '0', '8', '50');
insert into bd2.time_slot values ('B', 'M', '9', '0', '9', '50');
insert into bd2.time_slot values ('B', 'W', '9', '0', '9', '50');
insert into bd2.time_slot values ('B', 'F', '9', '0', '9', '50');
insert into bd2.time_slot values ('C', 'M', '11', '0', '11', '50');
insert into bd2.time_slot values ('C', 'W', '11', '0', '11', '50');
insert into bd2.time_slot values ('C', 'F', '11', '0', '11', '50');
insert into bd2.time_slot values ('D', 'M', '13', '0', '13', '50');
insert into bd2.time_slot values ('D', 'W', '13', '0', '13', '50');
insert into bd2.time_slot values ('D', 'F', '13', '0', '13', '50');
insert into bd2.time_slot values ('E', 'T', '10', '30', '11', '45 ');
insert into bd2.time_slot values ('E', 'R', '10', '30', '11', '45 ');
insert into bd2.time_slot values ('F', 'T', '14', '30', '15', '45 ');
insert into bd2.time_slot values ('F', 'R', '14', '30', '15', '45 ');
insert into bd2.time_slot values ('G', 'M', '16', '0', '16', '50');
insert into bd2.time_slot values ('G', 'W', '16', '0', '16', '50');
insert into bd2.time_slot values ('G', 'F', '16', '0', '16', '50');
insert into bd2.time_slot values ('H', 'W', '10', '0', '12', '30');

