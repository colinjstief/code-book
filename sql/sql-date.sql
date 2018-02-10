-- 4 main data types
timestamp
date
time
interval

-- timestamp
SELECT timestamp '2005-10-10 05:16:45'; -- ISO8601
--------------'year-month-day hour-minute-second'

-- current date/time
SELECT NOW();

-- change format of current date/time
SELECT TO_CHAR(NOW(), 'DD-MM-YYYY');
SELECT TO_CHAR(NOW(), 'Day, DD-MM-YYYY HH:MI:SS');
SELECT TO_CHAR(NOW(), 'FMDay, DD-MM-YYYY'); -- remove space at end of days not as long as the longest
SELECT TO_CHAR(NOW(), 'FMDay DDth FMMonth');

-- change format of given date/time
SELECT TO_TIMESTAMP('04-02-2013', 'DD-MM-YYYY');
SELECT TO_TIMESTAMP('Saturday 21st May', 'FMDay DDth FMMonth');
SELECT TO_TIMESTAMP('Saturday 21st May, 2016 06:19:11', 'FMDay DDth FMMonth, YYYY HH:MI:SS');



