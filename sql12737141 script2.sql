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
VALUES (3, 103, 'ins', 3, 'information to network system', 
        null, '2021-12-12', NULL, NULL, 1, '0981112345');

insert into prof_course(course_id, prof_id)
VALUES (101, 1), (102, 2);

insert into prof_course(course_id, prof_id)
VALUES (103, 1);
