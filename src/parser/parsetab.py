
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN COMMA DEF DIFF DIVIDE ELIF ELSE EQ FALSE FLOAT FOR GET GT ID IF IN INTEGER LBRACE LBRACKET LET LPAREN LT MINUS MINUSMINUS MULTIPLY NOT OR PLUS PLUSPLUS RBRACE RBRACKET RPAREN SEMI STRING TRUE WHILEcode : code sent\n\t\t\t\t| sent\n\t\t\t\t| emptysent : statement\n\t\t\t\t| instruction SEMIinstruction : assign\n\t\t\t\t\t   | functionstatement : function_definition\n\t\t\t\t\t | for_statement\n\t\t\t\t\t | if_statement\n\t\t\t\t\t | while_statementfor_statement : FOR LPAREN for_valid_expr COMMA for_valid_expr COMMA for_valid_iter RPAREN LBRACE code RBRACE\n\t\t\t\t\t \t | FOR LPAREN ID IN ID RPAREN LBRACE code RBRACEfor_valid_expr : expr_num\n\t\t\t\t\t\t  | expr_arithmfor_valid_iter : PLUS\n\t\t\t\t\t\t  | PLUSPLUS\n\t\t\t\t\t\t  | MINUS\n\t\t\t\t\t\t  | MINUSMINUSif_statement : IF LPAREN logic_list RPAREN LBRACE code RBRACE\n\t\t\t  \t\t\t| IF LPAREN logic_list RPAREN LBRACE code RBRACE elif_sent\n\t\t\t  \t\t\t| IF LPAREN logic_list RPAREN LBRACE code RBRACE ELSE LBRACE code RBRACE\n\t\t\t  \t\t\t| IF LPAREN logic_list RPAREN LBRACE code RBRACE elif_sent ELSE LBRACE code RBRACEelif_sent : ELIF LPAREN logic_list RPAREN LBRACE code RBRACE elif_sent\n\t\t\t\t\t | emptywhile_statement : WHILE LPAREN logic_list RPAREN LBRACE code RBRACEfunction_definition : DEF ID LPAREN RPAREN LBRACE code RBRACEassign : ID ASSIGN expr_type\n\t\t\t\t  | ID ASSIGN expr_arithm\n\t\t\t\t  | ID ASSIGN logic_list\n\t\t\t\t  | ID ASSIGN expr_listassign : ID ASSIGN functionfunction : ID LPAREN list RPARENlist : list COMMA ID\n\t\t\t\t| list COMMA function\n\t\t\t\t| function\n\t\t\t\t| IDlist : list COMMA expr_type\n\t\t\t\t| expr_type\n\t\t\t\t| emptylist : list COMMA expr_arithm\n\t\t\t\t| list COMMA logic_list\n\t\t\t\t| expr_arithm\n\t\t\t\t| logic_listlogic_list : LPAREN logic_list RPARENlogic_list : logic_list AND logic_list\n\t\t\t\t\t  | logic_list OR logic_list\n\t\t\t\t\t  | expr_boolexpr_bool : expr_bool EQ expr_bool\n\t\t\t\t\t | expr_bool LT expr_bool\n\t\t\t\t\t | expr_bool LET expr_bool\n\t\t\t\t\t | expr_bool GT expr_bool\n\t\t\t\t\t | expr_bool GET expr_bool\n\t\t\t\t\t | expr_bool DIFF expr_bool\n\t\t\t\t\t | NOT expr_boolexpr_bool : functionexpr_bool : expr_type\n\t\t\t\t\t | expr_arithmexpr_arithm : LPAREN expr_arithm RPARENexpr_arithm : expr_arithm PLUS expr_arithm\n\t\t\t\t\t   | expr_arithm MINUS expr_arithm\n\t\t\t\t\t   | expr_arithm MULTIPLY expr_arithm\n\t\t\t\t\t   | expr_arithm DIVIDE expr_arithm\n\t\t\t\t\t   | MINUS expr_arithmexpr_arithm : ID\n\t\t\t\t\t   | functionexpr_arithm : expr_typefunction : sent_index_listsent_index_list : sent_index_list LBRACKET ID RBRACKET\n\t\t\t\t\t\t   | ID LBRACKET ID RBRACKETsent_index_list : sent_index_list LBRACKET INTEGER RBRACKET\n\t\t\t\t\t\t   | ID LBRACKET INTEGER RBRACKETexpr_list : LBRACKET expr_inside_list RBRACKETexpr_inside_list : expr_inside_list COMMA expr_type\n\t\t\t\t\t\t\t| expr_inside_list COMMA expr_bool\n\t\t\t\t\t\t\t| expr_type\n\t\t\t\t\t\t\t| expr_bool\n\t\t\t\t\t\t\t| emptyexpr_type : expr_num\n\t\t\t\t\t | expr_stringexpr_bool : TRUEexpr_bool : FALSEexpr_num : FLOAT\n\t\t\t\t\t| INTEGERexpr_string : STRINGempty :'
    
