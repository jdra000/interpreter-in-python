from typing import List
import token

class Node:
	pass

class Statement(Node):
	pass

class Expression(Node):
	pass

class Program:
	def __init__(self):
		self.statements: List[Statement] = []

class LetStatement(Statement):
	def __init__(self, token: token.Token):
		self.token = token
		self.name = None # Identifier()
		self.value = None # Expression()

class ReturnStatement(Statement):
	def __init__(self, token: token.Token):
		self.token = token
		self.return_value = None # Expression()

class ExpressionStatement(Statement):
	def __init__(self, token: token.Token):
		self.token = token
		self.expression = None # Expression()

class Identifier(Expression):
	def __init__(self, token: token.Token, value: str):
		self.token = token 
		self.value = value

class Integerliteral(Expression):
	def __init__(self, token: token.Token, value: int):
		self.token = token
		self.value = value

class PrefixExpression(Expression):
	def __init__(self, token: token.Token, operator: str):
		self.token = token
		self.operator = operator
		self.right = None # Expression()
