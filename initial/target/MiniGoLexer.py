# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01ec\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.")
        buf.write("\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\65\7\65\u015c\n\65\f\65\16\65\u015f")
        buf.write("\13\65\3\66\3\66\3\66\7\66\u0164\n\66\f\66\16\66\u0167")
        buf.write("\13\66\5\66\u0169\n\66\3\67\3\67\3\67\6\67\u016e\n\67")
        buf.write("\r\67\16\67\u016f\38\38\38\68\u0175\n8\r8\168\u0176\3")
        buf.write("9\39\39\69\u017c\n9\r9\169\u017d\3:\3:\3:\5:\u0183\n:")
        buf.write("\3:\5:\u0186\n:\3;\3;\3;\7;\u018b\n;\f;\16;\u018e\13;")
        buf.write("\3;\3;\3<\6<\u0193\n<\r<\16<\u0194\3<\3<\3=\6=\u019a\n")
        buf.write("=\r=\16=\u019b\3=\3=\3>\3>\3>\3>\7>\u01a4\n>\f>\16>\u01a7")
        buf.write("\13>\3>\3>\3>\3>\7>\u01ad\n>\f>\16>\u01b0\13>\3>\3>\5")
        buf.write(">\u01b4\n>\3>\3>\3?\3?\3?\3?\3?\7?\u01bd\n?\f?\16?\u01c0")
        buf.write("\13?\3?\3?\3?\3?\3?\3@\3@\3A\3A\3B\3B\3C\5C\u01ce\nC\3")
        buf.write("D\3D\3E\3E\3F\3F\3G\3G\3H\3H\5H\u01da\nH\3H\6H\u01dd\n")
        buf.write("H\rH\16H\u01de\3I\6I\u01e2\nI\rI\16I\u01e3\3J\3J\3K\3")
        buf.write("K\3L\3L\3L\4\u01ae\u01be\2M\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C")
        buf.write("\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091")
        buf.write("\2\u0093\2\u0095\2\u0097\2\3\2\24\3\2\63;\4\2DDdd\4\2")
        buf.write("QQqq\4\2ZZzz\4\2$$^^\3\2\f\f\5\2\13\13\17\17\"\"\4\2\f")
        buf.write("\f\17\17\5\2C\\aac|\3\2\62;\3\2\62\63\3\2\629\5\2\62;")
        buf.write("CHch\4\2GGgg\4\2--//\3\2))\3\2$$\7\2$$^^ppttvv\2\u01f6")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\3\u0099\3\2\2\2\5\u009e\3\2\2\2\7\u00a1\3\2\2")
        buf.write("\2\t\u00a7\3\2\2\2\13\u00ac\3\2\2\2\r\u00b0\3\2\2\2\17")
        buf.write("\u00b7\3\2\2\2\21\u00bc\3\2\2\2\23\u00c3\3\2\2\2\25\u00cd")
        buf.write("\3\2\2\2\27\u00d3\3\2\2\2\31\u00d7\3\2\2\2\33\u00e0\3")
        buf.write("\2\2\2\35\u00e6\3\2\2\2\37\u00ea\3\2\2\2!\u00ef\3\2\2")
        buf.write("\2#\u00f5\3\2\2\2%\u00f9\3\2\2\2\'\u0100\3\2\2\2)\u0106")
        buf.write("\3\2\2\2+\u010e\3\2\2\2-\u0110\3\2\2\2/\u0112\3\2\2\2")
        buf.write("\61\u0114\3\2\2\2\63\u0116\3\2\2\2\65\u0118\3\2\2\2\67")
        buf.write("\u011b\3\2\2\29\u011e\3\2\2\2;\u0120\3\2\2\2=\u0123\3")
        buf.write("\2\2\2?\u0125\3\2\2\2A\u0128\3\2\2\2C\u012b\3\2\2\2E\u012e")
        buf.write("\3\2\2\2G\u0130\3\2\2\2I\u0132\3\2\2\2K\u0134\3\2\2\2")
        buf.write("M\u0137\3\2\2\2O\u013a\3\2\2\2Q\u013d\3\2\2\2S\u0140\3")
        buf.write("\2\2\2U\u0143\3\2\2\2W\u0146\3\2\2\2Y\u0148\3\2\2\2[\u014a")
        buf.write("\3\2\2\2]\u014c\3\2\2\2_\u014e\3\2\2\2a\u0150\3\2\2\2")
        buf.write("c\u0152\3\2\2\2e\u0154\3\2\2\2g\u0156\3\2\2\2i\u0158\3")
        buf.write("\2\2\2k\u0168\3\2\2\2m\u016a\3\2\2\2o\u0171\3\2\2\2q\u0178")
        buf.write("\3\2\2\2s\u017f\3\2\2\2u\u0187\3\2\2\2w\u0192\3\2\2\2")
        buf.write("y\u0199\3\2\2\2{\u01b3\3\2\2\2}\u01b7\3\2\2\2\177\u01c6")
        buf.write("\3\2\2\2\u0081\u01c8\3\2\2\2\u0083\u01ca\3\2\2\2\u0085")
        buf.write("\u01cd\3\2\2\2\u0087\u01cf\3\2\2\2\u0089\u01d1\3\2\2\2")
        buf.write("\u008b\u01d3\3\2\2\2\u008d\u01d5\3\2\2\2\u008f\u01d7\3")
        buf.write("\2\2\2\u0091\u01e1\3\2\2\2\u0093\u01e5\3\2\2\2\u0095\u01e7")
        buf.write("\3\2\2\2\u0097\u01e9\3\2\2\2\u0099\u009a\7h\2\2\u009a")
        buf.write("\u009b\7w\2\2\u009b\u009c\7p\2\2\u009c\u009d\7e\2\2\u009d")
        buf.write("\4\3\2\2\2\u009e\u009f\7k\2\2\u009f\u00a0\7h\2\2\u00a0")
        buf.write("\6\3\2\2\2\u00a1\u00a2\7d\2\2\u00a2\u00a3\7t\2\2\u00a3")
        buf.write("\u00a4\7g\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7m\2\2\u00a6")
        buf.write("\b\3\2\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7n\2\2\u00a9")
        buf.write("\u00aa\7u\2\2\u00aa\u00ab\7g\2\2\u00ab\n\3\2\2\2\u00ac")
        buf.write("\u00ad\7h\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7t\2\2\u00af")
        buf.write("\f\3\2\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7g\2\2\u00b2")
        buf.write("\u00b3\7v\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7t\2\2\u00b5")
        buf.write("\u00b6\7p\2\2\u00b6\16\3\2\2\2\u00b7\u00b8\7v\2\2\u00b8")
        buf.write("\u00b9\7{\2\2\u00b9\u00ba\7r\2\2\u00ba\u00bb\7g\2\2\u00bb")
        buf.write("\20\3\2\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be\7v\2\2\u00be")
        buf.write("\u00bf\7t\2\2\u00bf\u00c0\7w\2\2\u00c0\u00c1\7e\2\2\u00c1")
        buf.write("\u00c2\7v\2\2\u00c2\22\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4")
        buf.write("\u00c5\7p\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7\7g\2\2\u00c7")
        buf.write("\u00c8\7t\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca\7c\2\2\u00ca")
        buf.write("\u00cb\7e\2\2\u00cb\u00cc\7g\2\2\u00cc\24\3\2\2\2\u00cd")
        buf.write("\u00ce\7e\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0\7p\2\2\u00d0")
        buf.write("\u00d1\7u\2\2\u00d1\u00d2\7v\2\2\u00d2\26\3\2\2\2\u00d3")
        buf.write("\u00d4\7x\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6\7t\2\2\u00d6")
        buf.write("\30\3\2\2\2\u00d7\u00d8\7e\2\2\u00d8\u00d9\7q\2\2\u00d9")
        buf.write("\u00da\7p\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7k\2\2\u00dc")
        buf.write("\u00dd\7p\2\2\u00dd\u00de\7w\2\2\u00de\u00df\7g\2\2\u00df")
        buf.write("\32\3\2\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7c\2\2\u00e2")
        buf.write("\u00e3\7p\2\2\u00e3\u00e4\7i\2\2\u00e4\u00e5\7g\2\2\u00e5")
        buf.write("\34\3\2\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7k\2\2\u00e8")
        buf.write("\u00e9\7n\2\2\u00e9\36\3\2\2\2\u00ea\u00eb\7v\2\2\u00eb")
        buf.write("\u00ec\7t\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee\7g\2\2\u00ee")
        buf.write(" \3\2\2\2\u00ef\u00f0\7h\2\2\u00f0\u00f1\7c\2\2\u00f1")
        buf.write("\u00f2\7n\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4\7g\2\2\u00f4")
        buf.write("\"\3\2\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7p\2\2\u00f7")
        buf.write("\u00f8\7v\2\2\u00f8$\3\2\2\2\u00f9\u00fa\7u\2\2\u00fa")
        buf.write("\u00fb\7v\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd\7k\2\2\u00fd")
        buf.write("\u00fe\7p\2\2\u00fe\u00ff\7i\2\2\u00ff&\3\2\2\2\u0100")
        buf.write("\u0101\7h\2\2\u0101\u0102\7n\2\2\u0102\u0103\7q\2\2\u0103")
        buf.write("\u0104\7c\2\2\u0104\u0105\7v\2\2\u0105(\3\2\2\2\u0106")
        buf.write("\u0107\7d\2\2\u0107\u0108\7q\2\2\u0108\u0109\7q\2\2\u0109")
        buf.write("\u010a\7n\2\2\u010a\u010b\7g\2\2\u010b\u010c\7c\2\2\u010c")
        buf.write("\u010d\7p\2\2\u010d*\3\2\2\2\u010e\u010f\7-\2\2\u010f")
        buf.write(",\3\2\2\2\u0110\u0111\7/\2\2\u0111.\3\2\2\2\u0112\u0113")
        buf.write("\7,\2\2\u0113\60\3\2\2\2\u0114\u0115\7\61\2\2\u0115\62")
        buf.write("\3\2\2\2\u0116\u0117\7\'\2\2\u0117\64\3\2\2\2\u0118\u0119")
        buf.write("\7?\2\2\u0119\u011a\7?\2\2\u011a\66\3\2\2\2\u011b\u011c")
        buf.write("\7#\2\2\u011c\u011d\7?\2\2\u011d8\3\2\2\2\u011e\u011f")
        buf.write("\7>\2\2\u011f:\3\2\2\2\u0120\u0121\7>\2\2\u0121\u0122")
        buf.write("\7?\2\2\u0122<\3\2\2\2\u0123\u0124\7@\2\2\u0124>\3\2\2")
        buf.write("\2\u0125\u0126\7@\2\2\u0126\u0127\7?\2\2\u0127@\3\2\2")
        buf.write("\2\u0128\u0129\7(\2\2\u0129\u012a\7(\2\2\u012aB\3\2\2")
        buf.write("\2\u012b\u012c\7~\2\2\u012c\u012d\7~\2\2\u012dD\3\2\2")
        buf.write("\2\u012e\u012f\7#\2\2\u012fF\3\2\2\2\u0130\u0131\7<\2")
        buf.write("\2\u0131H\3\2\2\2\u0132\u0133\7?\2\2\u0133J\3\2\2\2\u0134")
        buf.write("\u0135\7-\2\2\u0135\u0136\7?\2\2\u0136L\3\2\2\2\u0137")
        buf.write("\u0138\7/\2\2\u0138\u0139\7?\2\2\u0139N\3\2\2\2\u013a")
        buf.write("\u013b\7,\2\2\u013b\u013c\7?\2\2\u013cP\3\2\2\2\u013d")
        buf.write("\u013e\7\61\2\2\u013e\u013f\7?\2\2\u013fR\3\2\2\2\u0140")
        buf.write("\u0141\7\'\2\2\u0141\u0142\7?\2\2\u0142T\3\2\2\2\u0143")
        buf.write("\u0144\7<\2\2\u0144\u0145\7?\2\2\u0145V\3\2\2\2\u0146")
        buf.write("\u0147\7\60\2\2\u0147X\3\2\2\2\u0148\u0149\7*\2\2\u0149")
        buf.write("Z\3\2\2\2\u014a\u014b\7+\2\2\u014b\\\3\2\2\2\u014c\u014d")
        buf.write("\7}\2\2\u014d^\3\2\2\2\u014e\u014f\7\177\2\2\u014f`\3")
        buf.write("\2\2\2\u0150\u0151\7]\2\2\u0151b\3\2\2\2\u0152\u0153\7")
        buf.write("_\2\2\u0153d\3\2\2\2\u0154\u0155\7.\2\2\u0155f\3\2\2\2")
        buf.write("\u0156\u0157\7=\2\2\u0157h\3\2\2\2\u0158\u015d\5\u0085")
        buf.write("C\2\u0159\u015c\5\u0085C\2\u015a\u015c\5\u0087D\2\u015b")
        buf.write("\u0159\3\2\2\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2")
        buf.write("\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015ej\3\2\2")
        buf.write("\2\u015f\u015d\3\2\2\2\u0160\u0169\7\62\2\2\u0161\u0165")
        buf.write("\t\2\2\2\u0162\u0164\5\u0087D\2\u0163\u0162\3\2\2\2\u0164")
        buf.write("\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2")
        buf.write("\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0160\3")
        buf.write("\2\2\2\u0168\u0161\3\2\2\2\u0169l\3\2\2\2\u016a\u016b")
        buf.write("\7\62\2\2\u016b\u016d\t\3\2\2\u016c\u016e\5\u0089E\2\u016d")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u016d\3\2\2\2")
        buf.write("\u016f\u0170\3\2\2\2\u0170n\3\2\2\2\u0171\u0172\7\62\2")
        buf.write("\2\u0172\u0174\t\4\2\2\u0173\u0175\5\u008bF\2\u0174\u0173")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0174\3\2\2\2\u0176")
        buf.write("\u0177\3\2\2\2\u0177p\3\2\2\2\u0178\u0179\7\62\2\2\u0179")
        buf.write("\u017b\t\5\2\2\u017a\u017c\5\u008dG\2\u017b\u017a\3\2")
        buf.write("\2\2\u017c\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017er\3\2\2\2\u017f\u0180\5k\66\2\u0180\u0182")
        buf.write("\7\60\2\2\u0181\u0183\5\u0091I\2\u0182\u0181\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u0186\5\u008f")
        buf.write("H\2\u0185\u0184\3\2\2\2\u0185\u0186\3\2\2\2\u0186t\3\2")
        buf.write("\2\2\u0187\u018c\5\u0095K\2\u0188\u018b\n\6\2\2\u0189")
        buf.write("\u018b\5\u0097L\2\u018a\u0188\3\2\2\2\u018a\u0189\3\2")
        buf.write("\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018d\u018f\3\2\2\2\u018e\u018c\3\2\2\2\u018f")
        buf.write("\u0190\5\u0095K\2\u0190v\3\2\2\2\u0191\u0193\t\7\2\2\u0192")
        buf.write("\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\b")
        buf.write("<\2\2\u0197x\3\2\2\2\u0198\u019a\t\b\2\2\u0199\u0198\3")
        buf.write("\2\2\2\u019a\u019b\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\b=\3\2\u019e")
        buf.write("z\3\2\2\2\u019f\u01a0\7\61\2\2\u01a0\u01a1\7\61\2\2\u01a1")
        buf.write("\u01a5\3\2\2\2\u01a2\u01a4\n\t\2\2\u01a3\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3")
        buf.write("\2\2\2\u01a6\u01b4\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01a9")
        buf.write("\7\61\2\2\u01a9\u01aa\7,\2\2\u01aa\u01ae\3\2\2\2\u01ab")
        buf.write("\u01ad\n\t\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01b0\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b1\3")
        buf.write("\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\7,\2\2\u01b2\u01b4")
        buf.write("\7\61\2\2\u01b3\u019f\3\2\2\2\u01b3\u01a8\3\2\2\2\u01b4")
        buf.write("\u01b5\3\2\2\2\u01b5\u01b6\b>\3\2\u01b6|\3\2\2\2\u01b7")
        buf.write("\u01b8\7\61\2\2\u01b8\u01b9\7,\2\2\u01b9\u01be\3\2\2\2")
        buf.write("\u01ba\u01bd\5}?\2\u01bb\u01bd\13\2\2\2\u01bc\u01ba\3")
        buf.write("\2\2\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c1\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c1\u01c2\7,\2\2\u01c2\u01c3\7\61\2\2")
        buf.write("\u01c3\u01c4\3\2\2\2\u01c4\u01c5\b?\3\2\u01c5~\3\2\2\2")
        buf.write("\u01c6\u01c7\13\2\2\2\u01c7\u0080\3\2\2\2\u01c8\u01c9")
        buf.write("\13\2\2\2\u01c9\u0082\3\2\2\2\u01ca\u01cb\13\2\2\2\u01cb")
        buf.write("\u0084\3\2\2\2\u01cc\u01ce\t\n\2\2\u01cd\u01cc\3\2\2\2")
        buf.write("\u01ce\u0086\3\2\2\2\u01cf\u01d0\t\13\2\2\u01d0\u0088")
        buf.write("\3\2\2\2\u01d1\u01d2\t\f\2\2\u01d2\u008a\3\2\2\2\u01d3")
        buf.write("\u01d4\t\r\2\2\u01d4\u008c\3\2\2\2\u01d5\u01d6\t\16\2")
        buf.write("\2\u01d6\u008e\3\2\2\2\u01d7\u01d9\t\17\2\2\u01d8\u01da")
        buf.write("\t\20\2\2\u01d9\u01d8\3\2\2\2\u01d9\u01da\3\2\2\2\u01da")
        buf.write("\u01dc\3\2\2\2\u01db\u01dd\t\13\2\2\u01dc\u01db\3\2\2")
        buf.write("\2\u01dd\u01de\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df")
        buf.write("\3\2\2\2\u01df\u0090\3\2\2\2\u01e0\u01e2\t\13\2\2\u01e1")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e4\3\2\2\2\u01e4\u0092\3\2\2\2\u01e5\u01e6\t")
        buf.write("\21\2\2\u01e6\u0094\3\2\2\2\u01e7\u01e8\t\22\2\2\u01e8")
        buf.write("\u0096\3\2\2\2\u01e9\u01ea\7^\2\2\u01ea\u01eb\t\23\2\2")
        buf.write("\u01eb\u0098\3\2\2\2\31\2\u015b\u015d\u0165\u0168\u016f")
        buf.write("\u0176\u017d\u0182\u0185\u018a\u018c\u0194\u019b\u01a5")
        buf.write("\u01ae\u01b3\u01bc\u01be\u01cd\u01d9\u01de\u01e3\4\3<")
        buf.write("\2\b\2\2")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    FUNC = 1
    IF = 2
    BREAK = 3
    ELSE = 4
    FOR = 5
    RETURN = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    CONST = 10
    VAR = 11
    CONTINUE = 12
    RANGE = 13
    NIL = 14
    TRUE = 15
    FALSE = 16
    INT_TYPE = 17
    STRING_TYPE = 18
    FLOAT_TYPE = 19
    BOOL_TYPE = 20
    PLUS = 21
    MINUS = 22
    MULT = 23
    DIV = 24
    MOD = 25
    EQUALS = 26
    NOT_EQUALS = 27
    LESS = 28
    LESS_EQUALS = 29
    GREATER = 30
    GREATER_EQUALS = 31
    LOGICAL_AND = 32
    LOGICAL_OR = 33
    LOGICAL_NOT = 34
    COLON = 35
    ASSIGN = 36
    PLUS_ASSIGN = 37
    MINUS_ASSIGN = 38
    MULT_ASSIGN = 39
    DIV_ASSIGN = 40
    MOD_ASSIGN = 41
    DECLARE_ASSIGN = 42
    ACCESS = 43
    L_PAREN = 44
    R_PAREN = 45
    L_CURLY = 46
    R_CURLY = 47
    L_BRACKET = 48
    R_BRACKET = 49
    COMMA = 50
    SEMI = 51
    ID = 52
    DECIMAL_LIT = 53
    BINARY_LIT = 54
    OCTAL_LIT = 55
    HEX_LIT = 56
    FLOAT_LIT = 57
    STRING_LIT = 58
    TERMINATOR = 59
    WS = 60
    LINE_COMMENT = 61
    COMMENT = 62
    ERROR_CHAR = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'func'", "'if'", "'break'", "'else'", "'for'", "'return'", 
            "'type'", "'struct'", "'interface'", "'const'", "'var'", "'continue'", 
            "'range'", "'nil'", "'true'", "'false'", "'int'", "'string'", 
            "'float'", "'boolean'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "':'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "':='", 
            "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "FUNC", "IF", "BREAK", "ELSE", "FOR", "RETURN", "TYPE", "STRUCT", 
            "INTERFACE", "CONST", "VAR", "CONTINUE", "RANGE", "NIL", "TRUE", 
            "FALSE", "INT_TYPE", "STRING_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
            "PLUS", "MINUS", "MULT", "DIV", "MOD", "EQUALS", "NOT_EQUALS", 
            "LESS", "LESS_EQUALS", "GREATER", "GREATER_EQUALS", "LOGICAL_AND", 
            "LOGICAL_OR", "LOGICAL_NOT", "COLON", "ASSIGN", "PLUS_ASSIGN", 
            "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DECLARE_ASSIGN", 
            "ACCESS", "L_PAREN", "R_PAREN", "L_CURLY", "R_CURLY", "L_BRACKET", 
            "R_BRACKET", "COMMA", "SEMI", "ID", "DECIMAL_LIT", "BINARY_LIT", 
            "OCTAL_LIT", "HEX_LIT", "FLOAT_LIT", "STRING_LIT", "TERMINATOR", 
            "WS", "LINE_COMMENT", "COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "FUNC", "IF", "BREAK", "ELSE", "FOR", "RETURN", "TYPE", 
                  "STRUCT", "INTERFACE", "CONST", "VAR", "CONTINUE", "RANGE", 
                  "NIL", "TRUE", "FALSE", "INT_TYPE", "STRING_TYPE", "FLOAT_TYPE", 
                  "BOOL_TYPE", "PLUS", "MINUS", "MULT", "DIV", "MOD", "EQUALS", 
                  "NOT_EQUALS", "LESS", "LESS_EQUALS", "GREATER", "GREATER_EQUALS", 
                  "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", "COLON", "ASSIGN", 
                  "PLUS_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "DECLARE_ASSIGN", "ACCESS", "L_PAREN", "R_PAREN", 
                  "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", "COMMA", 
                  "SEMI", "ID", "DECIMAL_LIT", "BINARY_LIT", "OCTAL_LIT", 
                  "HEX_LIT", "FLOAT_LIT", "STRING_LIT", "TERMINATOR", "WS", 
                  "LINE_COMMENT", "COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "LETTER", "DIGIT", "BIN_DIGIT", "OCTAL_DIGIT", 
                  "HEX_DIGIT", "EXP_LIT", "FRAC_LIT", "SQ", "DQ", "ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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
            


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.TERMINATOR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def TERMINATOR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

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

     


