import unittest
import ast_
import lexer
import parser

class ParserTest(unittest.TestCase):

	############ Testing statements ##########

	def test_let_statements(self):
		"""
		Test that it can parse LET statements.
		"""
		text = """let x = 5;
let y = 10;
let foobar = 838383;"""

		l = lexer.Lexer(text)
		p = parser.Parser(l)

		program = p.parse_program()

		self.assertEqual(len(program.statements), 3)

		test_identifiers = ["x", "y", "foobar"]

		for i in range (len(program.statements)):
			stmt = program.statements[i]

			self.assertIsInstance(stmt, ast_.LetStatement)

			self.assertEqual(stmt.token.Literal, "let")

			self.assertIsInstance(stmt.name, ast_.Identifier)
			self.assertEqual(stmt.name.value, test_identifiers[i])

	def test_return_statements(self):
		"""
		Test that it can parse RETURN statements.
		"""
		text = """return 5;
return 10;
return 838383;"""

		l = lexer.Lexer(text)
		p = parser.Parser(l)

		program = p.parse_program()

		self.assertEqual(len(program.statements), 3)

		for stmt in program.statements:
			self.assertIsInstance(stmt, ast_.ReturnStatement)
			self.assertEqual(stmt.token.Literal, "return")

	############ Testing expressions ##########

	def test_identifier_expressions(self):
		"""
		Test that it can parse IDENT expressions.
		"""
		text = """foobar;"""

		l = lexer.Lexer(text)
		p = parser.Parser(l)

		program = p.parse_program()

		self.assertEqual(len(program.statements), 1)

		stmt = program.statements[0]

		self.assertIsInstance(stmt, ast_.ExpressionStatement)

		self.assertEqual(stmt.token.Literal, "foobar")

		self.assertIsInstance(stmt.expression, ast_.Identifier)
		self.assertEqual(stmt.expression.value, "foobar")

	def test_integer_literal_expressions(self):
		"""
		Test that it can parse INT expressions.
		"""
		text = "5;"

		l = lexer.Lexer(text)
		p = parser.Parser(l)

		program = p.parse_program()

		self.assertEqual(len(program.statements), 1)

		stmt = program.statements[0]

		self.assertIsInstance(stmt, ast_.ExpressionStatement)

		self.assertEqual(stmt.token.Literal, "5")

		self.assertIsInstance(stmt.expression, ast_.IntegerLiteral)
		self.assertEqual(stmt.expression.value, 5)

	def test_prefix_expressions(self):
		"""
		Test that it can parse prefix expressions.
		"""
		tests = [
			{"input": "!5;", "operator": "!", "int_value": 5},
			{"input": "-15;", "operator": "-", "int_value": 15}
		]

		for test in tests:
			l = lexer.Lexer(test["input"])
			p = parser.Parser(l)

			program = p.parse_program()

			self.assertEqual(len(program.statements), 1)

			stmt = program.statements[0]

			self.assertIsInstance(stmt, ast_.ExpressionStatement)

			self.assertIsInstance(stmt.expression, ast_.PrefixExpression)
			self.assertEqual(stmt.expression.operator, test["operator"])
			self.assertIsInstance(stmt.expression.right, ast_.IntegerLiteral)
			self.assertEqual(stmt.expression.right.value, test["int_value"])


	def test_infix_expressions(self):
		"""
		Test that it can parse infix expressions.
		"""
		tests = [
			{"input": "5 + 5;", "left_value": 5, "operator": "+", "right_value": 5},
			{"input": "5 - 5;", "left_value": 5, "operator": "-", "right_value": 5},
			{"input": "5 * 5;", "left_value": 5, "operator": "*", "right_value": 5},
			{"input": "5 / 5;", "left_value": 5, "operator": "/", "right_value": 5},
			{"input": "5 > 5;", "left_value": 5, "operator": ">", "right_value": 5},
			{"input": "5 < 5;", "left_value": 5, "operator": "<", "right_value": 5},
			{"input": "5 == 5;", "left_value": 5, "operator": "==", "right_value": 5},
			{"input": "5 != 5;", "left_value": 5, "operator": "!=", "right_value": 5}
		]

		for test in tests:
			l = lexer.Lexer(test["input"])
			p = parser.Parser(l)

			program = p.parse_program()

			self.assertEqual(len(program.statements), 1)

			stmt = program.statements[0]

			self.assertIsInstance(stmt, ast_.ExpressionStatement)

			self.assertIsInstance(stmt.expression, ast_.InfixExpression)
			self.assertIsInstance(stmt.expression.left, ast_.IntegerLiteral)
			self.assertEqual(stmt.expression.left.value, test["left_value"])
			self.assertEqual(stmt.expression.operator, test["operator"])
			self.assertIsInstance(stmt.expression.right, ast_.IntegerLiteral)
			self.assertEqual(stmt.expression.right.value, test["right_value"])













