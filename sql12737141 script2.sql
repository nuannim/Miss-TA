use sql12737141;

alter table enroll
add Foreign Key (course_id) REFERENCES course(course_id);

alter table sql12737141.student
add num_ta int;


-- create table sql12737141.prof_course (
--     prof_course_id int primary key AUTO_INCREMENT,
--     course_id INT not NULL,
--     prof_id int not null,
--         Foreign Key (course_id) REFERENCES course(course_id)
--             on delete CASCADE,
--         Foreign Key (prof_id) REFERENCES professor(prof_id)
--             on delete CASCADE
-- );

-- describe sql12737141.course;
-- describe sql12737141.professor;


-- alter Table sql12737141.professor
-- add PRIMARY key (prof_id);

