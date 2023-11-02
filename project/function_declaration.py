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
tokens = ['LPRAN','RPRAN','NUM', 'ID', 'COMMA', 'SEMICOLON', 'SQBRACL', 'SQBRACR'] + list(cpp_keywords.values())

# Regular expressions for simple tokens
t_COMMA = r','
t_SEMICOLON = r';'
t_SQBRACL = r'\['
t_SQBRACR = r'\]'
t_LPRAN=r'\('
t_RPRAN=r'\)'

# Define a regular expression for identifiers


def t_NUM(t):
    r'[0-9][0-9]*'
    t.type = cpp_keywords.get(t.value, 'NUM')
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = cpp_keywords.get(t.value, 'ID')
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
    '''statements : type ID function SEMICOLON'''
    print("Valid declaration")

def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR
            | DOUBLE
            | VOID'''
def p_function(p):
    '''function : LPRAN arguments RPRAN
    '''
def p_arguments(p):
    '''arguments : type
                 | arguments COMMA type
                 | type ID
                 | arguments COMMA type ID
                 | type dArray
                 | arguments COMMA type dArray
                 | type Array
                 | arguments COMMA type Array
    
    '''
def p_dArray(p):
    '''dArray : ID Array
               | SQBRACL SQBRACR
               | ID SQBRACL SQBRACR
               | ID SQBRACL SQBRACR Array 
               | SQBRACL SQBRACR Array
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
