import requests

class YaCreateFolder:

    host = 'https://cloud-api.yandex.net/'
    token = 'y0_AgAAAAAQml7GAADLWwAAAADRcCCHsJlLaO3oST-5OvdRChPIiuG6M2g'

    def get_headers(self):
        return {
            'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self,path):
        headers = self.get_headers()
        url = self.host + "v1/disk/resources"
        params = {"path": path}
        res = requests.put(url, params=params, headers=headers)
        return res.status_code