import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = (
    'INT',
    'FLOAT',
    'DOUBLE',
    'CHAR',
    'ID',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMICOLON',
)

# Regular expression rules for simple C++ tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'

# Regular expression rules for more complex tokens
def t_DOUBLE(t):
    r'double'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_INT(t):
    r'int'
    return t

def t_CHAR(t):
    r'char'
    return t

# Regular expression for identifiers (function names, variable names, etc.)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the grammar rules for C++ function declarations
def p_function_declaration(p):
    '''
    function_declaration : type ID LPAREN parameter_list RPAREN SEMICOLON
                        | type ID LPAREN RPAREN SEMICOLON
    '''
    if len(p) == 7:
        print(f"Valid C++ function declaration: {p[1]} {p[2]}()")
    else:
        print(f"Valid C++ function declaration: {p[1]} {p[2]}()")

def p_type(p):
    '''type : INT
            | FLOAT
            | DOUBLE
            | CHAR
    '''
    p[0] = p[1]

def p_parameter_list(p):
    '''
    parameter_list : type ID
                | parameter_list COMMA type ID
    '''
    if len(p) == 3:
        p[0] = [(p[1], p[2])]
    else:
        p[0] = p[1] + [(p[3], p[4])]

def p_error(p):
    print(f"Syntax error in input: {p.value}")

# Build the parser
parser = yacc.yacc()

# Example inputs for testing
example_inputs = [
    "int add(int a, int b);",
    "double calculate();",
    "void invalid(int x,);"
]

# Parsing and checking the syntax for each input
for input_str in example_inputs:
    parser.parse(input_str)
