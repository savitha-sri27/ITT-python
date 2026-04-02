def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        t_i = string[i : i + k]
        u_i = "".join(dict.fromkeys(t_i))
        
        print(u_i)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)