# StockSense — Tech Stack

## Core Technologies

| Layer                       | Technology                                            |
| --------------------------- | ----------------------------------------------------- |
| Programming                 | Python                                                |
| API Integration             | REST APIs, Requests                                   |
| Web Data Collection         | BeautifulSoup / Scrapy / Playwright where appropriate |
| Data Processing             | Pandas                                                |
| File Format                 | Parquet                                               |
| Database                    | PostgreSQL                                            |
| ORM / Database Connectivity | SQLAlchemy                                            |
| Streaming                   | Apache Kafka                                          |
| Message Processing          | Kafka Producer / Consumer                             |
| Machine Learning            | Scikit-learn                                          |
| Dashboard                   | Streamlit                                             |
| Version Control             | Git + GitHub                                          |
| Development Environment     | VS Code                                               |

## External Data Sources

### Government Open Data

* Data.gov.in — Mandi daily commodity prices
* Data.gov.in — FCI daily food stock position
* Data.gov.in — Retail and wholesale prices of selected essential commodities

### Food Product Data

* Open Food Facts API — product, category, brand, barcode, ingredient and nutritional information

### Retail Web Data

* Blinkit or another permitted public retail source may be incorporated as an optional web-data source, subject to the website's access rules, terms and rate limits.

## Architecture

```text
                 EXTERNAL DATA SOURCES
                          |
        +-----------------+------------------+
        |                 |                  |
        v                 v                  v
   Data.gov.in      Open Food Facts     Retail Web Data
     REST API             API             Scraping*
        |                 |                  |
        +-----------------+------------------+
                          |
                          v
                    Python Ingestion
                          |
                          v
                     Raw Data Layer
                          |
                    JSON / Parquet
                          |
                          v
                   ETL / Validation
                          |
             +------------+------------+
             |                         |
             v                         v
         PostgreSQL                Parquet
             |
             |
             +----------------------+
                                    |
                                    v
                           Analytics / ML
                                    |
                                    v
                               Dashboard


              REAL-TIME PIPELINE

             Virtual POS Simulator
                       |
                       v
                Kafka Producer
                       |
                       v
                  Kafka Topic
                       |
                       v
                Kafka Consumer
                       |
                       v
                 ETL / Validation
                       |
                       v
                   PostgreSQL
                       |
                       v
              Real-Time Analytics
```

## Data Engineering Concepts Demonstrated

* REST API ingestion
* Web data extraction
* Batch data ingestion
* Streaming data ingestion
* ETL pipelines
* Data validation and cleaning
* Data normalization
* Historical data storage
* Parquet-based analytical storage
* Relational database design
* Data warehousing
* Kafka-based event streaming
* Real-time processing
* Feature engineering
* Demand forecasting
* Inventory analytics
* Stock-out risk analysis
* Data visualization

## Project Goal

StockSense is a data engineering and analytics platform designed to combine government food-market data, food-product information and simulated retail transactions into a unified pipeline.

The system collects external market and product observations, processes and stores historical data, generates a continuous stream of simulated sales transactions, and combines batch and streaming data to support inventory monitoring, demand analysis, price trends and stock-out prediction.

The project does not claim that simulated transactions represent real customer purchases or that publicly collected retail data represents private retailer sales.
