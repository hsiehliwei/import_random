import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	i = input('請輸入數字:')
	i = int(i)
	if i == r:
		print('被你猜中了!')
		break
	elif i > r:
		print('你猜的比答案大')
	elif i < r:
		print('你猜的比答案小')
	print('這是你猜的第', count, '次')
