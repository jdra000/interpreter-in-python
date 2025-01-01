import token_

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

	def next_token(self):

		self.skip_whitespace()

		match self.ch:
			case "=":
				if self.peek_next_char() == "=":
					ch = self.ch
					self.read_char()
					tok = new_token(token_.EQ, (ch + self.ch))
				else:
					tok = new_token(token_.ASSIGN, self.ch)
			case "+":
				tok = new_token(token_.PLUS, self.ch)
			case "-":
				tok = new_token(token_.MINUS, self.ch)
			case "!":
				if self.peek_next_char() == "=":
					ch = self.ch 
					self.read_char()
					tok = new_token(token_.NOT_EQ, (ch + self.ch))
				else:
					tok = new_token(token_.BANG, self.ch)
			case "/":
				tok = new_token(token_.SLASH, self.ch)
			case "*":
				tok = new_token(token_.ASTERISK, self.ch)
			case "<":
				tok = new_token(token_.LT, self.ch)
			case ">":
				tok = new_token(token_.GT, self.ch)
			case ";":
				tok = new_token(token_.SEMICOLON, self.ch)
			case ",":
				tok = new_token(token_.COMMA, self.ch)
			case "(":
				tok = new_token(token_.LPAREN, self.ch)
			case ")":
				tok = new_token(token_.RPAREN, self.ch)
			case "{":
				tok = new_token(token_.LBRACE, self.ch)
			case "}":
				tok = new_token(token_.RBRACE, self.ch)
			case 0:
				tok = new_token(token_.EOF, "")
			case _:

				if is_letter(self.ch):
					literal = self.read_identifier()
					type = token_.lookup_ident(literal)
					tok = new_token(type, literal)
					return tok

				elif is_digit(self.ch):
					literal = self.read_number()
					type = token_.INT
					tok = new_token(type, literal)
					return tok

				else:
					tok = new_token(token_.ILLEGAL, self.ch)

		self.read_char()
		return tok

	def peek_next_char(self):
		if self.readPosition >= len(self.input):
			return 0
		else:
			return self.input[self.readPosition]

	def skip_whitespace(self):
		while self.ch == " " or self.ch == "\t" or self.ch == "\n" or self.ch == "\r":
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

def new_token(type: token_.TokenType, ch: str):
	return token_.Token(Type = type, Literal = ch)



