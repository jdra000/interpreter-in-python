import unittest
import token_
import lexer



class LexerTest(unittest.TestCase):

	############ Testing lexer ##########

	def test_next_token(self):
		text = """let five = 5;
	let ten = 10;
	let add = fn(x, y) {
		x + y;
	};
	let result = add(five, ten);
	!-/*5;
	5 < 10 > 5;

	if (5 < 10) {
		return true;
	} else {
		return false;
	}

	10 == 10;
	10 != 9;"""
		
		tests = [
		    {"expected_type": token_.LET, "expected_literal": "let"},
		    {"expected_type": token_.IDENT, "expected_literal": "five"},
		    {"expected_type": token_.ASSIGN, "expected_literal": "="},
		    {"expected_type": token_.INT, "expected_literal": "5"},
		    {"expected_type": token_.SEMICOLON, "expected_literal": ";"},

		    {"expected_type": token_.LET, "expected_literal": "let"},
		    {"expected_type": token_.IDENT, "expected_literal": "ten"},
		    {"expected_type": token_.ASSIGN, "expected_literal": "="},
		    {"expected_type": token_.INT, "expected_literal": "10"},
		    {"expected_type": token_.SEMICOLON, "expected_literal": ";"},

		    {"expected_type": token_.LET, "expected_literal": "let"},
		    {"expected_type": token_.IDENT, "expected_literal": "add"},
		    {"expected_type": token_.ASSIGN, "expected_literal": "="},
		    {"expected_type": token_.FUNCTION, "expected_literal": "fn"},
		    {"expected_type": token_.LPAREN, "expected_literal": "("},
		    {"expected_type": token_.IDENT, "expected_literal": "x"},
		    {"expected_type": token_.COMMA, "expected_literal": ","},
		    {"expected_type": token_.IDENT, "expected_literal": "y"},
		    {"expected_type": token_.RPAREN, "expected_literal": ")"},
		    {"expected_type": token_.LBRACE, "expected_literal": "{"},
		    {"expected_type": token_.IDENT, "expected_literal": "x"},
		    {"expected_type": token_.PLUS, "expected_literal": "+"},
		    {"expected_type": token_.IDENT, "expected_literal": "y"},
		    {"expected_type": token_.SEMICOLON, "expected_literal": ";"},
		    {"expected_type": token_.RBRACE, "expected_literal": "}"},
		    {"expected_type": token_.SEMICOLON, "expected_literal": ";"},

		    {"expected_type": token_.LET, "expected_literal": "let"},
		    {"expected_type": token_.IDENT, "expected_literal": "result"},
		    {"expected_type": token_.ASSIGN, "expected_literal": "="},
		    {"expected_type": token_.IDENT, "expected_literal": "add"},
		    {"expected_type": token_.LPAREN, "expected_literal": "("},
		    {"expected_type": token_.IDENT, "expected_literal": "five"},
		    {"expected_type": token_.COMMA, "expected_literal": ","},
		    {"expected_type": token_.IDENT, "expected_literal": "ten"},
		    {"expected_type": token_.RPAREN, "expected_literal": ")"},
		    {"expected_type": token_.SEMICOLON, "expected_literal": ";"},

		    {"expected_type": token_.BANG, "expected_literal": "!"},
		    {"expected_type": token_.MINUS, "expected_literal": "-"},
		    {"expected_type": token_.SLASH, "expected_literal": "/"},
		    {"expected_type": token_.ASTERISK, "expected_literal": "*"},
		    {"expected_type": token_.INT, "expected_literal": "5"},
		    {"expected_type": token_.SEMICOLON, "expected_literal": ";"},

		    {"expected_type": token_.INT, "expected_literal": "5"},
		    {"expected_type": token_.LT, "expected_literal": "<"},
		    {"expected_type": token_.INT, "expected_literal": "10"},
		    {"expected_type": token_.GT, "expected_literal": ">"},
		    {"expected_type": token_.INT, "expected_literal": "5"},
		    {"expected_type": token_.SEMICOLON, "expected_literal": ";"},

		    {"expected_type": token_.IF, "expected_literal": "if"},
		    {"expected_type": token_.LPAREN, "expected_literal": "("},
		    {"expected_type": token_.INT, "expected_literal": "5"},
		    {"expected_type": token_.LT, "expected_literal": "<"},
		    {"expected_type": token_.INT, "expected_literal": "10"},
		    {"expected_type": token_.RPAREN, "expected_literal": ")"},
		    {"expected_type": token_.LBRACE, "expected_literal": "{"},
		    {"expected_type": token_.RETURN, "expected_literal": "return"},
		    {"expected_type": token_.TRUE, "expected_literal": "true"},
		    {"expected_type": token_.SEMICOLON, "expected_literal": ";"},
		    {"expected_type": token_.RBRACE, "expected_literal": "}"},
		    {"expected_type": token_.ELSE, "expected_literal": "else"},
		    {"expected_type": token_.LBRACE, "expected_literal": "{"},
		    {"expected_type": token_.RETURN, "expected_literal": "return"},
		    {"expected_type": token_.FALSE, "expected_literal": "false"},
		    {"expected_type": token_.SEMICOLON, "expected_literal": ";"},
		    {"expected_type": token_.RBRACE, "expected_literal": "}"},

		    {"expected_type": token_.INT, "expected_literal": "10"},
		    {"expected_type": token_.EQ, "expected_literal": "=="},
		    {"expected_type": token_.INT, "expected_literal": "10"},
		    {"expected_type": token_.SEMICOLON, "expected_literal": ";"},

		    {"expected_type": token_.INT, "expected_literal": "10"},
		    {"expected_type": token_.NOT_EQ, "expected_literal": "!="},
		    {"expected_type": token_.INT, "expected_literal": "9"},
		    {"expected_type": token_.SEMICOLON, "expected_literal": ";"},

		    {"expected_type": token_.EOF, "expected_literal": ""}
		]


		l = lexer.Lexer(text)

		for i, test in enumerate(tests):
			tok = l.next_token()

			self.assertEqual(tok.Type, test["expected_type"])
			self.assertEqual(tok.Literal, test["expected_literal"])



