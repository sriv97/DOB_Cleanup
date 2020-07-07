"""
App.py

A Simple Python Utility to Remove Date of Birth from .log file

Author: Sri Velagapudi <sri.velagapudi@outlook.com>
Date Created: 7/6/2020
"""

import logging
import boto3
from botocore.exceptions import ClientError
import re

#making an initial connection to AWS S3 using Preconfigured AWS CLI
bucket = 'stellar.health.test.sri.velagapudi'
filename = 'patients.log'
resource = boto3.resource('s3')
my_bucket = resource.Bucket(bucket)


#Lists all available files in AWS Bucket
def list_all_files():
    for file in my_bucket.objects.all():
        print(file.key)

#Function to Upload a File
def upload_file(file_name, bucket, object_name='patients.log'):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#Download File
my_bucket.download_file(filename, '/Users/sri/Documents/StellarHealth/original_patients.log')

#Function to cleanup DOB
def cleanup():
    with open('/Users/sri/Documents/StellarHealth/original_patients.log','r+') as file, \
        open('/Users/sri/Documents/StellarHealth/patients_new.log','w') as file2:
        data = file.read()
        dates = re.findall(r"\d{1,2}[-/]\d{1,2}[-/]\d{4}", data)
        dateString = re.findall(r"DOB='\w+\s\d\w+\s\d{4}", data)
        for d in dates:
            originalDate = f"='{d}"
            year=f"='X/X/{d[-4:]}"
            data=re.sub(originalDate,year,data)
        for d in dateString:
            originalDate = f"{d}"
            year=f"='X/X/{d[-4:]}"
            data=re.sub(originalDate,year,data)    
        file2.write(data)

#Running Cleanup Code
cleanup()

#Uploading new File to AWS S3 Bucket
upload_file('/Users/sri/Documents/StellarHealth/patients_new.log', bucket)
