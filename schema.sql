-- -- SCHEMA: schema

-- -- DROP SCHEMA IF EXISTS schema ;

-- CREATE SCHEMA IF NOT EXISTS schema
--     AUTHORIZATION postgres;
	
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

CREATE TABLE country_sea (
    country VARCHAR,
    sea VARCHAR
);

CREATE TABLE mean_sea_level(
    object_id INT PRIMARY KEY,
    country VARCHAR,
    iso2 VARCHAR,
    iso3 VARCHAR,
    indicator VARCHAR,
    unit VARCHAR,
    source VARCHAR,
    cts_code VARCHAR,
    cts_name VARCHAR,
    measure VARCHAR,
    date DATE,
    value FLOAT
);