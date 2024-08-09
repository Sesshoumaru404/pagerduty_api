from api import APISession
import argparse

def main(args):
  pd_api = APISession(args.apikey, args.email);

  users_data = pd_api.http_get("users", {"limit": 2})
  users = users_data.get("users", [])

  print(users)

if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Coding interview.')
  parser.add_argument('-a', '--apikey')
  parser.add_argument('-e', '--email')

  args = parser.parse_args()

  main(args)
