from src.map_parser_pkg.odr_map.signal import Signal
from src.map_parser_pkg.odr_map.signalreference import Signalreference
from typing import List


class Signals:
	def __init__(self,signal=None,signalreference_list=None,signal_list=None,signalreference=None):
		self.signal: Signal = signal
		self.signalreference_list: List[Signalreference] = signalreference_list
		self.signal_list: List[Signal] = signal_list
		self.signalreference: Signalreference = signalreference
