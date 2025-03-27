"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
import StaticError
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"
    def __eq__(self,other):
        if not isinstance(other,MType):
            return False
        return self.partype == other.partype and self.rettype == other.rettype
class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"
    def __eq__(self,other):
        if not isinstance(other,Symbol):
            return False
        return (
            self.name == other.name and
            self.mtype == other.mtype and
            self.value == other.value
        )
class StaticChecker(BaseVisitor,Utils):
        
    
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
                            Symbol("getInt",MType([],IntType())),
                            Symbol("putIntLn",MType([IntType()],VoidType())),
                            Symbol("putInt",MType([IntType()],VoidType())),
                            Symbol("getFloat",MType([],FloatType())),
                            Symbol("putFloat",MType([FloatType()],VoidType())),
                            Symbol("putFloatLn",MType([FloatType()],VoidType())),
                            Symbol("getBool",MType([],BoolType())),
                            Symbol("putBool",MType([BoolType()],VoidType())),
                            Symbol("putBoolLn",MType([BoolType()],VoidType())),
                            Symbol("getString",MType([],StringType())),
                            Symbol("putString",MType([StringType()],VoidType())),
                            Symbol("putStringLn",MType([StringType()],VoidType())),
                            Symbol("putLn",MType([],VoidType()))
                ]      
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        # c is {env,callfrom}
        # env = [[local_env],[param_env],[global_env]]
        # context = parentcontext
        c = {
            'env': [c],
            'context': False,
            'lhs': False,
            'func': None,
            'receiver': None,
            'pass': 0
        }
        # Step 1: first pass check --> Collect struct and interface --> dont touch field
        global_c = reduce(
            lambda acc,cur: self.visit(cur,acc),
            filter(lambda x: isinstance(x,(StructType,InterfaceType)),ast.decl),
            {**c,'pass': 1}
                            )
        # Step 2: second pass check --> check struct field and interface prototype
        global_c = reduce(
            lambda acc,cur: self.visit(cur,acc),
            filter(lambda x: isinstance(x,(StructType,InterfaceType)),ast.decl),
            {**global_c,'pass': 2}
                            )
        #Step 3: third pass check --> check function and struct methods --> dont touch body
        program_c = reduce(
            lambda acc,cur: self.visit(cur,acc),
            filter(lambda x: isinstance(x,(FuncDecl,MethodDecl)),ast.decl),
            {**program_c,'pass': 3}
                            )
        #Step 4: fourth pass check --> check var,const decl and function/method body
        program_c = reduce(
            lambda acc,cur: self.visit(cur,acc),
            filter(lambda x: not isinstance(x,(StructType,InterfaceType)),ast.decl),
            {**program_c,'pass': 4}
                            )
        #Step 5: check main function existence
        res = self.lookup("main",program_c['env'][-1],lambda x: x.name)
        if not res:
            raise Undeclared(Function(), "main")
        if not isinstance(res,Symbol) and not isinstance(res.mtype,MType):
            raise Undeclared(Function(), "main")
        
    def visitBlock(self,ast,c):
        new_c = {
            **c,
            'env': [[]] + c['env'],
            'context': False
        }
        reduce(lambda acc,ele: self.visit(ele,acc), ast.member,new_c)
    
    def visitVarDecl(self, ast, c):
        env = c['env']
        
        res = self.lookup(ast.varName,env[0],lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName)
        
        varType = self.visit(ast.varType,c) if ast.varType else None
        
        if ast.varInit:
            initType = self.visit(ast.varInit, {**c, 'context':True})
            
            if varType is None:
                varType = initType
                
            if not type(varType) is type(initType):
                raise TypeMismatch(ast)
            
        varSymbol = Symbol(ast.varName,varType,None)
        # ensure change doesnt affect the original c
        return {**c,'env': [env[0]+[varSymbol]] + env[1:]}
    
    def visitConstDecl(self,ast,c):
        env = c['env']
        
        res = self.lookup(ast.varName,env[0],lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName)
        
        if ast.iniExpr:
            initType = self.visit(ast.iniExpr,{**c, 'context':True})
            ast.conType = initType
            
        constSymbol = Symbol(ast.varName,ast.varType,None)
        
        return {**c,'env': [env[0] + [constSymbol]] + env[1:]}

    def visitFuncDecl(self,ast, c):
        env = c['env']
        
        if c['pass'] == 3:
            #only return Symbol(name,(partype,rettype)) --> dont touch body
            #check if function has already been declared
            if c['receiver']:
                struct_type = c['receiver'].mtype 
                
                if self.lookup(ast.name,struct_type.methods,lambda x: x.name):
                    raise Redeclared(Method(), ast.name)
                
                par_scope = []
            else:
                res = self.lookup(ast.name,env[0],lambda x: x.name)
                if res:
                    raise Redeclared(Function(), ast.name)
            
            par_scope = []
            
            par_c = reduce(
                lambda acc,cur: self.visit(cur,acc),
                ast.params,
                {**c,'env': [par_scope] + c}
            )
            # incase of method decl
            if c['receiver']:
                struct_type = c['receiver'].mtype 
                
                if self.lookup(ast.name,struct_type.methods,lambda x: x.name):
                    raise Redeclared(Method(), ast.name)
                
                func_symbol = Symbol(ast.name,MType(par_c['env'][0][1:],rettype))
                
                struct_type.methods.append(meth_symbol)
                return c
            else:
                func_symbol = Symbol(ast.name,MType(par_c['env'][0],rettype))
            
            rettype = self.visit(ast.retType,c)
            
            func_symbol = Symbol(ast.name,MType(par_c['env'][0],rettype))
            return 
            
            
        res = self.lookup(ast.name,env[0],lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)
        
        par_scope = [c['receiver']] if c['receiver'] else []
        
        par_c = reduce(lambda acc,cur: self.visit(cur,acc),ast.params,{**c,'env':[par_scope] + c['env']}) # have it own scope

        rettype = self.visit(ast.retType,c)
        
        func_symbol = Symbol(ast.name, MType(par_c['env'][0],rettype))
        if c['receiver']:
            struct_type = c['receiver'].mtype
            
            if self.lookup(ast.name,struct_type.methods,lambda x: x.name):
                raise Redeclared(Method(), ast.name)
            
            meth_symbol = Symbol(ast.name,MType(par_c['env'][0][1:],rettype))
            
            struct_type.methods.append(meth_symbol)
            
        # par_type = [[param_scope][global_scope]]
        body_env = [par_c['env'][0]] + [par_c['env'][1] + [func_symbol]] + par_c['env'][2:]

        self.visit(ast.body,{**c,'env':body_env,'func':func_symbol})
        
        return {**c, 'env': [env[0] + [func_symbol]] + env[1:]}
    
    def visitParamDecl(self,ast,c):
        env = c['env']
        res = self.lookup(ast.parName,env[0],lambda x: x.name) 
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        partype = self.visit(ast.parType,c)
        return {**c,'env': [env[0] + [Symbol(ast.parName,partype,None)]] + env[1:]}
    
    def visitMethodDecl(self,ast,c):
        env = c['env']
        struct_type = self.visit(ast.recType,c)
        if not struct_type:
            raise Undeclared(StaticError.Type(),ast.recType)
        # is struct_type a struct?
        if not isinstance(struct_type,StructType):
            raise TypeMismatch(ast)
        
        struct_methods = struct_type.methods
        # cant do c because only for scope of method
        fun_env = self.visit(ast.fun,{**c,'env': [[]] + c['env'],'receiver': Symbol(ast.receiver,struct_type,None)})
        
        return c
    ## VISIT TYPE ##
    def visitIntType(self,ast,c):
        return IntType()
    def visitFloatType(self,ast,c):
        return FloatType()
    def visitBoolType(self,ast,c):
        return BoolType()
    def visitStringType(self,ast,c):
        return StringType()
    def visitVoidType(self,ast,c):
        return VoidType()

    def visitArrayType(self,ast,c):
        dimens_c = {**c, 'context':True}
        dimens = list(map(lambda x: self.visit(x,dimens_c),ast.dimens))
        
        if not next(filter(lambda x: isinstance(x,IntType),dimens),None):
            raise TypeMismatch(ast)
        
        ele_type = self.visit(ast.eleType,c)
        
        return ArrayType(ast.dimens,ele_type)

    def _checkField(self,fields,c):
        # return a list that is struct_env
        # for checking use reduce then comprehension
        struct_env = []
        for ele in fields:
            if self.lookup(ele,struct_env,lambda x : x[0]):
                raise Redeclared(Field(),ele[0])
            struct_env.append(
                Symbol(ele[0],self.visit(ele[1],c),None)
            )
        return struct_env
    
    def visitStructType(self,ast,c):
        env = c['env']
        
        if c['pass'] == 1:
            # check if struct is redeclared
            if self.lookup(ast.name,env[0],lambda x: x.name):
                raise Redeclared(StaticError.Type(), ast.name)
            # return the whole struct
            return {**c,'env': [env[-1] + [ast]]} # --> global so no 1:
        # find the struct
        res = self.lookup(ast.name,env[0],lambda x: x.name)
        # check fields
        res.elements = self._checkField(res.elements,c)
        
        return c
    
    def visitInterfaceType(self,ast,c):
        env = c['env']
        
        if c['pass'] == 1:
            if self.lookup(ast.name,env[0],lambda x: x.name):
                raise Redeclared(StaticError.Type(), ast.name)
            # return the whole interface
            return {**c,'env': [env[-1] + [ast]]}
        # find the interface
        res = self.lookup(ast.name,env[0],lambda x: x.name)
        #check prototypes
        prototype_c = reduce(
            lambda acc,cur: self.visit(cur,acc),
            ast.methods,
            {**c,'env':[[]] + c['env']}
        )
        
        res.methods = prototype_c['env'][0]
        
        return c
    
    def visitPrototype(self,ast,c):
        #prototype redeclare
        env = c['env']
        
        if self.lookup(ast.name,env[0],lambda x: x.name):
            raise Redeclared(Prototype(), ast.name) 
        
        param_type = list(map(lambda x: self.visit(x,{**c,'env': env[1:]}),ast.params)) # --> list[Type]
        
        rettype = self.visit(ast.retType,c)
        
        prototype = Symbol(ast.name,MType(param_type,rettype))
        
        return {**c, 'env': [env[0] + [prototype]] + env[1:]}
        
    def visitAssign(self,ast,c):
        lhs_type = self.visit(ast.lhs,{**c, 'lhs': True})
        if isinstance(lhs_type,VoidType):
            raise TypeMismatch(ast.lhs)
        
        rhs_type = self.visit(ast.rhs,{**c,'context': True,'lhs': False})
        
        if isinstance(lhs_type,str):
            # it has not been declare yet --> add Symbol to env
            # but rhs cant contain the name --> autoresolve dont need to handle
            id_symbol = Symbol(lhs_type,rhs_type,None) 
            return {**c,'env': [c['env'][0] + [id_symbol]] + c['env'][1:]}
            
        if isinstance(lhs_type,ArrayType):
            # lhs is array type -> rhs arrType same size & rhs ele same type
            if not isinstance(rhs_type,ArrayType):
                raise TypeMismatch(ast)
            
            if isinstance(lhs_type.eleType,IntType) and not (isinstance(rhs_type.eleType,IntType) or isinstance(rhs_type.eleType,FloatType)):
                raise TypeMismatch(ast)
            
            if len(lhs_type.dimens) != len(rhs_type.dimens):
                raise TypeMismatch(ast)
            
            for lhs_dimen, rhs_dimen in zip(lhs_type.dimens,rhs_type.dimens):
                if lhs_dimen != rhs_dimen:
                    raise TypeMismatch(ast)
                
        if isinstance(lhs_type,InterfaceType):
            # rhs can be a struct
            if not isinstance(rhs_type,StructType):
                raise TypeMismatch(ast)
            # struct must have all interface prototype
            for prototype in lhs_type.methods:
                method_res = self.lookup(prototype.name,rhs_type.methods,lambda x: x.name)
                if method_res is None:
                    raise TypeMismatch(ast)
                # prototype,method_res -> Symbol,Symbol
                proto_mtype = prototype.mtype
                meth_mtype = method_res.mtype
                # check if enough parameter    
                if not len(meth_mtype.partype) == len(proto_mtype.partype):
                    raise TypeMismatch(ast)
                # check if parameter is of correct type
                if not all(map(lambda x: type(x[0].mtype) is type(x[1]),zip(meth_mtype.partype,proto_mtype.partype))):
                    raise TypeMismatch(ast) 
                # check return type
                if not type(meth_mtype.rettype) is type(proto_mtype.rettype):
                    raise TypeMismatch(ast)    
                        
        elif isinstance(lhs_type,FloatType) and isinstance(rhs_type,(IntType,FloatType)):
            # case where lhs is float and rhs is not int or float
            return c
        
        elif not type(lhs_type) is type(rhs_type):
            raise TypeMismatch(ast)
        
        return c
    
    def visitIf(self,ast,c):
        cond_c = {**c,'context': True}
        cond_type = self.visit(ast.expr,cond_c)
        if not isinstance(cond_type,BoolType):
            raise TypeMismatch(ast) 
        
        self.visit(ast.thenStmt,c)
        
        if ast.elseStmt:
            self.visit(ast.elseStmt,c) 

        return c
    
    def visitForBasic(self,ast,c):
        cond_c = {**c,'context': True}
        cond_type = self.visit(ast.cond,cond_c)
        if not isinstance(cond_type,BoolType):
            raise TypeMismatch(ast) 
        self.visit(ast.loop,c)  
        
        return c
    
    def visitForStep(self,ast,c):
        if not isinstance(ast.init,(VarDecl,Assign)):
            raise TypeMismatch(ast)

        self.visit(ast.init,c) 
        cond_c = {**c,'context': True}
        
        cond_type = self.visit(ast.cond,cond_c)
        
        if not isinstance(cond_type,BooleanType):
            raise TypeMismatch(ast)
        
        self.visit(ast.upda,c)
        
        self.visit(ast.loop,c) 
        
        return c
    
    def visitForEach(self,ast,c):
        # idx: Id, value: Id, arr: Expr, loop: Block
        arr_c = {
            **c, 
            'context': True
        }
        
        arr_type = self.visit(ast.arr,arr_c) # dimens: List(IntType) eleType: Type
        if not isinstance(arr_type,ArrayType):
            raise TypeMismatch(ast)
        idx_type = Symbol(ast.idx.name,IntType(),None)
        val_type = Symbol(ast.value.name,arr_type.eleType,None)
        loop_c = {
            **c,
            'env': [[idx_type] + [val_type]] + c['env']
        }
        self.visit(ast.loop,loop_c)
        return c
    def visitBreak(self,ast,c):
        return c
    def visitContinue(self,ast,c):
        return c
    
    def visitReturn(self,ast,c):
        # find the stmt parent function/method --> c['func'] :^)
        func_res = c['func']
        if not func_res:
            raise TypeMismatch(ast) 
        
        return_type = self.visit(ast.expr,c) if ast.expr else VoidType()
        
        if not type(func_res.mtype.rettype) is type(return_type):
            raise TypeMismatch(ast)
        
        return c
        
    def visitArrayCell(self,ast,c):
        # get the type of Array
        context_c = {**c,'context':True}
        
        arr_type = self.visit(ast.arr,context_c)
        if not isinstance(arr_type,ArrayType):
            raise TypeMismatch(ast)
        # check index
        for idx in ast.idx:
            self.visit(idx,context_c)
              
        return arr_type.eleType
    
    def visitFieldAccess(self,ast,c):
        context_c = {**c,'context': True}
        
        receiver_type = self.visit(ast.receiver,context_c)
        if not isinstance(receiver_type,StructType):
            raise TypeMismatch
        
        field_res = self.lookup(ast.field,receiver_type.elements,lambda x: x.name) 
        if not field_res:
            raise TypeMismatch(ast) 
        
        return field_res.mtype
    
    def visitFuncCall(self,ast,c):
        #check undeclare function
        env = c['env']
        func_res = next(
            (res for scope in env if (res := self.lookup(ast.funName,scope,lambda x: x.name))),
            None
        )
        if not func_res:
            raise Undeclared(Function(),ast.funName)
        # check if res is a funcdecl
        if not (isinstance(func_res,Symbol) and isinstance(func_res.mtype,MType)):
            raise TypeMismatch(ast)
        func_type = func_res.mtype
        args_c = {**c,'env':c['env'],'context':True}
        args = list(map(lambda x: self.visit(x,args_c),ast.args))
        # check parameter
        if not len(func_type.partype) == len(ast.args):
            raise TypeMismatch(ast)
        if not all(map(lambda x: type(x[1]) is type(x[0].mtype),zip(func_type.partype,args))):
            raise TypeMismatch(ast)
        # return type in call and in expr?
        if not c['context']:
            if not isinstance(func_type.rettype,VoidType):
                raise TypeMismatch(ast)
            return c
        
        if c['context']:
            if isinstance(func_type.rettype,VoidType):
                raise TypeMismatch(ast) 
            return func_type.rettype  
     
    def visitMethCall(self,ast,c):
        context_c = {**c,'context': True}
        
        receiver_type = self.visit(ast.receiver,context_c)
        if not isinstance(receiver_type,StructType):
            raise TypeMismatch
        
        method_res = self.lookup(ast.metName,receiver_type.methods,lambda x: x.name)
        if not method_res:
            raise Undeclared(Method(),ast.metName)
        method_type = method_res.mtype
        
        args = list(map(lambda x: self.visit(x,context_c),ast.args))
        
        if not len(method_type.partype) == len(ast.args):
            raise TypeMismatch(ast)
        
        if not all(map(lambda x: type(x[1]) is type(x[0].mtype),zip(method_type.partype,args))):
            raise TypeMismatch(ast)

        if not c['context']:
            if not isinstance(method_type.rettype,VoidType):
                raise TypeMismatch(ast)
            return c
        
        if c['context']:
            if isinstance(method_type.rettype,VoidType):
                raise TypeMismatch(ast) 
            return method_type.rettype  
    
    ###VISIT LITERAL###
    def visitIntLiteral(self,ast, c):
        return IntType()
    
    def visitFloatLiteral(self,ast, c):
        return FloatType()

    def visitStringLiteral(self,ast,c):
        return StringType()
    
    def visitBooleanLiteral(self,ast,c):
        return BoolType()
    
    def visitArrayLiteral(self,ast,c):
        dimens_c = {**c,'context': True}
        dimens = list(map(lambda x: self.visit(x,dimens_c),ast.dimens)) 
        if not next(filter(lambda x: isinstance(x,IntType),dimens),None):
            raise TypeMismatch(ast)
        # check if value is really eleType?
        ele_type = self.visit(ast.eleType,c)
        
        def ensure_nested(x):
            # base case
            if not isinstance(x,list):
                val = self.visit(x,c)# visit as it can be expr?
                if not type(val) is type(ele_type): # check if val is the same type as eleType
                    raise TypeMismatch(ast)
                return True
            # list case
            return reduce(lambda acc,cur: acc and ensure_nested(cur),x,True) # recursively iterate each val in the list
        ensure_nested(ast.value)
        
        return ArrayType(ast.dimens, ele_type)
    
    def visitStructLiteral(self,ast,c):
        # struct_literal -> name, elements [name, expr]
        env = c['env']
        struct_type = next(
            (res for scope in env if (res := self.lookup(ast.name,scope,lambda x: x.name))),
            None
        ) # --> name: str, elements [Symbol()],methods: [Symbol()]
        if not struct_type :
            raise Undeclared(StaticError.Type(),ast.name)
        field_c = {**c,'context':True}
        for ele in ast.elements:
            field_res = self.lookup(ele[0], struct_type.elements, lambda x: x.name) 
            if not field_res:
                raise Undeclared(Field(),ele[0])
            if not type(self.visit(ele[1],field_c)) is type(field_res.mtype):
                raise TypeMismatch(ast)
        
        return struct_type

    def visitNilLiteral(self,ast,c):
        return VoidType()
        
    def visitId(self,ast,c):
        env = c['env']
        res = next(
            (res for scope in env if (res := self.lookup(ast.name,scope,lambda x: x.name))),
            None
        )
        # 1: undeclared --> return ast.name --> add to env
        # 2: declared --> return type
        if res is None:
            if c['lhs']:
                return ast.name
            raise Undeclared(Identifier(), ast.name)
        if isinstance(res,(StructType,ArrayType,InterfaceType)):
            return res
        return res.mtype
    
    def visitBinaryOp(self,ast,c):
        expr_c = {**c,'context': True}
        left_type = self.visit(ast.left,expr_c)
        right_type = self.visit(ast.right,expr_c) 
        ## ARTIHMETIC OPERATOR
        if ast.op == '+':
            # Both operands are String
            if isinstance(left_type,StringType) and isinstance(right_type,StringType):
                return StringType()
            # Both operands are Int
            if isinstance(left_type,IntType) and isinstance(right_type,IntType):
                return IntType()
            # Both operands are Float
            if isinstance(left_type,FloatType) and isinstance(right_type,FloatType):
                return FloatType() 
            # Either operand is Float and the other is Int
            if (isinstance(left_type,IntType) and isinstance(right_type,FloatType))\
                or (isinstance(left_type,FloatType) and isinstance(right_type,IntType)):
                return FloatType()
            raise TypeMismatch(ast)
        if ast.op in ['-','*','/']:
            # Both operands are Int
            if isinstance(left_type,IntType) and isinstance(right_type,IntType):
                return IntType()
            # Both operands are Float
            if isinstance(left_type,FloatType) and isinstance(right_type,FloatType):
                return FloatType() 
            # Either operand is Float and the other is Int
            if (isinstance(left_type,IntType) and isinstance(right_type,FloatType))\
                or (isinstance(left_type,FloatType) and isinstance(right_type,IntType)):
                return FloatType()
            raise TypeMismatch(ast)
        if ast.op in ['%']:
            # Both operands are Int
            if isinstance(left_type,IntType) and isinstance(right_type,IntType):
                return IntType()
            raise TypeMismatch(ast)
        ## RELATIONAL OPERATOR
        if ast.op in ['==','!=','<','>','<=','>=']:
            if not isinstance(left_type,(IntType,FloatType,StringType)):
                raise TypeMismatch(ast)
            if not type(left_type) is type(right_type):
                raise TypeMismatch(ast)
            return BoolType()
        ## BOOLEAN OPERATOR
        if ast.op in ['&&','||']:
            if not (isinstance(left_type,BoolType) and isinstance(right_type,BoolType)):
                raise TypeMismatch(ast)
            return BoolType()
        
    def visitUnaryOp(self, ast, c):
        body_type = self.visit(ast.body, {**c, 'context': True})
        ops = {
            '-': (IntType,FloatType),
            '!': (BoolType,)
        }
        
        if isinstance(body_type, ops.get(ast.op)):
            return body_type

        raise TypeMismatch(ast)

    
            
        
        
        
