from itertools import groupby

def compress_string():
  
    s = input().strip()
    
    results = []
    for key, group in groupby(s):
  
        count = len(list(group))
     
        results.append((count, int(key)))
    

    print(*results)

if __name__ == "__main__":
    compress_string()
