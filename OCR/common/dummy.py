# import random
#
# random_number = random.randint(100000,999999)
#
# print(random_number)


# import requests
#
# url = "https://www.fast2sms.com/dev/bulkV2"
#
# payload = "sender_id=TXTIND&message=Hello this is test message from naveen &route=v3&numbers=7095695390"
#
# headers = {
#     'authorization': "DBU2nXDRHhsw2sWAM3I4edHRkRcOy7qOCJoSqj5tw68T1t7kTB9gg6OSQZrQ",
#     'Content-Type': "application/x-www-form-urlencoded",
#     'Cache-Control': "no-cache",
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)

from common.utils import sendTextMessage

response = sendTextMessage("Hello I am Naveen","70956953901")
print(response)