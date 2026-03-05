# AWS Image Metadata Logger

This project demonstrates a serverless architecture built using AWS Free Tier services.

## Architecture

S3 → Lambda → DynamoDB

## Services Used

- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch

## How It Works

1. An image is uploaded to the S3 images/ folder.
2. S3 triggers the Lambda function.
3. Lambda extracts file metadata.
4. Metadata is stored in DynamoDB.

## Technologies

Python, AWS Lambda, DynamoDB, S3

## Author

Adamu Muhammed