# kryptoassingment
A price alert application that triggers an email when the user’s target price is achieved.

STEPS TO RUN THE APPLICATION:

Import all the tables from postgree_database.
Make a folder app and copy all the remaining .py files inside it.
Establish the connection between database and python and also with your frontend(Client side).
Now, you are good to run the application.
Finish

Automatic price alerts that send you an email automatically. A price alert application that triggers an email when the user’s target price is achieved. The application should send an email to the user when the price of BTC reaches 33,000$.

A rest API endpoint for the user’s to create an alert.

I used yahoo finance to get the real time price of BTC(Bit coin) and with the help of smtplib and email message library my API is sending Alert Emails to users if BTC price match with target price.

When the price of the coin reaches the price specified by the users, send an email to all the users that set the alert at that price. (send mail using Gmail SMTP)
