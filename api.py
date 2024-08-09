import requests;

class APISession:
    def __init__(self, access_token, from_email):
      self.email = from_email
      self.session = self.create_session(access_token)

    def create_session(self, access_token):
      s = requests.Session();
      s.headers.update({'Accept': 'application/json'})
      s.headers.update({'Content-Type': 'application/json'})
      s.headers.update({'Authorization': f'Token token={access_token}'})
      s.headers.update({'From': f"From:{access_token}"})

      return s
