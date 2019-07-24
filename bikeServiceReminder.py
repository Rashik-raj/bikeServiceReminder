# import the smtplib module. It should be included in Python by default
import smtplib
from datetime import date

year = date.today().year
month1 = ['01', '04', '07', '10']
month2 = ['03', '06', '09', '12']
day = [24,11]
matchingDate1 = []
matchingDate2 = []

#creating data for matchingDate1
for eachMonth in month1:
	if eachMonth in month1[0:2]:
		matchingDate1.append(str(day[0]) + '/' + eachMonth + '/' + str(year+1))
	else:
		matchingDate1.append(str(day[0]) + '/' + eachMonth + '/' + str(year))

#creating data for matchingDate2
for eachMonth in month2:
	if eachMonth in month2[0]:
		matchingDate2.append(str(day[1]) + '/' + eachMonth + '/' + str(year+1))
	else:
		matchingDate2.append(str(day[1]) + '/' + eachMonth + '/' + str(year))

today = date.today()
today = today.strftime("%d/%m/%Y")

def sendMail(user):
	#login credentials
	_host_email = 'rashik123.rs@gmail.com'
	_receiver_email = ['rashik123.rs@gmail.com', 'sbibek23@gmail.com']
	_pass = 'bldhcebkivndfdis'

	# set up the SMTP server
	try:
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.ehlo()
		s.starttls()
	except:
		s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		s.ehlo()

	s.login(_host_email, _pass)

	#send mail
	s.sendmail(_host_email, _receiver_email[user], 'Subject: You need to service your motorcycle tommorrow.')
	s.quit()

if today in matchingDate1: #send to user 1
	sendMail(0)

if today in matchingDate2: #send to user 2
	sendMail(1)