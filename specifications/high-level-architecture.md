```
+------------------------------------------+
|                User Interface            |
|                                          |
| +------------+     +------------------+  |
| | React App |<--->| Device Dashboard |  |
| +------------+     +------------------+  |
+------------------------------------------+
           ^
           | HTTP/API Calls
           v
+------------------------------------------+
|               Backend Server              |
|                                          |
| +---------+       +----------+  +------  |
| | FastAPI |<----->| AWS S3   |  | AWS   |
| +---------+       | (History)|  | Lambda|
|                   +----------+  +------  |
|                        ^                 |
|                        |                 |
|                   +----------+           |
|                   | AWS RDS  |           |
|                   +----------+           |
|                        ^                 |
|                        |                 |
|                   +----------+           |
|                   | DynamoDB |           |
|                   +----------+           |
+------------------------------------------+
```
