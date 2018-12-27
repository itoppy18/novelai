#!/usr/bin/python3
#main.py:メイン処理
#©2018 Mamoru Itoi

import analysis
import create
import learn
import ui

def main():
	ui.main()
	analysis.main(ui.text)
	learn.main()
	create.main()
	
def start():
	learn.start()

def end():
	learn.end()
		
start()
main()
end()
