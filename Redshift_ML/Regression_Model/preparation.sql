
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
         
         

CREATE OR REPLACE VEIW weather_view AS
SELECT  
    CONVERT_TIMEZONE('US/Eastern', 
      DATE_TRUNC('hour',datetime_utc)) daytime
    , ROUND(AVG(temp_c)) temp_c
    , ROUND(AVG(precip_amount_mm)) precip_amount_mm
FROM weather
GROUP BY 1;



CREATE TABLE trip_data AS 
SELECT         
   r.trip_time
  ,r.trip_count
  ,r.trip_hour
  ,r.trip_day
  ,r.trip_month
  ,r.trip_year
  ,r.trip_quarter
  ,r.trip_month_week
  ,r.trip_week_day
  ,w.temp_c
  ,w.precip_amount_mm
  ,CASE
      WHEN h.holiday_date IS NOT NULL
      THEN 1
      WHEN TO_CHAR(r.trip_time,'D')::INT IN (1,7)
      THEN 1
      ELSE 0
    END is_holiday
  , ROW_NUMBER() OVER (ORDER BY RANDOM()) serial_number
FROM           
  ridership_view r
JOIN            weather_view w
  ON ( r.trip_time = w.daytime )
LEFT OUTER JOIN holiday h
  ON ( TRUNC(r.trip_time) = h.holiday_date );
  
  
  
