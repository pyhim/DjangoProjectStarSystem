import requests
import json


class Connector:

    server = "http://127.0.0.1:8000"
    api = ""
    auth = "rest-auth/login"
    path_to_cred = r"D:\All for Python\DjangoStarSystemProject\Api\auth.json"

    def __init__(self):
        self.session = requests.session()
        cred = json.load(open(self.path_to_cred, 'r'))
        res = self.session.post(self.auth_url, json=cred)
        self.session.headers.update({
            "Authorization": "Token " + res.json()["key"],
        })

    def url_maker(self, *items):
        m = "/".join([self.server, *items])+"/"
        return m

    @property
    def api_url(self):
        return self.url_maker(self.api)

    @property
    def auth_url(self):
        return self.url_maker(self.auth)

    def get_list(self, lc_model: str):
        res = self.session.get(self.url_maker(lc_model))
        return res.json()

    def create(self, lc_model: str, data):
        res = self.session.post(self.url_maker(lc_model), json=data)
        return res.json()
