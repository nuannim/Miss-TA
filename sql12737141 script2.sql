use sql12737141;


insert into professor
VALUES (1, 'chotipat', 'chocho', 5),
        (2, 'nopporn', 'cho', 3);


select * from professor;


insert into course
VALUES (1, 101, 'pscp', 1, 'problem solving and computer programming',
        NULL, '12-12-2023', '16-12-2023', NULL, 0, '0900001234'),
        
        (2, 102, 'mm', 2, 'multimedia technology',
        NULL, NULL, NULL, NULL, 0, '0800001234')

insert into course
VALUES (4, 104, 'oop', 2, 'object oriented programming',
        NULL, NULL, NULL, NULL, 0, '0855555555');

insert into course
VALUES (3, 103, 'ins', 3, 'information to network system', 
        null, '2021-12-12', NULL, NULL, 1, '0981112345');

insert into prof_course(course_id, prof_id)
VALUES (101, 1), (102, 2);

insert into prof_course(course_id, prof_id)
VALUES (103, 1);

insert into enroll(student_id, course_id)
VALUES (66070276, 102);

insert into student
VALUES (66070999, 'sita', 'teeradechsakul', 2, 0);

insert into enroll(student_id, course_id)
values (66070999, 102);

insert into enroll(student_id, course_id)
values (66070999, 104);

update course
SET name = 'pc'
where course_id = 104;

update course
SET description = 'physical computing'
where course_id = 104;


alter table sql12737141.enroll
MODIFY enroll_id int AUTO_INCREMENT;

select history_id
FROM history
where enroll_id = (select enroll_id
                from enroll
                where course_id = 102);