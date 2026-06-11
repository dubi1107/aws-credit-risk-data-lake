# aws-credit-risk-data-lake
Practice Project to work on data engineering skillset

## Project Log

## Day 1
- Created repository
- Set up Python virtual environment
- Installed pandas, numpy, and Faker
- Configured VS Code interpreter

- Added ability to generate customer data in generate_data.py
    - Used Faker to generate the data
    - Function has ability to vary the number of entries
- Created 1000 fake customer records

## Day 2
- Added function for generating accounts since people have transactions across different accounts
- Created a Jupyter notebook for data exploration purposes

## Day 3
- Added function for generating random transactions of differing amounts and categories
- Transaction values are using exponential function
- Saved raw data and starting to prepare the results for analytics

## Day 4
- Established practice S3 bucket in AWS to upload the parquet file to
- Spun up Athena to query the parquet and save the output in S3 bucket
- Ran several queries in Athena on the parquet that was uploaded