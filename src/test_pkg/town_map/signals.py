from src.test_pkg.town_map.signal import Signal
from src.test_pkg.town_map.signalReference import Signalreference
from src.test_pkg.town_map.signalReference import Signalreference
from typing import List
from src.test_pkg.town_map.signal import Signal


class Signals:
	def __init__(self, signal,signalReference,signalReference_list,signal_list):
		self.signal: Signal = signal
		self.signalReference: Signalreference = signalReference
		self.signalReference_list: List[Signalreference] = list()
		self.signal_list: List[Signal] = list()