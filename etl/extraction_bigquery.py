#Script สำหรับดึงข้อมูลจาก BigQuery Public Datasets
import os
import pandas as pd
from google.cloud import bigquery
from dotenv import load_dotenv

#download file from dotenv
load_dotenv()

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
raw_data_path = "data/raw"

#Bigquery client
client = bigquery.Client(project=PROJECT_ID)

def extract_google_trends():
    """
    ดึงข้อมูล google trends จาก bigquery public dataset
    ดูว่าคนค้นหาอะไรมากที่สุดในแต่ละสัปดาห์
    """
    print("\n" + "=" * 50)
    print("ดึงข้อมูล google trends")
    print("=" * 50)

    #เช็คไฟล์มีจริงไหม
    output_file = os.path.join(raw_data_path, "google_trends.csv")
    if os.path.exists(output_file):
        print("found downloaded file, skip download")
        return
    
    #sql query for google trends
    query="""
        select
            term,
            week,
            score,
            `rank`
        from
            `bigquery-public-data.google_trends.top_terms`
        where
            week >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
        order by
            week DESC,
            `rank` ASC
        limit 5000
    """

    print("downloading from bigquery....")

    #รัน query แล้วแปลงเป็น dataframe
    df=client.query(query).to_dataframe()

    #บันทึกลงไฟล์ csv
    df.to_csv(output_file, index=False)

    print(f" Extracted!")
    print(f"rows: {len(df):,} | columns: {len(df.columns)}")
    print(f"save to: {output_file}")

#run script
if __name__ == "__main__":
    extract_google_trends()
    print("\n" + "=" *50)
    print("Extract bigquery done!")
    print("=" * 50)