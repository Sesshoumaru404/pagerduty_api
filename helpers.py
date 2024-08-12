import requests

class User:
  def __init__(self, user_data):
    self.name = user_data.get("name")
    self.email = user_data.get("email")
    self.contact_methods = user_data.get("contact_methods")

  def display_contacts(self):
    for contact in self.contact_methods:
      print(f"{contact.get('summary')} - {contact.get('address')}")


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

    # Update 'From' header only if self.email is provided
    if self.email:
        s.headers.update({'From': f"{self.email}"})

    return s

  def http_get(self, endpoint, params=None):
    session = self.session
    res = session.get(self.url + endpoint, params=params)

    if res.status_code not in [200]:
      print(f"Status {res.status_code}")
      print(f"Error: {res.reason}")
      return None

    # print(f"Status {res.status_code}")
    data = res.json()
    return data

  def http_post(self, endpoint, data=None):
    session = self.session
    res = session.post(self.url + endpoint, json=data)

    if res.status_code not in [200]:
        print(f"Status {res.status_code}")
        print(f"Error: {res.text}")
        return None

    data = res.json()
    return data

def loop_users(users):
  for user in users:
    print(f"{user.get('id')} - {user.get('name')}")
