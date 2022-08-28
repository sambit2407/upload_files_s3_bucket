
import boto3
import pandas as pd
import argparse
import yaml

def read_params(config_path):
    """
    read parameters from the params.yaml file
    input: params.yaml location
    output: parameters as dictionary
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def connection(config_path):
    config=read_params(config_path)
    s3 = boto3.client('s3')


    s3 = boto3.resource(
    service_name='s3',
    region_name='your region name',
    aws_access_key_id=config['auth']['Access key ID'],
    aws_secret_access_key=config['auth']['Secret access key']
    )
    # Print out bucket names
    for bucket in s3.buckets.all():
        if bucket=='your bucket name':

            bucket_name=bucket

    
    filename = 'file.xlsx'
    s3.Bucket(bucket_name).upload_file(Filename=filename, Key=filename)



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="config.yml")
    parsed_args = args.parse_args()
    connection(config_path=parsed_args.config)