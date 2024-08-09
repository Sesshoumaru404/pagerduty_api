import requests

class PagerdutyClient:
  def __init__(self, access_token, from_email):
    self.email = from_email
    self.session = self.create_session(access_token)
    self.url = "https://api.pagerduty.com/"

  def create_session(self, access_token):
    s = requests.Session();
    s.headers.update({'Accept': 'application/json'})
    s.headers.update({'Content-Type': 'application/json'})
    s.headers.update({'Authorization': f'Token token={access_token}'})
    s.headers.update({'From': f"From:{self.email}"})

    return s

  def http_get(self, endpoint, params=None):
    session = self.session
    res = session.get(self.url + endpoint, params=params)

    if res.status_code != 200:
      print(f"Status {res.status_code}")
      print(f"Error: {res.text}")
      return None

    data = res.json()
    return data

  def http_post(self, endpoint, data=None):
    session = self.session
    res = session.post(self.url + endpoint, json=data)

    if res.status_code != 200:
        print(f"Status {res.status_code}")
        print(f"Error: {res.text}")
        return None

    data = res.json()
    return data
