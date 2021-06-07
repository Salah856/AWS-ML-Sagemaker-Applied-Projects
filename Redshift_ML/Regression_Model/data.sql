CREATE TABLE IF NOT EXISTS ridership
( trip_id               INT
, trip_duration_seconds INT
, trip_start_time       timestamp
, trip_stop_time        timestamp
, from_station_name     VARCHAR(50)
, to_station_name       VARCHAR(50)
, from_station_id       SMALLINT
, to_station_id         SMALLINT
, user_type             VARCHAR(20));

CREATE TABLE IF NOT EXISTS weather
( longitude_x         DECIMAL(5,2)
, latitude_y          DECIMAL(5,2)
, station_name        VARCHAR(20)
, climate_id          BIGINT
, datetime_utc        TIMESTAMP
, weather_year        SMALLINT
, weather_month       SMALLINT
, weather_day         SMALLINT
, time_utc            VARCHAR(5)
, temp_c              DECIMAL(5,2)
, temp_flag           VARCHAR(1)
, dew_point_temp_c    DECIMAL(5,2)
, dew_point_temp_flag VARCHAR(1)
, rel_hum             SMALLINT
, rel_hum_flag        VARCHAR(1)
, precip_amount_mm    DECIMAL(5,2)
, precip_amount_flag  VARCHAR(1)
, wind_dir_10s_deg    VARCHAR(10)
, wind_dir_flag       VARCHAR(1)
, wind_spd_kmh        VARCHAR(10)
, wind_spd_flag       VARCHAR(1)
, visibility_km       VARCHAR(10)
, visibility_flag     VARCHAR(1)
, stn_press_kpa       DECIMAL(5,2)
, stn_press_flag      VARCHAR(1)
, hmdx                SMALLINT
, hmdx_flag           VARCHAR(1)
, wind_chill          VARCHAR(10)
, wind_chill_flag     VARCHAR(1)
, weather             VARCHAR(10));

CREATE TABLE IF NOT EXISTS holiday
( holiday_date  DATE
, description VARCHAR(100));
