/**
*   Student's Name    : Nguyen Anh Khoa
*   Student's ID      : 2211612
**/
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
last_token = None
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        self.last_token = super().emit()
        return super().emit();
        
}

options{
	language=Python3;
}

program  : decl_list EOF ;
/* ****************PARSER*****************/ 
decl_list
    : top_level_decl eos decl_list
    | top_level_decl eos
    ;
top_level_decl
    : funcdecl 
    | method_decl 
    | decl
    ;
decl
    : vardecl 
    | constdecl 
    | type_decl
    ;
stmt_list
    : stmt eos stmt_list
    | stmt eos
    ;
stmt
    : vardecl
    | constdecl
    | if_stmt
    | for_stmt
    | assignment
    | break_stmt
    | continue_stmt
    | call_stmt
    | return_stmt
    ;
lhs
    : lhs_prime (ACCESS ID| index)
    | ID
    ;
lhs_prime
    : lhs_ele
    | lhs_prime (ACCESS ID| index)
    ;
lhs_ele
    : ID
    | func_call
    | method_call
    ;
return_stmt
    : RETURN (expr| )
    ;
call_stmt
    : func_call
    | method_call
    ;
func_call
    : ID expr_params 
    ;
continue_stmt
    : CONTINUE
    ;
break_stmt
    : BREAK 
    ;
if_stmt
    : IF L_PAREN expr R_PAREN block  (ELSE (if_stmt | block) | )
    ;
for_stmt
    : FOR for_clause block
    ;
for_clause
    : expr
    | for_ICU_clause
    | for_range_clause
    ;
init_stmt
    : assignment
    | vardecl
    ;
cond_stmt
    : expr
    ;
update_stmt
    : assignment
    ;
for_ICU_clause
    : init_stmt eos cond_stmt eos update_stmt
    ;
for_range_clause
    : (for_idx COMMA for_val) DECLARE_ASSIGN RANGE expr
    ;
for_idx
    : ID
    ;
for_val
    : ID
    ;
for_array
    : expr
    ;
assignment
    : lhs assign_op expr
    ;
assign_op
    : PLUS_ASSIGN
    | MINUS_ASSIGN
    | MULT_ASSIGN
    | DIV_ASSIGN
    | MOD_ASSIGN
    | DECLARE_ASSIGN
    | ASSIGN
    ;
block
    : L_CURLY stmt_list R_CURLY
    ;
funcdecl
    : FUNC ID func_params (return_type| ) block
    ;
func_params
    : L_PAREN (func_params_list| ) R_PAREN
    ;
func_params_list
    : func_param COMMA func_params_list
    | func_param
    ;
func_param
    : id_list type_
    ;
return_type
    : type_
    ;
expr_params
    : L_PAREN (expr_list| ) R_PAREN
    ;
constdecl
    : CONST const_spec
    ;
const_spec
    : ID ASSIGN expr
    ;
vardecl
    : VAR var_spec
    ;
var_spec
    : ID (type_ (ASSIGN expr | ) | ASSIGN expr)
    ;
id_list
    : ID COMMA id_list | ID
    ;
expr_list
    : expr COMMA expr_list 
    | expr
    ;
type_
    : single_type
    | type_lit
    | ID
    ;
type_lit
    : array_type
    | struct_type
    | interface_type
    | slice_type
    ;
complex_type
    : struct_type
    | type_name
    ;
list_type
    : array_type
    ;
type_name
    : ID
    ;
complex_lit
    : complex_type complex_val
    | list_type list_val
    ;
list_val
    : L_CURLY (element_list| ) R_CURLY
    ;
complex_val
    : L_CURLY (key_element_list| ) R_CURLY
    ;
key_element_list
    : keyed_element COMMA key_element_list 
    | keyed_element
    ;
element_list
    : element COMMA element_list
    | element
    ;
keyed_element
    : field_name COLON expr
    ;
field_name
    : ID
    ;
element
    : primitive_lit
    | complex_type complex_val
    | ID
    | list_val
    ;
type_decl
    : TYPE type_spec;
type_spec
    : ID (struct_type| interface_type)
    ;
interface_type
    : INTERFACE L_CURLY method_list R_CURLY
    ;
method_decl
    : FUNC receiver method_spec
    ;
method_spec
    : ID func_params (return_type| ) block
    ;
receiver
    : L_PAREN ID method_type R_PAREN
    ;
method_type
    : ID
    | struct_type
    | interface_type
    ;
method_list
    : method eos method_list
    | method eos
    ;
method
    : ID method_params (return_type | )
    ;
method_params
    : L_PAREN (method_param_prime| )R_PAREN
    ;
method_param_prime
    : method_param COMMA method_param_prime
    | method_param
    ;
method_param
    : id_list type_
    ;
method_call
    : expr ACCESS ID expr_params
    ;
struct_type
    : STRUCT L_CURLY  field_prime R_CURLY;
field_prime
    : ID type_ eos field_prime
    | ID type_ eos 
    ;
slice_type
    : L_BRACKET R_BRACKET type_
    ;
array_type
    : array_decl type_
    ;
