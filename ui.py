#!/usr/bin/python3
#ui.py:UIを生成
#©2018 Mamoru Itoi

text = None

def main():
	path = input("解析したいファイルのパスを入力してください。")
	with open(path, "r") as f:
		global text
		text = f.read().replace("\n", "")
	
