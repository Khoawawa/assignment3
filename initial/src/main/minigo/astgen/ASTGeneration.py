from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    # program  : decl_list EOF
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.decl_list()))
    # decl_list: (top_level_decl eos) decl_list | (top_level_decl eos)
    def visitDecl_list(self,ctx:MiniGoParser.Decl_listContext):
        if ctx.getChildCount() == 2:
            # top_level_decl eos
            return [self.visit(ctx.top_level_decl())]
        # (top_level_decl eos) decl_list
        return [self.visit(ctx.top_level_decl())] + self.visit(ctx.decl_list())
        
    def visitFuncdecl(self,ctx:MiniGoParser.FuncdeclContext):
        # funcdecl: FUNC ID func_params (return_type_| ) block
        return_type = self.visit(ctx.return_type()) if ctx.return_type() else VoidType()
        
        return FuncDecl(ctx.ID().getText(),self.visit(ctx.func_params()),return_type,self.visit(ctx.block()))
    def visitFunc_params(self,ctx:MiniGoParser.Func_paramsContext):
        # L_PAREN (func_params_list| ) R_PAREN
        return self.visit(ctx.func_params_list()) if ctx.func_params_list() else []
    def visitFunc_params_list(self,ctx:MiniGoParser.Func_params_listContext):
        # func_param COMMA func_params_list| func_param	
        if ctx.getChildCount() == 1:
            #func_param
            return self.visit(ctx.func_param())
        # func_param COMMA func_params_list
        return self.visit(ctx.func_param()) + self.visit(ctx.func_params_list())
    def visitFunc_param(self,ctx:MiniGoParser.Func_paramContext):
        # id_list type_
        id_list = self.visit(ctx.id_list())
        param_list = []
        type_ = self.visit(ctx.type_())
        for id in id_list:
            param_list.append(ParamDecl(id,type_))
        return param_list
    def visitId_list(self,ctx:MiniGoParser.Id_listContext):
        # ID COMMA id_list | ID
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.id_list())
    def visitSingle_type(self,ctx:MiniGoParser.Single_typeContext):
        if ctx.INT_TYPE():
            return IntType()
        if ctx.FLOAT_TYPE():
            return FloatType()
        if ctx.STRING_TYPE():
            return StringType()
        if ctx.BOOL_TYPE():
            return BoolType()
    # def visitType_lit(self,ctx:MiniGoParser.Type_lit)
    def visitSlice_type(self,ctx:MiniGoParser.Slice_typeContext):
        return ArrayType([],self.visit(ctx.type_()))
    def visitArray_decl(self,ctx:MiniGoParser.Array_declContext):
        # array_len array_decl | array_len
        if ctx.getChildCount() == 1:
            return [int(ctx.array_len().getText())]
        return self.visit(ctx.arra_decl()) + [int(ctx.array_len().getText())]
    def visitStruct_type(self,ctx:MiniGoParser.Struct_typeContext):
        return self.visit(ctx.field_prime()) if ctx.field_prime() else []
    # def visitField_prime(self,ctx:MiniGoParser.Field_primeContext):
    #     # ID type_ eos field_prime | ID type_ eos
    #     if ctx.getChildCount() == 3:
    #         # TO DO
    #         return
    
        
    def visitVardecl(self,ctx:MiniGoParser.VardeclContext):
        return self.visit(ctx.var_spec())
    def visitVar_spec(self,ctx:MiniGoParser.Var_specContext):
        # ID (type_ (ASSIGN expr | ) | ASSIGN expr)
        # ID ASSIGN expr
        # ID type_ (ASSIGN expr| )
        varType = self.visit(ctx.type_()) if ctx.type_() else None
        varInit = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(ctx.ID().getText(),varType,varInit)
    def visitExpr(self,ctx:MiniGoParser.ExprContext):
        #primary_expr
        # |<assoc=right> unary_op expr
        # | expr mul_op expr
        # | expr add_op expr
        # | expr compare_op expr
        # | expr LOGICAL_AND expr
        # | expr LOGICAL_OR exp
        
        if ctx.primary_expr():
            #primary_expr
            return self.visit(ctx.primary_expr())
        if ctx.unary_op():
            # unary_op
            return UnaryOp(ctx.unary_op().getText(),self.visit(ctx.expr(0)))
        op = ctx.getChild(1)
        if not (ctx.LOGICAL_AND() or ctx.LOGICAL_OR()):
            op = op.getChild(0)
        
        return BinaryOp(op.getText(),self.visit(ctx.expr(0)),self.visit(ctx.expr(1)))
    def visitPrimary_expr(self,ctx:MiniGoParser.Primary_exprContext):
        # operand 
        # | primary_expr (ACCESS ID | index| ACCESS func_call)
        # | ID expr_params
        if ctx.operand():
            return self.visit(ctx.operand())
        if ctx.func_call():
            meth_call = self.visit(ctx.func_call())
            meth_call.receiver = self.visit(ctx.primary_expr())
            return meth_call
        if ctx.index():
            idx = self.visit(ctx.index())
            arr = self.visit(ctx.primary_expr())
            if isinstance(arr,ArrayCell):
                arr.idx += [idx]
                return arr
            return ArrayCell(arr,[idx])
        if ctx.expr_params():
            return FuncCall(ctx.ID().getText(),self.visit(ctx.expr_params()))
        return FieldAccess(self.visit(ctx.primary_expr()),ctx.ID().getText()) 
    def visitOperand(self,ctx:MiniGoParser.OperandContext):
        # ID
        # | L_PAREN expr R_PAREN
        # | literal
        if ctx.getChildCount() == 3:
            # L_PAREN expr R_PAREN
            return self.visit(ctx.expr())
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.literal())
    def visitPrimitive_lit(self,ctx:MiniGoParser.Primitive_litContext):
        # integer
        # | STRING_LIT
        # | NIL
        # | FLOAT_LIT
        # | TRUE | FALSE
        if ctx.integer():
            return self.visit(ctx.integer())
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        if ctx.NIL():
            return NilLiteral()
        # TRUE FALSE
        return BooleanLiteral(ctx.getChild(0).getText())
    def visitInteger(self, ctx: MiniGoParser.IntegerContext):
        int_lit = ctx.getChild(0).getText()
        return IntLiteral(int_lit)
            
    def visitComplex_lit(self,ctx: MiniGoParser.Complex_litContext):
        # complex_type complex_val
        # get type then add value later
        lit = self.visit(ctx.getChild(0))
        if ctx.list_type():
            lit.value = self.visit(ctx.getChild(1))
        else:
            lit.elements = self.visit(ctx.getChild(1))
        return lit
    def visitList_val(self,ctx:MiniGoParser.List_valContext):
        return self.visit(ctx.element_list()) if ctx.element_list() else []
    def visitElement_list(self,ctx:MiniGoParser.Element_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.element())] 
        return [self.visit(ctx.element())] + self.visit(ctx.element_list())
    def visitElement(self,ctx:MiniGoParser.ElementContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.complex_type():
            lit = self.visit(ctx.complex_type())
            lit.elements = self.visit(ctx.complex_val())
            return lit
        return self.visit(ctx.getChild(0))
    def visitComplex_val(self,ctx:MiniGoParser.Complex_valContext):
        return self.visit(ctx.key_element_list()) if ctx.key_element_list() else []
    def visitKey_element_list(self,ctx:MiniGoParser.Key_element_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.keyed_element())] 
        return [self.visit(ctx.keyed_element())] + self.visit(ctx.key_element_list())
    def visitKeyed_element(self,ctx:MiniGoParser.Keyed_elementContext):
        field_name = self.visit(ctx.field_name())
        expr = self.visit(ctx.expr())
        return (field_name,expr)
    def visitField_name(self,ctx:MiniGoParser.Field_nameContext):
        return ctx.ID().getText()    
    def visitArray_type(self,ctx:MiniGoParser.Array_typeContext):
        dimens = self.visit(ctx.array_decl())
        eleType = self.visit(ctx.type_())
        parent = ctx.parentCtx
        if isinstance(parent,MiniGoParser.List_typeContext):
            return ArrayLiteral([dimen for dimen in dimens],eleType,None)
        return ArrayType(dimens,eleType)
    def visitArray_decl(self,ctx:MiniGoParser.Array_declContext):
        # array_decl: array_len array_decl | array_len
        array_len = self.visit(ctx.array_len())
        if ctx.getChildCount() == 1:
            return [array_len]
        return [array_len] + self.visit(ctx.array_decl())
    def visitArray_len(self,ctx:MiniGoParser.Array_lenContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.integer())
    def visitConstdecl(self,ctx:MiniGoParser.ConstdeclContext):
        return self.visit(ctx.getChild(1))
    def visitConst_spec(self,ctx:MiniGoParser.Const_specContext):
        return ConstDecl(ctx.ID().getText(),None,self.visit(ctx.expr()))
    def visitBlock(self,ctx:MiniGoParser.BlockContext):
        stmt_list = self.visit(ctx.stmt_list()) if ctx.stmt_list() else []
        return Block(stmt_list)
    def visitStmt_list(self,ctx:MiniGoParser.Stmt_listContext):
        stmt = [self.visit(ctx.stmt())]
        if ctx.getChildCount() == 2:
            return stmt
        return stmt + self.visit(ctx.stmt_list())
    def visitReturn_stmt(self,ctx:MiniGoParser.Return_stmtContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return Return(expr)
    def visitFunc_call(self,ctx:MiniGoParser.Func_callContext):
        if isinstance(ctx.parentCtx,MiniGoParser.Primary_exprContext):
            return MethCall(None,ctx.ID().getText(),self.visit(ctx.expr_params()))
        return FuncCall(ctx.ID().getText(),self.visit(ctx.expr_params()))
    def visitExpr_params(self,ctx:MiniGoParser.Expr_paramsContext):
        return self.visit(ctx.expr_list()) if ctx.expr_list() else []
    def visitExpr_list(self,ctx:MiniGoParser.Expr_listContext):
        expr = [self.visit(ctx.expr())]
        if ctx.getChildCount() == 1:
            return expr
        return expr + self.visit(ctx.expr_list())
    def visitMethod_decl(self,ctx:MiniGoParser.Method_declContext):
        recv,recType = self.visit(ctx.receiver())
        fun = self.visit(ctx.method_spec())
        return MethodDecl(recv,recType,fun)
        # TO DO
    def visitMethod_spec(self,ctx:MiniGoParser.Method_specContext):
        # : ID func_params (return_type| ) block
        name = ctx.ID().getText()
        params = self.visit(ctx.func_params())
        retType = self.visit(ctx.return_type()) if ctx.return_type() else VoidType()
        body = self.visit(ctx.block())
        return FuncDecl(name,params,retType,body)
    def visitReceiver(self,ctx:MiniGoParser.ReceiverContext):
        return ctx.ID().getText(),self.visit(ctx.method_type())
    def visitMethod_type(self,ctx:MiniGoParser.Method_typeContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0))
    def visitAssignment(self,ctx:MiniGoParser.AssignmentContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr())
        op = self.visit(ctx.assign_op())
        if not op:
            return Assign(lhs,rhs)
        op.left = lhs
        op.right = rhs
        return Assign(lhs,op)
    def visitAssign_op(self,ctx:MiniGoParser.Assign_opContext):
        if ctx.ASSIGN() or ctx.DECLARE_ASSIGN():
            return None
        return BinaryOp(ctx.getChild(0).getText()[0],None,None)
    def visitLhs(self,ctx:MiniGoParser.LhsContext):
        '''
        lhs
        : lhs_prime (ACCESS ID| index)
        | ID
        ;
        '''
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        lhs = self.visit(ctx.lhs_prime())

        # Case 2: array cell
        if ctx.index():
            if isinstance(lhs,ArrayCell):
                lhs.idx.append(self.visit(ctx.index()))
            else:
                lhs = ArrayCell(lhs,[self.visit(ctx.index())])
            return lhs
        # Case 3: Field Access
        return FieldAccess(lhs,ctx.ID().getText())
    def visitLhs_prime(self,ctx:MiniGoParser.Lhs_primeContext):
        # lhs_prime
        # : lhs_ele
        # | lhs_prime (ACCESS ID| index)
        
        # Case 1: Base case - lhs_ele
        if ctx.getChildCount() == 1:
            return self.visit(ctx.lhs_ele())
        # visit the leftmost lhs
        lhs = self.visit(ctx.lhs_prime())
        # Case 2: array cell
        if ctx.index():
            if isinstance(lhs,ArrayCell):
                lhs.idx.append(self.visit(ctx.index()))
            else:
                lhs = ArrayCell(lhs,[self.visit(ctx.index())])
            return lhs
        # Case 3: Field Access
        return FieldAccess(lhs,ctx.ID().getText())
    def visitLhs_ele(self,ctx:MiniGoParser.Lhs_eleContext):
        '''
        lhs_ele
        : ID
        | func_call
        | method_call
        '''
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0))
    def visitMethod_call(self,ctx:MiniGoParser.Method_callContext):
        #     : expr ACCESS ID expr_params
        recv = self.visit(ctx.expr())
        metName = ctx.ID().getText()
        args = self.visit(ctx.expr_params())
        return MethCall(recv,metName,args)
    def visitIndex(self,ctx:MiniGoParser.IndexContext):
        return self.visit(ctx.expr())
    
    def visitType_name(self,ctx):
        return StructLiteral(ctx.ID().getText(),[])
    def visitIf_stmt(self,ctx:MiniGoParser.If_stmtContext):
        expr = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.block(0))
        if not ctx.ELSE():
            else_stmt = None
        elif ctx.if_stmt():
            else_stmt = self.visit(ctx.if_stmt())
        else:
            else_stmt = self.visit(ctx.block(1))
        return If(expr,then_stmt,else_stmt)
    def visitFor_stmt(self,ctx:MiniGoParser.For_stmtContext):
        for_clause = self.visit(ctx.for_clause())
        for_clause.loop = self.visit(ctx.block())
        return for_clause
    def visitFor_clause(self,ctx:MiniGoParser.For_clauseContext):
        if ctx.expr():
            return ForBasic(self.visit(ctx.expr()),None)
        return self.visit(ctx.getChild(0))
    def visitFor_ICU_clause(self,ctx:MiniGoParser.For_ICU_clauseContext):
        #     : init_stmt SEMI cond_stmt SEMI update_stmt
        init = self.visit(ctx.init_stmt())
        cond = self.visit(ctx.cond_stmt())
        upda = self.visit(ctx.update_stmt())
        return ForStep(init,cond,upda,None)
    def visitFor_range_clause(self,ctx:MiniGoParser.For_range_clauseContext):
        #    : (for_idx COMMA for_val) COLON ASSIGN RANGE expr;
        idx = self.visit(ctx.for_idx())
        value = self.visit(ctx.for_val())
        for_array = self.visit(ctx.expr())
        return ForEach(idx,value,for_array,None)
    def visitFor_idx(self,ctx:MiniGoParser.For_idxContext):
        return Id(ctx.ID().getText())
    def visitFor_val(self,ctx:MiniGoParser.For_valContext):
        return Id(ctx.ID().getText())
    def visitContinue_stmt(self,ctx:MiniGoParser.Continue_stmtContext):
        return Continue()
    def visitBreak_stmt(self,ctx:MiniGoParser.Break_stmtContext):
        return Break()
    def visitType_decl(self,ctx:MiniGoParser.Type_declContext):
        return self.visit(ctx.type_spec())
    def visitType_spec(self,ctx:MiniGoParser.Type_specContext):
        type_ = self.visit(ctx.getChild(1))
        type_.name = ctx.ID().getText()
        return type_
    def visitStruct_type(self,ctx:MiniGoParser.Struct_typeContext):
        elements = self.visit(ctx.field_prime())
        return StructType('',elements,[])
    def visitField_prime(self,ctx:MiniGoParser.Field_primeContext):
        element = [(ctx.ID().getText(),self.visit(ctx.type_()))]
        if not ctx.field_prime():
            return element
        return element + self.visit(ctx.field_prime())
    def visitType_(self,ctx:MiniGoParser.Type_Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0))       
    def visitInterface_type(self,ctx:MiniGoParser.Interface_typeContext):
        # INTERFACE L_CURLY method_list R_CURLY
        return InterfaceType('',self.visit(ctx.method_list()))
    def visitMethod_list(self,ctx:MiniGoParser.Method_listContext):
        #: method eos method_list
        #| method eos
        method = [self.visit(ctx.method())]
        if not ctx.method_list():
            return method
        return method + self.visit(ctx.method_list())
    def visitMethod(self,ctx:MiniGoParser.MethodContext):
        # ID func_params (return_type | )
        retType = self.visit(ctx.return_type()) if ctx.return_type() else VoidType()
        return Prototype(ctx.ID().getText(),self.visit(ctx.method_params()),retType)
    def visitMethod_params(self,ctx:MiniGoParser.Method_paramsContext):
        return self.visit(ctx.method_param_prime()) if ctx.method_param_prime() else []
    def visitMethod_param_prime(self,ctx:MiniGoParser.Method_param_primeContext):
        meth_param = self.visit(ctx.method_param())
        if not ctx.method_param_prime():
            return meth_param
        return meth_param + self.visit(ctx.method_param_prime())
    def visitMethod_param(self,ctx:MiniGoParser.Method_paramContext):
        return [self.visit(ctx.type_()) for _ in self.visit(ctx.id_list())]