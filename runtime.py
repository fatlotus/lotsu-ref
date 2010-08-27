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
	
	def push(self, ctx):
		self.contexts.append(list(ctx))
	
	def pop(self):
		self.contexts.pop()
	
	def incr_state(self):
		self.contexts[-1][1] += 1

def main(argv):
	state.push(('(runtime)', 0))
	
	if len(argv) > 0:
		filename = argv.shift()
		sys.stdin = open(filename, 'r')
	else:
		filename = '(stdin)'
	
	
	
	state.pop()