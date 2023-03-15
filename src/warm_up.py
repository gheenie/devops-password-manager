import boto3


s3 = boto3.client('s3')


bucket_name = 'gee-ns-bucket'
s3.create_bucket(Bucket=bucket_name)


# Assuming this script is run from the project's root

with open('.python-version', 'rb') as f:
    response_file1 = s3.put_object(Body=f, Bucket=bucket_name, Key='data/file1.txt')
print(response_file1)

with open('requirements.txt', 'rb') as f:
    response_file2 = s3.put_object(Body=f, Bucket=bucket_name, Key='data/file2.txt')
print(response_file2)


list_response = s3.list_objects_v2(Bucket=bucket_name)
key_list = [f['Key'] for f in list_response['Contents']]
print(key_list)

body = s3.get_object(Bucket=bucket_name, Key='data/file1.txt')['Body']
print(body.read().decode('utf-8'))

body = s3.get_object(Bucket=bucket_name, Key='data/file2.txt')['Body']
print(body.read().decode('utf-8'))


delete_block = {"Objects": [{"Key": t} for t in key_list]}
print(delete_block)
s3.delete_objects(Bucket=bucket_name, Delete=delete_block)


s3.delete_bucket(Bucket=bucket_name)
