import ply.lex as lex
import ply.yacc as yacc

# Define a list of C++ keywords
cpp_keywords = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'double': 'DOUBLE',
    'void': 'VOID'
}

# Define the tokens
tokens = ['GCI', 'GCO', 'CIN', 'Q', 'COUT', 'MSG','HELO', 'LPRAN', 'RPRAN', 'NUM', 'ID', 'COMMA', 'SEMICOLON', 'SQBRACL', 'SQBRACR', 'LBRACES', 'RBRACES'] + list(cpp_keywords.values())

# Regular expressions for simple tokens
t_Q = r'"'
t_GCO = r'\<<'
t_GCI = r'\>>'
t_SEMICOLON = r';'
t_COMMA = r','
t_SQBRACL = r'\['
t_SQBRACR = r'\]'
t_LPRAN = r'\('
t_RPRAN = r'\)'
t_LBRACES = r'{'
t_RBRACES = r'}'

# Define regular expressions for specific tokens
def t_COUT(t):
    r'cout'
    t.type = cpp_keywords.get(t.value, 'COUT')
    return t

def t_CIN(t):
    r'cin'
    t.type = cpp_keywords.get(t.value, 'CIN')
    return t


def t_MSG(t):
    r'//[a-zA-Z0-9_]*'
    t.type = cpp_keywords.get(t.value, 'MSG')
    return t


def t_NUM(t):
    r'[0-9][0-9]*'
    t.type = cpp_keywords.get(t.value, 'NUM')
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = cpp_keywords.get(t.value, 'ID')
    return t
def t_HELO(t):
    r'[A-Z][A-Z0-9]*|[a-z][a-z0-9]*'
    t.type = cpp_keywords.get(t.value, 'HELO')
    return t
# Ignore whitespace and tabs
t_ignore = ' \t'

# Error handling for invalid tokens
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules for variable declarations
def p_statements(p):
    '''statements : type ID function content'''
    print("Valid declaration")


def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR
            | DOUBLE
            | VOID
    '''

def p_content(p):
    '''content : LBRACES arguments1 RBRACES
    '''

def p_arguments1(p):
    '''arguments1 : type ID SEMICOLON arguments1
                 | COUT GCO Q HELO Q SEMICOLON arguments1
                 | CIN GCI  ID SEMICOLON arguments1
                 | MSG 
                 |
                 '''

def p_arguments(p):
    '''arguments : type ID
                 | arguments COMMA type ID
                 | type dArray
                 | arguments COMMA type dArray
                 |
    '''

def p_function(p):
    '''function : LPRAN arguments RPRAN
    '''

def p_dArray(p):
    '''dArray : ID Array
               | ID SQBRACL SQBRACR
               | ID SQBRACL SQBRACR Array 
                    '''

def p_Array(p):
    '''Array : SQBRACL NUM SQBRACR
             | SQBRACL NUM SQBRACR Array
             '''

# Error handling for syntax errors
def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

# Input code to parse
while True:
    try:
        s = input("Enter: ")
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)
#competed