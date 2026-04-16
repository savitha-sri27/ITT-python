import sys

def word_order():
    
    n = int(sys.stdin.readline().strip())
    
  
    word_counts = {}
    
    for _ in range(n):
        word = sys.stdin.readline().strip()
  
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    print(len(word_counts))

    print(*(word_counts.values()))

if __name__ == '__main__':
    word_order()
