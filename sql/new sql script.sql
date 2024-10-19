use sql12738833;

------------------------- อันไหนสร้างแล้วจะ comment ไว้ -------------------------
-- describe sql
describe sql12738833.course;
describe sql12738833.enroll;
DESCRIBE sql12738833.grade;
describe sql12738833.professor;
describe sql12738833.prof_course;
describe sql12738833.prof_req;
describe sql12738833.student;
describe sql12738833.student_req;
describe sql12738833.wage;


-- create table
create table sql12738833.professor (
	prof_id int,
    firstname varchar(255),
    lastname varchar(255)
);
alter Table sql12738833.professor
add PRIMARY key (prof_id);

create table sql12738833.enroll (
	enroll_id int primary key,
    student_id int,
    course_id int
);

create table sql12738833.course (
    id int not NULL,
    course_id int PRIMARY KEY,
    name VARCHAR(255) not NULL,
    YEAR INT,
    description varchar(255),
    image varchar(255),
    adate DATE,
    wdate DATE,
    cdate DATE,
    qtype INT,
    contact VARCHAR(255)
);

create table sql12738833.prof_req (
    p_req_id INT PRIMARY key AUTO_INCREMENT,
    course_id INT,
    req_no INT,
    req_question VARCHAR(255),
    required_to_fill INT,
        Foreign Key (course_id) REFERENCES course(course_id)
            on delete CASCADE
);


create table sql12738833.grade (
    grade_id int PRIMARY KEY AUTO_INCREMENT,
    student_id INT not NULL,
    course_id INT not NULL,
    grade VARCHAR(255),
        Foreign Key (student_id) REFERENCES student(student_id)
            on delete CASCADE,
        Foreign Key (course_id) REFERENCES course(course_id)
            on delete CASCADE
);

create table wage(
    wage_id int primary KEY AUTO_INCREMENT,
    student_id int not NULL,
    course_id int not NULL,
    ta_type VARCHAR(255),
    wage FLOAT,
    hire_date DATE,
        Foreign Key (student_id) REFERENCES student(student_id)
            on delete CASCADE,
        Foreign Key (course_id) REFERENCES course(course_id)
            on delete CASCADE 
);

drop table sql12738833.grade;



create table sql12738833.history(
    history_id INT PRIMARY KEY AUTO_INCREMENT,
    enroll_id INT not NULL,
    ta_status VARCHAR(255),
    announce_list_status varchar(255),
    waiting_list_status VARCHAR(255),
        Foreign Key (enroll_id) REFERENCES enroll(enroll_id)
            on delete CASCADE
);


create table sql12738833.student_req (
    s_req_id int PRIMARY KEY AUTO_INCREMENT,
    course_id int NOT NULL,
    req_no INT,
    student_id int not NULL,
    req_ans VARCHAR(255),
    required_to_fill int,
        Foreign Key (course_id) REFERENCES course(course_id)
            on delete CASCADE,
        Foreign Key (student_id) REFERENCES student(student_id)
            on delete CASCADE
);

create table sql12738833.prof_course (
    prof_course_id int primary key AUTO_INCREMENT,
    course_id INT not NULL,
    prof_id int not null,
        Foreign Key (course_id) REFERENCES course(course_id)
            on delete CASCADE,
        Foreign Key (prof_id) REFERENCES professor(prof_id)
            on delete CASCADE
);


------------------------- สร้างตารางให้ครบก่อนแล้วค่อยใช้อันนี้ -------------------------
-- alter table modify
alter table sql12738833.student
	modify student_id int,
    MODIFY firstname varchar(255),
    MODIFY lastname varchar(255);

alter table sql12738833.course
	modify course_id int,
    modify name varchar(255),
    modify year int,
    modify qtype INT;
    

-- alter table add primary
alter table sql12738833.student
add primary key (student_id);

-- alter table add foreign key
alter table sql12738833.enroll
add constraint student_id_enroll_fk
	foreign key (student_id)
    references sql12738833.student(student_id)
    on delete cascade;

alter table sql12738833.enroll
add constraint course_id_enroll_fk
	foreign key (course_id)
    references sql12738833.course(course_id)
    on delete cascade;

-- drop table
drop Table sql12738833.course;



alter table grade
modify grade INT;

delete from grade;

