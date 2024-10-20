use sql12738833;

create table test(
    id int PRIMARY KEY
);


select * 
from course, course_history
where course.course_id = course_history.course_id;

SELECT *
FROM course
JOIN course_history ON course.course_id = course_history.course_id
JOIN prof_course ON course.course_id = prof_course.course_id
WHERE prof_id = 1;


ELECT * FROM course ' 
'JOIN course_history ' 
'ON course.course_id = course_history.course_id '
'WHERE course_history_id = %s

DESCRIBE course_history;

INSERT INTO course VALUES 
(1, 111, 'Problem Solving and Computer Programming', 1, 'PSCP', NULL, '12-12-2023', '16-12-2023', NULL, 0, '0900001234'),
(2, 211, 'Multimedia Technology', 2, 'MM', NULL, '12-12-2023', '13-12-2023', NULL, 0, '0800001234'),
(3, 212, 'Information to Network System', 2, 'INS', NULL, '12-12-2023', '13-12-2023', NULL, 1, '0981112345'),
(4, 121, 'Object Oriented Programming', 1, 'OOP', NULL, '12-12-2023', '13-12-2023', NULL, 0, '0812345678'),
(5, 112, 'INFORMATION TECHNOLOGY FUNDAMENTALS', 1, 'ITF', NULL, '12-12-2023', '13-12-2023', NULL, 0, '0855555555'),
(6, 213, 'Physical Computing', 2, 'PC', NULL, '12-12-2023', '13-12-2023', NULL, 0, '0855555555');

delete from course_history;

alter table course_history
AUTO_INCREMENT = 1;

alter table course_history
modify wdate DATETIME;

insert into course_history(course_id, description, adate, wdate, cdate, qtype, contact)
VALUES (111, 'pscp description', '2024-12-01', '2024-12-02 00:00:00', '2024-12-03', 1, '0901234567'),
(211, 'mm description', '2024-12-01', '2024-12-02 00:00:00', '2024-12-03', 1, '0123456789'),
(212, 'ins description', '2024-12-01', '2024-12-02 00:00:00', '2024-12-03', 1, '0987654321')

insert into course_history(course_id, description, adate, wdate, cdate, qtype, contact)
VALUES (211, 'mm description', '2024-12-01', '2024-12-02 00:00:00', '2024-12-03', 1, '0123456789');