use sql12737141;

select *
from course, prof_course
where course.course_id = prof_course.course_id
and prof_id = 1;
