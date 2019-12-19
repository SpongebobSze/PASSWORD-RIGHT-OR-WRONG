# 密码重试程式：密码='a123456'
# 最多三次机会
# 不对的话就印出'密码错误！你还有_次机会'；对的话就印出'登入成功'
password = 'a123456'
chance = 3
while True:
	pwd = input('请输入密码：')
	if pwd == password:
		print('登入成功')
		break
	else:
		chance = chance - 1
		print('你还有', chance ,'次机会')
		if chance == 0:
			break
		