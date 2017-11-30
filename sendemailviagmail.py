 
# Import smtplib for the actual sending function
import smtplib
 
# For guessing MIME type
import mimetypes
 
# Import the email modules we'll need
import email
import email.mime.application
 
#Import sys to deal with command line arguments
import sys
 
# Create a text/plain message
msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = 'Yo'
msg['From'] = 'cfjsjd67@gmail.com'
msg['To'] = 'deddddi@mnmail.com'
 
# The main body is just another attachment
body = email.mime.Text.MIMEText("""Here you can write as many things as you want!""")
msg.attach(body)
 
# PDF attachment block code
 
##directory=sys.argv[1]
 
# Split de directory into fields separated by / to substract filename
 
##spl_dir=directory.split('/')
 
# We attach the name of the file to filename by taking the last
# position of the fragmented string, which is, indeed, the name
# of the file we've selected
 
##filename=spl_dir[len(spl_dir)-1]
 
# We'll do the same but this time to extract the file format (pdf, epub, docx...)
 
##spl_type=directory.split('.')
 
##type=spl_type[len(spl_type)-1]
 
##fp=open(directory,'rb')
##att = email.mime.application.MIMEApplication(fp.read(),_subtype=type)
##fp.close()
##att.add_header('Content-Disposition','attachment',filename=filename)
##msg.attach(att)
 
# send via Gmail server
# NOTE: my ISP, Centurylink, seems to be automatically rewriting
# port 25 packets to be port 587 and it is trashing port 587 packets.
# So, I use the default port 25, but I authenticate.
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login('c********@gmail.com','*******')
s.sendmail('dedhhhi@gmail.com',['hfg.bhd@gmail.com'], msg.as_string())
s.quit()