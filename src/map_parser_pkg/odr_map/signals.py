from src.map_parser_pkg.odr_map.signal import Signal
from typing import List
from src.map_parser_pkg.odr_map.signalreference import Signalreference


class Signals:
	def __init__(cls,signal=None,signal_list=None,signalreference=None,signalreference_list=None):
		cls.signal: Signal = signal
		cls.signal_list: List[Signal] = signal_list
		cls.signalreference: Signalreference = signalreference
		cls.signalreference_list: List[Signalreference] = signalreference_list
