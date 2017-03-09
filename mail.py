import smtplib

gmail_user = 'XXXX@gmail.com'  
gmail_password = 'XXXX'

fromur = gmail_user  
to = ['ayasedd@yahoo.com.tw']  
subject = 'YUIGAHAMA IS MY WIFE'  
body = 'YUIGAHAMA IS MY WIFEYUIGAHAMA IS MY WIFEYUIGAHAMA IS MY WIFEYUIGAHAMA IS MY WIFE'

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (fromur, ", ".join(to), subject, body)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    while 1:
    	server.sendmail(fromur, to, email_text)
    server.close()
    print('Email sent')
except:  
    print('GG')
