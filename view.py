from helpers import PagerdutyClient
import argparse

def main(args):
  pd_api = PagerdutyClient(args.apikey, args.email)

  users_data = pd_api.http_get("users", {"limit": 2})

  if not users_data:
    print("Nothing returned")
    return

  users = users_data.get("users", [])

  for user in users:
    print(user.get("name"))

if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Coding interview.')
  parser.add_argument('-a', '--apikey')
  parser.add_argument('-e', '--email')

  args = parser.parse_args()

  main(args)
