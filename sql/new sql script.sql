use sql12738833;

------------------------- อันไหนสร้างแล้วจะ commit ไว้ -------------------------
-- describe sql
describe sql12737141.course;
describe sql12737141.enroll;
DESCRIBE sql12737141.grade;
describe sql12737141.professor;
describe sql12737141.prof_course;
describe sql12737141.prof_req;
describe sql12737141.student;
describe sql12737141.student_req;
describe sql12737141.wage;


-- create table
create table sql12738833.professor (
	prof_id int,
    firstname varchar(255),
    lastname varchar(255)
);

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

alter table grade
modify grade INT;

delete from grade;

DESCRIBE sql12738833.grade;
select * from grade;


alter table enroll
add Foreign Key (course_id) REFERENCES course(course_id);

alter table sql12738833.student
add num_ta int;


create table sql12738833.prof_course (
    prof_course_id int primary key AUTO_INCREMENT,
    course_id INT not NULL,
    prof_id int not null,
        Foreign Key (course_id) REFERENCES course(course_id)
            on delete CASCADE,
        Foreign Key (prof_id) REFERENCES professor(prof_id)
            on delete CASCADE
);

describe sql12738833.course;
describe sql12738833.professor;


alter Table sql12738833.professor
add PRIMARY key (prof_id);

