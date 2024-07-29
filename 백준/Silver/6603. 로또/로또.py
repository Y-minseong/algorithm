from itertools import combinations

def main():
    while True:
        data = input().strip().split()
        if data[0] == '0':
            break
        k = int(data[0])
        S = list(map(int, data[1:]))
        
        for comb in combinations(S, 6):
            print(" ".join(map(str, comb)))
        print()

if __name__ == "__main__":
    main()
