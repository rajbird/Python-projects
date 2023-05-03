*****************************************************
Rajbir Deol
*****************************************************

bot in python that:
- inputs a list of products provide in a csv. Formatted as such product_name,product_url,product_price
- parses the csv
- goes to the product_url and gets the product prices
- compares the product_price and if the price is lower, it records the lowered price
- creates a new csv with the product_name,product_url,product_price,new_lowered_price,difference_in_price
- sends an email to the user


*****************************************************
Run Code
*****************************************************

1. create a CSV file named products.csv in the same directory with the following format: product_name,product_url,product_price.
    - Fill it with your desired products and their URLs and prices.
2. update main.py to replace all occurances of your_email@gmail.com with a real email
3. update line 73 in main.py with the password of the email from step 2
4. Install Python and needed libraries pandas, requests, and BeautifulSoup.
5. run main.py
      - python main.py
