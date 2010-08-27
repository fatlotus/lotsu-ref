#!/usr/bin/env python

import threading

state = State()

import parser
parser.state = state

class State(threading.local):
	contexts = [ ]
	
	def filename(self):
		return self.contexts[-1][0]
	
	def lineno(self):
		return self.contexts[-1][1]

def main(argv):
	if len(argv) > 0:
		