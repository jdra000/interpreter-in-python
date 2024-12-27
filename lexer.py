import token

class Lexer:
	def __init__(self, input: str):

		self.input = input
		self.position = 0
		self.readPosition = 0
		self.ch = ""

		self.read_char()

	def read_char(self):
		if self.readPosition >= len(self.input):
			self.ch = 0
		else:
			self.ch = self.input[self.readPosition]

		self.position = self.readPosition
		self.readPosition += 1

	def next_token(self) -> token.Token:

		self.skip_whitespace()

		match self.ch:
			case "=":
				if self.peek_next_char() == "=":
					ch = self.ch
					self.read_char()
					tok = new_token(token.EQ, (ch + self.ch))
				else:
					tok = new_token(token.ASSIGN, self.ch)
			case "+":
				tok = new_token(token.PLUS, self.ch)
			case "-":
				tok = new_token(token.MINUS, self.ch)
			case "!":
				if self.peek_next_char() == "=":
					ch = self.ch 
					self.read_char()
					tok = new_token(token.NOT_EQ, (ch + self.ch))
				else:
					tok = new_token(token.BANG, self.ch)
			case "/":
				tok = new_token(token.SLASH, self.ch)
			case "*":
				tok = new_token(token.ASTERISK, self.ch)
			case "<":
				tok = new_token(token.LT, self.ch)
			case ">":
				tok = new_token(token.GT, self.ch)
			case ";":
				tok = new_token(token.SEMICOLON, self.ch)
			case ",":
				tok = new_token(token.COMMA, self.ch)
			case "(":
				tok = new_token(token.LPAREN, self.ch)
			case ")":
				tok = new_token(token.RPAREN, self.ch)
			case "{":
				tok = new_token(token.LBRACE, self.ch)
			case "}":
				tok = new_token(token.RBRACE, self.ch)
			case 0:
				tok = new_token(token.EOF, "")
			case _:
				if is_letter(self.ch):
					literal = self.read_identifier()
					type = token.lookup_ident(literal)
					tok = new_token(type, literal)
					return tok
				elif is_digit(self.ch):
					literal = self.read_number()
					type = token.INT
					tok = new_token(type, literal)
					return tok
				else:
					tok = new_token(token.ILLEGAL, self.ch)

		self.read_char()
		return tok

	def peek_next_char(self):
		if self.readPosition >= len(self.input):
			return 0
		else:
			return self.input[self.readPosition]

	def skip_whitespace(self):
		if self.ch == " " or self.ch == "\t" or self.ch == "\n" or self.ch == "\r":
			self.read_char()

	def read_identifier(self):
		position = self.position
		while is_letter(self.ch):
			self.read_char()
		return self.input[position:self.position]

	def read_number(self):
		position = self.position
		while is_digit(self.ch):
			self.read_char()
		return self.input[position:self.position]


def is_letter(ch: str):
	return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or (ch == '_') 

def is_digit(ch: str):
	return ('0' <= ch <= '9')

def new_token(type: token.TokenType, ch: str):
	return token.Token(Type = type, Literal = ch)



