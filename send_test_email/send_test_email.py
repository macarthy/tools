#!/usr/bin/env python3

import smtplib
import sys
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from xdg import BaseDirectory
from dotenv import dotenv_values

# Load the defaults from the configuration file
config_path = BaseDirectory.save_config_path('send_test_email')
config_file = f'{config_path}/send_test_email.conf'
config = dotenv_values(config_file)

# Create ArgumentParser object
parser = argparse.ArgumentParser(description='Send an email from the command line.')

# Add arguments
parser.add_argument('receiver_email', help='The recipient of the email.')
parser.add_argument('subject', help='The subject of the email.')
parser.add_argument('--body', help='The body text of the email.', default='')
parser.add_argument('--txt_file', help='A text file containing the body of the email.')
parser.add_argument('--html_file', help='An HTML file containing the body of the email.')

# Parse the arguments
args = parser.parse_args()

# Validate that at least one source of body content has been provided
if not args.body and not args.txt_file and not args.html_file:
    print("Error: You must provide a body, text file, or HTML file for the email content.")
    sys.exit()

# Create the email header
message = MIMEMultipart("alternative")
message["From"] = config['sender_email']
message["To"] = args.receiver_email
message["Subject"] = args.subject

# Attach the body text, if provided
if args.body:
    message.attach(MIMEText(args.body, "plain"))

# Attach the text file content, if provided
if args.txt_file:
    with open(args.txt_file, 'r') as file:
        text_content = file.read()
        message.attach(MIMEText(text_content, "plain"))

# Attach the HTML file content, if provided
if args.html_file:
    with open(args.html_file, 'r') as file:
        html_content = file.read()
        message.attach(MIMEText(html_content, "html"))

# Connect and login to the SMTP server
with smtplib.SMTP(config['smtp_server'], int(config['smtp_port'])) as server:
    server.starttls()
    server.login(config['username'], config['password'])

    # Send the email
    server.sendmail(config['sender_email'], args.receiver_email, message.as_string())

print("Email sent successfully")
