def calc(expr):
    allowed = '-+/*'
    if not any(i in expr for i in allowed):
        raise ValueError(f"does`nt found {allowed}")
    for sign in allowed:
        if sign in expr:
            try:
                left, right = expr.split(sign)
                left, right = int(left), int(right)
                if sign == '+':
                    return left + right
                if sign == '-':
                    return left - right
                if sign == '*':
                    return left * right
                if sign == '/':
                    return left / right
            except (ValueError, TypeError):
                raise ValueError(f"It must be with 2 numbers")


print(calc('4/2'))
