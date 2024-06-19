import http.client
import json
from datetime import date

class WGDataApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.conn = http.client.HTTPSConnection("api.wgdatalab.com", timeout=None)
        self.headers = {
            'X-API-KEY': self.api_key
        }

    def get_all_sites(self):
        print('Getting WG Sites...')
        payload = ''
        self.conn.request("GET", "/api/v1/sites/search", payload, self.headers)
        res = self.conn.getresponse()
        confirm = json.loads(res.read().decode('utf-8'))
        return confirm

    def update_site(self, site):
        payload = json.dumps(site)
        headers = {
            'X-API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }
        self.conn.request("PUT", f"/api/v1/sites/{site['wgSiteId']}", payload, headers)
        res = self.conn.getresponse()
        self.conn.close()
        return res.status
    
    def getDevices(self):
        payload = ''
        self.conn.request("GET", "/api/v1/devices/search", payload, self.headers)
        res = self.conn.getresponse()
        confirm = json.loads(res.read().decode('utf-8'))
        return confirm
    
    