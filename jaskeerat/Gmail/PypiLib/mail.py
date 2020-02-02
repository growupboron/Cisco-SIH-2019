import gmail as gm
password='kivypzbeurmnnvqk'
mailFrom='jaskee789@gmail.com'
message='mail cisco meraki'

auth=gm.Gmail(mailFrom,password)
msg=gm.Message(subject,to=mailTo,text=message)
auth.send(msg)
