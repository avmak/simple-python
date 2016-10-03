def get_odds():
	for item in range(0, 10, 2):
		yield item

for count, item in enumerate(get_odds()):
	if count == 3:
		print(item)
		break
