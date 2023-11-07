import ply.lex as lex
import ply.yacc as yacc

# Define a list of C++ keywords
cpp_keywords = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'double': 'DOUBLE',
    'void':'VOID',
    'public':'PUBLIC',
    'private':'PRIVATE',
    'protected':'PROTECTED',
    'class':'CLASS'
}
tokens = ['NUM', 'ID', 'COLON', 'SEMICOLON','LBRACES','RBRACES','SQBRACL','SQBRACR','COMMA'] + list(cpp_keywords.values())

# Regular expressions for simple tokens
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_SQBRACL = r'\['
t_SQBRACR = r'\]'
t_LBRACES = r'{'
t_RBRACES = r'}'

def t_NUM(t):
    r'[0-9][0-9]*'
    t.type = cpp_keywords.get(t.value, 'NUM')
    return t
    
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = cpp_keywords.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_start(p):
    '''start : declaration '''
    print("Valid declaration")

def p_declaration(p):
    '''declaration  : class ID LBRACES content RBRACES SEMICOLON'''

def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR
            | DOUBLE
            | VOID'''
    
def p_class(p):
    '''class : CLASS  
    '''
    
def p_content(p):
    '''content : access arguments SEMICOLON 
               | arguments SEMICOLON 
               | arguments COMMA ID SEMICOLON 
               | access arguments COMMA ID SEMICOLON 
               | arguments COMMA Array SEMICOLON 
               | access arguments COMMA Array SEMICOLON 
               | arguments COMMA dArray SEMICOLON 
               | access arguments COMMA dArray SEMICOLON 
               | 
    '''

def p_access(p):
    '''access : PUBLIC COLON
              | PRIVATE COLON
              | PROTECTED COLON
              |
    '''

def p_arguments(p):
    '''arguments : type ID
                 | type Array
                 | type dArray
    '''

def p_Array(p):
    '''Array : SQBRACL NUM SQBRACR
             | SQBRACL NUM SQBRACR Array
             '''

def p_dArray(p):
    '''dArray : ID Array
               | SQBRACL SQBRACR
               | ID SQBRACL SQBRACR
               | ID SQBRACL SQBRACR Array 
               | SQBRACL SQBRACR Array
    '''


def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

while True:
    try:
        s = input("Enter: ")
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)