_lr_action_items = {'DEF':([0,1,2,3,4,6,7,8,9,18,19,106,130,131,132,137,138,139,145,146,147,149,150,153,154,155,157,159,160,161,163,164,165,167,168,169,170,171,],[12,12,-2,-3,-4,-8,-9,-10,-11,-1,-5,12,12,12,12,12,12,-27,12,-20,-26,12,-21,-25,12,-13,12,12,12,12,-12,12,-22,-23,12,12,-86,-24,]),'FOR':([0,1,2,3,4,6,7,8,9,18,19,106,130,131,132,137,138,139,145,146,147,149,150,153,154,155,157,159,160,161,163,164,165,167,168,169,170,171,],[14,14,-2,-3,-4,-8,-9,-10,-11,-1,-5,14,14,14,14,14,14,-27,14,-20,-26,14,-21,-25,14,-13,14,14,14,14,-12,14,-22,-23,14,14,-86,-24,]),'IF':([0,1,2,3,4,6,7,8,9,18,19,106,130,131,132,137,138,139,145,146,147,149,150,153,154,155,157,159,160,161,163,164,165,167,168,169,170,171,],[15,15,-2,-3,-4,-8,-9,-10,-11,-1,-5,15,15,15,15,15,15,-27,15,-20,-26,15,-21,-25,15,-13,15,15,15,15,-12,15,-22,-23,15,15,-86,-24,]),'WHILE':([0,1,2,3,4,6,7,8,9,18,19,106,130,131,132,137,138,139,145,146,147,149,150,153,154,155,157,159,160,161,163,164,165,167,168,169,170,171,],[16,16,-2,-3,-4,-8,-9,-10,-11,-1,-5,16,16,16,16,16,16,-27,16,-20,-26,16,-21,-25,16,-13,16,16,16,16,-12,16,-22,-23,16,16,-86,-24,]),'ID':([0,1,2,3,4,6,7,8,9,12,18,19,21,22,23,24,25,26,27,37,38,40,44,56,63,73,74,75,76,77,78,84,85,86,87,88,89,96,100,101,106,122,130,131,132,137,138,139,145,146,147,149,150,153,154,155,157,158,159,160,161,163,164,165,167,168,169,170,171,],[13,13,-2,-3,-4,-8,-9,-10,-11,20,-1,-5,29,47,54,58,68,68,70,29,29,68,68,29,29,29,29,29,29,68,68,68,68,68,68,68,68,123,29,129,13,68,13,13,13,13,13,-27,13,-20,-26,13,-21,-25,13,-13,13,68,13,13,13,-12,13,-22,-23,13,13,-86,-24,]),'$end':([0,1,2,3,4,6,7,8,9,18,19,139,146,147,150,153,155,163,165,167,170,171,],[-86,0,-2,-3,-4,-8,-9,-10,-11,-1,-5,-27,-20,-26,-21,-25,-13,-12,-22,-23,-86,-24,]),'RBRACE':([2,3,4,6,7,8,9,18,19,106,130,131,132,137,138,139,145,146,147,149,150,153,154,155,157,159,160,161,163,164,165,167,168,169,170,171,],[-2,-3,-4,-8,-9,-10,-11,-1,-5,-86,-86,-86,139,146,147,-27,-86,-20,-26,155,-21,-25,-86,-13,-86,163,-86,165,-12,167,-22,-23,-86,170,-86,-24,]),'SEMI':([5,10,11,17,29,30,31,32,33,34,35,36,39,41,42,43,45,46,61,62,65,66,67,68,83,94,95,97,98,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,],[19,-6,-7,-68,-65,-28,-29,-30,-31,-32,-79,-80,-48,-83,-84,-85,-81,-82,-66,-67,-56,-57,-58,-65,-64,-55,-33,-70,-72,-69,-71,-60,-61,-62,-63,-46,-47,-59,-45,-49,-50,-51,-52,-53,-54,-73,]),'ASSIGN':([13,],[21,]),'LPAREN':([13,14,15,16,20,21,22,24,25,26,29,37,38,40,44,47,56,58,63,68,73,74,75,76,77,78,84,85,86,87,88,89,96,100,122,123,152,158,],[22,24,25,26,28,37,37,56,63,63,22,37,56,56,56,22,56,22,63,22,56,56,56,56,63,63,56,56,56,56,56,56,37,56,56,22,158,63,]),'LBRACKET':([13,17,21,29,47,58,68,97,98,104,105,123,],[23,27,40,23,23,23,23,-70,-72,-69,-71,23,]),'PLUS':([17,29,30,31,34,35,36,41,42,43,47,49,50,52,58,59,60,61,62,65,66,67,68,79,81,82,83,91,95,97,98,99,104,105,107,108,109,110,113,123,124,125,126,133,135,],[-68,-65,-67,73,-66,-79,-80,-83,-84,-85,-65,-66,-67,73,-65,-79,73,-66,-67,-66,-67,73,-65,73,-66,-67,73,-67,-33,-70,-72,73,-69,-71,73,73,73,73,-59,-65,-66,-67,73,-67,141,]),'MINUS':([17,21,22,24,25,26,29,30,31,34,35,36,37,38,40,41,42,43,44,47,49,50,52,56,58,59,60,61,62,63,65,66,67,68,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,91,95,96,97,98,99,100,104,105,107,108,109,110,113,122,123,124,125,126,133,135,158,],[-68,38,38,38,38,38,-65,-67,74,-66,-79,-80,38,38,38,-83,-84,-85,38,-65,-66,-67,74,38,-65,-79,74,-66,-67,38,-66,-67,74,-65,38,38,38,38,38,38,74,-66,-67,74,38,38,38,38,38,38,-67,-33,38,-70,-72,74,38,-69,-71,74,74,74,74,-59,38,-65,-66,-67,74,-67,143,38,]),'MULTIPLY':([17,29,30,31,34,35,36,41,42,43,47,49,50,52,58,59,60,61,62,65,66,67,68,79,81,82,83,91,95,97,98,99,104,105,107,108,109,110,113,123,124,125,126,133,],[-68,-65,-67,75,-66,-79,-80,-83,-84,-85,-65,-66,-67,75,-65,-79,75,-66,-67,-66,-67,75,-65,75,-66,-67,75,-67,-33,-70,-72,75,-69,-71,75,75,75,75,-59,-65,-66,-67,75,-67,]),'DIVIDE':([17,29,30,31,34,35,36,41,42,43,47,49,50,52,58,59,60,61,62,65,66,67,68,79,81,82,83,91,95,97,98,99,104,105,107,108,109,110,113,123,124,125,126,133,],[-68,-65,-67,76,-66,-79,-80,-83,-84,-85,-65,-66,-67,76,-65,-79,76,-66,-67,-66,-67,76,-65,76,-66,-67,76,-67,-33,-70,-72,76,-69,-71,76,76,76,76,-59,-65,-66,-67,76,-67,]),'EQ':([17,29,30,31,34,35,36,39,41,42,43,45,46,47,49,50,52,61,62,65,66,67,68,79,81,82,83,91,92,94,95,97,98,104,105,107,108,109,110,113,115,116,117,118,119,120,123,124,125,126,133,134,],[-68,-65,-57,-58,-56,-79,-80,84,-83,-84,-85,-81,-82,-65,-56,-57,-58,-66,-67,-56,-57,-58,-65,-58,-56,-57,-64,-57,84,84,-33,-70,-72,-69,-71,-60,-61,-62,-63,-59,84,84,84,84,84,84,-65,-56,-57,-58,-57,84,]),'LT':([17,29,30,31,34,35,36,39,41,42,43,45,46,47,49,50,52,61,62,65,66,67,68,79,81,82,83,91,92,94,95,97,98,104,105,107,108,109,110,113,115,116,117,118,119,120,123,124,125,126,133,134,],[-68,-65,-57,-58,-56,-79,-80,85,-83,-84,-85,-81,-82,-65,-56,-57,-58,-66,-67,-56,-57,-58,-65,-58,-56,-57,-64,-57,85,85,-33,-70,-72,-69,-71,-60,-61,-62,-63,-59,85,85,85,85,85,85,-65,-56,-57,-58,-57,85,]),'LET':([17,29,30,31,34,35,36,39,41,42,43,45,46,47,49,50,52,61,62,65,66,67,68,79,81,82,83,91,92,94,95,97,98,104,105,107,108,109,110,113,115,116,117,118,119,120,123,124,125,126,133,134,],[-68,-65,-57,-58,-56,-79,-80,86,-83,-84,-85,-81,-82,-65,-56,-57,-58,-66,-67,-56,-57,-58,-65,-58,-56,-57,-64,-57,86,86,-33,-70,-72,-69,-71,-60,-61,-62,-63,-59,86,86,86,86,86,86,-65,-56,-57,-58,-57,86,]),'GT':([17,29,30,31,34,35,36,39,41,42,43,45,46,47,49,50,52,61,62,65,66,67,68,79,81,82,83,91,92,94,95,97,98,104,105,107,108,109,110,113,115,116,117,118,119,120,123,124,125,126,133,134,],[-68,-65,-57,-58,-56,-79,-80,87,-83,-84,-85,-81,-82,-65,-56,-57,-58,-66,-67,-56,-57,-58,-65,-58,-56,-57,-64,-57,87,87,-33,-70,-72,-69,-71,-60,-61,-62,-63,-59,87,87,87,87,87,87,-65,-56,-57,-58,-57,87,]),'GET':([17,29,30,31,34,35,36,39,41,42,43,45,46,47,49,50,52,61,62,65,66,67,68,79,81,82,83,91,92,94,95,97,98,104,105,107,108,109,110,113,115,116,117,118,119,120,123,124,125,126,133,134,],[-68,-65,-57,-58,-56,-79,-80,88,-83,-84,-85,-81,-82,-65,-56,-57,-58,-66,-67,-56,-57,-58,-65,-58,-56,-57,-64,-57,88,88,-33,-70,-72,-69,-71,-60,-61,-62,-63,-59,88,88,88,88,88,88,-65,-56,-57,-58,-57,88,]),'DIFF':([17,29,30,31,34,35,36,39,41,42,43,45,46,47,49,50,52,61,62,65,66,67,68,79,81,82,83,91,92,94,95,97,98,104,105,107,108,109,110,113,115,116,117,118,119,120,123,124,125,126,133,134,],[-68,-65,-57,-58,-56,-79,-80,89,-83,-84,-85,-81,-82,-65,-56,-57,-58,-66,-67,-56,-57,-58,-65,-58,-56,-57,-64,-57,89,89,-33,-70,-72,-69,-71,-60,-61,-62,-63,-59,89,89,89,89,89,89,-65,-56,-57,-58,-57,89,]),'AND':([17,29,30,31,32,34,35,36,39,41,42,43,45,46,47,49,50,52,53,61,62,64,65,66,67,68,69,79,80,81,82,83,94,95,97,98,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,162,],[-68,-65,-57,-58,77,-56,-79,-80,-48,-83,-84,-85,-81,-82,-65,-56,-57,-58,77,-66,-67,77,-56,-57,-58,-65,77,-58,77,-56,-57,-64,-55,-33,-70,-72,-69,-71,-60,-61,-62,-63,77,77,-59,-45,-49,-50,-51,-52,-53,-54,-65,-56,-57,-58,77,77,]),'OR':([17,29,30,31,32,34,35,36,39,41,42,43,45,46,47,49,50,52,53,61,62,64,65,66,67,68,69,79,80,81,82,83,94,95,97,98,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,162,],[-68,-65,-57,-58,78,-56,-79,-80,-48,-83,-84,-85,-81,-82,-65,-56,-57,-58,78,-66,-67,78,-56,-57,-58,-65,78,-58,78,-56,-57,-64,-55,-33,-70,-72,-69,-71,-60,-61,-62,-63,78,78,-59,-45,-49,-50,-51,-52,-53,-54,-65,-56,-57,-58,78,78,]),'RPAREN':([17,22,28,29,35,36,39,41,42,43,45,46,47,48,49,50,51,52,53,61,62,64,65,66,67,68,69,79,80,81,82,83,94,95,97,98,99,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,129,140,141,142,143,144,162,],[-68,-86,72,-65,-79,-80,-48,-83,-84,-85,-81,-82,-37,95,-36,-39,-40,-43,-44,-66,-67,102,-56,-57,-58,-65,103,113,114,-56,-57,-64,-55,-33,-70,-72,113,-69,-71,-60,-61,-62,-63,-46,-47,-59,-45,-49,-50,-51,-52,-53,-54,-34,-35,-38,-41,-42,136,148,-16,-17,-18,-19,166,]),'COMMA':([17,22,29,35,36,39,40,41,42,43,45,46,47,48,49,50,51,52,53,57,58,59,60,61,62,65,66,67,68,83,90,91,92,93,94,95,97,98,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,128,133,134,],[-68,-86,-65,-79,-80,-48,-86,-83,-84,-85,-81,-82,-37,96,-36,-39,-40,-43,-44,100,-65,-14,-15,-66,-67,-56,-57,-58,-65,-64,122,-57,-77,-78,-55,-33,-70,-72,-69,-71,-60,-61,-62,-63,-46,-47,-59,-45,-49,-50,-51,-52,-53,-54,-34,-35,-38,-41,-42,135,-57,-75,]),'RBRACKET':([17,29,35,36,40,41,42,43,45,46,54,55,61,62,65,66,67,68,70,71,83,90,91,92,93,94,95,97,98,104,105,107,108,109,110,113,115,116,117,118,119,120,133,134,],[-68,-65,-79,-80,-86,-83,-84,-85,-81,-82,97,98,-66,-67,-56,-57,-58,-65,104,105,-64,121,-57,-77,-78,-55,-33,-70,-72,-69,-71,-60,-61,-62,-63,-59,-49,-50,-51,-52,-53,-54,-57,-75,]),'FLOAT':([21,22,24,25,26,37,38,40,44,56,63,73,74,75,76,77,78,84,85,86,87,88,89,96,100,122,158,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'INTEGER':([21,22,23,24,25,26,27,37,38,40,44,56,63,73,74,75,76,77,78,84,85,86,87,88,89,96,100,122,158,],[42,42,55,42,42,42,71,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'STRING':([21,22,24,25,26,37,38,40,44,56,63,73,74,75,76,77,78,84,85,86,87,88,89,96,100,122,158,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'NOT':([21,22,25,26,37,40,44,63,77,78,84,85,86,87,88,89,96,122,158,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'TRUE':([21,22,25,26,37,40,44,63,77,78,84,85,86,87,88,89,96,122,158,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'FALSE':([21,22,25,26,37,40,44,63,77,78,84,85,86,87,88,89,96,122,158,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'IN':([58,],[101,]),'LBRACE':([72,102,103,136,148,151,156,166,],[106,130,131,145,154,157,160,168,]),'PLUSPLUS':([135,],[142,]),'MINUSMINUS':([135,],[144,]),'ELSE':([146,150,153,170,171,],[151,156,-25,-86,-24,]),'ELIF':([146,170,],[152,152,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,106,130,131,145,154,157,160,168,],[1,132,137,138,149,159,161,164,169,]),'sent':([0,1,106,130,131,132,137,138,145,149,154,157,159,160,161,164,168,169,],[2,18,2,2,2,18,18,18,2,18,2,2,18,2,18,18,2,18,]),'empty':([0,22,40,106,130,131,145,146,154,157,160,168,170,],[3,51,93,3,3,3,3,153,3,3,3,3,153,]),'statement':([0,1,106,130,131,132,137,138,145,149,154,157,159,160,161,164,168,169,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'instruction':([0,1,106,130,131,132,137,138,145,149,154,157,159,160,161,164,168,169,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'function_definition':([0,1,106,130,131,132,137,138,145,149,154,157,159,160,161,164,168,169,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'for_statement':([0,1,106,130,131,132,137,138,145,149,154,157,159,160,161,164,168,169,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'if_statement':([0,1,106,130,131,132,137,138,145,149,154,157,159,160,161,164,168,169,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'while_statement':([0,1,106,130,131,132,137,138,145,149,154,157,159,160,161,164,168,169,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'assign':([0,1,106,130,131,132,137,138,145,149,154,157,159,160,161,164,168,169,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'function':([0,1,21,22,24,25,26,37,38,40,44,56,63,73,74,75,76,77,78,84,85,86,87,88,89,96,100,106,122,130,131,132,137,138,145,149,154,157,158,159,160,161,164,168,169,],[11,11,34,49,61,65,65,81,61,65,65,61,81,61,61,61,61,65,65,65,65,65,65,65,65,124,61,11,65,11,11,11,11,11,11,11,11,11,65,11,11,11,11,11,11,]),'sent_index_list':([0,1,21,22,24,25,26,37,38,40,44,56,63,73,74,75,76,77,78,84,85,86,87,88,89,96,100,106,122,130,131,132,137,138,145,149,154,157,158,159,160,161,164,168,169,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'expr_type':([21,22,24,25,26,37,38,40,44,56,63,73,74,75,76,77,78,84,85,86,87,88,89,96,100,122,158,],[30,50,62,66,66,82,62,91,66,62,82,62,62,62,62,66,66,66,66,66,66,66,66,125,62,133,66,]),'expr_arithm':([21,22,24,25,26,37,38,40,44,56,63,73,74,75,76,77,78,84,85,86,87,88,89,96,100,122,158,],[31,52,60,67,67,79,83,67,67,99,79,107,108,109,110,67,67,67,67,67,67,67,67,126,60,67,67,]),'logic_list':([21,22,25,26,37,63,77,78,96,158,],[32,53,64,69,80,80,111,112,127,162,]),'expr_list':([21,],[33,]),'expr_num':([21,22,24,25,26,37,38,40,44,56,63,73,74,75,76,77,78,84,85,86,87,88,89,96,100,122,158,],[35,35,59,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,59,35,35,]),'expr_string':([21,22,24,25,26,37,38,40,44,56,63,73,74,75,76,77,78,84,85,86,87,88,89,96,100,122,158,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'expr_bool':([21,22,25,26,37,40,44,63,77,78,84,85,86,87,88,89,96,122,158,],[39,39,39,39,39,92,94,39,39,39,115,116,117,118,119,120,39,134,39,]),'list':([22,],[48,]),'for_valid_expr':([24,100,],[57,128,]),'expr_inside_list':([40,],[90,]),'for_valid_iter':([135,],[140,]),'elif_sent':([146,170,],[150,171,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> code sent','code',2,'p_code','nbz_parser.py',41),
  ('code -> sent','code',1,'p_code','nbz_parser.py',42),
  ('code -> empty','code',1,'p_code','nbz_parser.py',43),
  ('sent -> statement','sent',1,'p_sent','nbz_parser.py',54),
  ('sent -> instruction SEMI','sent',2,'p_sent','nbz_parser.py',55),
  ('instruction -> assign','instruction',1,'p_instruction','nbz_parser.py',59),
  ('instruction -> function','instruction',1,'p_instruction','nbz_parser.py',60),
  ('statement -> function_definition','statement',1,'p_statement','nbz_parser.py',64),
  ('statement -> for_statement','statement',1,'p_statement','nbz_parser.py',65),
  ('statement -> if_statement','statement',1,'p_statement','nbz_parser.py',66),
  ('statement -> while_statement','statement',1,'p_statement','nbz_parser.py',67),
  ('for_statement -> FOR LPAREN for_valid_expr COMMA for_valid_expr COMMA for_valid_iter RPAREN LBRACE code RBRACE','for_statement',11,'p_sent_for_flow_int','nbz_parser.py',71),
  ('for_statement -> FOR LPAREN ID IN ID RPAREN LBRACE code RBRACE','for_statement',9,'p_sent_for_flow_int','nbz_parser.py',72),
  ('for_valid_expr -> expr_num','for_valid_expr',1,'p_for_valid_expressions_num','nbz_parser.py',85),
  ('for_valid_expr -> expr_arithm','for_valid_expr',1,'p_for_valid_expressions_num','nbz_parser.py',86),
  ('for_valid_iter -> PLUS','for_valid_iter',1,'p_for_valid_iterators','nbz_parser.py',90),
  ('for_valid_iter -> PLUSPLUS','for_valid_iter',1,'p_for_valid_iterators','nbz_parser.py',91),
  ('for_valid_iter -> MINUS','for_valid_iter',1,'p_for_valid_iterators','nbz_parser.py',92),
  ('for_valid_iter -> MINUSMINUS','for_valid_iter',1,'p_for_valid_iterators','nbz_parser.py',93),
  ('if_statement -> IF LPAREN logic_list RPAREN LBRACE code RBRACE','if_statement',7,'p_sent_if_flow','nbz_parser.py',97),
  ('if_statement -> IF LPAREN logic_list RPAREN LBRACE code RBRACE elif_sent','if_statement',8,'p_sent_if_flow','nbz_parser.py',98),
  ('if_statement -> IF LPAREN logic_list RPAREN LBRACE code RBRACE ELSE LBRACE code RBRACE','if_statement',11,'p_sent_if_flow','nbz_parser.py',99),
  ('if_statement -> IF LPAREN logic_list RPAREN LBRACE code RBRACE elif_sent ELSE LBRACE code RBRACE','if_statement',12,'p_sent_if_flow','nbz_parser.py',100),
  ('elif_sent -> ELIF LPAREN logic_list RPAREN LBRACE code RBRACE elif_sent','elif_sent',8,'p_sent_elif_flow','nbz_parser.py',130),
  ('elif_sent -> empty','elif_sent',1,'p_sent_elif_flow','nbz_parser.py',131),
  ('while_statement -> WHILE LPAREN logic_list RPAREN LBRACE code RBRACE','while_statement',7,'p_sent_while_flow','nbz_parser.py',141),
  ('function_definition -> DEF ID LPAREN RPAREN LBRACE code RBRACE','function_definition',7,'p_function_definition','nbz_parser.py',148),
  ('assign -> ID ASSIGN expr_type','assign',3,'p_assign_expr','nbz_parser.py',156),
  ('assign -> ID ASSIGN expr_arithm','assign',3,'p_assign_expr','nbz_parser.py',157),
  ('assign -> ID ASSIGN logic_list','assign',3,'p_assign_expr','nbz_parser.py',158),
  ('assign -> ID ASSIGN expr_list','assign',3,'p_assign_expr','nbz_parser.py',159),
  ('assign -> ID ASSIGN function','assign',3,'p_assign_func','nbz_parser.py',165),
  ('function -> ID LPAREN list RPAREN','function',4,'p_expr_funcs','nbz_parser.py',172),
  ('list -> list COMMA ID','list',3,'p_list_var','nbz_parser.py',182),
  ('list -> list COMMA function','list',3,'p_list_var','nbz_parser.py',183),
  ('list -> function','list',1,'p_list_var','nbz_parser.py',184),
  ('list -> ID','list',1,'p_list_var','nbz_parser.py',185),
  ('list -> list COMMA expr_type','list',3,'p_list_value','nbz_parser.py',224),
  ('list -> expr_type','list',1,'p_list_value','nbz_parser.py',225),
  ('list -> empty','list',1,'p_list_value','nbz_parser.py',226),
  ('list -> list COMMA expr_arithm','list',3,'p_list_expression','nbz_parser.py',237),
  ('list -> list COMMA logic_list','list',3,'p_list_expression','nbz_parser.py',238),
  ('list -> expr_arithm','list',1,'p_list_expression','nbz_parser.py',239),
  ('list -> logic_list','list',1,'p_list_expression','nbz_parser.py',240),
  ('logic_list -> LPAREN logic_list RPAREN','logic_list',3,'p_group_logic_list','nbz_parser.py',248),
  ('logic_list -> logic_list AND logic_list','logic_list',3,'p_logic_list','nbz_parser.py',252),
  ('logic_list -> logic_list OR logic_list','logic_list',3,'p_logic_list','nbz_parser.py',253),
  ('logic_list -> expr_bool','logic_list',1,'p_logic_list','nbz_parser.py',254),
  ('expr_bool -> expr_bool EQ expr_bool','expr_bool',3,'p_expr_logical','nbz_parser.py',264),
  ('expr_bool -> expr_bool LT expr_bool','expr_bool',3,'p_expr_logical','nbz_parser.py',265),
  ('expr_bool -> expr_bool LET expr_bool','expr_bool',3,'p_expr_logical','nbz_parser.py',266),
  ('expr_bool -> expr_bool GT expr_bool','expr_bool',3,'p_expr_logical','nbz_parser.py',267),
  ('expr_bool -> expr_bool GET expr_bool','expr_bool',3,'p_expr_logical','nbz_parser.py',268),
  ('expr_bool -> expr_bool DIFF expr_bool','expr_bool',3,'p_expr_logical','nbz_parser.py',269),
  ('expr_bool -> NOT expr_bool','expr_bool',2,'p_expr_logical','nbz_parser.py',270),
  ('expr_bool -> function','expr_bool',1,'p_logic_valid_var','nbz_parser.py',287),
  ('expr_bool -> expr_type','expr_bool',1,'p_logic_valid_type','nbz_parser.py',297),
  ('expr_bool -> expr_arithm','expr_bool',1,'p_logic_valid_type','nbz_parser.py',298),
  ('expr_arithm -> LPAREN expr_arithm RPAREN','expr_arithm',3,'p_group_expr_arithmethic','nbz_parser.py',302),
  ('expr_arithm -> expr_arithm PLUS expr_arithm','expr_arithm',3,'p_expr_aritmethic','nbz_parser.py',306),
  ('expr_arithm -> expr_arithm MINUS expr_arithm','expr_arithm',3,'p_expr_aritmethic','nbz_parser.py',307),
  ('expr_arithm -> expr_arithm MULTIPLY expr_arithm','expr_arithm',3,'p_expr_aritmethic','nbz_parser.py',308),
  ('expr_arithm -> expr_arithm DIVIDE expr_arithm','expr_arithm',3,'p_expr_aritmethic','nbz_parser.py',309),
  ('expr_arithm -> MINUS expr_arithm','expr_arithm',2,'p_expr_aritmethic','nbz_parser.py',310),
  ('expr_arithm -> ID','expr_arithm',1,'p_arithm_valid_var','nbz_parser.py',323),
  ('expr_arithm -> function','expr_arithm',1,'p_arithm_valid_var','nbz_parser.py',324),
  ('expr_arithm -> expr_type','expr_arithm',1,'p_arithm_valid_num','nbz_parser.py',343),
  ('function -> sent_index_list','function',1,'p_sent_index_list','nbz_parser.py',347),
  ('sent_index_list -> sent_index_list LBRACKET ID RBRACKET','sent_index_list',4,'p_index_list_var','nbz_parser.py',351),
  ('sent_index_list -> ID LBRACKET ID RBRACKET','sent_index_list',4,'p_index_list_var','nbz_parser.py',352),
  ('sent_index_list -> sent_index_list LBRACKET INTEGER RBRACKET','sent_index_list',4,'p_index_list_value','nbz_parser.py',378),
  ('sent_index_list -> ID LBRACKET INTEGER RBRACKET','sent_index_list',4,'p_index_list_value','nbz_parser.py',379),
  ('expr_list -> LBRACKET expr_inside_list RBRACKET','expr_list',3,'p_expr_list','nbz_parser.py',393),
  ('expr_inside_list -> expr_inside_list COMMA expr_type','expr_inside_list',3,'p_list_expr_inside_list','nbz_parser.py',397),
  ('expr_inside_list -> expr_inside_list COMMA expr_bool','expr_inside_list',3,'p_list_expr_inside_list','nbz_parser.py',398),
  ('expr_inside_list -> expr_type','expr_inside_list',1,'p_list_expr_inside_list','nbz_parser.py',399),
  ('expr_inside_list -> expr_bool','expr_inside_list',1,'p_list_expr_inside_list','nbz_parser.py',400),
  ('expr_inside_list -> empty','expr_inside_list',1,'p_list_expr_inside_list','nbz_parser.py',401),
  ('expr_type -> expr_num','expr_type',1,'p_expr_type','nbz_parser.py',412),
  ('expr_type -> expr_string','expr_type',1,'p_expr_type','nbz_parser.py',413),
  ('expr_bool -> TRUE','expr_bool',1,'p_expr_bool_true','nbz_parser.py',417),
  ('expr_bool -> FALSE','expr_bool',1,'p_expr_bool_false','nbz_parser.py',421),
  ('expr_num -> FLOAT','expr_num',1,'p_expr_number','nbz_parser.py',425),
  ('expr_num -> INTEGER','expr_num',1,'p_expr_number','nbz_parser.py',426),
  ('expr_string -> STRING','expr_string',1,'p_expr_string','nbz_parser.py',430),
  ('empty -> <empty>','empty',0,'p_empty','nbz_parser.py',435),
]
