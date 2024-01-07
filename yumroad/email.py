from flask_mail import Message
from yumroad.extensions import mail
from flask import render_template

DEFAULT_FROM = ('Yumroad', 'itzsahil0908@gmail.com')

def send_basic_welcome_message(recipient_email):
    message = Message('Welcome to yumroad',
                      sender=DEFAULT_FROM,
                      recipients=[recipient_email],
                      body="Thanks for joining. Let us know if you have any questions!")
    mail.send(message)

def send_welcome_message(user):
    store = user.stores
    message = Message('Welcome to yumroad {}'.format(store.name),
                      sender=DEFAULT_FROM,
                      recipients=[user.email])

    message.html = render_template('emails/welcome_basic.html', store=store)
    mail.send(message)

def send_pretty_welcome_message(user):
    store = user.store
    message = Message('Welcome to yumroad {}'.format(store.name),
                      sender=DEFAULT_FROM,
                      recipients=[user.email])

    message.html = render_template('emails/welcome_pretty.html', store=store, preview_text='Here is how you get started with Yumroad')
    mail.send(message)