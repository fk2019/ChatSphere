#!/usr/bin/python3
from user import User


def main():
    kwargs = { "first_name": "luffy", "last_name": "mugiwara"}
    u = User(**kwargs)
  #  u.first_name = "luffy"
    u.save()
    



main()
