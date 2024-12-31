import ast_
import token_
import lexer

expression_dict = {
	"LOWEST": 1,
	"EQUALS": 2,
	"LESSGREATER": 3,
	"SUM": 4,
	"PRODUCT": 5,
	"PREFIX": 6,
	"CALL": 7,
}

precedence_dict = {
	token_.EQ: expression_dict["EQUALS"],
	token_.NOT_EQ: expression_dict["EQUALS"],

	token_.LT: expression_dict["LESSGREATER"],
	token_.GT: expression_dict["LESSGREATER"],

	token_.PLUS: expression_dict["SUM"],
	token_.MINUS: expression_dict["SUM"],

	token_.ASTERISK: expression_dict["PRODUCT"],
	token_.SLASH: expression_dict["PRODUCT"],
}

class Parser:
	def __init__(self, l: lexer.Lexer):
		self.l = l
		self.errors = []

		self.cur_token: token_.Token = None
		self.peek_token: token_.Token = None

		# Dicts to handle prefix and infix functions for expressions
		self.prefix_fns = {}
		self.infix_fns = {}

		# Read two tokens, so curToken and peekToken are both set
		self.next_token()
		self.next_token()

		# foobar;
		self.register_prefix(token_.IDENT, self.parse_identifier)
		# 5;
		self.register_prefix(token_.INT, self.parse_integer_literal)

		# !foobar,  -5
		self.register_prefix(token_.BANG, self.parse_prefix_expression)
		self.register_prefix(token_.MINUS, self.parse_prefix_expression)




		self.register_infix(token_.EQ, self.parse_infix_expression)
		self.register_infix(token_.NOT_EQ, self.parse_infix_expression)
		self.register_infix(token_.LT, self.parse_infix_expression)
		self.register_infix(token_.GT, self.parse_infix_expression)
		self.register_infix(token_.PLUS, self.parse_infix_expression)
		self.register_infix(token_.MINUS, self.parse_infix_expression)
		self.register_infix(token_.ASTERISK, self.parse_infix_expression)
		self.register_infix(token_.SLASH, self.parse_infix_expression)

	def register_prefix(self, token_type: token_.TokenType, fn):
		if token_type not in self.prefix_fns:
			self.prefix_fns[token_type] = fn

	def register_infix(self, token_type: token_.TokenType, fn):
		if token_type not in self.infix_fns:
			self.infix_fns[token_type] = fn






	def next_token(self):
		self.cur_token = self.peek_token
		self.peek_token = self.l.next_token()

	def parse_program(self):
		program = ast_.Program()

		while not self.cur_token_is(token_.EOF):
			stmt = self.parse_statement()
			if stmt != None:
				program.statements.append(stmt)

			self.next_token()

		return program

	def parse_statement(self):

		match self.cur_token.Type:
			# If the first token is LET we know is a LET statement
			case token_.LET:
				return self.parse_let_statement()
			# If it is RETURN we know is a RETURN statement
			case token_.RETURN:
				return self.parse_return_statement()
			# Otherwise, we know it has to be an EXPRESSION statement
			case _:
				return self.parse_expression_statement()

	def parse_let_statement(self):
		stmt = ast_.LetStatement(self.cur_token)

		if not self.expect_peek(token_.IDENT):
			return None

		stmt.name = ast_.Identifier(self.cur_token, self.cur_token.Literal)

		if not self.expect_peek(token_.ASSIGN):
			return None

		# Skip until encounter a semicolon
		while not self.cur_token_is(token_.SEMICOLON):
			self.next_token()

		return stmt

	def parse_return_statement(self):
		stmt = ast_.ReturnStatement(self.cur_token)

		self.next_token()

		# Skip until encounter a semicolon
		while not self.cur_token_is(token_.SEMICOLON):
			self.next_token()

		return stmt

	def parse_expression_statement(self):
		stmt = ast_.ExpressionStatement(self.cur_token)

		stmt.expression = self.parse_expression(expression_dict["LOWEST"])

		if self.peek_token_is(token_.SEMICOLON):
			self.next_token()

		return stmt

	def parse_expression(self, precedence: int):
		prefix = self.prefix_fns[self.cur_token.Type]

		if not prefix:
			return None

		left_exp = prefix()

		while not self.peek_token_is(token_.SEMICOLON) and precedence < self.peek_precedence():
			infix = self.infix_fns[self.peek_token.Type]
			if infix == None:
				return left_exp

			self.next_token()

			left_exp = infix(left_exp)

		return left_exp

	def parse_identifier(self):
		return ast_.Identifier(self.cur_token, self.cur_token.Literal)

	def parse_integer_literal(self):
		try:
			value = int(self.cur_token.Literal)
		except ValueError:
			msg = f"Could not parse {self.cur_token.Literal} as integer"
			return msg

		return ast_.IntegerLiteral(self.cur_token, value)

	def parse_prefix_expression(self):
		expression = ast_.PrefixExpression(self.cur_token, self.cur_token.Literal)

		self.next_token()

		expression.right = self.parse_expression(expression_dict["PREFIX"])

		return expression

	def parse_infix_expression(self, left):
		expression = ast_.InfixExpression(self.cur_token, self.cur_token.Literal, left)

		precedence = self.cur_precedence()

		self.next_token()

		expression.right = self.parse_expression(precedence)

		return expression






	# Helper methods
	def cur_token_is(self, t: token_.TokenType):
		return self.cur_token.Type == t

	def peek_token_is(self, t: token_.TokenType):
		return self.peek_token.Type == t

	def expect_peek(self, t: token_.TokenType):
		if self.peek_token_is(t):
			self.next_token()
			return True
		else:
			self.peek_error(t)
			return False

	def peek_error(self, t: token_.TokenType):
		msg = f"Expected token to be {t}, got {self.peek_token.Type}"
		self.errors.append(msg)

	def peek_precedence(self):
		return precedence_dict[self.peek_token.Type]

	def cur_precedence(self):
		return precedence_dict[self.cur_token.Type]














