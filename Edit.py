import requests,os
success = 0
webhooklink = "https://discord.com/api/webhooks/12341234/abcxyz" #replace with webhook link here
messageid = input(" > Message ID, not the message link but the ID?\n > ")
while True:
	message = input(" > Message To Edit TO?\n > ")
	result = requests.patch(f"{webhooklink}/messages/{messageid}",json={"content":message})
	if result.status_code == 200:
		success += 1
		os.system(f"title [{success}] Message Edited!")
	else:
		print(f" > Error - Site responded with \n > {result.text}")
		os.system("title Error")
