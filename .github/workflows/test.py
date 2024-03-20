import os
import pysftp
def main():
  print("Hello there")
  token = os.environ.get("TOKEN")
  hostname = os.environ.get("HOST")
  user = os.environ.get("USERNAME")
  if not token:
    print("token is not defined")
  else:
    print("token is good")
    srv = pysftp.Connection(host=hostname, username=user, private_key=token)
    print("connection established successfully")
    srv.close()
  
# handling sftp connection for file deletion




# https://www.datacourses.com/deleting-files-on-sftp-server-2469/

if __name__ == '__main__':
  main()
