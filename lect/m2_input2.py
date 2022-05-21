import sys

def main():
    num = int(sys.stdin.readline())
    out = []
    for i in range(num):
        v1,v2 = map(int, input().rstrip().split(' '))
        out.append(v1+v2)
    print("\n".join(map(str,out)))

if __name__ == '__main__':
    main()