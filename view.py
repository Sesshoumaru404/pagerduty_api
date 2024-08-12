from helpers import PagerdutyClient, User, loop_users
import argparse

def main(args):
  pd_api = PagerdutyClient(args.apikey, args.email)

  users_data = pd_api.http_get("users")

  if not users_data:
    print("Nothing returned")
    return
  user_input = ""
  while not user_input:
    users = users_data.get("users", [])
    loop_users(users)
    user_input = input("Select a user by user ID or enter for next page: ")
    if not user_input:
      more = users_data.get("more", False)
      limit = users_data.get("limit", False)
      offset = users_data.get("offset", False)
      if more:
        users_data = pd_api.http_get("users", {"offset": offset + limit})
      else:
        return
    else:
      break

  user_data = pd_api.http_get(f"users/{user_input}", {"include[]": "contact_methods"})

  if not user_data:
    return
  else:
    user_data= user_data.get("user")

  user = User(user_data)

  print(user.name)
  print(user.display_contacts())

if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Coding interview.')
  parser.add_argument('-a', '--apikey')
  parser.add_argument('-e', '--email')

  args = parser.parse_args()

  main(args)
