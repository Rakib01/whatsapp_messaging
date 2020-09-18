import threading
from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


def send_msg():
    message = client.messages.create(
        from_='whatsapp:+1 415 523 8886 ',
        body='You are that woman who transformed my imperfections into perfections, just by the touch of your love. Love you my dearest wife! 😘💋❤️',
        to='whatsapp:+8801860989781'
    )
    print(message.sid)


def printit():
    threading.Timer(1.0, printit).start()
    print(send_msg())


printit()
