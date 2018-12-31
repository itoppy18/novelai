#!/usr/bin/python3
#create.py:小説を生成させる
#©2018 Mamoru Itoi

import random

novel = ""

def main():
	tokenList = Learn.tokenList
	connections = Learn.connections
	newToken = ""
	oldToken = ""
	count = 0
	while count < 10:
		newToken = random.choice(connections[oldToken])
		global novel
		novel += newToken
		oldToken = newToken
		if newToken == "。":	
			count += 1
			newPart = "名詞"
	print("\n" + novel + "\n")
