#!/usr/bin/env python

import sys
import threading

state = None

import parser

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
	global state
	
	state = State()
	parser.state = state
	
	state.push(('(runtime)', 0))
	
	if len(argv) > 0:
		filename = argv.pop(0)
		sys.stdin = open(filename, 'r')
	else:
		filename = '(stdin)'
	
	parser._r()
	state.tok = parser.next_token()
	parser.stmts()
	
	state.pop()

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))