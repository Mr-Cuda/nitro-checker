import requests
from requests.api import head
from requests.models import parse_url

tokenlist_r = open("token.txt", "r")
tokenlist = tokenlist_r.readlines()

for current_token in tokenlist:
    token = current_token.rstrip("\n")
    headers = {"Authorization": token}
    check_payment_sources = requests.get('https://discord.com/api/v9/users/@me/billing/payment-sources', headers=headers)
    if '''"invalid": false''' in check_payment_sources.text:
        output = open("payment.txt", "a")
        output.write(f"Valid: {token}\n")
        output.close()
    check_subscription = requests.get('https://discord.com/api/v9/users/@me/billing/subscriptions', headers=headers)
    if check_subscription.status_code == '200' and check_subscription.text == '[]':
        pass
    else:
        output = open("subscription.txt", "a")
        output.write(f"Valid: {token}\n")
        output.close()
