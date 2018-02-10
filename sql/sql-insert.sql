-- Create a table
CREATE TABLE public.Users 
( id integer NOT NULL,   
name character(30),
CONSTRAINT pk_users_id PRIMARY KEY (id) );

-- Insert value
INSERT INTO public.users(id, name)
VALUES (1, 'Colin');