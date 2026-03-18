# Cloud ETL Pipeline

A containerized ETL (Extract, Transform, and Load) pipeline built with Python that ingests product data from a REST API, transforms the data, and loads it into a PostgreSQL database. The project is designed using Docker for portability and prepared for future cloud deployment.

## Project Overview

This project demonstrates core data engineering concepts including API data ingestion, data transformation, relational database loading, and containerized deployment.

The pipeline extracts product data from the Fake Store API, processes the data using Python and Pandas, and stores the cleaned data in a PostgreSQL database.

## Architecture

Fake Store API → Python ETL Pipeline → PostgreSQL Database → Docker Containers

Components:

- Python ETL scripts
- REST API data ingestion
- Data transformation with Pandas
- PostgreSQL relational database
- Docker containerization
- Docker Compose service orchestration

## Technologies Used

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- REST APIs
- python-dotenv

## Project Structure


Cloud-ETL-Pipeline
│
├── etl
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── main.py
│
├── logs
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md


## ETL Process

### Extract
Data is retrieved from the Fake Store API.

```
https://fakestoreapi.com/products
```

### Transform
The raw JSON data is cleaned and normalized using Pandas.

Example transformations include:

- Selecting relevant fields
- Flattening nested JSON
- Preparing structured tabular data

### Load
The transformed data is inserted into a PostgreSQL database using SQLAlchemy.

## Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Eric-Acha/Cloud-ETL-Pipeline.git
cd Cloud-ETL-Pipeline
2. Create Environment Variables

Create a .env file:

DB_USER=postgres
DB_PASSWORD=password
DB_HOST=postgres
DB_PORT=5432
DB_NAME=etl_db
3. Build and Run with Docker
docker compose up --build

This will start:

PostgreSQL database container

ETL pipeline container

4. Verify the Data

Connect to PostgreSQL:

docker exec -it etl_postgres psql -U postgres -d etl_db

Run a query:

SELECT * FROM fact_products;
Example Output

After running the pipeline, product records from the API will be stored in PostgreSQL.

Example columns:

product_id

product_name

image

unit_price

category

rating_rate

rating_count

description

estimated_revenue

Future Improvements

Add Airflow for pipeline orchestration

Deploy containers to Azure Container Apps

Integrate Azure Database for PostgreSQL

Add automated scheduling

Implement CI/CD using GitHub Actions

Learning Objectives

This project demonstrates:

Building a modular ETL pipeline

Working with REST APIs

Data transformation with Pandas

Loading data into relational databases

Containerizing applications with Docker

Designing cloud-ready data pipelines

Author

Eric Acha
Information Technology Management student
DeVry University
