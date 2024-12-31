TokenType = str

# Constants
# DIFFERENT ONES
ILLEGAL = "ILLEGAL"
EOF = "EOF"

# ASSIGNMENTS
IDENT = "IDENT" # add, x, y, ...
INT	= "INT" # 1234546..

# OPERATORS
ASSIGN = "="
PLUS = "+"
MINUS = "-"
BANG = "!"
ASTERISK = "*"
SLASH = "/"
LT = "<"
GT = ">"

# SYNTAX
COMMA = ","
SEMICOLON = ";"
LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"
EQ = "=="
NOT_EQ = "!="

# KEYWORDS
FUNCTION = "FUNCTION"
LET = "LET"
TRUE = "TRUE"
FALSE = "FALSE"
IF = "IF"
ELSE = "ELSE"
RETURN = "RETURN"

class Token:
	def __init__(self, Type: TokenType, Literal: str):
		self.Type = Type
		self.Literal = Literal

keywords = {
	"fn": FUNCTION,
	"let": LET,
	"true": TRUE,
	"false": FALSE,
	"if": IF,
	"else": ELSE,
	"return": RETURN
}

def lookup_ident(ident: str):
	if ident in keywords.keys():
		return keywords[ident]
	return IDENT



