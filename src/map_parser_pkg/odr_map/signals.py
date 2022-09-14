from src.map_parser_pkg.odr_map.signal import Signal
from src.map_parser_pkg.odr_map.signalreference import Signalreference
from typing import List


class Signals:
	def __init__(self,signal=None,signalreference=None,signal_list=None,signalreference_list=None):
		self.signal: Signal = signal
		self.signalreference: Signalreference = signalreference
		self.signal_list: List[Signal] = signal_list
		self.signalreference_list: List[Signalreference] = signalreference_list
