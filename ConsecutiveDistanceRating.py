rows = int(raw_input("how many rows? "))
cols = int(raw_input("how many columns? "))

def build_challenge(zuples):
    arr = []
    for x in range(0, zuples):
       nums = raw_input("input row: ").split()
       arr.append(nums)
    return arr

def solve(arr, cols, rows):
    for r in range(0,rows):
        sum = 0
        for x in range(0,cols):
            for y in range(0,cols):
                val = int(arr[r][y])-int(arr[r][x])
                if val == 1:
                   sum+=abs(y-x)
        print(sum)




matrix = build_challenge(rows)
solve(matrix, cols, rows)