DESCRIBE sql12738833.grade;
select * from grade;


alter table enroll
add Foreign Key (course_id) REFERENCES course(course_id);

alter table sql12738833.student
add num_ta int;




describe sql12738833.course;
describe sql12738833.professor;




------------------------------------ insert
use sql12738833;



insert into professor
VALUES (1, 'Chotipat', 'Pornavalai'),
        (2, 'nopporn', 'Chotikakamthorn'),
        (3, 'Kitsuchart', 'Pasupa');



-- insert into course
-- VALUES (1, 111, 'Problem Solving and Computer Programming', 1, 'PSCP',
--         NULL, '12-12-2023', '16-12-2023', NULL, 0, '0900001234'),
        
--         (2, 211, 'Multimedia Technology', 2, 'MM', 
--         NULL, '12-12-2023', '13-12-2023', NULL, 0, '0800001234'),

--         (3, 212, 'Information to Network System', 2, 'INS', 
--         null, '12-12-2023', '13-12-2023', NULL, 1, '0981112345'),
        
--         (4, 121, 'Object Oriented Programming', 1, 'OOP',
--         NULL, '12-12-2023', '13-12-2023', NULL, 0, '0812345678'),
        
--         (5, 112, 'INFORMATION TECHNOLOGY FUNDAMENTALS', 1, 'ITF',
--         NULL, '12-12-2023', '13-12-2023', NULL, 0, '0855555555');

--         (6, 213, 'Physical Computing', 2, 'PC',
--         NULL, '12-12-2023', '13-12-2023', NULL, 0, '0855555555');

INSERT INTO course VALUES 
(1, 111, 'Problem Solving and Computer Programming', 1, 'PSCP', NULL, '12-12-2023', '16-12-2023', NULL, 0, '0900001234'),
(2, 211, 'Multimedia Technology', 2, 'MM', NULL, '12-12-2023', '13-12-2023', NULL, 0, '0800001234'),
(3, 212, 'Information to Network System', 2, 'INS', NULL, '12-12-2023', '13-12-2023', NULL, 1, '0981112345'),
(4, 121, 'Object Oriented Programming', 1, 'OOP', NULL, '12-12-2023', '13-12-2023', NULL, 0, '0812345678'),
(5, 112, 'INFORMATION TECHNOLOGY FUNDAMENTALS', 1, 'ITF', NULL, '12-12-2023', '13-12-2023', NULL, 0, '0855555555'),
(6, 213, 'Physical Computing', 2, 'PC', NULL, '12-12-2023', '13-12-2023', NULL, 0, '0855555555');

insert into course_history(course_id, description, adate, wdate, cdate, qtype, contact)
VALUES (111, 'pscp description', '2024-12-01', '2024-12-02', '2024-12-03', 1, '0901234567'),
(211, 'mm description', '2024-12-01', '2024-12-02', '2024-12-03', 1, '0123456789'),
(212, 'ins description', '2024-12-01', '2024-12-02', '2024-12-03', 1, '0987654321')

alter table course_history
modify qtype INT;

insert into prof_course(course_id, prof_id)
VALUES (111, 1), (211, 2), (212, 1),
        (112, 3), (213, 3);

-- insert into enroll(student_id, course_id)
-- VALUES (66070276, 102);

insert into student
VALUES (66070999, 'Sita', 'Teeradechsakul', 2, NULL),
        (66070998, 'Vitita', 'Srasreesom', 1, NULL);

insert into enroll(student_id, course_id)
values (66070999, 211), (66070999, 212), (66070286, 213),
        (66070998, 111), (66070998, 112);

insert into history(enroll_id, ta_status)
VALUES (1, 'passed'), (3, 'waiting');

insert into history(enroll_id, ta_status)
VALUES (2, 'not passed');

update course
SET name = 'pc'
where course_id = 104;

update course
SET description = 'physical computing'
where course_id = 104;


alter table sql12738833.enroll
MODIFY enroll_id int AUTO_INCREMENT;

select *
from history, enroll, student
where history.enroll_id = enroll.enroll_id
and enroll.student_id = student.student_id;

select *
from history, enroll
where history.enroll_id = enroll.enroll_id
ORDER BY history_id;


insert into course (name, course_id, description)
VALUES ('test in sql', 9999999999, 'test in sql');