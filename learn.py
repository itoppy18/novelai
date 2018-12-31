#!/usr/bin/python3
#learn.py:学習処理
#©2018 Mamoru Itoi

import pickle

import analysis

#メイン関数
def main():
	connectionLearner()
	tokenListAppender()

#起動時に実行する処理
def start():
	with open("connections.pickle", "rb") as f:	
		Learn.connections = pickle.load(f)
	with open("tokenList.pickle", "rb") as f:
		Learn.tokenList = pickle.load(f)
	with open("parts.pickle", "rb") as f:
		Learn.parts = pickle.load(f)
	
#品詞のつながりを学習
def connectionLearner():
	tokens = analysis.tokens
	parts = Learn.parts
	#品詞リストの作成
	for token in tokens:
		surface = token[0]
		part = token[1]
		typeOfPart = token[2]
		inflection = token[6]
		parts.append([surface, part, typeOfPart, inflection])
	connections = Learn.connections
	i = 0
	#品詞のつながりを学習
	for part in parts:
		if i != 0:
			a = parts[i - 1][0]
			b = part[0]
			if not a in connections:
				connections[a] = []
			connections[a].append(b)
		i += 1
		
def tokenListAppender():
	tokenList = Learn.tokenList
	parts = Learn.parts
	for part in parts:
		surface = part[0]
		part = part[1]
		if not part in tokenList:
			tokenList[part] = []
		if not surface in part:
			tokenList[part].append(surface)

def end():
	with open("connections.pickle", "wb") as f:
		pickle.dump(Learn.connections, f)
	with open("tokenList,pickle", "wb") as f:
		pickle.dump(Learn.tokenList, f)
	with open("parts.pickle", "wb") as f:
		pickle.dump(Learn.parts, f)
	reset()
		
def reset():
	with open("connections.pickle", "wb") as f:
		pickle.dump({}, f)
	with open("tokenList.pickle", "wb") as f:
		pickle.dump({}, f)
	with open("parts.pickle", "wb") as f:
		pickle.dump([], f)
