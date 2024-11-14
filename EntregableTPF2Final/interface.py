import uuid
from corporate_data import CorporateData


class Interface:
    def __init__(self, config_data):
        self.session_id = config_data.get("session_id", str(uuid.uuid4()))
        self.cpu_id = config_data.get("cpu_id", str(uuid.getnode()))
        self.sede_id = config_data.get("sede_id", "UADER-FCyT-IS2")
        self.corporate_data = CorporateData()


    def get_data(self):
        data_response = self.corporate_data.getData(
            self.session_id, self.sede_id
        )
        return data_response

    def get_cuit(self):
        cuit_response = self.corporate_data.getCUIT(
            self.session_id, self.sede_id
        )
        return cuit_response

    def get_seq_id(self):
        seq_id_response = self.corporate_data.getSeqID(
            self.session_id, self.sede_id
        )
        return seq_id_response

    def list_corporate_data(self):
        data_list = self.corporate_data.listCorporateData(self.sede_id, self.session_id)
        return data_list

    def list_corporate_log(self):
        log_list = self.corporate_data.listCorporateLog(self.cpu_id, self.session_id)
        return log_list
