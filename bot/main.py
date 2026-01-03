from publisher import send_message_sync

offers = [
    {
        "title": "Power Bank 20.000mAh – Offerta",
        "link": "https://amzn.to/49pAAVm"
    }
]

for offer in offers:
    send_message_sync(offer["title"], offer["link"])
