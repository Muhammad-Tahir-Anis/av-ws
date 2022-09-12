from src.map_parser_pkg.odr_map.signal import Signal
from src.map_parser_pkg.odr_map.signalreference import Signalreference
from src.map_parser_pkg.odr_map.signal import Signal
from typing import List
from src.map_parser_pkg.odr_map.signalreference import Signalreference

class Signals:
	def __init__(self,signal=None,signalReference=None,signal_list=None,signalReference_list=None):
		self.signal: Signal = signal
		self.signalreference: Signalreference = signalreference
		self.signal_list: List[Signal] = list()
		self.signalreference_list: List[Signalreference] = list()
