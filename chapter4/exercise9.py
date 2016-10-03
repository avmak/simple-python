def get_odds():
	for item in range(10):
		if item % 2 == 0:
			yield item

count = 0

for item in get_odds():
	if count == 3:
		print(item)
		break
	count += 1
