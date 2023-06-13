print("Starting server...")
# Config
projectid = ""
username = "radijz"
sessionid = ""

# Starting code (dont touch)
from dbhandler import getmail
from dbhandler import add_email
import scratchattach as scratch3
session = scratch3.Session(sessionid, username=username)
conn = session.connect_cloud(projectid)
server = scratch3.CloudRequests(conn)

# Requests
@server.request
def connect(username):
  print("Connected with " + username)
  return username
@server.request
def getusermails(username):
  mailsfromuser = []
  with open('db.json') as db:
    amountofmails = len(db)
    for i in amountofmails:
      result = getmail(i)
      if result[3] == username:
        mailsfromuser.append(result[3])
  returndata = mailsfromuser
  return returndata

@server.request
def getmailby(id):
  return getmail(id)

@server.request
def addmail(info):
  try:
    add_email(info)
    return "Mail made"
  except:
    return "Error"
# End code
@server.event
def on_ready():
    print("Server started!")

server.run()
