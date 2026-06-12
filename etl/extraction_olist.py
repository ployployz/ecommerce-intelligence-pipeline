#import data from olist_brazilian
import os
import kaggle
import pandas as pd
from dotenv import load_dotenv

#Load data from .env file
load_dotenv()

#กำหนด path ของ folder ที่จะเก็บข้อมูล
raw_data_path = "data/raw"

#list of all file
olist_files=[
    "olist_orders_dataset.csv",
    "olist_customers_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv"
]

def download_olist_data():
    """
    Download Olist dataset จาก Kaggle
    ถ้าข้อมูลมีอยู่แล้วจะไม่ Download ซ้ำ
    """
    print("=" *50)
    print("เริ่ม Extract olist dataset")
    print("=" * 50)

    #Check exist file. if found file dont duplicate download
    first_file = os.path.join(raw_data_path, olist_files[0])
    if os.path.exists(first_file):
        print("found downloaded file, skip download")
    else:
        #download file from kaggle
        print("downloading from kaggle....")
        kaggle.api.dataset_download_files(
            dataset="olistbr/brazilian-ecommerce",
            path=raw_data_path,
            unzip=True
        )
        print("Downloaded!")

def validate_data():
    """
    ตรวจสอบข้อมูลที่ Download มาว่าถูกต้อง
    แสดงจำนวน rows และ columns ของแต่ละไฟล์
    """
    print("\n" + "=" * 50)
    print("ตรวจสอบข้อมูล")
    print("=" * 50)

    for filename in olist_files:
        filepath = os.path.join(raw_data_path, filename)

        #เช็คไฟล์มีจริงไหม
        if os.path.exists(filepath):
            df = pd.read_csv(filepath)
            print(f"{filename}")
            print(f" rows: {len(df):,} | column: {len(df.columns)}")
            print(f" columns: {list(df.columns)}\n")
        else:
            print(f"not found: {filename}")

def download_amazon_reviews():
    """
    Download amazon consumer reviews from kaggle
    for use sentiment analysis by Gemini API
    """
    print("\n" + "=" * 50)
    print("query Amazon product reviews")
    print("=" * 50)

    #เช็คไฟล์มีจริงไหม
    output_file = os.path.join(raw_data_path, "datafiniti_amazon_consumer_reviews_of_amazon_products.csv")
    if os.path.exists(output_file):
        print("found downloaded file, skip download")
        return
    
    #Download dataset from kaggle
    print("downloading from kaggle....")
    kaggle.api.dataset_download_files(
        dataset="datafiniti/consumer-reviews-of-amazon-products",
        path=raw_data_path,
        unzip=True
    )
    print("Downloaded!")

#run script
if __name__ == "__main__":
    download_olist_data()
    download_amazon_reviews()
    validate_data()
    print("=" * 50)
    print("Extract olist done!")
    print("=" *50)