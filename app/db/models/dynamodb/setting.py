import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class DeviceSetting:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='your_region_name')
        self.table = self.dynamodb.Table('iot-data-platform-settings')

    def put_setting(self, device_id, setting_name, setting_value):
        """
        Insert or update a setting for a device in the DeviceSettings table.
        """
        try:
            response = self.table.put_item(
                Item={
                    'device_id': device_id,
                    'setting_name': setting_name,
                    'setting_value': setting_value
                }
            )
            return response
        except ClientError as e:
            print(f"Error inserting/updating setting: {e}")
            return None

    def get_setting(self, device_id, setting_name):
        """
        Retrieve a setting for a device from the DeviceSettings table.
        """
        try:
            response = self.table.get_item(
                Key={
                    'device_id': device_id,
                    'setting_name': setting_name
                }
            )
            return response['Item']
        except ClientError as e:
            print(f"Error retrieving setting: {e}")
            return None

    def delete_setting(self, device_id, setting_name):
        """
        Delete a setting for a device.
        """
        try:
            response = self.table.delete_item(
                Key={
                    'device_id': device_id,
                    'setting_name': setting_name
                }
            )
            return response
        except ClientError as e:
            print(f"Error deleting setting: {e}")
            return None

# Example usage:
# setting_db = DeviceSetting()
# setting_db.put_setting("device123", "brightness", "70%")
# print(setting_db.get_setting("device123", "brightness"))
# setting_db.delete_setting("device123", "brightness")
