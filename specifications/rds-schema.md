## Users Table

| Column Name         | Data Type        | Constraints     |
|---------------------|------------------|-----------------|
| user_id             | INT              | PK, AUTO_INCREMENT |
| username            | VARCHAR(255)     | NOT NULL, UNIQUE|
| email               | VARCHAR(255)     | NOT NULL, UNIQUE|
| password            | VARCHAR(255)     | NOT NULL        |
| registration_date   | DATETIME         | NOT NULL        |
| last_login          | DATETIME         |                 |
| profile_picture_url | VARCHAR(512)     |                 |
| role                | ENUM('admin', 'standard', 'guest') | NOT NULL|

## Devices Table

| Column Name           | Data Type    | Constraints         |
|-----------------------|--------------|---------------------|
| device_id             | INT          | PK, AUTO_INCREMENT  |
| user_id               | INT          | FK to Users(user_id)|
| device_name           | VARCHAR(255) | NOT NULL            |
| device_type           | VARCHAR(255) | NOT NULL            |
| registration_date     | DATETIME     | NOT NULL            |
| last_active_date      | DATETIME     |                     |
| authentication_token  | VARCHAR(512) | NOT NULL, UNIQUE    |

## Device Groups Table

| Column Name   | Data Type    | Constraints         |
|---------------|--------------|---------------------|
| group_id      | INT          | PK, AUTO_INCREMENT  |
| group_name    | VARCHAR(255) | NOT NULL            |
| user_id       | INT          | FK to Users(user_id)|

## DeviceGroupMapping Table

| Column Name   | Data Type    | Constraints                    |
|---------------|--------------|--------------------------------|
| mapping_id    | INT          | PK, AUTO_INCREMENT             |
| group_id      | INT          | FK to Device Groups(group_id)  |
| device_id     | INT          | FK to Devices(device_id)       |

## Notifications Table

| Column Name     | Data Type    | Constraints         |
|-----------------|--------------|---------------------|
| notification_id | INT          | PK, AUTO_INCREMENT  |
| user_id         | INT          | FK to Users(user_id)|
| message         | TEXT         | NOT NULL            |
| created_at      | DATETIME     | NOT NULL            |
| read_status     | ENUM('read', 'unread') | NOT NULL   |


+--------------+
|    Users     |
+--------------+
| user_id (PK) |
| username     |
| email        |
| password     |
| registration_date |
| last_login   |
| profile_picture_url |
| role         |
+--------------+
       |
       | One-to-Many
       |
+--------------+
|   Devices    |
+--------------+
| device_id (PK)|
| user_id (FK)  |
| device_name  |
| device_type  |
| registration_date |
| last_active_date |
| authentication_token |
+--------------+
       |
       | One-to-Many
       |
+-----------------------------------+
|    DeviceGroupMapping              |
+-----------------------------------+
| mapping_id (PK)                   |
| group_id (FK)                     |
| device_id (FK)                    |
+-----------------------------------+
       |
       | Many-to-One
       |
+----------------+
| Device Groups  |
+----------------+
| group_id (PK)  |
| group_name     |
| user_id (FK)   |
+----------------+
       |
       | One-to-Many
       |
+----------------+
| Notifications  |
+----------------+
| notification_id (PK) |
| user_id (FK)   |
| message        |
| created_at     |
| read_status    |
+----------------+
