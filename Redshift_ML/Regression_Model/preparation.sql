
CREATE OR REPLACE VEIW ridership_view AS
SELECT
    trip_time
    , trip_count
    , TO_CHAR(trip_time,'hh24') ::INT trip_hour
    , TO_CHAR(trip_time, 'dd') :: INT trip_day
    , TO_CHAR(trip_time, 'mm') :: INT trip_month
    , TO_CHAR(trip_time, 'yy') :: INT trip_year
    , TO_CHAR(trip_time, 'q') :: INT trip_quarter
    , TO_CHAR(trip_time, 'w') :: INT trip_month_week
    , TO_CHAR(trip_time, 'd') :: INT trip_week_day
FROM  
    (SELECT  
         CASE
           WHEN TRUNC(r.trip_start_time) < '2017-07-01'::DATE
           THEN CONVERT_TIMEZONE('US/Eastern', DATE_TRUNC('hour',r.trip_start_time))
           ELSE DATE_TRUNC('hour',r.trip_start_time)
         END trip_time
         , COUNT(1) trip_count
     FROM    
         ridership r
     WHERE    r.trip_duration_seconds BETWEEN 60 AND 60 * 60 * 24
     GROUP BY
         1);
         
         
