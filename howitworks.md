# How it works
This will document how SMail works, and more technical details.

## Getting mails
When loading the mails of a user, there are a few steps. First we open the file, then we look how many mails there are in the database and then for each one we use the-

``` 
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
```




-```getmail``` function:

```
def getmail(id):
  import json
  with open('db.json') as db:
    data = json.load(db)
  mail = "mail-" + str(id)
  title = data[mail][0]['title']
  content = data[mail][0]['content']
  author = data[mail][0]['author']
  sendto = data[mail][0]['sendto']
  returndata = []
  returndata.append(mail)
  returndata.append(title)
  returndata.append(content)
  returndata.append(author)
  returndata.append(sendto)
  return returndata
```
This funtion is split into multiple parts, first it imports the json module and it opens the file. Then it sets the "mail" variable to the targeted item in the database, then it will set variables to all data from the email and make a list from it. Finnaly it will return the list.
Once a value is returned from the getmail function, it returns that value to the client.
Then scratch requests each mail from the user, this is to let more users use requests at the same time. This works with this simple request:
```
@server.request
def getmailby(id):
  return getmail(id)
```
