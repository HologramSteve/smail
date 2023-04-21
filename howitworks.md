# How it works
This will document how SMail works, and more technical details.

## Getting mails
When loading the mails of a user, there are a few steps.
1, Getting the mails belonging to a user:
First, it gets the mails of a user by requesting it.
```
@client.request # Defines a cloud request
def getmails(username):
  return usermails.get(username) # Returns the username value from the usermails database
```
This will return all the mails of a user formatted like this:
```
MailId,MailId,MailId (for example; 84643298,82901288,91275263)
```
But, what is a mailid?
There are 2 databases: 1. Usermails, this contains all the users and what mails belong to them. For example:
```
{"Meneer_grave": [84643298,82901288,91275263]', "anderegebruiker": ["29183729"]}
```
The second database is Mails, this contains all the mails ever send by id. For example:
```
{"84643298": "hey hoe is het in frankrijk", "29183729": "Erg leuk, bedankt"}
```
### SMail uses [PickleDB](https://pythonhosted.org/pickleDB/) for its database

## Requesting a specific mailsees i
Requesting a specific mail goes like this:
```
@client.request # Defines a request
def getmail(id):
      return mails.get(id) # Gets the chosen mail by id and returns it
```
This returns the content of a mail, not that complicated.

## Sending a mail
Sending a mail isn't really sending a mail, it gets set into the database so when the person who recieves sees it when loading all the mails.
```
@client.request
def createmail(content)
    # and thats where the documentation stopped
```
