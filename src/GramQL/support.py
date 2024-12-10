import logging as log
defLogLevel = log.INFO
log.basicConfig(level=defLogLevel)


#from .kDB import *
#defDBLocation = 'db.sql'
#kDB.init(defDBLocation)


#service
class qwe:
	def log(self, _msg=''):
		if _msg:
			_msg = f"with {_msg}"
		log.info(f"{self.__class__} Inited {_msg}")
