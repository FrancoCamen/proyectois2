from datetime import datetime
import uuid
import boto3
from corporate_data import CorporateData


# def post(self, session_id, method_name):
cpu_id = uuid.getnode()
timestamp = str(uuid.uuid4())
# table.put_item(
#     Item={
#         "id": session_id,
#             "method": method_name,
#             "CPUid": cpu_id,
#             "timestamp": timestamp,
#             }

# print(response)
timestamp = datetime.now().astimezone().isoformat(" ", timespec="microseconds")
print (timestamp)