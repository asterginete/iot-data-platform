## DataStream Table

| Column Name   | Data Type    | Description                                    |
|---------------|--------------|------------------------------------------------|
| device_id     | String       | Partition Key; Identifier of the IoT device    |
| timestamp     | Number       | Sort Key; UNIX timestamp of the data entry     |
| data_payload  | Map          | JSON object with data (e.g., `{ "temperature": 22, "humidity": 50 }`) |

## Events Table

| Column Name  | Data Type    | Description                                     |
|--------------|--------------|-------------------------------------------------|
| event_id     | String       | Partition Key; Unique identifier for the event  |
| device_id    | String       | Identifier of the IoT device                    |
| timestamp    | Number       | UNIX timestamp of when the event was recorded   |
| event_type   | String       | Type of event (e.g., `threshold_breach`, `geofence_exit`) |
| event_data   | Map          | Additional details about the event in JSON format |

## DeviceSettings Table

| Column Name    | Data Type    | Description                               |
|----------------|--------------|-------------------------------------------|
| device_id      | String       | Partition Key; Identifier of the IoT device |
| setting_name   | String       | Sort Key; Name of the specific setting    |
| setting_value  | String/Map/Number/List | Value of the setting (could vary based on the setting type) |
