use sql12737141;

select *
from course, prof_course
where course.course_id = prof_course.course_id
and prof_id = 1;

SELECT *
FROM course AS c 
JOIN prof_course AS pc ON c.course_id = pc.course_id 
WHERE pc.prof_id = 1;


