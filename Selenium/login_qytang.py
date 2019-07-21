import time
from selenium import webdriver
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://qytsystem.qytang.com/accounts/login/');
time.sleep(3) # Let the user actually see something!
assert "乾颐堂" in driver.title

username = driver.find_element_by_id('id_username')
username.clear()
username.send_keys('pye_lijian')

password = driver.find_element_by_name('password')
password.clear()
password.send_keys('2Ao.Xsg')

# Find the element Login button

# Method 1 - LinkText- not working
#btn = driver.find_element_by_link_text("Sign in").click()
# Method 2 - X paht

btn = driver.find_element_by_xpath('//button[text()="Sign in"]')
# btn = driver.find_element_by_css_selector('button.btn dialog-confirm btn-primary')
btn.click()
time.sleep(7) # Let the user actually see something!
# 这里等待时间长，可以考虑用wait element

# find the element - Link - 课程日历
ljink = driver.find_element_by_link_text("课程日历").click()
time.sleep(3)

# # find the element - URL - Homework details for each day
today = str(datetime.datetime.today().date().isoformat())
today_day = datetime.datetime.today().strftime('%d')
#
url = driver.find_element_by_xpath("//table/tbody/tr[3]/td").find_element_by_tag_name('a')
url.click()
time.sleep(5)
whole_page = driver.find_element_by_tag_name('body')
whole_page_png = whole_page.screenshot_as_png
with open(f"{today}_homework.png", "wb") as file:
    file.write(whole_page_png)
driver.quit()
#
#
fromaddr = 'orchidv524@outlook.com'
toaddr = 'jian.li.de@outlook.com'

# More on MIME and multipart: https://en.wikipedia.org/wiki/MIME#Multipart_messages
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = f'Python Learning Homework_{today}'
# with open(f'{today}_homework.png', 'rb') as png:
#     msgImage = MIMEImage(png.read())
#
# msgImage.add_header('homework_screenshot', '<image1>')
# msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
# '<p><img src="cid:imgage1"></p>' +
# '</body></html>', 'html', 'utf-8'))

text = MIMEText("test")
msg.attach(text)
with open(f'{today}_homework.png', 'rb') as png:
    image = MIMEImage(png.read())

msg.attach(image)



# Define the image's ID as referenced above

# Sending the email via Gmail's SMTP server on port 587
server = smtplib.SMTP('smtp-mail.outlook.com', 587)

# SMTP connection is in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted.
server.starttls()

# Logging in to Gmail and sending the e-mail
server.login('orchidv524@outlook.com', 'kobe3117456789')
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()



