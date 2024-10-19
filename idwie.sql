use sql12738833;

create table test(
    id int PRIMARY KEY
);


select * 
from course, course_history
where course.course_id = course_history.course_id
and course_history_id=1;

SELECT *
FROM course
JOIN course_history ON course.course_id = course_history.course_id
JOIN prof_course ON course.course_id = prof_course.course_id
WHERE prof_id = 1;


DESCRIBE course_history;