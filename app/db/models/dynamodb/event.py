import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class Event:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='your_region_name')
        self.table = self.dynamodb.Table('iot-data-platform-events')

    def put_event(self, event_id, device_id, timestamp, event_type, event_data):
        """
        Insert an event into the Events table.
        """
        try:
            response = self.table.put_item(
                Item={
                    'event_id': event_id,
                    'device_id': device_id,
                    'timestamp': timestamp,
                    'event_type': event_type,
                    'event_data': event_data
                }
            )
            return response
        except ClientError as e:
            print(f"Error inserting event: {e}")
            return None

    def get_event(self, event_id):
        """
        Retrieve an event from the Events table based on event_id.
        """
        try:
            response = self.table.get_item(
                Key={
                    'event_id': event_id
                }
            )
            return response['Item']
        except ClientError as e:
            print(f"Error retrieving event: {e}")
            return None

    def query_events_by_device(self, device_id):
        """
        Query events based on a device_id.
        """
        try:
            response = self.table.query(
                IndexName='device_id-index',  # Assuming a GSI with device_id
                KeyConditionExpression=Key('device_id').eq(device_id)
            )
            return response['Items']
        except ClientError as e:
            print(f"Error querying events: {e}")
            return None

# Example usage:
# event_db = Event()
# event_db.put_event("event123", "device123", 1631302838, "threshold_breach", {"temperature": 27})
# print(event_db.get_event("event123"))
# print(event_db.query_events_by_device("device123"))
