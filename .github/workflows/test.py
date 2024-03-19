import os
import pysftp
def main():
  print("Hello there")
  token = os.environ.get("TOKEN")
  if not token:
    print("token is not defined")
  else
    print("token is good")
  

if __name__ == '__main__':
  main()
