import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class DataStream:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='your_region_name')
        self.table = self.dynamodb.Table('iot-data-platform-datastream')

    def put_item(self, device_id, timestamp, data_payload):
        """
        Insert an item into the DataStream table.
        """
        try:
            response = self.table.put_item(
                Item={
                    'device_id': device_id,
                    'timestamp': timestamp,
                    'data_payload': data_payload
                }
            )
            return response
        except ClientError as e:
            print(f"Error inserting item: {e}")
            return None

    def get_item(self, device_id, timestamp):
        """
        Retrieve an item from the DataStream table based on device_id and timestamp.
        """
        try:
            response = self.table.get_item(
                Key={
                    'device_id': device_id,
                    'timestamp': timestamp
                }
            )
            return response['Item']
        except ClientError as e:
            print(f"Error retrieving item: {e}")
            return None

    def query_items_by_device(self, device_id, start_timestamp=None, end_timestamp=None):
        """
        Query items based on a device_id. Optionally, filter by timestamp range.
        """
        try:
            if start_timestamp and end_timestamp:
                response = self.table.query(
                    KeyConditionExpression=Key('device_id').eq(device_id) & Key('timestamp').between(start_timestamp, end_timestamp)
                )
            else:
                response = self.table.query(
                    KeyConditionExpression=Key('device_id').eq(device_id)
                )
            return response['Items']
        except ClientError as e:
            print(f"Error querying items: {e}")
            return None

# Example usage:
# data_stream = DataStream()
# data_stream.put_item("device123", 1631302838, {"temperature": 22, "humidity": 50})
# print(data_stream.get_item("device123", 1631302838))
# print(data_stream.query_items_by_device("device123"))
