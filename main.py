import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.in/Titan-Analog-Black-Dial-Watch-1834NL01/dp/" \
      "B07XYD1LCQ/ref=sr_1_2?dchild=1&fst=as%3Aoff&pf_rd_i=2563504031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_" \
      "p=ea82bcc8-5c87-43c9-b2d6-ebaa0069f86b&pf_rd_r=CMSY8EX38YEG1HHRQDX1&pf_rd_" \
      "s=merchandised-search-5&qid=1617277974&refinements=p_89%3ATitan&rnid=1350388031&s=watch&sr=1-2"

header = {
    "User-Agent": "Mozilla/5.0 (Machintosh; Intel Mac OS X 10_15_5) ApplleWebkit/537.36 (KHTML, like Gecko) Chrome/"
                  "84.0.4147.125 Safari/537.125 Safari/537.36",
    "Accept-Language": "en=GB, en-US;q=0.8"
}


MY_EMAIL = "srikanth@gmail.com"
MY_PASSWORD = "Vagisha$299"
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

title = soup.find(id="procudtTitle").get_text().strip()
price(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addr="ramana@gmail.com",
            msg=f"Subject:Price Alert From Amazon Is Here :- \n\n{message}\n{url}"
        )



