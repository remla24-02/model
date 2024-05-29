"""
Download and extract training, testing and validation data.
"""

import os
import boto3
from botocore import UNSIGNED
from botocore.client import Config


def download_data(bucket_name, file_name, output_file):
    """
    Download data from S3 bucket.
    """
    s3 = boto3.client('s3', region_name='eu-north-1',
                      config=Config(signature_version=UNSIGNED))
    s3.download_file(bucket_name, file_name, output_file)


def main(model_name: str = 'trained_model'):
    """
    Main function.
    """
    bucket_name = 'dvc-remla24-02'

    # read the .dvc file in models folder
    with open(os.path.join('models', 'trained_model.joblib.dvc'), 'r', encoding='utf-8') as file:
        md5_hash = file.read()
        md5_hash = md5_hash.split(' ')[2]
        key = 'data/files/md5/' + md5_hash[:2] + '/' + md5_hash[2:]

    download_data(bucket_name, key.rstrip('\n'),
                  os.path.join('models', f'{model_name}.joblib'))


if __name__ == '__main__':
    main()
