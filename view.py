from api import APISession

if __name__ == '__main__':
  pd_api = APISession("test", "email");

  print(pd_api.session.headers)
