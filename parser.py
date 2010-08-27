import sys

state = None

def _r():
	state.r = sys.stdin.read(1)
	return state.r

def _read_name():
	nbuf = [ state.r ]
	
	state.r = _r()
	while state.r.isalpha():
		nbuf.append(_r())
	
	return ''.join(nbuf)

def next_token():
	while True:
		if state.r in ' \t':
			pass
		elif state.r.isalpha() or state.r in '_?!': # name
			return ('name', _read_name())
		elif state.r.isdigit():
			raise NotImplementedError("numbers aren't yet supported.")
		elif state.r in "{}()"
			_r()
			return (state.r,)
		elif state.r == '@':
			_r()
			return ('instvar', _read_name())
		else:
			return ("unknown", state.r)

def stmt():
	tok = next_token()
	
	if tok[0] == 'name':
		if tok[1] == 'class': # check for keywords
			pass
		else: # method call
			pass
