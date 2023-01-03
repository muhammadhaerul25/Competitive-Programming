def max_consecutive_ones(n):
    # Write your code here
    biner = list(bin(n))
    biner.pop(0)
    biner.pop(0)
    biner = ''.join(biner)
    biner = biner.split('0')
    biner = list(filter(None, biner))
    biner = [len(i) for i in biner]
    return max(biner)
    
if __name__ == '__main__':
    n = int(input().strip())
    print(max_consecutive_ones(n))
