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

def add_email(emailinfo):
    import json
    email_data = emailinfo

    title, content, author, sendto = email_data.split(',')

    new_email = {
      "title": title.strip(),
      "content": content.strip(),
      "author": author.strip(),
      "sendto": sendto.strip()
    }
    with open('db.json') as f:
        data = json.load(f)
    email_id = "mail-" + str(len(data) + 1)
    data[email_id] = [new_email]
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=2)

# example usage
#new_email = {
#    "title": "New Email Title",
#    "content": "This is the content of the new email",
#    "author": "John Doe",
#    "sendto": "jane@example.com"
#}
#add_email('your_file.json', new_email)
