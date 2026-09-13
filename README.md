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

---

## External Data Sources

### 1. Government Open Data

**Data.gov.in**

Government datasets will be used as a source of publicly available food-market and commodity-related data.

Possible datasets include:

* Mandi daily commodity prices
* Food stock and availability information
* Retail and wholesale prices of selected food commodities

The government data will primarily provide **market-level information such as commodity prices, dates, locations and availability-related observations**.

---

### 2. Retail Product Data

**BigBasket — Web Scraping**

BigBasket will be used as a retail web-data source where permitted by its website's access rules, terms of service and technical restrictions.

The scraper may collect publicly visible product information such as:

* Product name
* Brand
* Category
* Price
* Discount
* Pack size
* Availability
* Product URL
* Rating, where publicly available

This data will help StockSense connect **market-level information with retail product-level observations**.

The project will respect the website's robots.txt, terms, rate limits and other applicable restrictions.

---

### 3. Food Product API

**Open Food Facts API**

Open Food Facts will provide structured food-product information through its public API.

Possible fields include:

* Product name
* Barcode
* Brand
* Category
* Ingredients
* Nutritional information
* Product quantity
* Food classification

This source will complement the retail and government datasets by providing **additional product-level information**.

---

# Architecture

```text
                    EXTERNAL DATA SOURCES
                             |
          +------------------+------------------+
          |                  |                  |
          v                  v                  v
     Data.gov.in         BigBasket        Open Food Facts
       REST API          Web Scraping          API
          |                  |                  |
          +------------------+------------------+
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
                    ETL / Data Validation
                             |
                    +--------+--------+
                    |                 |
                    v                 v
                PostgreSQL         Parquet
                    |
                    v
             Analytics / ML
                    |
                    +----------------+
                    |                |
                    v                v
              Inventory         Demand
               Analytics       Analysis
                    |                |
                    +-------+--------+
                            |
                            v
                       StockSense
                        Dashboard
                        (Streamlit)


              REAL-TIME TRANSACTION PIPELINE

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
                             |
                             v
                      Streamlit Dashboard
```

---

# Data Engineering Concepts Demonstrated

* REST API ingestion
* Web scraping
* Batch data ingestion
* Streaming data ingestion
* ETL pipelines
* Data validation and cleaning
* Data normalization
* Schema design
* Historical data storage
* Parquet-based analytical storage
* Relational database design
* PostgreSQL
* SQLAlchemy
* Kafka-based event streaming
* Kafka producers and consumers
* Real-time data processing
* Feature engineering
* Demand forecasting
* Inventory analytics
* Price trend analysis
* Stock-out risk analysis
* Data visualization

---

# Project Goal

StockSense is a **data engineering and analytics platform** designed to combine government food-market data, retail product data and food-product information into a unified data pipeline.

The system collects publicly available data from **Data.gov.in**, extracts permitted retail information from **BigBasket**, and retrieves additional food-product information through the **Open Food Facts API**.

The collected data is processed through Python-based ingestion and ETL pipelines, validated and transformed using Pandas, and stored in PostgreSQL and Parquet for historical analysis.

To demonstrate real-time data engineering, StockSense also includes a **Virtual POS Simulator** that continuously generates simulated sales transactions. These transactions are published to Apache Kafka, consumed and processed through the streaming pipeline, and stored in PostgreSQL.

The combined batch and streaming architecture supports:

* Inventory monitoring
* Product and commodity analysis
* Retail price tracking
* Price trend analysis
* Sales velocity analysis
* Demand forecasting
* Stock-out risk prediction
* Reorder recommendations
* Real-time transaction analytics

### Important Data Disclaimer

StockSense does **not** claim that simulated POS transactions represent real customer purchases.

Government datasets represent publicly available market information, while BigBasket data represents publicly accessible retail observations collected subject to applicable website rules and restrictions.

Open Food Facts provides product information through its public food-product database.

The project combines these sources for **educational, data engineering and analytical purposes** and does not represent private retailer sales, confidential business data or actual customer purchasing behavior.
