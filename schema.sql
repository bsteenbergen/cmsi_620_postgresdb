CREATE TABLE country_sea (
    country VARCHAR PRIMARY KEY,
    sea VARCHAR
);

CREATE TABLE location (
  city VARCHAR,
  country VARCHAR,
  latitude VARCHAR,
  longitude VARCHAR,
  PRIMARY KEY (city, country),
  FOREIGN KEY (country) REFERENCES country_sea(country)
);

CREATE TABLE temperature (
  temperature_id SERIAL PRIMARY KEY,
  city VARCHAR,
  country VARCHAR,
  date_collected DATE,
  avg_temp FLOAT,
  avg_temp_uncertainty FLOAT,
  FOREIGN KEY (country) REFERENCES country_sea(country)
);

CREATE TABLE mean_sea_level (
    id INT PRIMARY KEY,
    unit VARCHAR,
    sea_name VARCHAR,
    date_measured DATE,
    sea_level FLOAT
);

CREATE TABLE emissions (
  emissions_id SERIAL PRIMARY KEY,
  country VARCHAR,
  year_measured INT,
  population BIGINT,
  co2 FLOAT,
  cumulative_co2 FLOAT,
  FOREIGN KEY (country) REFERENCES country_sea(country)
);