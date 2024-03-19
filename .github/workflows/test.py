import os
import pysftp
def main():
  print("Hello there")
  token = os.environ.get("TOKEN")
  if not token:
    print("token is not defined")
  else:
    print("token is good")
  
# handling sftp connection for file deletion

# https://www.datacourses.com/deleting-files-on-sftp-server-2469/

if __name__ == '__main__':
  main()
