import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    num = 400

    def test_redeclare(self):
        tcs = [
            ("""var a int;type a struct {a int;};""", "Redeclared Type: a\n"),
            ("""type a struct {a int;};var a int;""", "Redeclared Variable: a\n"),
            ("""func a(){return;};var a int;""", "Redeclared Variable: a\n"),
            ("""func a(a int,a int){return;};""", "Redeclared Parameter: a\n"),
            ("""func main(){var a int; var a int;};""","Redeclared Variable: a\n"),
            ("""func main(){x:= 1;};""",""),
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)

    def test_undeclare(self):
        tcs = [
            ("""func a(){b();};""", "Undeclared Function: b\n"),
            ("""func a(){b();};func b(){b();};""", "Undeclared Function: b\n"),
            ("""func a(){b();};func b(){b();};func c(){b();};""", "Undeclared Function: b\n"),
            ("""func b(){b();};func c(){d();};""", "Undeclared Function: d\n"),
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)

    def test_arr(self):
        tcs = [
            ("""func main(){var a = [5]int{1,2,3,5};};""", ""),
            ("""var a int = [5]int{1,2,3,4};""","Type Mismatch: VarDecl(a,IntType,ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))\n"),
            ("""func main(){var a = [1]int{1};};""",""),
            ("""func main(){var a = [3]int{1,"Hello"}; };""","Type Mismatch: ArrayLiteral([IntLiteral(3)],IntType,[IntLiteral(1),StringLiteral(\"Hello\")])\n"),
            ("""func main(){var d = [2][2]int{{1,2},{3,4}};};""",""),
            ("""var a [5]int = 10;""","Type Mismatch: VarDecl(a,ArrayType(IntType,[IntLiteral(5)]),IntLiteral(10))\n"),
            ("""var b = [2][3]float{{1.1, 2.2, 3.3}, {4, 5.5, 6.6}};""","Type Mismatch: ArrayLiteral([IntLiteral(2),IntLiteral(3)],FloatType,[[FloatLiteral(1.1),FloatLiteral(2.2),FloatLiteral(3.3)],[IntLiteral(4),FloatLiteral(5.5),FloatLiteral(6.6)]])\n"),
            ("""var a[5]int; func main(){a[1] = 2;};""",""),
            ("""var a[5]int = [5]int{1,2,3,4,5}; func main(){a[1] = 2;};""",""),
            ("""type A struct {a int;}; func main(){var arr[2]A;};""",""),
            ("""type A struct {a int;}; func test(a A, b A, c A, d A){var arr = [2][2]A{{a,b},{c,d}};};func main(){var arr[2]A;};""",""),
            ("""type A struct {a int;}; func main(){var arr [2]int = A{a:10};};""", 
            "Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(2)]),StructLiteral(A,[(a,IntLiteral(10))]))\n"),
            ("""type A struct {a int;}; var arr [2]A; func main(){arr[1] = 10;};""",
            "Type Mismatch: Assign(ArrayCell(Id(arr),[IntLiteral(1)]),IntLiteral(10))\n"),
            
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)

    def test_field(self):
        tcs = [
            ("""type A struct{
                a int;
                };
                var a = A{a:1};
            """,
            "Undeclared Function: main\n"),
            (""" var a = A{a:1};""", "Undeclared Type: A\n"),
            ("""type A struct{
                a int;
                };
                var a = A{b:1};
            """,
            "Undeclared Field: b\n"),
            ("""type A struct{
                a int;
                };
                var a = A{a:1,b:2};
            """,
            "Undeclared Field: b\n"),
            ("""type A struct{
                a int;
                };
                var a = A{a:1};
                var b = A{a:1};
            """,
            "Undeclared Function: main\n"),
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)

    def test_assign(self):
        tcs = [
            ("""var a int; func main(){a = 1;};""", ""),
            ("""var a int = 1.2;""", "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"),
            ("""func main(){a := 1;};""",""),
            ("""func main(){a := a + 1;};""","Undeclared Identifier: a\n"),
            ("""func main(){a *= 1;};""","Undeclared Identifier: a\n"),
            ("""var a int = 10; func main(){a += 10;};""",""),
            ("""var a float; func main(){a = 2;};""",""),
            ("""var a boolean; func main(){a = 1;};""", "Type Mismatch: Assign(Id(a),IntLiteral(1))\n"),
            ("""var a int; func main(){a -= 1.5;};""", "Type Mismatch: Assign(Id(a),BinaryOp(Id(a),-,FloatLiteral(1.5)))\n"),
            ("""var a float; func main(){b := a / 2;};""", ""),
            ("""func main(){a:= 1 + 1 * 2 / 3 - 4 + a;};""","Undeclared Identifier: a\n"),
            ("""var a = [5]int{1,2,3,4,5}; var b[5] int; func main(){b = a;};""",""),
            ("""var a = [5][3][1]int{1,2,3,4,5}; var b[5][3][1] int; func main(){b = a;};""",""),
            ("""var a = [5]int{1,2,3,4,5}; var b[5] int; func main(){b = a;};""",""),
            ("""var a = [5]int{1,2,3,4,5}; var b[6] int; func main(){b = a;};""","Type Mismatch: Assign(Id(b),Id(a))\n"),
            ("""var a = [6][5] int{1,2,3,4,5}; var b[6] int; func main(){b = a;};""","Type Mismatch: Assign(Id(b),Id(a))\n"),
            ("""var a = [6][5] int{1,2,3,4,5}; var b[6][4] int; func main(){b = a;};""","Type Mismatch: Assign(Id(b),Id(a))\n"),
            # interface and struct
            ("""
             type I interface{Add(x int,y int);}
             type S struct{
                sum int;
             }
             func (s S) Add(x int,y int){
                s.sum = x + y;
             }
             func main(){
                var i I;
                i = S{sum:0}; 
             }
             """,
             ""),
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)

    def test_expr(self):
        tcs = [
            ("""var a float;
             func main(){
                    a = 1 + 2;
                 };""", ""),
            ("""
             func add(x int, y int) int{
                return x + y;
             }
             func main(){
                var a int;
                a = add(1,2); 
             }
             """,
             ""),
            (
                """
                func main(){
                    var a = 1 + "Hello"
                }
                """,
                "Type Mismatch: BinaryOp(IntLiteral(1),+,StringLiteral(\"Hello\"))\n"
            ),
            (
                """
                var a int = 1.2;
                """,
                "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n" 
            ),
            (
              """
              var a int;
              var b float;
              func main(){
                a = b;
              }
              """,
              "Type Mismatch: Assign(Id(a),Id(b))\n"  
            ),
            (
            """
            
            func main(){
                var a int;
                a = 10 + 5 * 3 / 2    
            }
            """,
            ""
            ),
            (
            """
            func main(){
                var a int;
                a = -10 + 5 * 3 / 2    
            }
            """,
            ""
            ),
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)
    def test_func(self):
        tcs = [
            (
                """
                func a(){
                    return;   
                }
                func main(){
                    a();
                }
                """,
                ""
            ),
            (
                """
                func a() int{
                    return 1
                }
                func main(){
                    a();
                }
                """,
                "Type Mismatch: FuncCall(a,[])\n"
            ),
            (
                """
                func a() {
                    return;
                }
                func main(){
                    var a int = a()
                }
                """,
                "Type Mismatch: FuncCall(a,[])\n"    
            ),
            (
                """
                func add(x int, y int) int {
                    return x + y;
                }
                func main() {
                    var z int = add(3, 5);
                }
                """,
                ""
            ),
            (
                """
                func doSomething() {
                    return;
                }
                func main() {
                    var x int = 1 + doSomething();
                }
                """,
                "Type Mismatch: FuncCall(doSomething,[])\n"
            ),
            (
                """
                func a(x int, y int) int{
                    return x + y
                }
                func main(){
                    a(3)
                }
                """,
                "Type Mismatch: FuncCall(a,[IntLiteral(3)])\n"
            ),
            (
                """
                func a(x int, y int) int{
                    return x + y
                }
                func main(){
                    a(3.2)
                }
                """,
                "Type Mismatch: FuncCall(a,[FloatLiteral(3.2)])\n"
            ),
            (
                """
                func factorial(n int) int {
                    return n * factorial(n - 1);
                }
                func main() {
                    var result int = factorial(5);
                }
                """,
                ""  
            ),
            (
               """
                func factorial(n int) bool {
                    return n * factorial(n - 1);
                }
                func main() {
                    var result int = factorial(5);
                }
                """,
                "Undeclared Identifier: bool\n" 
            )
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)
    def test_if(self):
        tcs = [
            # test if base
            ("""func main(){if (true) {a=1;};};""",""),
            ("""func main(){if (false) {a=1;} else {a=2;};};""",""),
            ("""func main(){if (true){if (true) {a=1;} else {b=2;};} else {c=3;};};""",""),
            ("""func main(){if (false) {a=1;} else if (false) {a=2;} else {a=3;};};""",""),
            ("""func main(){a := true; if (a) {b=2;};};""", ""),
            ("""func main(){if (1 > 0) {a=1;};};""", ""),
            ("""func main(){if (!true) {a=1;};};""", ""),
            # test not bool on cond
            ("""func main(){if (1) {a=1;};};""", "Type Mismatch: If(IntLiteral(1),Block([Assign(Id(a),IntLiteral(1))]))\n"),
            ("""func main(){if (1.2) {a=1;};};""", "Type Mismatch: If(FloatLiteral(1.2),Block([Assign(Id(a),IntLiteral(1))]))\n"),
            ("""func main(){if ("Hello") {a=1;};};""", "Type Mismatch: If(StringLiteral(\"Hello\"),Block([Assign(Id(a),IntLiteral(1))]))\n"),
            ("""func main(){if (10 + 5) {a=1;};};""", "Type Mismatch: If(BinaryOp(IntLiteral(10),+,IntLiteral(5)),Block([Assign(Id(a),IntLiteral(1))]))\n"),
            ("""func main(){if (a) {a=1;};};""","Undeclared Identifier: a\n"),
            ("""var a int; func main(){if (a) {a=1;};};""", "Type Mismatch: If(Id(a),Block([Assign(Id(a),IntLiteral(1))]))\n"),
            ("""var a float; func main(){if (a) {a=1;};};""", "Type Mismatch: If(Id(a),Block([Assign(Id(a),IntLiteral(1))]))\n"),
            ("""var a string; func main(){if (a) {a=1;};};""", "Type Mismatch: If(Id(a),Block([Assign(Id(a),IntLiteral(1))]))\n"),
            ("""var a int; func main(){if (!a) {b=1;};};""", "Type Mismatch: UnaryOp(!,Id(a))\n"),
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)
    def test_struct(self):
        tcs = [
            ("""type A struct {a int;}; type B struct {arr [2]A;}; func main(){var x = B{arr:[2]A{A{a:1}, A{a:2}}};};""", ""),
            ("""type A struct {a int;}; var arr [2]int = A{a:10};""", 
     "Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(2)]),StructLiteral(A,[(a,IntLiteral(10))]))\n"),
            ("""type A struct {arr [5] int;}; func main(){var a A = A{arr: [3]int {1,2,3}};};""",""),
            ("""type A struct {a int;};func main(){ var arr [2]int = A{a:10};};""", 
     "Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(2)]),StructLiteral(A,[(a,IntLiteral(10))]))\n"),
            ("""type A struct { arr [5]int; }; 
func main() {
    var a = A{};
    a.arr = 100;
}
""","Type Mismatch: Assign(FieldAccess(Id(a),arr),IntLiteral(100))\n"),
            ("""type A struct { arr int; }; 
func main() {
    var a A;
    a.arr = 100;
}
""",""),
            (
                """
                type S struct{
                    i int;
                }
                func (s S) foo(x int) int{
                    return x + s.foo(x);
                }
                func main(){
                    var s S;
                    var a int = s.foo(10);
                }
                """
                ,""
            ),
            (
                """
                type S struct{
                    i int;
                }
                func (s S) foo(x int) int{
                    return x + s.foo(x);
                }
                func main(){
                    var s S;
                    var a int = s.foo(10,20);
                }
                """,
                "Type Mismatch: MethodCall(Id(s),foo,[IntLiteral(10),IntLiteral(20)])\n"
            ),
            (
                """
                type S struct{
                    i int;
                }
                func (s S) foo(x int) int{
                    return x + s.foo(x);
                }
                func main(){
                    var s S;
                    s.foo(10);
                }
                """,
                "Type Mismatch: MethodCall(Id(s),foo,[IntLiteral(10)])\n"
            )
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)
    def test_interface(self):
        tcs = [
            (
                """
                type I interface {
                    foo(x int) int
                }
                type S struct{
                    i int
                }
                func (s S) foo(x string) int{
                    return s.i
                }
                func main(){
                    var i I = S{i:1}
                }
                """,
                "Type Mismatch: VarDecl(i,Id(I),StructLiteral(S,[(i,IntLiteral(1))]))\n"
            ),
            (
                """
                type I interface{
                    foo(x int) int
                    foo(y int) int
                }
                """,
                "Redeclared Prototype: foo\n"
            ),
            (
                """
                type I interface {
    foo(x int) int;
};

type S struct {i int; };

func (a S) foo(x int) string { // Mismatch: expected foo(int) int but got foo(int) string
    return "hello";
}

func main() {
    var a S;
    var i I = a;  // Type Mismatch: A does not correctly implement I
}
                """,
                "Type Mismatch: VarDecl(i,Id(I),Id(a))\n"
            )
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)
    def test_for(self):
        tcs = [
            (
                """
                func main(){
                    var i int = 10
                    for i < 10 {
                        a = 1
                    }
                }
                """,
                ""
            ),
            (
                """
                func a() boolean {return true;}
                func main(){
                    var a int
                    for a() {
                        a = 1
                    }
                }
                """,
                "Type Mismatch: FuncCall(a,[])\n"
            ),
            (
                """
                
                """
            )
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)
    def test_global(self):
        tcs = [
            
        ]
        CheckSuite.num = load_tcs(self, tcs, CheckSuite.num)
def load_tcs(suite: CheckSuite, tcs, start_num):
    for tc in tcs:
        # print(start_num)
        input = tc[0]
        exp = tc[1]
        if not isinstance(exp, str):
            exp = str(exp)
        try:
            suite.assertTrue(TestChecker.test(input, exp, start_num))
        except AssertionError as e:
            print(f"Test failed at index {start_num}")
            print(f"Input: {input}")
            print(f"Expected: {exp}")
            print(f"Error: {e}")
        finally:
            start_num += 1
    
    return start_num
