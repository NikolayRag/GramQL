from .support import *


class GramQL (qwe):
	chatId = 0

	def __init__(self, _chatId):
		self.chatId = _chatId

		self.log(_chatId)

