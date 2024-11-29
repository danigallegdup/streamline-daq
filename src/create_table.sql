-- Create table for processed data
CREATE TABLE processed_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    data JSONB NOT NULL,
    error_rate FLOAT DEFAULT 0.0
);

-- Create table for raw data (if applicable)
CREATE TABLE raw_data (
    id SERIAL PRIMARY KEY,
    source VARCHAR(255),
    timestamp TIMESTAMP NOT NULL,
    data JSONB NOT NULL
);

-- Add more tables if required for your application
