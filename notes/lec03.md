## Technical debt

Expected cost of overhead you will have to pay by choosing implementation that addresses today's needs but (probably) doesn't address tomorrow's needs.

- Might have a different application programming interface (API) today than tomorrow, have to update other code
- Different assumptions
- Different tests

Careful design can mitigate these issues—_if you actually know that you are incurring technical debt!_

Debt is not always bad. Sometimes you don't have time to craft a solution that works for both today and tomorrow.

__Project 1 has multiple instances of this kind of problem!__

## TD in the class project

Main TD is incurred based on _formula evaluation_ and _cycle detection_.

- Project 1 is pretty simple; can have depth-first search (DFS) algorithms, recursion
- Project 3 assigns a score based on fast evals
- Projects 4 and 5 require more sophisticated formula evaluation and cycle detection; DFS will not work
G
__Advise__: It's not a bad thing to write two implementations (one simple, one fancy). Can use the simple one to evaluate the fancy one.

## Formula parsing and evaluation

We will use `Lark` to parse things that start with `=`.

Many options:
- `lark.Visitor` = scan through a parse tree
- `lark.Transformer` = simple bottom-up tree transformation
    - Easiest, but won't cut it for P4
- `lark.visitor.Interpreter` = sophisticated tree traversal, transformation, and evaluation
    - _TD_—more work initially but might be worth it!

## Demo

In order to update a sheet, it will be useful to build a dependency graph between all the cells. 
We will use `Lark` to make the parsing much easier.

Set up virtual environment:

```
hpeter@thinkpad-t15:~/Documents/CS130$ python --version
Python 3.13.0
hpeter@thinkpad-t15:~/Documents/CS130$ python -m venv venv
hpeter@thinkpad-t15:~/Documents/CS130$ source venv/bin/activate
(venv) hpeter@thinkpad-t15:~/Documents/CS130$ pip install lark
```

Example of parsing a formula:

```
(venv) hpeter@thinkpad-t15:~/Documents/CS130/demos$ python
Python 3.13.0 | packaged by conda-forge | (main, Oct  8 2024, 20:04:32) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import lark
>>> parser = lark.Lark.open('formulas.lark', start='formula')
>>> print(parser.parse('=a1+3*A2').pretty())
add_expr
  cell  a1
  +
  mul_expr
    number      3
    *
    cell        A2
```

Using the `CellRefFinder` to get cell references from the tree:

```
>>> from visit import CellRefFinder
>>> v = CellRefFinder()
>>> v.refs
set()
>>> v.visit(tree)
Tree(Token('RULE', 'add_expr'), [Tree(Token('RULE', 'cell'), [Token('CELLREF', 'a1')]), Token('ADD_OP', '+'), Tree(Token('RULE', 'mul_expr'), [Tree('number', [Token('NUMBER', '3')]), Token('MUL_OP', '*'), Tree(Token('RULE', 'cell'), [Token('CELLREF', 'A2')])])])
>>> v.refs
{'A2', 'a1'}            # note that you'll probably want to make cell references uniform in case
```

Using `FormulaEvaluator` in a few different cases:

- A number: 

```
>>> from interp import FormulaEvaluator
>>> ev = FormulaEvaluator()
>>> tree = parser.parse('=43')
>>> tree
Tree('number', [Token('NUMBER', '43')])
>>> ev.visit(tree)
Decimal('43')
```

- A string: 

```
>>> tree = parser.parse('="hello"')
>>> print(tree.pretty())
string  "hello"             # note the double quotes around a string

>>> ev.visit(tree)
'hello'
```

- Parentheses:

```
>>> tree = parser.parse('=((((3))))')
>>> ev.visit(tree)
Decimal('3')
```

- Addition:

```
>>> ev.visit(parser.parse('=4+5'))
Decimal('9')
```

- An example of an error we will have to fix:

```
>>> ev.visit(parser.parse('=4+"hi"'))           # what do we do when one of the numbers is actually a string?!
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    ev.visit(parser.parse('=4+"hi"'))
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hpeter/Documents/CS130/venv/lib/python3.13/site-packages/lark/visitors.py", line 423, in visit
    return self._visit_tree(tree)
           ~~~~~~~~~~~~~~~~^^^^^^
  File "/home/hpeter/Documents/CS130/venv/lib/python3.13/site-packages/lark/visitors.py", line 431, in _visit_tree
    return f(tree)
  File "/home/hpeter/Documents/CS130/demos/interp.py", line 8, in add_expr
    return values[0] + values[2] # what if values[0] is not a number? what if it's an error?
           ~~~~~~~~~~^~~~~~~~~~~
TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'str'
```


## A note on git branches

_Donnie's recommendation:_ Keep everything on one branch and have everyone work together on it. If you know you're about to do something that will break stuff, make a quick branch and merge later.