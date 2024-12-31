from typing import List
import token_

class Node:
	pass

class Statement(Node):
	pass

class Expression(Node):
	pass

class Program:
	def __init__(self):
		self.statements: List[Statement] = []

	def string(self):
		out = ""
		for stmt in self.statements:
			out += stmt.string()
		return out

class LetStatement(Statement):
	def __init__(self, token: token_.Token):
		self.token = token
		self.name = None # Identifier()
		self.value = None # Expression()

	def string(self):
		out = f"{self.token.Literal} {self.name.string()} = {self.value.string()}"
		return out


class ReturnStatement(Statement):
	def __init__(self, token: token_.Token):
		self.token = token
		self.return_value = None # Expression()

	def string(self):
		out = f"{self.token.Literal} {self.return_value.string()}"
		return out

class ExpressionStatement(Statement):
	def __init__(self, token: token_.Token):
		self.token = token
		self.expression = None # Expression()

	def string(self):
		return self.expression.string()

class Identifier(Expression):
	def __init__(self, token: token_.Token, value: str):
		self.token = token 
		self.value = value

	def string(self):
		return self.value

class IntegerLiteral(Expression):
	def __init__(self, token: token_.Token, value: int):
		self.token = token
		self.value = value

	def string(self):
		return self.value

class PrefixExpression(Expression):
	def __init__(self, token: token_.Token, operator: str):
		self.token = token
		self.operator = operator
		self.right = None # Expression()

	def string(self):
		out = f"( {self.operator} {self.right.string()} )"
		return out

class InfixExpression(Expression):
	def __init__(self, token: token_.Token, operator: str, left):
		self.token = token
		self.left = left
		self.operator = operator
		self.right = None

	def string(self):
		out = f"( {self.left.string()} {self.operator} {self.right.string()} )"









