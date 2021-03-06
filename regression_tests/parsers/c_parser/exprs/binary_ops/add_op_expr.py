"""
    An add operator (``+``).
"""

from regression_tests.parsers.c_parser.exprs.binary_ops.binary_op_expr import BinaryOpExpr


class AddOpExpr(BinaryOpExpr):
    """An add operator (``+``)."""

    def is_add_op(self):
        """Returns ``True``."""
        return True

    def __str__(self):
        return '{} + {}'.format(self.lhs, self.rhs)
