# download.py
import yfinance as yf
import boto3

s3 = boto3.client('s3')
bucket = 'your-yahoo-data-pipeline'

def handler():
    data = yf.download('AAPL', start='2022-01-01', end='2023-01-01')
    file_path = '/tmp/aapl.csv'
    data.to_csv(file_path)
    s3.upload_file(file_path, bucket, 'raw/aapl.csv')

if __name__ == "__main__":
    handler()