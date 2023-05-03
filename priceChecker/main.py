import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def main():
    # Load the CSV file with the products and prices
    products = pd.read_csv('products.csv')

    # Loop through each row of the CSV file
    for index, row in products.iterrows():
        # Get the URL of the product
        url = row['product_url']

        # Get the HTML content of the URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the element with the price of the product
        price_element = soup.find('span', {'class': 'price'})

        # Get the current price of the product
        current_price = float(price_element.text.strip().replace('$', '').replace(',', ''))

        # Compare the current price with the original price in the CSV file
        original_price = float(row['product_price'])
        if current_price < original_price:
            # Record the lowered price and the difference
            lowered_price = current_price
            difference = original_price - current_price
        else:
            # If the price did not lower, set the lowered price and difference to 0
            lowered_price = 0
            difference = 0

        # Add the lowered price and difference to the row
        products.loc[index, 'new_lowered_price'] = lowered_price
        products.loc[index, 'difference_in_price'] = difference

    # Save the updated CSV file with the lowered prices and differences
    products.to_csv('products_with_prices.csv', index=False)

    # Send an email with the updated CSV file attached
    send_email('your_email@gmail.com', 'Products with Lowered Prices', 'Please find attached the updated prices of the products.', 'products_with_prices.csv')


def send_email(to_address, subject, body, attachment_path):
    # Set up the email message
    message = MIMEMultipart()
    message['From'] = 'your_email@gmail.com'
    message['To'] = to_address
    message['Subject'] = subject

    # Attach the body of the email
    body_text = MIMEText(body)
    message.attach(body_text)

    # Attach the CSV file to the email
    with open(attachment_path, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='csv')
        attachment.add_header('Content-Disposition', 'attachment', filename='products_with_prices.csv')
        message.attach(attachment)

    # Send the email
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'your_email@gmail.com'
    smtp_password = 'your_email_password'
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_address, message.as_string())


if __name__ == '__main__':
    main()
