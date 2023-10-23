#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except (ZeroDivisionError):
        div = None
    finally:
        print("result inside: {}".format(div))
        return div
