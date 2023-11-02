
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CHAR COMMA DOUBLE FLOAT ID INT LPRAN NUM RPRAN SEMICOLON SQBRACL SQBRACR VOIDstatements : type ID function SEMICOLONtype : INT\n            | FLOAT\n            | CHAR\n            | DOUBLE\n            | VOIDfunction : LPRAN arguments RPRAN\n    arguments : type\n                 | arguments COMMA type\n                 | type ID\n                 | arguments COMMA type ID\n                 | type dArray\n                 | arguments COMMA type dArray\n                 | type Array\n                 | arguments COMMA type Array\n    \n    dArray : ID Array\n               | SQBRACL SQBRACR\n               | ID SQBRACL SQBRACR\n               | ID SQBRACL SQBRACR Array \n               | SQBRACL SQBRACR Array\n                    Array : SQBRACL NUM SQBRACR\n             | SQBRACL NUM SQBRACR Array\n\n             '
    
_lr_action_items = {'INT':([0,10,15,],[3,3,3,]),'FLOAT':([0,10,15,],[4,4,4,]),'CHAR':([0,10,15,],[5,5,5,]),'DOUBLE':([0,10,15,],[6,6,6,]),'VOID':([0,10,15,],[7,7,7,]),'$end':([1,11,],[0,-1,]),'ID':([2,3,4,5,6,7,13,20,],[8,-2,-3,-4,-5,-6,16,25,]),'SQBRACL':([3,4,5,6,7,13,16,20,23,25,28,31,],[-2,-3,-4,-5,-6,19,22,19,29,22,29,29,]),'RPRAN':([3,4,5,6,7,12,13,16,17,18,20,21,23,25,26,27,28,30,31,32,33,],[-2,-3,-4,-5,-6,14,-8,-10,-12,-14,-9,-16,-17,-11,-13,-15,-18,-20,-21,-19,-22,]),'COMMA':([3,4,5,6,7,12,13,16,17,18,20,21,23,25,26,27,28,30,31,32,33,],[-2,-3,-4,-5,-6,15,-8,-10,-12,-14,-9,-16,-17,-11,-13,-15,-18,-20,-21,-19,-22,]),'LPRAN':([8,],[10,]),'SEMICOLON':([9,14,],[11,-7,]),'SQBRACR':([19,22,24,],[23,28,31,]),'NUM':([19,22,29,],[24,24,24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,],[1,]),'type':([0,10,15,],[2,13,20,]),'function':([8,],[9,]),'arguments':([10,],[12,]),'dArray':([13,20,],[17,26,]),'Array':([13,16,20,23,25,28,31,],[18,21,27,30,21,32,33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> type ID function SEMICOLON','statements',4,'p_statements','function_declaration.py',48),
  ('type -> INT','type',1,'p_type','function_declaration.py',52),
  ('type -> FLOAT','type',1,'p_type','function_declaration.py',53),
  ('type -> CHAR','type',1,'p_type','function_declaration.py',54),
  ('type -> DOUBLE','type',1,'p_type','function_declaration.py',55),
  ('type -> VOID','type',1,'p_type','function_declaration.py',56),
  ('function -> LPRAN arguments RPRAN','function',3,'p_function','function_declaration.py',58),
  ('arguments -> type','arguments',1,'p_arguments','function_declaration.py',61),
  ('arguments -> arguments COMMA type','arguments',3,'p_arguments','function_declaration.py',62),
  ('arguments -> type ID','arguments',2,'p_arguments','function_declaration.py',63),
  ('arguments -> arguments COMMA type ID','arguments',4,'p_arguments','function_declaration.py',64),
  ('arguments -> type dArray','arguments',2,'p_arguments','function_declaration.py',65),
  ('arguments -> arguments COMMA type dArray','arguments',4,'p_arguments','function_declaration.py',66),
  ('arguments -> type Array','arguments',2,'p_arguments','function_declaration.py',67),
  ('arguments -> arguments COMMA type Array','arguments',4,'p_arguments','function_declaration.py',68),
  ('dArray -> ID Array','dArray',2,'p_dArray','function_declaration.py',72),
  ('dArray -> SQBRACL SQBRACR','dArray',2,'p_dArray','function_declaration.py',73),
  ('dArray -> ID SQBRACL SQBRACR','dArray',3,'p_dArray','function_declaration.py',74),
  ('dArray -> ID SQBRACL SQBRACR Array','dArray',4,'p_dArray','function_declaration.py',75),
  ('dArray -> SQBRACL SQBRACR Array','dArray',3,'p_dArray','function_declaration.py',76),
  ('Array -> SQBRACL NUM SQBRACR','Array',3,'p_Array','function_declaration.py',79),
  ('Array -> SQBRACL NUM SQBRACR Array','Array',4,'p_Array','function_declaration.py',80),
]