#!/usr/bin/python3
#gui.py:GUIを生成
#©2018 Mamoru Itoi

#モジュール読み込み
import sys
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QBrush, QColor, QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QAction, QApplication, QCheckBox, QGridLayout, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QTextEdit, QWidget

#内部のモジュール読み込み
import analysis
import create
import learn
from data import *

text = ""

class Main(QWidget):

	def __init__(self):
		super().__init__()
		self.title = "novelAI α0.0"
		self.left = 100
		self.top = 100
		self.width = 1000
		self.height = 600
		self.initUI()
	
	def initUI(self):
		#タイトル設定
		self.setWindowTitle(self.title)
		#位置・サイズ設定
		self.setGeometry(self.left, self.top, self.width, self.height)
		#最大化できないようにする
		self.setMaximumHeight(self.height)
		self.setMaximumWidth(self.width)
		self.setMinimumHeight(self.height)
		self.setMinimumWidth(self.width)
		#入力欄
		self.textbox = QLineEdit(self)
		self.textbox.move(5, 560)
		self.textbox.resize(350,30)
		#ログ領域
		self.responselbl = QTextEdit(self)
		self.responselbl.move(505, 10)
		self.responselbl.resize(460, 580)
		self.responselbl.setText(Create.novel)
		#送信ボタン
		self.sendButton = QPushButton("送信", self)
		self.sendButton.move(380,560)
		self.sendButton.clicked.connect(self.sendButtonClick)
		#実行
		self.show()
		
	@pyqtSlot()
	def sendButtonClick(self):
		global text
		text = self.textbox.text()
		if text == "":
			quit()
		else:
			analysis.main(text)
			learn.main()
			create.main()
			self.responselbl.setText(Create.novel)
			self.show()
			
app = QApplication(sys.argv)
ex = Main()
sys.exit(app.exec_())
