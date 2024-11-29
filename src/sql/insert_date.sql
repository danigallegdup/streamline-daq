-- Insert mock data into processed_data
INSERT INTO processed_data (timestamp, data, error_rate)
VALUES 
    ('2024-01-01 00:00:00', '{"sensor": "temperature", "value": 23}', 0.01),
    ('2024-01-01 00:01:00', '{"sensor": "temperature", "value": 24}', 0.02);

-- Insert mock data into raw_data
INSERT INTO raw_data (source, timestamp, data)
VALUES 
    ('sensor_1', '2024-01-01 00:00:00', '{"temperature": 23}'),
    ('sensor_2', '2024-01-01 00:01:00', '{"temperature": 24}');
