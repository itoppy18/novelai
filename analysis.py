#!/usr/bin/python3
#main.py:メイン処理
#©2018 Mamoru Itoi

import MeCab

import ui

tokens = []

def main(text):
	global tokens
	tokens = []
	t = MeCab.Tagger("")
	t.parse("")
	m = t.parseToNode(text)
	while m:
		tokenData = m.feature.split(",")
		token = [m.surface]
		for data in tokenData:
			token.append(data)
		tokens.append(token)
		m = m.next
