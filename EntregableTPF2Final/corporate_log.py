import boto3
import json
import uuid
import logging
from datetime import datetime

class CorporateLog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CorporateLog, cls).__new__(cls)
            cls.dynamodb = boto3.resource("dynamodb")
            cls.table = cls.dynamodb.Table("CorporateLog")
        return cls._instance

    def post(self, session_id, method_name):
        cpu_id = str(uuid.getnode())
        uniqueID = str(uuid.uuid4())
        timestamp = datetime.now().astimezone().isoformat(" ", timespec="microseconds")
        self.table.put_item(
            Item={
                "id" : uniqueID,
                "sessionid" : session_id,
                "method" : method_name,
                "CPUid": cpu_id,
                "timestamp": timestamp,
            }
        )

    def list(self, cpu_id, session_id=None):
        filter_expression = boto3.dynamodb.conditions.Attr("CPUid").eq(cpu_id)
        if session_id:
            filter_expression = filter_expression & boto3.dynamodb.conditions.Attr("sessionid").eq(session_id)
        response = self.table.scan(FilterExpression=filter_expression)
        return response["Items"]
