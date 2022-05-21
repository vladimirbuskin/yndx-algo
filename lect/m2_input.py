import sys

def main():
    num_lines = int(input())
    exit;
    output_numbers = []
    for i in range(num_lines):
        line = sys.stdin.readline().rstrip()
        value_1, value_2 = line.split()
        value_1 = int(value_1)
        value_2 = int(value_2)
        result = value_1 + value_2
        output_numbers.append(str(result))
    print('\n'.join(output_numbers))

if __name__ == '__main__':
    main()