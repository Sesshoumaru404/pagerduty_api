from api import APISession
import argparse

def main(args):
  pd_api = APISession(args.apikey, args.email);

  print(vars(args))
  print(pd_api.session.headers)

  pd_api.get("users", {"limit": 2})

if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Coding interview.')
  parser.add_argument('-a', '--apikey')
  parser.add_argument('-e', '--email')

  args = parser.parse_args()

  main(args)
