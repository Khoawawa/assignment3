# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_list.
    def visitDecl_list(self, ctx:MiniGoParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#top_level_decl.
    def visitTop_level_decl(self, ctx:MiniGoParser.Top_level_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt_list.
    def visitStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs_prime.
    def visitLhs_prime(self, ctx:MiniGoParser.Lhs_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs_ele.
    def visitLhs_ele(self, ctx:MiniGoParser.Lhs_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_stmt.
    def visitCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_clause.
    def visitFor_clause(self, ctx:MiniGoParser.For_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_stmt.
    def visitInit_stmt(self, ctx:MiniGoParser.Init_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#cond_stmt.
    def visitCond_stmt(self, ctx:MiniGoParser.Cond_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#update_stmt.
    def visitUpdate_stmt(self, ctx:MiniGoParser.Update_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_ICU_clause.
    def visitFor_ICU_clause(self, ctx:MiniGoParser.For_ICU_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_range_clause.
    def visitFor_range_clause(self, ctx:MiniGoParser.For_range_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_idx.
    def visitFor_idx(self, ctx:MiniGoParser.For_idxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_val.
    def visitFor_val(self, ctx:MiniGoParser.For_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_array.
    def visitFor_array(self, ctx:MiniGoParser.For_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment.
    def visitAssignment(self, ctx:MiniGoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_op.
    def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_params.
    def visitFunc_params(self, ctx:MiniGoParser.Func_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_params_list.
    def visitFunc_params_list(self, ctx:MiniGoParser.Func_params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_param.
    def visitFunc_param(self, ctx:MiniGoParser.Func_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_type.
    def visitReturn_type(self, ctx:MiniGoParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_params.
    def visitExpr_params(self, ctx:MiniGoParser.Expr_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_spec.
    def visitConst_spec(self, ctx:MiniGoParser.Const_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_spec.
    def visitVar_spec(self, ctx:MiniGoParser.Var_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#id_list.
    def visitId_list(self, ctx:MiniGoParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_list.
    def visitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_.
    def visitType_(self, ctx:MiniGoParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_lit.
    def visitType_lit(self, ctx:MiniGoParser.Type_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#complex_type.
    def visitComplex_type(self, ctx:MiniGoParser.Complex_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_type.
    def visitList_type(self, ctx:MiniGoParser.List_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_name.
    def visitType_name(self, ctx:MiniGoParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#complex_lit.
    def visitComplex_lit(self, ctx:MiniGoParser.Complex_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_val.
    def visitList_val(self, ctx:MiniGoParser.List_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#complex_val.
    def visitComplex_val(self, ctx:MiniGoParser.Complex_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#key_element_list.
    def visitKey_element_list(self, ctx:MiniGoParser.Key_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element_list.
    def visitElement_list(self, ctx:MiniGoParser.Element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#keyed_element.
    def visitKeyed_element(self, ctx:MiniGoParser.Keyed_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_name.
    def visitField_name(self, ctx:MiniGoParser.Field_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element.
    def visitElement(self, ctx:MiniGoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_decl.
    def visitType_decl(self, ctx:MiniGoParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_spec.
    def visitType_spec(self, ctx:MiniGoParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_type.
    def visitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_spec.
    def visitMethod_spec(self, ctx:MiniGoParser.Method_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_type.
    def visitMethod_type(self, ctx:MiniGoParser.Method_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_list.
    def visitMethod_list(self, ctx:MiniGoParser.Method_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_params.
    def visitMethod_params(self, ctx:MiniGoParser.Method_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_param_prime.
    def visitMethod_param_prime(self, ctx:MiniGoParser.Method_param_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_param.
    def visitMethod_param(self, ctx:MiniGoParser.Method_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_call.
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_prime.
    def visitField_prime(self, ctx:MiniGoParser.Field_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#slice_type.
    def visitSlice_type(self, ctx:MiniGoParser.Slice_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_decl.
    def visitArray_decl(self, ctx:MiniGoParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_len.
    def visitArray_len(self, ctx:MiniGoParser.Array_lenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#single_type.
    def visitSingle_type(self, ctx:MiniGoParser.Single_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_lit.
    def visitPrimitive_lit(self, ctx:MiniGoParser.Primitive_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#integer.
    def visitInteger(self, ctx:MiniGoParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primary_expr.
    def visitPrimary_expr(self, ctx:MiniGoParser.Primary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index.
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unary_op.
    def visitUnary_op(self, ctx:MiniGoParser.Unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mul_op.
    def visitMul_op(self, ctx:MiniGoParser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#add_op.
    def visitAdd_op(self, ctx:MiniGoParser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compare_op.
    def visitCompare_op(self, ctx:MiniGoParser.Compare_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#eos.
    def visitEos(self, ctx:MiniGoParser.EosContext):
        return self.visitChildren(ctx)



del MiniGoParser