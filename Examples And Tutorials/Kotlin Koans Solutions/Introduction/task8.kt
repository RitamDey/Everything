fun eval(expr: Expr): Int =
/**
 * Since we're switching on the type of the variable, actual operations can be safely executed without a explict cast
**/
        when (expr) {
            is Num -> expr.value
            is Sum -> eval(expr.left) + eval(expr.right)
            else -> throw IllegalArgumentException("Unknown expression")
        }

interface Expr
class Num(val value: Int) : Expr
class Sum(val left: Expr, val right: Expr) : Expr

