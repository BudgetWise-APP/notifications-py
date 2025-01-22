import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('goooneoooogle@gmail.com', 'gwbs anwl buwf edhj')
    print("SMTP connection successful")
    server.quit()
except Exception as e:
    print(f"Error connecting to SMTP server: {e}")