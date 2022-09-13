from src.map_parser_pkg.odr_map.signalreference import Signalreference
from typing import List
from src.map_parser_pkg.odr_map.signal import Signal
from src.map_parser_pkg.odr_map.signalreference import Signalreference
from src.map_parser_pkg.odr_map.signal import Signal

class Signals:
	def __init__(self,signalreference_list=None,signal=None,signalreference=None,signal_list=None):
		self.signalreference_list = signalreference_list
		self.signal: Signal = signal
		self.signalreference = signalreference
		self.signal_list: List[Signal] = list()
