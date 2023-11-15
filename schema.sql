-- SCHEMA: schema

-- DROP SCHEMA IF EXISTS schema ;

CREATE SCHEMA IF NOT EXISTS schema
    AUTHORIZATION postgres;
	
CREATE TABLE location (
  city VARCHAR,
  country VARCHAR,
  latitude VARCHAR,
  longitude VARCHAR,
  PRIMARY KEY (city, country)
);

CREATE TABLE temperature (
  city VARCHAR,
  country VARCHAR,
  date_collected DATE,
  avg_temp FLOAT,
  avg_temp_uncertainty FLOAT,
  FOREIGN KEY (city, country) REFERENCES location
);
