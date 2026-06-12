# E-Commerce Intelligence Pipeline
It pulls data from three public sources — Olist Brazilian E-Commerce dataset 
from Kaggle, Amazon Consumer Reviews of Amazon Products from Kaggle, 
and Google Trends from BigQuery — cleans and transforms it using Python, 
loads it into BigQuery, runs ML models for demand forecasting and customer 
segmentation, uses Gemini API to analyze review sentiment, and visualizes 
the results in Looker Studio.

The idea came from my experience working with customer transaction data in banking. Purchase patterns in e-commerce are surprisingly similar: frequency, value, category, churn. I wanted to see if the same analytical thinking applies, and what tools are needed to get there.

## What this project does
It pulls data from three public sources (Olist Brazilian E-Commerce dataset, Amazon Reviews on BigQuery, and Google Trends), cleans and transforms it using Python, loads it into BigQuery, runs ML models for demand forecasting and customer segmentation, uses Gemini API to analyze review sentiment, and visualizes the results in Looker Studio.

## Project structure
ecommerce-intelligence-pipeline/
etl/                    # extract, transform, load scripts
ml/                     # demand forecasting and customer segmentation
ai/                     # sentiment analysis with Gemini API
notebooks/              # EDA and model experiments
dashboard/              # SQL queries for Looker Studio
data/                   # raw and processed data
.env.example            # environment variables template
requirements.txt        # dependencies

## Tools used
Python, Pandas, Kaggle API, Google BigQuery, Scikit-learn, Prophet, 
Gemini API, Looker Studio

## How to run
ิ#bash1
git clone https://github.com/ployployz/ecommerce-intelligence-pipeline.git

#bash2
cd ecommerce-intelligence-pipeline

#bash3
python -m venv venv

#bash4
venv\Scripts\activate

#bash5
pip install -r requirements.txt

Copy `.env.example` to `.env` and fill in your API keys before running.

## What I learned
Merging data from sources with different time granularities (daily vs weekly) was trickier than expected. Also discovered that delivery delays drove more negative reviews than product quality itself — which wasn't what I assumed going in.