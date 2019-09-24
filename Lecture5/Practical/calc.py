import pretty_print
def calculate_square(x):
    return x**2

def calculate_cube(x):
    return x**3

def main():
    pretty_print.simple_print(calculate_square(2))
    pretty_print.pro_print(calculate_cube(4))

if __name__ == '__main__':
    main()