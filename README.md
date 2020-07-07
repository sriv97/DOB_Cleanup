# Stellar Health Coding Challenge
Anonymizes Date of Birth Format in Patient File Logs

### Detailed Setup Instructions
Requires Installation of Boto3 Package to interact with AWS Cloud [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)

Requires Installation of AWS CLI Tools [AWSCLI](https://aws.amazon.com/cli/)

After Successful Installation of AWS CLI

Run ```aws configure``` in a Terminal / CMD window

Enter in the Access Key ID and Secret Access Key to authenticate with AWS S3 Bucket

**_Please Note the Preset directory locations need to modified to your local working directory_**

#### What does the Python Script do?
Step 1: Creates a Connection with AWS Bucket

Step 2: Downloads the patients.log file and saves it to a local directory as original_patients.log

Step 3: Cleanup Function is run to remove month and day of DOB

Step 4: New file is created locally with the modified data

Step 5: The new file is uploaded to AWS Bucket with the same Object Key name to duplicate the existing logfile