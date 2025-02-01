import decimal
import lark
from lark.visitors import visit_children_decor

class FormulaEvaluator(lark.visitors.Interpreter):
    @visit_children_decor # this is a decorator so that you don't have to do the following:
    # def add_expr(self, tree):
    #     values = self.visit_children(tree)
    def add_expr(self, values):
        if values[1] == '+':
            return values[0] + values[2] # what if values[0] is not a number? what if it's an error?
        elif values[1] == '-':
            return values[0] - values[2]
        else:
            assert False, f'Unexpected operator {values[1]}'

    def parens(self, tree):
        values = self.visit_children(tree)
        assert len(values) == 1, f'Unexpected tree {tree.pretty()}'
        return values[0]

    def number(self, tree):
        return decimal.Decimal(tree.children[0]) # tokens are subclasses of str, decimal.Decimal can consume a str assuming it's a number

    def string(self, tree):
        return tree.children[0].value[1:-1] # remove quotes