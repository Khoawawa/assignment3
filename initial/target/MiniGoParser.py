# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u028c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00b7\n")
        buf.write("\3\3\4\3\4\3\4\5\4\u00bc\n\4\3\5\3\5\3\5\5\5\u00c1\n\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00ca\n\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00d5\n\7\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u00db\n\b\3\b\5\b\u00de\n\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u00e7\n\t\7\t\u00e9\n\t\f\t\16\t\u00ec\13\t")
        buf.write("\3\n\3\n\3\n\5\n\u00f1\n\n\3\13\3\13\3\13\5\13\u00f6\n")
        buf.write("\13\3\f\3\f\5\f\u00fa\n\f\3\r\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u010b")
        buf.write("\n\20\3\20\5\20\u010e\n\20\3\21\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\5\22\u0117\n\22\3\23\3\23\5\23\u011b\n\23\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\5\36\u0144\n\36\3\36\3\36\3")
        buf.write("\37\3\37\3\37\5\37\u014b\n\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \5 \u0154\n \3!\3!\3!\3\"\3\"\3#\3#\3#\5#\u015e\n#\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\5\'\u0171\n\'\3\'\3\'\5\'\u0175\n\'\3(\3(\3(\3(\5(\u017b")
        buf.write("\n(\3)\3)\3)\3)\3)\5)\u0182\n)\3*\3*\3*\5*\u0187\n*\3")
        buf.write("+\3+\3+\3+\5+\u018d\n+\3,\3,\5,\u0191\n,\3-\3-\3.\3.\3")
        buf.write("/\3/\3/\3/\3/\3/\5/\u019d\n/\3\60\3\60\3\60\5\60\u01a2")
        buf.write("\n\60\3\60\3\60\3\61\3\61\3\61\5\61\u01a9\n\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\5\62\u01b2\n\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\5\63\u01b9\n\63\3\64\3\64\3\64\3\64\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u01c7\n\66")
        buf.write("\3\67\3\67\3\67\38\38\38\58\u01cf\n8\39\39\39\39\39\3")
        buf.write(":\3:\3:\3:\3;\3;\3;\3;\5;\u01de\n;\3;\3;\3<\3<\3<\3<\3")
        buf.write("<\3=\3=\3=\5=\u01ea\n=\3>\3>\3>\3>\3>\3>\3>\5>\u01f3\n")
        buf.write(">\3?\3?\3?\3?\5?\u01f9\n?\3@\3@\3@\5@\u01fe\n@\3@\3@\3")
        buf.write("A\3A\3A\3A\3A\5A\u0207\nA\3B\3B\3B\3C\3C\3C\3C\3C\3D\3")
        buf.write("D\3D\3D\3D\3E\3E\3E\3E\3E\3E\3E\3E\3E\5E\u021f\nE\3F\3")
        buf.write("F\3F\3F\3G\3G\3G\3H\3H\3H\3H\5H\u022c\nH\3I\3I\3I\5I\u0231")
        buf.write("\nI\3I\3I\3J\3J\3K\3K\5K\u0239\nK\3L\3L\3L\3L\3L\3L\5")
        buf.write("L\u0241\nL\3M\3M\3N\3N\3N\3N\3N\3N\5N\u024b\nN\3O\3O\3")
        buf.write("O\3O\5O\u0251\nO\3O\3O\3O\3O\3O\3O\5O\u0259\nO\7O\u025b")
        buf.write("\nO\fO\16O\u025e\13O\3P\3P\3P\3P\3Q\3Q\3R\3R\3S\3S\3T")
        buf.write("\3T\3U\3U\3U\3U\3U\5U\u0271\nU\3U\3U\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\7U\u0285\nU\fU\16U\u0288")
        buf.write("\13U\3V\3V\3V\2\5\20\u009c\u00a8W\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write("\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a")
        buf.write("\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\2\t\3")
        buf.write("\2&,\3\2\23\26\3\2\67:\4\2\30\30$$\3\2\31\33\3\2\27\30")
        buf.write("\3\2\34!\2\u0284\2\u00ac\3\2\2\2\4\u00b6\3\2\2\2\6\u00bb")
        buf.write("\3\2\2\2\b\u00c0\3\2\2\2\n\u00c9\3\2\2\2\f\u00d4\3\2\2")
        buf.write("\2\16\u00dd\3\2\2\2\20\u00df\3\2\2\2\22\u00f0\3\2\2\2")
        buf.write("\24\u00f2\3\2\2\2\26\u00f9\3\2\2\2\30\u00fb\3\2\2\2\32")
        buf.write("\u00fe\3\2\2\2\34\u0100\3\2\2\2\36\u0102\3\2\2\2 \u010f")
        buf.write("\3\2\2\2\"\u0116\3\2\2\2$\u011a\3\2\2\2&\u011c\3\2\2\2")
        buf.write("(\u011e\3\2\2\2*\u0120\3\2\2\2,\u0126\3\2\2\2.\u012e\3")
        buf.write("\2\2\2\60\u0130\3\2\2\2\62\u0132\3\2\2\2\64\u0134\3\2")
        buf.write("\2\2\66\u0138\3\2\2\28\u013a\3\2\2\2:\u013e\3\2\2\2<\u0147")
        buf.write("\3\2\2\2>\u0153\3\2\2\2@\u0155\3\2\2\2B\u0158\3\2\2\2")
        buf.write("D\u015a\3\2\2\2F\u0161\3\2\2\2H\u0164\3\2\2\2J\u0168\3")
        buf.write("\2\2\2L\u016b\3\2\2\2N\u017a\3\2\2\2P\u0181\3\2\2\2R\u0186")
        buf.write("\3\2\2\2T\u018c\3\2\2\2V\u0190\3\2\2\2X\u0192\3\2\2\2")
        buf.write("Z\u0194\3\2\2\2\\\u019c\3\2\2\2^\u019e\3\2\2\2`\u01a5")
        buf.write("\3\2\2\2b\u01b1\3\2\2\2d\u01b8\3\2\2\2f\u01ba\3\2\2\2")
        buf.write("h\u01be\3\2\2\2j\u01c6\3\2\2\2l\u01c8\3\2\2\2n\u01cb\3")
        buf.write("\2\2\2p\u01d0\3\2\2\2r\u01d5\3\2\2\2t\u01d9\3\2\2\2v\u01e1")
        buf.write("\3\2\2\2x\u01e9\3\2\2\2z\u01f2\3\2\2\2|\u01f4\3\2\2\2")
        buf.write("~\u01fa\3\2\2\2\u0080\u0206\3\2\2\2\u0082\u0208\3\2\2")
        buf.write("\2\u0084\u020b\3\2\2\2\u0086\u0210\3\2\2\2\u0088\u021e")
        buf.write("\3\2\2\2\u008a\u0220\3\2\2\2\u008c\u0224\3\2\2\2\u008e")
        buf.write("\u022b\3\2\2\2\u0090\u022d\3\2\2\2\u0092\u0234\3\2\2\2")
        buf.write("\u0094\u0238\3\2\2\2\u0096\u0240\3\2\2\2\u0098\u0242\3")
        buf.write("\2\2\2\u009a\u024a\3\2\2\2\u009c\u0250\3\2\2\2\u009e\u025f")
        buf.write("\3\2\2\2\u00a0\u0263\3\2\2\2\u00a2\u0265\3\2\2\2\u00a4")
        buf.write("\u0267\3\2\2\2\u00a6\u0269\3\2\2\2\u00a8\u0270\3\2\2\2")
        buf.write("\u00aa\u0289\3\2\2\2\u00ac\u00ad\5\4\3\2\u00ad\u00ae\7")
        buf.write("\2\2\3\u00ae\3\3\2\2\2\u00af\u00b0\5\6\4\2\u00b0\u00b1")
        buf.write("\5\u00aaV\2\u00b1\u00b2\5\4\3\2\u00b2\u00b7\3\2\2\2\u00b3")
        buf.write("\u00b4\5\6\4\2\u00b4\u00b5\5\u00aaV\2\u00b5\u00b7\3\2")
        buf.write("\2\2\u00b6\u00af\3\2\2\2\u00b6\u00b3\3\2\2\2\u00b7\5\3")
        buf.write("\2\2\2\u00b8\u00bc\5:\36\2\u00b9\u00bc\5r:\2\u00ba\u00bc")
        buf.write("\5\b\5\2\u00bb\u00b8\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bc\7\3\2\2\2\u00bd\u00c1\5J&\2\u00be")
        buf.write("\u00c1\5F$\2\u00bf\u00c1\5l\67\2\u00c0\u00bd\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\t\3\2\2\2\u00c2")
        buf.write("\u00c3\5\f\7\2\u00c3\u00c4\5\u00aaV\2\u00c4\u00c5\5\n")
        buf.write("\6\2\u00c5\u00ca\3\2\2\2\u00c6\u00c7\5\f\7\2\u00c7\u00c8")
        buf.write("\5\u00aaV\2\u00c8\u00ca\3\2\2\2\u00c9\u00c2\3\2\2\2\u00c9")
        buf.write("\u00c6\3\2\2\2\u00ca\13\3\2\2\2\u00cb\u00d5\5J&\2\u00cc")
        buf.write("\u00d5\5F$\2\u00cd\u00d5\5\36\20\2\u00ce\u00d5\5 \21\2")
        buf.write("\u00cf\u00d5\5\64\33\2\u00d0\u00d5\5\34\17\2\u00d1\u00d5")
        buf.write("\5\32\16\2\u00d2\u00d5\5\26\f\2\u00d3\u00d5\5\24\13\2")
        buf.write("\u00d4\u00cb\3\2\2\2\u00d4\u00cc\3\2\2\2\u00d4\u00cd\3")
        buf.write("\2\2\2\u00d4\u00ce\3\2\2\2\u00d4\u00cf\3\2\2\2\u00d4\u00d0")
        buf.write("\3\2\2\2\u00d4\u00d1\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d3\3\2\2\2\u00d5\r\3\2\2\2\u00d6\u00da\5\20\t\2\u00d7")
        buf.write("\u00d8\7-\2\2\u00d8\u00db\7\66\2\2\u00d9\u00db\5\u009e")
        buf.write("P\2\u00da\u00d7\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\u00de")
        buf.write("\3\2\2\2\u00dc\u00de\7\66\2\2\u00dd\u00d6\3\2\2\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00de\17\3\2\2\2\u00df\u00e0\b\t\1\2\u00e0")
        buf.write("\u00e1\5\22\n\2\u00e1\u00ea\3\2\2\2\u00e2\u00e6\f\3\2")
        buf.write("\2\u00e3\u00e4\7-\2\2\u00e4\u00e7\7\66\2\2\u00e5\u00e7")
        buf.write("\5\u009eP\2\u00e6\u00e3\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7")
        buf.write("\u00e9\3\2\2\2\u00e8\u00e2\3\2\2\2\u00e9\u00ec\3\2\2\2")
        buf.write("\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\21\3\2")
        buf.write("\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00f1\7\66\2\2\u00ee\u00f1")
        buf.write("\5\30\r\2\u00ef\u00f1\5\u0084C\2\u00f0\u00ed\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\23\3\2\2\2\u00f2")
        buf.write("\u00f5\7\b\2\2\u00f3\u00f6\5\u00a8U\2\u00f4\u00f6\3\2")
        buf.write("\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6\25")
        buf.write("\3\2\2\2\u00f7\u00fa\5\30\r\2\u00f8\u00fa\5\u0084C\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\27\3\2\2\2\u00fb")
        buf.write("\u00fc\7\66\2\2\u00fc\u00fd\5D#\2\u00fd\31\3\2\2\2\u00fe")
        buf.write("\u00ff\7\16\2\2\u00ff\33\3\2\2\2\u0100\u0101\7\5\2\2\u0101")
        buf.write("\35\3\2\2\2\u0102\u0103\7\4\2\2\u0103\u0104\7.\2\2\u0104")
        buf.write("\u0105\5\u00a8U\2\u0105\u0106\7/\2\2\u0106\u010d\58\35")
        buf.write("\2\u0107\u010a\7\6\2\2\u0108\u010b\5\36\20\2\u0109\u010b")
        buf.write("\58\35\2\u010a\u0108\3\2\2\2\u010a\u0109\3\2\2\2\u010b")
        buf.write("\u010e\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u0107\3\2\2\2")
        buf.write("\u010d\u010c\3\2\2\2\u010e\37\3\2\2\2\u010f\u0110\7\7")
        buf.write("\2\2\u0110\u0111\5\"\22\2\u0111\u0112\58\35\2\u0112!\3")
        buf.write("\2\2\2\u0113\u0117\5\u00a8U\2\u0114\u0117\5*\26\2\u0115")
        buf.write("\u0117\5,\27\2\u0116\u0113\3\2\2\2\u0116\u0114\3\2\2\2")
        buf.write("\u0116\u0115\3\2\2\2\u0117#\3\2\2\2\u0118\u011b\5\64\33")
        buf.write("\2\u0119\u011b\5J&\2\u011a\u0118\3\2\2\2\u011a\u0119\3")
        buf.write("\2\2\2\u011b%\3\2\2\2\u011c\u011d\5\u00a8U\2\u011d\'\3")
        buf.write("\2\2\2\u011e\u011f\5\64\33\2\u011f)\3\2\2\2\u0120\u0121")
        buf.write("\5$\23\2\u0121\u0122\5\u00aaV\2\u0122\u0123\5&\24\2\u0123")
        buf.write("\u0124\5\u00aaV\2\u0124\u0125\5(\25\2\u0125+\3\2\2\2\u0126")
        buf.write("\u0127\5.\30\2\u0127\u0128\7\64\2\2\u0128\u0129\5\60\31")
        buf.write("\2\u0129\u012a\3\2\2\2\u012a\u012b\7,\2\2\u012b\u012c")
        buf.write("\7\17\2\2\u012c\u012d\5\u00a8U\2\u012d-\3\2\2\2\u012e")
        buf.write("\u012f\7\66\2\2\u012f/\3\2\2\2\u0130\u0131\7\66\2\2\u0131")
        buf.write("\61\3\2\2\2\u0132\u0133\5\u00a8U\2\u0133\63\3\2\2\2\u0134")
        buf.write("\u0135\5\16\b\2\u0135\u0136\5\66\34\2\u0136\u0137\5\u00a8")
        buf.write("U\2\u0137\65\3\2\2\2\u0138\u0139\t\2\2\2\u0139\67\3\2")
        buf.write("\2\2\u013a\u013b\7\60\2\2\u013b\u013c\5\n\6\2\u013c\u013d")
        buf.write("\7\61\2\2\u013d9\3\2\2\2\u013e\u013f\7\3\2\2\u013f\u0140")
        buf.write("\7\66\2\2\u0140\u0143\5<\37\2\u0141\u0144\5B\"\2\u0142")
        buf.write("\u0144\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0142\3\2\2\2")
        buf.write("\u0144\u0145\3\2\2\2\u0145\u0146\58\35\2\u0146;\3\2\2")
        buf.write("\2\u0147\u014a\7.\2\2\u0148\u014b\5> \2\u0149\u014b\3")
        buf.write("\2\2\2\u014a\u0148\3\2\2\2\u014a\u0149\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014c\u014d\7/\2\2\u014d=\3\2\2\2\u014e\u014f")
        buf.write("\5@!\2\u014f\u0150\7\64\2\2\u0150\u0151\5> \2\u0151\u0154")
        buf.write("\3\2\2\2\u0152\u0154\5@!\2\u0153\u014e\3\2\2\2\u0153\u0152")
        buf.write("\3\2\2\2\u0154?\3\2\2\2\u0155\u0156\5N(\2\u0156\u0157")
        buf.write("\5R*\2\u0157A\3\2\2\2\u0158\u0159\5R*\2\u0159C\3\2\2\2")
        buf.write("\u015a\u015d\7.\2\2\u015b\u015e\5P)\2\u015c\u015e\3\2")
        buf.write("\2\2\u015d\u015b\3\2\2\2\u015d\u015c\3\2\2\2\u015e\u015f")
        buf.write("\3\2\2\2\u015f\u0160\7/\2\2\u0160E\3\2\2\2\u0161\u0162")
        buf.write("\7\f\2\2\u0162\u0163\5H%\2\u0163G\3\2\2\2\u0164\u0165")
        buf.write("\7\66\2\2\u0165\u0166\7&\2\2\u0166\u0167\5\u00a8U\2\u0167")
        buf.write("I\3\2\2\2\u0168\u0169\7\r\2\2\u0169\u016a\5L\'\2\u016a")
        buf.write("K\3\2\2\2\u016b\u0174\7\66\2\2\u016c\u0170\5R*\2\u016d")
        buf.write("\u016e\7&\2\2\u016e\u0171\5\u00a8U\2\u016f\u0171\3\2\2")
        buf.write("\2\u0170\u016d\3\2\2\2\u0170\u016f\3\2\2\2\u0171\u0175")
        buf.write("\3\2\2\2\u0172\u0173\7&\2\2\u0173\u0175\5\u00a8U\2\u0174")
        buf.write("\u016c\3\2\2\2\u0174\u0172\3\2\2\2\u0175M\3\2\2\2\u0176")
        buf.write("\u0177\7\66\2\2\u0177\u0178\7\64\2\2\u0178\u017b\5N(\2")
        buf.write("\u0179\u017b\7\66\2\2\u017a\u0176\3\2\2\2\u017a\u0179")
        buf.write("\3\2\2\2\u017bO\3\2\2\2\u017c\u017d\5\u00a8U\2\u017d\u017e")
        buf.write("\7\64\2\2\u017e\u017f\5P)\2\u017f\u0182\3\2\2\2\u0180")
        buf.write("\u0182\5\u00a8U\2\u0181\u017c\3\2\2\2\u0181\u0180\3\2")
        buf.write("\2\2\u0182Q\3\2\2\2\u0183\u0187\5\u0092J\2\u0184\u0187")
        buf.write("\5T+\2\u0185\u0187\7\66\2\2\u0186\u0183\3\2\2\2\u0186")
        buf.write("\u0184\3\2\2\2\u0186\u0185\3\2\2\2\u0187S\3\2\2\2\u0188")
        buf.write("\u018d\5\u008cG\2\u0189\u018d\5\u0086D\2\u018a\u018d\5")
        buf.write("p9\2\u018b\u018d\5\u008aF\2\u018c\u0188\3\2\2\2\u018c")
        buf.write("\u0189\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018b\3\2\2\2")
        buf.write("\u018dU\3\2\2\2\u018e\u0191\5\u0086D\2\u018f\u0191\5Z")
        buf.write(".\2\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191W\3\2")
        buf.write("\2\2\u0192\u0193\5\u008cG\2\u0193Y\3\2\2\2\u0194\u0195")
        buf.write("\7\66\2\2\u0195[\3\2\2\2\u0196\u0197\5V,\2\u0197\u0198")
        buf.write("\5`\61\2\u0198\u019d\3\2\2\2\u0199\u019a\5X-\2\u019a\u019b")
        buf.write("\5^\60\2\u019b\u019d\3\2\2\2\u019c\u0196\3\2\2\2\u019c")
        buf.write("\u0199\3\2\2\2\u019d]\3\2\2\2\u019e\u01a1\7\60\2\2\u019f")
        buf.write("\u01a2\5d\63\2\u01a0\u01a2\3\2\2\2\u01a1\u019f\3\2\2\2")
        buf.write("\u01a1\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\7")
        buf.write("\61\2\2\u01a4_\3\2\2\2\u01a5\u01a8\7\60\2\2\u01a6\u01a9")
        buf.write("\5b\62\2\u01a7\u01a9\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\7\61\2")
        buf.write("\2\u01aba\3\2\2\2\u01ac\u01ad\5f\64\2\u01ad\u01ae\7\64")
        buf.write("\2\2\u01ae\u01af\5b\62\2\u01af\u01b2\3\2\2\2\u01b0\u01b2")
        buf.write("\5f\64\2\u01b1\u01ac\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write("c\3\2\2\2\u01b3\u01b4\5j\66\2\u01b4\u01b5\7\64\2\2\u01b5")
        buf.write("\u01b6\5d\63\2\u01b6\u01b9\3\2\2\2\u01b7\u01b9\5j\66\2")
        buf.write("\u01b8\u01b3\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9e\3\2\2")
        buf.write("\2\u01ba\u01bb\5h\65\2\u01bb\u01bc\7%\2\2\u01bc\u01bd")
        buf.write("\5\u00a8U\2\u01bdg\3\2\2\2\u01be\u01bf\7\66\2\2\u01bf")
        buf.write("i\3\2\2\2\u01c0\u01c7\5\u0096L\2\u01c1\u01c2\5V,\2\u01c2")
        buf.write("\u01c3\5`\61\2\u01c3\u01c7\3\2\2\2\u01c4\u01c7\7\66\2")
        buf.write("\2\u01c5\u01c7\5^\60\2\u01c6\u01c0\3\2\2\2\u01c6\u01c1")
        buf.write("\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7")
        buf.write("k\3\2\2\2\u01c8\u01c9\7\t\2\2\u01c9\u01ca\5n8\2\u01ca")
        buf.write("m\3\2\2\2\u01cb\u01ce\7\66\2\2\u01cc\u01cf\5\u0086D\2")
        buf.write("\u01cd\u01cf\5p9\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2")
        buf.write("\2\2\u01cfo\3\2\2\2\u01d0\u01d1\7\13\2\2\u01d1\u01d2\7")
        buf.write("\60\2\2\u01d2\u01d3\5z>\2\u01d3\u01d4\7\61\2\2\u01d4q")
        buf.write("\3\2\2\2\u01d5\u01d6\7\3\2\2\u01d6\u01d7\5v<\2\u01d7\u01d8")
        buf.write("\5t;\2\u01d8s\3\2\2\2\u01d9\u01da\7\66\2\2\u01da\u01dd")
        buf.write("\5<\37\2\u01db\u01de\5B\"\2\u01dc\u01de\3\2\2\2\u01dd")
        buf.write("\u01db\3\2\2\2\u01dd\u01dc\3\2\2\2\u01de\u01df\3\2\2\2")
        buf.write("\u01df\u01e0\58\35\2\u01e0u\3\2\2\2\u01e1\u01e2\7.\2\2")
        buf.write("\u01e2\u01e3\7\66\2\2\u01e3\u01e4\5x=\2\u01e4\u01e5\7")
        buf.write("/\2\2\u01e5w\3\2\2\2\u01e6\u01ea\7\66\2\2\u01e7\u01ea")
        buf.write("\5\u0086D\2\u01e8\u01ea\5p9\2\u01e9\u01e6\3\2\2\2\u01e9")
        buf.write("\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2\u01eay\3\2\2\2\u01eb")
        buf.write("\u01ec\5|?\2\u01ec\u01ed\5\u00aaV\2\u01ed\u01ee\5z>\2")
        buf.write("\u01ee\u01f3\3\2\2\2\u01ef\u01f0\5|?\2\u01f0\u01f1\5\u00aa")
        buf.write("V\2\u01f1\u01f3\3\2\2\2\u01f2\u01eb\3\2\2\2\u01f2\u01ef")
        buf.write("\3\2\2\2\u01f3{\3\2\2\2\u01f4\u01f5\7\66\2\2\u01f5\u01f8")
        buf.write("\5~@\2\u01f6\u01f9\5B\"\2\u01f7\u01f9\3\2\2\2\u01f8\u01f6")
        buf.write("\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9}\3\2\2\2\u01fa\u01fd")
        buf.write("\7.\2\2\u01fb\u01fe\5\u0080A\2\u01fc\u01fe\3\2\2\2\u01fd")
        buf.write("\u01fb\3\2\2\2\u01fd\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2")
        buf.write("\u01ff\u0200\7/\2\2\u0200\177\3\2\2\2\u0201\u0202\5\u0082")
        buf.write("B\2\u0202\u0203\7\64\2\2\u0203\u0204\5\u0080A\2\u0204")
        buf.write("\u0207\3\2\2\2\u0205\u0207\5\u0082B\2\u0206\u0201\3\2")
        buf.write("\2\2\u0206\u0205\3\2\2\2\u0207\u0081\3\2\2\2\u0208\u0209")
        buf.write("\5N(\2\u0209\u020a\5R*\2\u020a\u0083\3\2\2\2\u020b\u020c")
        buf.write("\5\u00a8U\2\u020c\u020d\7-\2\2\u020d\u020e\7\66\2\2\u020e")
        buf.write("\u020f\5D#\2\u020f\u0085\3\2\2\2\u0210\u0211\7\n\2\2\u0211")
        buf.write("\u0212\7\60\2\2\u0212\u0213\5\u0088E\2\u0213\u0214\7\61")
        buf.write("\2\2\u0214\u0087\3\2\2\2\u0215\u0216\7\66\2\2\u0216\u0217")
        buf.write("\5R*\2\u0217\u0218\5\u00aaV\2\u0218\u0219\5\u0088E\2\u0219")
        buf.write("\u021f\3\2\2\2\u021a\u021b\7\66\2\2\u021b\u021c\5R*\2")
        buf.write("\u021c\u021d\5\u00aaV\2\u021d\u021f\3\2\2\2\u021e\u0215")
        buf.write("\3\2\2\2\u021e\u021a\3\2\2\2\u021f\u0089\3\2\2\2\u0220")
        buf.write("\u0221\7\62\2\2\u0221\u0222\7\63\2\2\u0222\u0223\5R*\2")
        buf.write("\u0223\u008b\3\2\2\2\u0224\u0225\5\u008eH\2\u0225\u0226")
        buf.write("\5R*\2\u0226\u008d\3\2\2\2\u0227\u0228\5\u0090I\2\u0228")
        buf.write("\u0229\5\u008eH\2\u0229\u022c\3\2\2\2\u022a\u022c\5\u0090")
        buf.write("I\2\u022b\u0227\3\2\2\2\u022b\u022a\3\2\2\2\u022c\u008f")
        buf.write("\3\2\2\2\u022d\u0230\7\62\2\2\u022e\u0231\5\u0098M\2\u022f")
        buf.write("\u0231\7\66\2\2\u0230\u022e\3\2\2\2\u0230\u022f\3\2\2")
        buf.write("\2\u0231\u0232\3\2\2\2\u0232\u0233\7\63\2\2\u0233\u0091")
        buf.write("\3\2\2\2\u0234\u0235\t\3\2\2\u0235\u0093\3\2\2\2\u0236")
        buf.write("\u0239\5\u0096L\2\u0237\u0239\5\\/\2\u0238\u0236\3\2\2")
        buf.write("\2\u0238\u0237\3\2\2\2\u0239\u0095\3\2\2\2\u023a\u0241")
        buf.write("\5\u0098M\2\u023b\u0241\7<\2\2\u023c\u0241\7\20\2\2\u023d")
        buf.write("\u0241\7;\2\2\u023e\u0241\7\21\2\2\u023f\u0241\7\22\2")
        buf.write("\2\u0240\u023a\3\2\2\2\u0240\u023b\3\2\2\2\u0240\u023c")
        buf.write("\3\2\2\2\u0240\u023d\3\2\2\2\u0240\u023e\3\2\2\2\u0240")
        buf.write("\u023f\3\2\2\2\u0241\u0097\3\2\2\2\u0242\u0243\t\4\2\2")
        buf.write("\u0243\u0099\3\2\2\2\u0244\u024b\7\66\2\2\u0245\u0246")
        buf.write("\7.\2\2\u0246\u0247\5\u00a8U\2\u0247\u0248\7/\2\2\u0248")
        buf.write("\u024b\3\2\2\2\u0249\u024b\5\u0094K\2\u024a\u0244\3\2")
        buf.write("\2\2\u024a\u0245\3\2\2\2\u024a\u0249\3\2\2\2\u024b\u009b")
        buf.write("\3\2\2\2\u024c\u024d\bO\1\2\u024d\u0251\5\u009aN\2\u024e")
        buf.write("\u024f\7\66\2\2\u024f\u0251\5D#\2\u0250\u024c\3\2\2\2")
        buf.write("\u0250\u024e\3\2\2\2\u0251\u025c\3\2\2\2\u0252\u0258\f")
        buf.write("\4\2\2\u0253\u0254\7-\2\2\u0254\u0259\7\66\2\2\u0255\u0259")
        buf.write("\5\u009eP\2\u0256\u0257\7-\2\2\u0257\u0259\5\30\r\2\u0258")
        buf.write("\u0253\3\2\2\2\u0258\u0255\3\2\2\2\u0258\u0256\3\2\2\2")
        buf.write("\u0259\u025b\3\2\2\2\u025a\u0252\3\2\2\2\u025b\u025e\3")
        buf.write("\2\2\2\u025c\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u009d")
        buf.write("\3\2\2\2\u025e\u025c\3\2\2\2\u025f\u0260\7\62\2\2\u0260")
        buf.write("\u0261\5\u00a8U\2\u0261\u0262\7\63\2\2\u0262\u009f\3\2")
        buf.write("\2\2\u0263\u0264\t\5\2\2\u0264\u00a1\3\2\2\2\u0265\u0266")
        buf.write("\t\6\2\2\u0266\u00a3\3\2\2\2\u0267\u0268\t\7\2\2\u0268")
        buf.write("\u00a5\3\2\2\2\u0269\u026a\t\b\2\2\u026a\u00a7\3\2\2\2")
        buf.write("\u026b\u026c\bU\1\2\u026c\u0271\5\u009cO\2\u026d\u026e")
        buf.write("\5\u00a0Q\2\u026e\u026f\5\u00a8U\b\u026f\u0271\3\2\2\2")
        buf.write("\u0270\u026b\3\2\2\2\u0270\u026d\3\2\2\2\u0271\u0286\3")
        buf.write("\2\2\2\u0272\u0273\f\7\2\2\u0273\u0274\5\u00a2R\2\u0274")
        buf.write("\u0275\5\u00a8U\b\u0275\u0285\3\2\2\2\u0276\u0277\f\6")
        buf.write("\2\2\u0277\u0278\5\u00a4S\2\u0278\u0279\5\u00a8U\7\u0279")
        buf.write("\u0285\3\2\2\2\u027a\u027b\f\5\2\2\u027b\u027c\5\u00a6")
        buf.write("T\2\u027c\u027d\5\u00a8U\6\u027d\u0285\3\2\2\2\u027e\u027f")
        buf.write("\f\4\2\2\u027f\u0280\7\"\2\2\u0280\u0285\5\u00a8U\5\u0281")
        buf.write("\u0282\f\3\2\2\u0282\u0283\7#\2\2\u0283\u0285\5\u00a8")
        buf.write("U\4\u0284\u0272\3\2\2\2\u0284\u0276\3\2\2\2\u0284\u027a")
        buf.write("\3\2\2\2\u0284\u027e\3\2\2\2\u0284\u0281\3\2\2\2\u0285")
        buf.write("\u0288\3\2\2\2\u0286\u0284\3\2\2\2\u0286\u0287\3\2\2\2")
        buf.write("\u0287\u00a9\3\2\2\2\u0288\u0286\3\2\2\2\u0289\u028a\7")
        buf.write("\65\2\2\u028a\u00ab\3\2\2\2\66\u00b6\u00bb\u00c0\u00c9")
        buf.write("\u00d4\u00da\u00dd\u00e6\u00ea\u00f0\u00f5\u00f9\u010a")
        buf.write("\u010d\u0116\u011a\u0143\u014a\u0153\u015d\u0170\u0174")
        buf.write("\u017a\u0181\u0186\u018c\u0190\u019c\u01a1\u01a8\u01b1")
        buf.write("\u01b8\u01c6\u01ce\u01dd\u01e9\u01f2\u01f8\u01fd\u0206")
        buf.write("\u021e\u022b\u0230\u0238\u0240\u024a\u0250\u0258\u025c")
        buf.write("\u0270\u0284\u0286")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "'if'", "'break'", "'else'", 
                     "'for'", "'return'", "'type'", "'struct'", "'interface'", 
                     "'const'", "'var'", "'continue'", "'range'", "'nil'", 
                     "'true'", "'false'", "'int'", "'string'", "'float'", 
                     "'boolean'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "':'", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "':='", "'.'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "FUNC", "IF", "BREAK", "ELSE", "FOR", 
                      "RETURN", "TYPE", "STRUCT", "INTERFACE", "CONST", 
                      "VAR", "CONTINUE", "RANGE", "NIL", "TRUE", "FALSE", 
                      "INT_TYPE", "STRING_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
                      "PLUS", "MINUS", "MULT", "DIV", "MOD", "EQUALS", "NOT_EQUALS", 
                      "LESS", "LESS_EQUALS", "GREATER", "GREATER_EQUALS", 
                      "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", "COLON", 
                      "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "DECLARE_ASSIGN", "ACCESS", 
                      "L_PAREN", "R_PAREN", "L_CURLY", "R_CURLY", "L_BRACKET", 
                      "R_BRACKET", "COMMA", "SEMI", "ID", "DECIMAL_LIT", 
                      "BINARY_LIT", "OCTAL_LIT", "HEX_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "TERMINATOR", "WS", "LINE_COMMENT", 
                      "COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_top_level_decl = 2
    RULE_decl = 3
    RULE_stmt_list = 4
    RULE_stmt = 5
    RULE_lhs = 6
    RULE_lhs_prime = 7
    RULE_lhs_ele = 8
    RULE_return_stmt = 9
    RULE_call_stmt = 10
    RULE_func_call = 11
    RULE_continue_stmt = 12
    RULE_break_stmt = 13
    RULE_if_stmt = 14
    RULE_for_stmt = 15
    RULE_for_clause = 16
    RULE_init_stmt = 17
    RULE_cond_stmt = 18
    RULE_update_stmt = 19
    RULE_for_ICU_clause = 20
    RULE_for_range_clause = 21
    RULE_for_idx = 22
    RULE_for_val = 23
    RULE_for_array = 24
    RULE_assignment = 25
    RULE_assign_op = 26
    RULE_block = 27
    RULE_funcdecl = 28
    RULE_func_params = 29
    RULE_func_params_list = 30
    RULE_func_param = 31
    RULE_return_type = 32
    RULE_expr_params = 33
    RULE_constdecl = 34
    RULE_const_spec = 35
    RULE_vardecl = 36
    RULE_var_spec = 37
    RULE_id_list = 38
    RULE_expr_list = 39
    RULE_type_ = 40
    RULE_type_lit = 41
    RULE_complex_type = 42
    RULE_list_type = 43
    RULE_type_name = 44
    RULE_complex_lit = 45
    RULE_list_val = 46
    RULE_complex_val = 47
    RULE_key_element_list = 48
    RULE_element_list = 49
    RULE_keyed_element = 50
    RULE_field_name = 51
    RULE_element = 52
    RULE_type_decl = 53
    RULE_type_spec = 54
    RULE_interface_type = 55
    RULE_method_decl = 56
    RULE_method_spec = 57
    RULE_receiver = 58
    RULE_method_type = 59
    RULE_method_list = 60
    RULE_method = 61
    RULE_method_params = 62
    RULE_method_param_prime = 63
    RULE_method_param = 64
    RULE_method_call = 65
    RULE_struct_type = 66
    RULE_field_prime = 67
    RULE_slice_type = 68
    RULE_array_type = 69
    RULE_array_decl = 70
    RULE_array_len = 71
    RULE_single_type = 72
    RULE_literal = 73
    RULE_primitive_lit = 74
    RULE_integer = 75
    RULE_operand = 76
    RULE_primary_expr = 77
    RULE_index = 78
    RULE_unary_op = 79
    RULE_mul_op = 80
    RULE_add_op = 81
    RULE_compare_op = 82
    RULE_expr = 83
    RULE_eos = 84

    ruleNames =  [ "program", "decl_list", "top_level_decl", "decl", "stmt_list", 
                   "stmt", "lhs", "lhs_prime", "lhs_ele", "return_stmt", 
                   "call_stmt", "func_call", "continue_stmt", "break_stmt", 
                   "if_stmt", "for_stmt", "for_clause", "init_stmt", "cond_stmt", 
                   "update_stmt", "for_ICU_clause", "for_range_clause", 
                   "for_idx", "for_val", "for_array", "assignment", "assign_op", 
                   "block", "funcdecl", "func_params", "func_params_list", 
                   "func_param", "return_type", "expr_params", "constdecl", 
                   "const_spec", "vardecl", "var_spec", "id_list", "expr_list", 
                   "type_", "type_lit", "complex_type", "list_type", "type_name", 
                   "complex_lit", "list_val", "complex_val", "key_element_list", 
                   "element_list", "keyed_element", "field_name", "element", 
                   "type_decl", "type_spec", "interface_type", "method_decl", 
                   "method_spec", "receiver", "method_type", "method_list", 
                   "method", "method_params", "method_param_prime", "method_param", 
                   "method_call", "struct_type", "field_prime", "slice_type", 
                   "array_type", "array_decl", "array_len", "single_type", 
                   "literal", "primitive_lit", "integer", "operand", "primary_expr", 
                   "index", "unary_op", "mul_op", "add_op", "compare_op", 
                   "expr", "eos" ]

    EOF = Token.EOF
    FUNC=1
    IF=2
    BREAK=3
    ELSE=4
    FOR=5
    RETURN=6
    TYPE=7
    STRUCT=8
    INTERFACE=9
    CONST=10
    VAR=11
    CONTINUE=12
    RANGE=13
    NIL=14
    TRUE=15
    FALSE=16
    INT_TYPE=17
    STRING_TYPE=18
    FLOAT_TYPE=19
    BOOL_TYPE=20
    PLUS=21
    MINUS=22
    MULT=23
    DIV=24
    MOD=25
    EQUALS=26
    NOT_EQUALS=27
    LESS=28
    LESS_EQUALS=29
    GREATER=30
    GREATER_EQUALS=31
    LOGICAL_AND=32
    LOGICAL_OR=33
    LOGICAL_NOT=34
    COLON=35
    ASSIGN=36
    PLUS_ASSIGN=37
    MINUS_ASSIGN=38
    MULT_ASSIGN=39
    DIV_ASSIGN=40
    MOD_ASSIGN=41
    DECLARE_ASSIGN=42
    ACCESS=43
    L_PAREN=44
    R_PAREN=45
    L_CURLY=46
    R_CURLY=47
    L_BRACKET=48
    R_BRACKET=49
    COMMA=50
    SEMI=51
    ID=52
    DECIMAL_LIT=53
    BINARY_LIT=54
    OCTAL_LIT=55
    HEX_LIT=56
    FLOAT_LIT=57
    STRING_LIT=58
    TERMINATOR=59
    WS=60
    LINE_COMMENT=61
    COMMENT=62
    ERROR_CHAR=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.decl_list()
            self.state = 171
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def top_level_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Top_level_declContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = MiniGoParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.top_level_decl()
                self.state = 174
                self.eos()
                self.state = 175
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.top_level_decl()
                self.state = 178
                self.eos()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Top_level_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_top_level_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTop_level_decl" ):
                return visitor.visitTop_level_decl(self)
            else:
                return visitor.visitChildren(self)




    def top_level_decl(self):

        localctx = MiniGoParser.Top_level_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_top_level_decl)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.funcdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.method_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def type_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Type_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.vardecl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.constdecl()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.type_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = MiniGoParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt_list)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.stmt()
                self.state = 193
                self.eos()
                self.state = 194
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.stmt()
                self.state = 197
                self.eos()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.constdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
                self.assignment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 206
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 207
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 208
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 209
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_primeContext,0)


        def ACCESS(self):
            return self.getToken(MiniGoParser.ACCESS, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lhs)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.lhs_prime(0)
                self.state = 216
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ACCESS]:
                    self.state = 213
                    self.match(MiniGoParser.ACCESS)
                    self.state = 214
                    self.match(MiniGoParser.ID)
                    pass
                elif token in [MiniGoParser.L_BRACKET]:
                    self.state = 215
                    self.index()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs_ele(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_eleContext,0)


        def lhs_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_primeContext,0)


        def ACCESS(self):
            return self.getToken(MiniGoParser.ACCESS, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_prime" ):
                return visitor.visitLhs_prime(self)
            else:
                return visitor.visitChildren(self)



    def lhs_prime(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Lhs_primeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_lhs_prime, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.lhs_ele()
            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Lhs_primeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs_prime)
                    self.state = 224
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 228
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.ACCESS]:
                        self.state = 225
                        self.match(MiniGoParser.ACCESS)
                        self.state = 226
                        self.match(MiniGoParser.ID)
                        pass
                    elif token in [MiniGoParser.L_BRACKET]:
                        self.state = 227
                        self.index()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Lhs_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_ele" ):
                return visitor.visitLhs_ele(self)
            else:
                return visitor.visitChildren(self)




    def lhs_ele(self):

        localctx = MiniGoParser.Lhs_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lhs_ele)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.method_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(MiniGoParser.RETURN)
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT, MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.LOGICAL_NOT, MiniGoParser.L_PAREN, MiniGoParser.L_BRACKET, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 241
                self.expr(0)
                pass
            elif token in [MiniGoParser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_call_stmt)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.method_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr_params(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_paramsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(MiniGoParser.ID)
            self.state = 250
            self.expr_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(MiniGoParser.IF)
            self.state = 257
            self.match(MiniGoParser.L_PAREN)
            self.state = 258
            self.expr(0)
            self.state = 259
            self.match(MiniGoParser.R_PAREN)
            self.state = 260
            self.block()
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.state = 261
                self.match(MiniGoParser.ELSE)
                self.state = 264
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF]:
                    self.state = 262
                    self.if_stmt()
                    pass
                elif token in [MiniGoParser.L_CURLY]:
                    self.state = 263
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MiniGoParser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def for_clause(self):
            return self.getTypedRuleContext(MiniGoParser.For_clauseContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(MiniGoParser.FOR)
            self.state = 270
            self.for_clause()
            self.state = 271
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def for_ICU_clause(self):
            return self.getTypedRuleContext(MiniGoParser.For_ICU_clauseContext,0)


        def for_range_clause(self):
            return self.getTypedRuleContext(MiniGoParser.For_range_clauseContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_clause" ):
                return visitor.visitFor_clause(self)
            else:
                return visitor.visitChildren(self)




    def for_clause(self):

        localctx = MiniGoParser.For_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_for_clause)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.for_ICU_clause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.for_range_clause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_stmt" ):
                return visitor.visitInit_stmt(self)
            else:
                return visitor.visitChildren(self)




    def init_stmt(self):

        localctx = MiniGoParser.Init_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_init_stmt)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT, MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.LOGICAL_NOT, MiniGoParser.L_PAREN, MiniGoParser.L_BRACKET, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.assignment()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_cond_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond_stmt" ):
                return visitor.visitCond_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cond_stmt(self):

        localctx = MiniGoParser.Cond_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cond_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_stmt" ):
                return visitor.visitUpdate_stmt(self)
            else:
                return visitor.visitChildren(self)




    def update_stmt(self):

        localctx = MiniGoParser.Update_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_update_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_ICU_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Init_stmtContext,0)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.EosContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.EosContext,i)


        def cond_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Cond_stmtContext,0)


        def update_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Update_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_ICU_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_ICU_clause" ):
                return visitor.visitFor_ICU_clause(self)
            else:
                return visitor.visitChildren(self)




    def for_ICU_clause(self):

        localctx = MiniGoParser.For_ICU_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_for_ICU_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.init_stmt()
            self.state = 287
            self.eos()
            self.state = 288
            self.cond_stmt()
            self.state = 289
            self.eos()
            self.state = 290
            self.update_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_range_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def for_idx(self):
            return self.getTypedRuleContext(MiniGoParser.For_idxContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def for_val(self):
            return self.getTypedRuleContext(MiniGoParser.For_valContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_range_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_range_clause" ):
                return visitor.visitFor_range_clause(self)
            else:
                return visitor.visitChildren(self)




    def for_range_clause(self):

        localctx = MiniGoParser.For_range_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_for_range_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.for_idx()
            self.state = 293
            self.match(MiniGoParser.COMMA)
            self.state = 294
            self.for_val()
            self.state = 296
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 297
            self.match(MiniGoParser.RANGE)
            self.state = 298
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_idxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_idx

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_idx" ):
                return visitor.visitFor_idx(self)
            else:
                return visitor.visitChildren(self)




    def for_idx(self):

        localctx = MiniGoParser.For_idxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_for_idx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_val" ):
                return visitor.visitFor_val(self)
            else:
                return visitor.visitChildren(self)




    def for_val(self):

        localctx = MiniGoParser.For_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_array" ):
                return visitor.visitFor_array(self)
            else:
                return visitor.visitChildren(self)




    def for_array(self):

        localctx = MiniGoParser.For_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_for_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniGoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.lhs()
            self.state = 307
            self.assign_op()
            self.state = 308
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS_ASSIGN(self):
            return self.getToken(MiniGoParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(MiniGoParser.MINUS_ASSIGN, 0)

        def MULT_ASSIGN(self):
            return self.getToken(MiniGoParser.MULT_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_op" ):
                return visitor.visitAssign_op(self)
            else:
                return visitor.visitChildren(self)




    def assign_op(self):

        localctx = MiniGoParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MULT_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN) | (1 << MiniGoParser.DECLARE_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(MiniGoParser.L_CURLY)
            self.state = 313
            self.stmt_list()
            self.state = 314
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_params(self):
            return self.getTypedRuleContext(MiniGoParser.Func_paramsContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def return_type(self):
            return self.getTypedRuleContext(MiniGoParser.Return_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(MiniGoParser.FUNC)
            self.state = 317
            self.match(MiniGoParser.ID)
            self.state = 318
            self.func_params()
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT, MiniGoParser.INTERFACE, MiniGoParser.INT_TYPE, MiniGoParser.STRING_TYPE, MiniGoParser.FLOAT_TYPE, MiniGoParser.BOOL_TYPE, MiniGoParser.L_BRACKET, MiniGoParser.ID]:
                self.state = 319
                self.return_type()
                pass
            elif token in [MiniGoParser.L_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 323
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def func_params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Func_params_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_params" ):
                return visitor.visitFunc_params(self)
            else:
                return visitor.visitChildren(self)




    def func_params(self):

        localctx = MiniGoParser.Func_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MiniGoParser.L_PAREN)
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 326
                self.func_params_list()
                pass
            elif token in [MiniGoParser.R_PAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 330
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_param(self):
            return self.getTypedRuleContext(MiniGoParser.Func_paramContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def func_params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Func_params_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_params_list" ):
                return visitor.visitFunc_params_list(self)
            else:
                return visitor.visitChildren(self)




    def func_params_list(self):

        localctx = MiniGoParser.Func_params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_func_params_list)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.func_param()
                self.state = 333
                self.match(MiniGoParser.COMMA)
                self.state = 334
                self.func_params_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.func_param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_param" ):
                return visitor.visitFunc_param(self)
            else:
                return visitor.visitChildren(self)




    def func_param(self):

        localctx = MiniGoParser.Func_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_func_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.id_list()
            self.state = 340
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_type" ):
                return visitor.visitReturn_type(self)
            else:
                return visitor.visitChildren(self)




    def return_type(self):

        localctx = MiniGoParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_return_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_params" ):
                return visitor.visitExpr_params(self)
            else:
                return visitor.visitChildren(self)




    def expr_params(self):

        localctx = MiniGoParser.Expr_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MiniGoParser.L_PAREN)
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT, MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.LOGICAL_NOT, MiniGoParser.L_PAREN, MiniGoParser.L_BRACKET, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 345
                self.expr_list()
                pass
            elif token in [MiniGoParser.R_PAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 349
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def const_spec(self):
            return self.getTypedRuleContext(MiniGoParser.Const_specContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(MiniGoParser.CONST)
            self.state = 352
            self.const_spec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_spec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_spec" ):
                return visitor.visitConst_spec(self)
            else:
                return visitor.visitChildren(self)




    def const_spec(self):

        localctx = MiniGoParser.Const_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_const_spec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(MiniGoParser.ID)
            self.state = 355
            self.match(MiniGoParser.ASSIGN)
            self.state = 356
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def var_spec(self):
            return self.getTypedRuleContext(MiniGoParser.Var_specContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(MiniGoParser.VAR)
            self.state = 359
            self.var_spec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_spec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_spec" ):
                return visitor.visitVar_spec(self)
            else:
                return visitor.visitChildren(self)




    def var_spec(self):

        localctx = MiniGoParser.Var_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_var_spec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(MiniGoParser.ID)
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT, MiniGoParser.INTERFACE, MiniGoParser.INT_TYPE, MiniGoParser.STRING_TYPE, MiniGoParser.FLOAT_TYPE, MiniGoParser.BOOL_TYPE, MiniGoParser.L_BRACKET, MiniGoParser.ID]:
                self.state = 362
                self.type_()
                self.state = 366
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ASSIGN]:
                    self.state = 363
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 364
                    self.expr(0)
                    pass
                elif token in [MiniGoParser.SEMI]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 368
                self.match(MiniGoParser.ASSIGN)
                self.state = 369
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = MiniGoParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_id_list)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(MiniGoParser.ID)
                self.state = 373
                self.match(MiniGoParser.COMMA)
                self.state = 374
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr_list)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.expr(0)
                self.state = 379
                self.match(MiniGoParser.COMMA)
                self.state = 380
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_type(self):
            return self.getTypedRuleContext(MiniGoParser.Single_typeContext,0)


        def type_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Type_litContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniGoParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_type_)
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_TYPE, MiniGoParser.STRING_TYPE, MiniGoParser.FLOAT_TYPE, MiniGoParser.BOOL_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.single_type()
                pass
            elif token in [MiniGoParser.STRUCT, MiniGoParser.INTERFACE, MiniGoParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.type_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 387
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def slice_type(self):
            return self.getTypedRuleContext(MiniGoParser.Slice_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_lit" ):
                return visitor.visitType_lit(self)
            else:
                return visitor.visitChildren(self)




    def type_lit(self):

        localctx = MiniGoParser.Type_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_type_lit)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.array_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.struct_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 392
                self.interface_type()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 393
                self.slice_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complex_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_complex_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplex_type" ):
                return visitor.visitComplex_type(self)
            else:
                return visitor.visitChildren(self)




    def complex_type(self):

        localctx = MiniGoParser.Complex_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_complex_type)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.struct_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.type_name()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_type" ):
                return visitor.visitList_type(self)
            else:
                return visitor.visitChildren(self)




    def list_type(self):

        localctx = MiniGoParser.List_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.array_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = MiniGoParser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_type_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complex_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def complex_type(self):
            return self.getTypedRuleContext(MiniGoParser.Complex_typeContext,0)


        def complex_val(self):
            return self.getTypedRuleContext(MiniGoParser.Complex_valContext,0)


        def list_type(self):
            return self.getTypedRuleContext(MiniGoParser.List_typeContext,0)


        def list_val(self):
            return self.getTypedRuleContext(MiniGoParser.List_valContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_complex_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplex_lit" ):
                return visitor.visitComplex_lit(self)
            else:
                return visitor.visitChildren(self)




    def complex_lit(self):

        localctx = MiniGoParser.Complex_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_complex_lit)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.complex_type()
                self.state = 405
                self.complex_val()
                pass
            elif token in [MiniGoParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.list_type()
                self.state = 408
                self.list_val()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_val" ):
                return visitor.visitList_val(self)
            else:
                return visitor.visitChildren(self)




    def list_val(self):

        localctx = MiniGoParser.List_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_list_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(MiniGoParser.L_CURLY)
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT, MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.L_CURLY, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 413
                self.element_list()
                pass
            elif token in [MiniGoParser.R_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 417
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complex_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def key_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Key_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_complex_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplex_val" ):
                return visitor.visitComplex_val(self)
            else:
                return visitor.visitChildren(self)




    def complex_val(self):

        localctx = MiniGoParser.Complex_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_complex_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(MiniGoParser.L_CURLY)
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 420
                self.key_element_list()
                pass
            elif token in [MiniGoParser.R_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 424
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyed_element(self):
            return self.getTypedRuleContext(MiniGoParser.Keyed_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def key_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Key_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_key_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_element_list" ):
                return visitor.visitKey_element_list(self)
            else:
                return visitor.visitChildren(self)




    def key_element_list(self):

        localctx = MiniGoParser.Key_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_key_element_list)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.keyed_element()
                self.state = 427
                self.match(MiniGoParser.COMMA)
                self.state = 428
                self.key_element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.keyed_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(MiniGoParser.ElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_list" ):
                return visitor.visitElement_list(self)
            else:
                return visitor.visitChildren(self)




    def element_list(self):

        localctx = MiniGoParser.Element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_element_list)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.element()
                self.state = 434
                self.match(MiniGoParser.COMMA)
                self.state = 435
                self.element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyed_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_name(self):
            return self.getTypedRuleContext(MiniGoParser.Field_nameContext,0)


        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_keyed_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyed_element" ):
                return visitor.visitKeyed_element(self)
            else:
                return visitor.visitChildren(self)




    def keyed_element(self):

        localctx = MiniGoParser.Keyed_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_keyed_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.field_name()
            self.state = 441
            self.match(MiniGoParser.COLON)
            self.state = 442
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_name" ):
                return visitor.visitField_name(self)
            else:
                return visitor.visitChildren(self)




    def field_name(self):

        localctx = MiniGoParser.Field_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_litContext,0)


        def complex_type(self):
            return self.getTypedRuleContext(MiniGoParser.Complex_typeContext,0)


        def complex_val(self):
            return self.getTypedRuleContext(MiniGoParser.Complex_valContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def list_val(self):
            return self.getTypedRuleContext(MiniGoParser.List_valContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_element)
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.primitive_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.complex_type()
                self.state = 448
                self.complex_val()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 450
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 451
                self.list_val()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def type_spec(self):
            return self.getTypedRuleContext(MiniGoParser.Type_specContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_decl" ):
                return visitor.visitType_decl(self)
            else:
                return visitor.visitChildren(self)




    def type_decl(self):

        localctx = MiniGoParser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_type_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(MiniGoParser.TYPE)
            self.state = 455
            self.type_spec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_spec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_spec" ):
                return visitor.visitType_spec(self)
            else:
                return visitor.visitChildren(self)




    def type_spec(self):

        localctx = MiniGoParser.Type_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_type_spec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(MiniGoParser.ID)
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 458
                self.struct_type()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 459
                self.interface_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Method_listContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_interface_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(MiniGoParser.INTERFACE)
            self.state = 463
            self.match(MiniGoParser.L_CURLY)
            self.state = 464
            self.method_list()
            self.state = 465
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def method_spec(self):
            return self.getTypedRuleContext(MiniGoParser.Method_specContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_method_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(MiniGoParser.FUNC)
            self.state = 468
            self.receiver()
            self.state = 469
            self.method_spec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_params(self):
            return self.getTypedRuleContext(MiniGoParser.Func_paramsContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def return_type(self):
            return self.getTypedRuleContext(MiniGoParser.Return_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_spec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_spec" ):
                return visitor.visitMethod_spec(self)
            else:
                return visitor.visitChildren(self)




    def method_spec(self):

        localctx = MiniGoParser.Method_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_method_spec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(MiniGoParser.ID)
            self.state = 472
            self.func_params()
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT, MiniGoParser.INTERFACE, MiniGoParser.INT_TYPE, MiniGoParser.STRING_TYPE, MiniGoParser.FLOAT_TYPE, MiniGoParser.BOOL_TYPE, MiniGoParser.L_BRACKET, MiniGoParser.ID]:
                self.state = 473
                self.return_type()
                pass
            elif token in [MiniGoParser.L_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 477
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def method_type(self):
            return self.getTypedRuleContext(MiniGoParser.Method_typeContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(MiniGoParser.L_PAREN)
            self.state = 480
            self.match(MiniGoParser.ID)
            self.state = 481
            self.method_type()
            self.state = 482
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_type" ):
                return visitor.visitMethod_type(self)
            else:
                return visitor.visitChildren(self)




    def method_type(self):

        localctx = MiniGoParser.Method_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_method_type)
        try:
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.struct_type()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 486
                self.interface_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Method_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_list" ):
                return visitor.visitMethod_list(self)
            else:
                return visitor.visitChildren(self)




    def method_list(self):

        localctx = MiniGoParser.Method_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_method_list)
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.method()
                self.state = 490
                self.eos()
                self.state = 491
                self.method_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.method()
                self.state = 494
                self.eos()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def method_params(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramsContext,0)


        def return_type(self):
            return self.getTypedRuleContext(MiniGoParser.Return_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(MiniGoParser.ID)
            self.state = 499
            self.method_params()
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT, MiniGoParser.INTERFACE, MiniGoParser.INT_TYPE, MiniGoParser.STRING_TYPE, MiniGoParser.FLOAT_TYPE, MiniGoParser.BOOL_TYPE, MiniGoParser.L_BRACKET, MiniGoParser.ID]:
                self.state = 500
                self.return_type()
                pass
            elif token in [MiniGoParser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def method_param_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Method_param_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_params" ):
                return visitor.visitMethod_params(self)
            else:
                return visitor.visitChildren(self)




    def method_params(self):

        localctx = MiniGoParser.Method_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_method_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(MiniGoParser.L_PAREN)
            self.state = 507
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 505
                self.method_param_prime()
                pass
            elif token in [MiniGoParser.R_PAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 509
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_param_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_param(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def method_param_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Method_param_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_param_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_param_prime" ):
                return visitor.visitMethod_param_prime(self)
            else:
                return visitor.visitChildren(self)




    def method_param_prime(self):

        localctx = MiniGoParser.Method_param_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_method_param_prime)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.method_param()
                self.state = 512
                self.match(MiniGoParser.COMMA)
                self.state = 513
                self.method_param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.method_param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_param" ):
                return visitor.visitMethod_param(self)
            else:
                return visitor.visitChildren(self)




    def method_param(self):

        localctx = MiniGoParser.Method_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_method_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.id_list()
            self.state = 519
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ACCESS(self):
            return self.getToken(MiniGoParser.ACCESS, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr_params(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_paramsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.expr(0)
            self.state = 522
            self.match(MiniGoParser.ACCESS)
            self.state = 523
            self.match(MiniGoParser.ID)
            self.state = 524
            self.expr_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def field_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Field_primeContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(MiniGoParser.STRUCT)
            self.state = 527
            self.match(MiniGoParser.L_CURLY)
            self.state = 528
            self.field_prime()
            self.state = 529
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def field_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Field_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_prime" ):
                return visitor.visitField_prime(self)
            else:
                return visitor.visitChildren(self)




    def field_prime(self):

        localctx = MiniGoParser.Field_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_field_prime)
        try:
            self.state = 540
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.match(MiniGoParser.ID)
                self.state = 532
                self.type_()
                self.state = 533
                self.eos()
                self.state = 534
                self.field_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.match(MiniGoParser.ID)
                self.state = 537
                self.type_()
                self.state = 538
                self.eos()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Slice_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(MiniGoParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(MiniGoParser.R_BRACKET, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_slice_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSlice_type" ):
                return visitor.visitSlice_type(self)
            else:
                return visitor.visitChildren(self)




    def slice_type(self):

        localctx = MiniGoParser.Slice_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_slice_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(MiniGoParser.L_BRACKET)
            self.state = 543
            self.match(MiniGoParser.R_BRACKET)
            self.state = 544
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.array_decl()
            self.state = 547
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_len(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lenContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = MiniGoParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_array_decl)
        try:
            self.state = 553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 549
                self.array_len()
                self.state = 550
                self.array_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.array_len()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(MiniGoParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(MiniGoParser.R_BRACKET, 0)

        def integer(self):
            return self.getTypedRuleContext(MiniGoParser.IntegerContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_len

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_len" ):
                return visitor.visitArray_len(self)
            else:
                return visitor.visitChildren(self)




    def array_len(self):

        localctx = MiniGoParser.Array_lenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_array_len)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(MiniGoParser.L_BRACKET)
            self.state = 558
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT]:
                self.state = 556
                self.integer()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 557
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 560
            self.match(MiniGoParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(MiniGoParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(MiniGoParser.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(MiniGoParser.STRING_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(MiniGoParser.BOOL_TYPE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_single_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_type" ):
                return visitor.visitSingle_type(self)
            else:
                return visitor.visitChildren(self)




    def single_type(self):

        localctx = MiniGoParser.Single_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_single_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT_TYPE) | (1 << MiniGoParser.STRING_TYPE) | (1 << MiniGoParser.FLOAT_TYPE) | (1 << MiniGoParser.BOOL_TYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_litContext,0)


        def complex_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Complex_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_literal)
        try:
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self.primitive_lit()
                pass
            elif token in [MiniGoParser.STRUCT, MiniGoParser.L_BRACKET, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 565
                self.complex_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(MiniGoParser.IntegerContext,0)


        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_lit" ):
                return visitor.visitPrimitive_lit(self)
            else:
                return visitor.visitChildren(self)




    def primitive_lit(self):

        localctx = MiniGoParser.Primitive_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_primitive_lit)
        try:
            self.state = 574
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 568
                self.integer()
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 569
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 570
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 571
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 572
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 573
                self.match(MiniGoParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_LIT(self):
            return self.getToken(MiniGoParser.DECIMAL_LIT, 0)

        def BINARY_LIT(self):
            return self.getToken(MiniGoParser.BINARY_LIT, 0)

        def OCTAL_LIT(self):
            return self.getToken(MiniGoParser.OCTAL_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_integer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = MiniGoParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DECIMAL_LIT) | (1 << MiniGoParser.BINARY_LIT) | (1 << MiniGoParser.OCTAL_LIT) | (1 << MiniGoParser.HEX_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_operand)
        try:
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 578
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 579
                self.match(MiniGoParser.L_PAREN)
                self.state = 580
                self.expr(0)
                self.state = 581
                self.match(MiniGoParser.R_PAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 583
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr_params(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_paramsContext,0)


        def primary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_exprContext,0)


        def ACCESS(self):
            return self.getToken(MiniGoParser.ACCESS, 0)

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primary_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expr" ):
                return visitor.visitPrimary_expr(self)
            else:
                return visitor.visitChildren(self)



    def primary_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Primary_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 154
        self.enterRecursionRule(localctx, 154, self.RULE_primary_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 587
                self.operand()
                pass

            elif la_ == 2:
                self.state = 588
                self.match(MiniGoParser.ID)
                self.state = 589
                self.expr_params()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 602
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                    self.state = 592
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 598
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        self.state = 593
                        self.match(MiniGoParser.ACCESS)
                        self.state = 594
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 595
                        self.index()
                        pass

                    elif la_ == 3:
                        self.state = 596
                        self.match(MiniGoParser.ACCESS)
                        self.state = 597
                        self.func_call()
                        pass

             
                self.state = 604
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(MiniGoParser.L_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def R_BRACKET(self):
            return self.getToken(MiniGoParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = MiniGoParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(MiniGoParser.L_BRACKET)
            self.state = 606
            self.expr(0)
            self.state = 607
            self.match(MiniGoParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGICAL_NOT(self):
            return self.getToken(MiniGoParser.LOGICAL_NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_unary_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_op" ):
                return visitor.visitUnary_op(self)
            else:
                return visitor.visitChildren(self)




    def unary_op(self):

        localctx = MiniGoParser.Unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.LOGICAL_NOT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(MiniGoParser.MULT, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mul_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_op" ):
                return visitor.visitMul_op(self)
            else:
                return visitor.visitChildren(self)




    def mul_op(self):

        localctx = MiniGoParser.Mul_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_mul_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULT) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_add_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_op" ):
                return visitor.visitAdd_op(self)
            else:
                return visitor.visitChildren(self)




    def add_op(self):

        localctx = MiniGoParser.Add_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_add_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compare_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(MiniGoParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(MiniGoParser.NOT_EQUALS, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def LESS_EQUALS(self):
            return self.getToken(MiniGoParser.LESS_EQUALS, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def GREATER_EQUALS(self):
            return self.getToken(MiniGoParser.GREATER_EQUALS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_compare_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare_op" ):
                return visitor.visitCompare_op(self)
            else:
                return visitor.visitChildren(self)




    def compare_op(self):

        localctx = MiniGoParser.Compare_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_compare_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUALS) | (1 << MiniGoParser.NOT_EQUALS) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESS_EQUALS) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATER_EQUALS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_exprContext,0)


        def unary_op(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_opContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def mul_op(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_opContext,0)


        def add_op(self):
            return self.getTypedRuleContext(MiniGoParser.Add_opContext,0)


        def compare_op(self):
            return self.getTypedRuleContext(MiniGoParser.Compare_opContext,0)


        def LOGICAL_AND(self):
            return self.getToken(MiniGoParser.LOGICAL_AND, 0)

        def LOGICAL_OR(self):
            return self.getToken(MiniGoParser.LOGICAL_OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 166
        self.enterRecursionRule(localctx, 166, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT, MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.L_PAREN, MiniGoParser.L_BRACKET, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 618
                self.primary_expr(0)
                pass
            elif token in [MiniGoParser.MINUS, MiniGoParser.LOGICAL_NOT]:
                self.state = 619
                self.unary_op()
                self.state = 620
                self.expr(6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 644
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 642
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 624
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 625
                        self.mul_op()
                        self.state = 626
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 628
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 629
                        self.add_op()
                        self.state = 630
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 632
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 633
                        self.compare_op()
                        self.state = 634
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 636
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 637
                        self.match(MiniGoParser.LOGICAL_AND)
                        self.state = 638
                        self.expr(3)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 639
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 640
                        self.match(MiniGoParser.LOGICAL_OR)
                        self.state = 641
                        self.expr(2)
                        pass

             
                self.state = 646
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_eos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEos" ):
                return visitor.visitEos(self)
            else:
                return visitor.visitChildren(self)




    def eos(self):

        localctx = MiniGoParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_eos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.lhs_prime_sempred
        self._predicates[77] = self.primary_expr_sempred
        self._predicates[83] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def lhs_prime_sempred(self, localctx:Lhs_primeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def primary_expr_sempred(self, localctx:Primary_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




