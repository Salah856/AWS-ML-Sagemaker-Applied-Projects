COPY ridership FROM 
's3://redshift-ml-bikesharing-data/bike-sharing-data/ridership/'
IAM_ROLE 'arn:aws:iam::<accountid>:role/RedshiftML'
FORMAT csv IGNOREHEADER 1 DATEFORMAT 'auto' TIMEFORMAT 'auto' REGION 'us-west-2' gzip;

COPY weather FROM
's3://redshift-ml-bikesharing-data/bike-sharing-data/weather/'
IAM_ROLE ' arn:aws:iam::<accountid>:role/RedshiftML''
FORMAT csv IGNOREHEADER 1 DATEFORMAT 'auto' TIMEFORMAT 'auto' REGION 'us-west-2' gzip;

COPY holiday FROM
's3://redshift-ml-bikesharing-data/bike-sharing-data/holiday/'
IAM_ROLE ' arn:aws:iam::<accountid>:role/RedshiftML''
FORMAT csv IGNOREHEADER 1 DATEFORMAT 'auto' TIMEFORMAT 'auto' REGION 'us-west-2' gzip;

