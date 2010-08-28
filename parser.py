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

def _expect(*types):
	tok = state.tok
	
	index = types.index(tok[0])
	
	if index == None:
		if len(types) > 1:
			joined = ', '.join(types[:-1]) + ' or ' + types[-1]
		else:
			joined = types[0]
		raise SyntaxError("unexpected %s, expecting %s." % (tok[0], joined))
	
	return (index, tok)

def _exp(*types):
	got, tok = _expect()
	
	state.tok = tok
	
	return (got, tok)

def block():
	next_token()

def stmt():
	got, tok = _expect('name')
	
	if got == 0:
		if tok[1] == 'class': # check for keywords
			got, tok = _expect('name')
			
			class_name = tok[1]
			
			got, tok = _expect('{')
		else: # method call
			method_name = tok[1]
			
			
			expr()
			
			