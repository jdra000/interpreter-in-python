import ast
import token
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

class Parser:
	def __init__(l: lexer.Lexer):
		self.l = l
		self.errors = []

		self.cur_token: token.Token = None
		self.peek_token: token.Token = None

		# Dicts to handle prefix and infix functions for expressions
		self.prefix_fns = {}
		self.infix_fns = {}

		# Read two tokens, so curToken and peekToken are both set
		self.next_token()
		self.next_token()

		# foobar;
		self.register_prefix(token.IDENT, self.parse_identifier())
		# 5;
		self.register_prefix(token.INT, self.parse_integer_literal())

		# !foobar,  -5
		self.register_prefix(token.BANG, self.parse_prefix_expression())
		self.register_prefix(token.MINUS, self.parse_prefix_expression())

	def register_prefix(self, token_type: token.TokenType, fn):
		if token_type not in self.prefix_fns:
			self.prefix_fns[token_type] = fn

	def register_infix(self, token_type: token.TokenType, fn):
		if token_type not in self.infix_fns:
			self.infix_fns[token_type] = fn




	def next_token(self):
		self.cur_token = self.peek_token
		self.peek_token = self.l.next_token()

	def parse_program(self):
		program = ast.Program()

		while not self.cur_token(token.EOF):
			stmt = self.parse_statement()
			if stmt != None:
				program.statements.append(stmt)

			self.next_token()

		return program

	def parse_statement(self):
		match self.cur_token.Type:
			# If the first token is LET we know is a LET statement
			case token.LET:
				return self.parse_let_statement()
			# If it is RETURN we know is a RETURN statement
			case token.RETURN:
				return self.parse_return_statement()
			# Otherwise, we know it has to be an EXPRESSION statement
			case _:
				return self.parse_expression_statement()

	def parse_let_statement(self):
		stmt = ast.LetStatement(self.cur_token)

		if not self.expect_peek(token.IDENT):
			return None

		stmt.name = ast.Identifier(self.cur_token, self.cur_token.Literal)

		if not self.expect_peek(token.ASSIGN):
			return None

		# Skip until encounter a semicolon
		while not self.cur_token_is(token.SEMICOLON):
			self.next_token()

		return stmt

	def parse_return_statement(self):
		stmt = ast.ReturnStatement(self.cur_token)

		self.next_token()

		# Skip until encounter a semicolon
		while not self.cur_token_is(token.SEMICOLON):
			self.next_token()

		return stmt

	def parse_expression_statement(self):
		stmt = ast.ExpressionStatement(self.cur_token)

		stmt.expression = self.parse_expression(expression_dict["LOWEST"])

		if self.peek_token_is(token.SEMICOLON):
			self.next_token()

		return stmt

	def parse_expression(self, precedence: int):
		prefix = self.prefix_fns[self.cur_token.Type]

		if prefix == None:
			return None

		left_exp = prefix()
		return left_exp

	def parse_identifier(self):
		return ast.Identifier(self.cur_token, self.cur_token.Literal)

	def parse_integer_literal(self):
		return ast.Integerliteral(self.cur_token, int(self.cur_token.Literal))

	def parse_prefix_expression(self):
		expression = ast.PrefixExpression(self.cur_token, self.cur_token.Literal)

		self.next_token()

		expression.right = self.parse_expression(expression_dict["PREFIX"])

		return expression



	# Helper methods
	def cur_token_is(self, t: token.TokenType):
		return self.cur_token.Type == t

	def peek_token_is(self, t: token.TokenType):
		return self.peek_token.Type == t

	def expect_peek(self, t: token.TokenType):
		if peek_token_is(t):
			p.next_token()
			return True
		else:
			p.peek_error(t)
			return False

	def peek_error(self, t: token.TokenType):
		msg = f"Expected token to be {t}, got {self.peek_token.Type}"
		self.errors.append(msg)