array_decl
    : array_len array_decl
    | array_len
    ;
array_len
    : L_BRACKET (integer| ID) R_BRACKET
    ;
single_type
    : INT_TYPE
    | FLOAT_TYPE
    | STRING_TYPE
    | BOOL_TYPE
    ;
literal
    : primitive_lit
    | complex_lit
    ;
primitive_lit
    : integer
    | STRING_LIT
    | NIL
    | FLOAT_LIT
    | TRUE | FALSE
    ;
integer
    : DECIMAL_LIT
    | BINARY_LIT
    | OCTAL_LIT
    | HEX_LIT
    ;
operand
    : ID
    | L_PAREN expr R_PAREN
    | literal
    ;
primary_expr
    : operand
    | primary_expr (ACCESS ID | index| ACCESS func_call)
    | ID expr_params
    ; 
index
    : L_BRACKET expr R_BRACKET
    ;
unary_op
    : LOGICAL_NOT
    | MINUS;
mul_op
    : MULT
    | DIV
    | MOD
    ;
add_op
    : PLUS
    | MINUS
    ;
compare_op
    : EQUALS
    | NOT_EQUALS
    | LESS
    | LESS_EQUALS
    | GREATER
    | GREATER_EQUALS
    ;
expr
    : primary_expr
    |<assoc=right> unary_op expr
    | expr mul_op expr
    | expr add_op expr
    | expr compare_op expr
    | expr LOGICAL_AND expr
    | expr LOGICAL_OR expr
    ;
eos
    : SEMI
    ;

/* ****************lEXER*****************/ 
// Keywords
FUNC: 'func';
IF: 'if';
BREAK: 'break' ;
ELSE: 'else';
FOR: 'for';
RETURN: 'return' ;
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue' ;
RANGE: 'range';
NIL: 'nil' ;
TRUE: 'true' ;
FALSE: 'false' ;
// Type Keyword
INT_TYPE: 'int';
STRING_TYPE: 'string';
FLOAT_TYPE: 'float';
BOOL_TYPE: 'boolean';
// Math Operator
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
// Compare Operator
EQUALS: '==';
NOT_EQUALS: '!=';
LESS: '<';
LESS_EQUALS: '<=';
GREATER: '>';
GREATER_EQUALS: '>=';
// Logical Operator
LOGICAL_AND: '&&';
LOGICAL_OR: '||';
LOGICAL_NOT: '!';
// Assign Operator
COLON: ':';
ASSIGN: '=';
PLUS_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
MULT_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
DECLARE_ASSIGN: ':=';
// Access Operator
ACCESS: '.';

// Separator
L_PAREN: '(';
R_PAREN: ')' ;
L_CURLY: '{';
R_CURLY: '}' ;
L_BRACKET: '[';
R_BRACKET: ']' ;
COMMA: ',' ;
SEMI: ';' ;
// Identifier
ID: LETTER (LETTER | DIGIT)* ;
// Literal 
DECIMAL_LIT: '0' | ([1-9] DIGIT*) ;
BINARY_LIT: '0' [bB] BIN_DIGIT+ ;
OCTAL_LIT: '0' [oO]  OCTAL_DIGIT+ ;
HEX_LIT: '0' [xX] HEX_DIGIT+ ;

FLOAT_LIT: DECIMAL_LIT ('.' FRAC_LIT? EXP_LIT?) ;

STRING_LIT: DQ (~["\\] | ESCAPE)* DQ ;

TERMINATOR:  
[\n]+ 
{
    switch_list = [
        self.ID,
        self.DECIMAL_LIT,self.BINARY_LIT,self.OCTAL_LIT,self.HEX_LIT,
        self.FLOAT_LIT,
        self.STRING_LIT,
        self.TRUE,self.FALSE,
        self.NIL,
        self.INT_TYPE,self.FLOAT_TYPE,self.BOOL_TYPE,self.STRING_TYPE,
        self.RETURN,self.CONTINUE,self.BREAK
        ,self.R_PAREN,self.R_BRACKET,self.R_CURLY]
    if self.last_token and self.last_token.type in switch_list:
        self._type = self.SEMI
        self._text = ';'
    else:
        self.skip()
}
;

//Skip Token
WS : [ \r\t]+ -> skip ; // skip spaces, tabs, carriage return
LINE_COMMENT: (('//' ~[\r\n]*) | ('/*' ~[\r\n]*? '*/')) -> skip;
COMMENT: ('/*' (COMMENT|.)*? '*/') -> skip;
// NL : [\r\n]+ -> skip;
ERROR_CHAR: .;
ILLEGAL_ESCAPE:.;
UNCLOSE_STRING:.;

//Fragments
fragment LETTER: [a-zA-Z] | '_';
fragment DIGIT: [0-9];
fragment BIN_DIGIT: [01];
fragment OCTAL_DIGIT: [0-7];
fragment HEX_DIGIT: [0-9a-fA-F];
fragment EXP_LIT: [eE] [+-]? [0-9]+;
fragment FRAC_LIT: [0-9]+;
fragment SQ: ['];
fragment DQ: ["];
fragment ESCAPE: '\\' [ntr"\\];

