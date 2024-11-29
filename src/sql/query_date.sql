-- Select all data from processed_data
SELECT * FROM processed_data;

-- Select data with error_rate above a threshold
SELECT * FROM processed_data WHERE error_rate > 0.01;

-- Select all raw data
SELECT * FROM raw_data;

-- Select data for a specific source
SELECT * FROM raw_data WHERE source = 'sensor_1';
