import lexer
import token

PROMPT = ">>"

def start():
	user_input = input(PROMPT)
	l = lexer.Lexer(user_input)

	while (tok := l.next_token()).Type != token.EOF:
		print(f"Type: {tok.Type}, Literal: {tok.Literal}")

start()