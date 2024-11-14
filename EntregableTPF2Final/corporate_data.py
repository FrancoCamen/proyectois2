import boto3
import uuid
import botocore
import logging
from decimal import Decimal
from corporate_log import (
    CorporateLog,
)


class CorporateData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CorporateData, cls).__new__(cls)
            cls.dynamodb = boto3.resource("dynamodb")
            cls.table = cls.dynamodb.Table("CorporateData")
            cls.logger = CorporateLog()  # Instancia de CorporateLog para registrar logs
            
        return cls._instance

    def _log_method_call(self,session_id, method_name):
        """Método privado para registrar las llamadas a los métodos en CorporateLog."""
        self.logger.post(session_id, method_name=method_name)

    def getData(self, session_id, sede_id):
        """Recuperar datos de la tabla CorporateData y registrar la operación."""
        self._log_method_call(session_id,"getData")
        try:
            response = self.table.get_item(
                Key={"id": sede_id}
            )
            if "Item" in response:
                return {
                    "id": sede_id,
                    "domicilio": response["Item"].get("domicilio", ""),
                    "localidad": response["Item"].get("localidad", ""),
                    "cp": response["Item"].get("cp", ""),
                    "provincia": response["Item"].get("provincia", ""),
                }
            else:
                return {"error": "Registro no encontrado"}
        except Exception as e:
            return {"error": str(e)}

    def getCUIT(self, session_id, sede_id):
        """Recuperar CUIT de la tabla CorporateData y registrar la operación."""
        self._log_method_call(session_id, "getCUIT")
        try:
            response = self.table.get_item(
                Key={"id": sede_id}
            )
            if "Item" in response:
                return {"CUIT": response["Item"].get("CUIT", ""), "error": None}
            else:
                return {"error": "Registro no encontrado"}
        except Exception as e:
            return {"error": str(e)}

    def getSeqID(self, session_id,  sede_id):
        """Recuperar e incrementar el identificador único de secuencia y registrar la operación."""
        self._log_method_call(session_id ,"getSeqID")
        try:
            response = self.table.get_item(
                Key={"id": sede_id}
            )

            if "Item" in response:
                current_id = response['Item']['idSeq']
                new_id = current_id + 1

                # Actualizar el identificador único de secuencia en la tabla
                try:
                    response = self.table.update_item(
                        Key={"id": "UADER-FCyT-IS2"},
                        UpdateExpression="SET idSeq = :r",
                        ExpressionAttributeValues={":r": new_id},
                        ReturnValues="UPDATED_NEW",
                    )
                except botocore.exceptions.ClientError as err:
                    print("error accediendo tabla %s Error [%s,%s]" % (self.table.name,err.response["Error"]["Code"],err.response["Error"]["Message"]))
                    raise

                return {f"idSeq Actual : {current_id}. isSeq Incrementado : {new_id}"}
            else:
                return {"error": "Registro no encontrado"}
        except Exception as e:
            return {"error": str(e)}

    def listCorporateData(self, sede_id, session_id):
        """Listar datos corporativos por ID y registrar la operación."""
        self._log_method_call(session_id, "listCorporateData")
        response = self.table.scan(
            FilterExpression=boto3.dynamodb.conditions.Attr("id").eq(sede_id)
        )
        return response["Items"]

    def listCorporateLog(self, cpu_id, session_id):
        """Listar logs corporativos por CPU y registrar la operación."""
        self._log_method_call(session_id,"listCorporateLog")
        log_table = self.dynamodb.Table("CorporateLog")
        response = log_table.scan(
            FilterExpression=boto3.dynamodb.conditions.Attr("CPUid").eq(cpu_id)
        )
        return response["Items"]
