import os
import pysftp
def main():
  print("Hello there")
  token = os.environ.get("TOKEN")
  print(token)
  srv = pysftp.Connection(host="your_FTP_server", username="your_username",
  password="your_password")

if __name__ == '__main__':
  main()
