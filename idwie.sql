use sql12738833;

create table test(
    id int PRIMARY KEY
);


select * 
from course, course_history
where course.course_id = course_history.course_id
and course_history_id=1;

DESCRIBE course_history;