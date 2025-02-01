import lark

class CellRefFinder(lark.Visitor):
    def __init__(self, sheetname: str):
        self.sheetname = sheetname
        self.refs = set()

    def cell(self, tree):
        if len(tree.children) == 1:
            self.refs.add(self.sheetname + '!' + str(tree.children[0])) # lark token is subtype of str
        elif len(tree.children) == 2:
            self.refs.add('!'.join(tree.children))
        else:
            assert False, 'wtf'