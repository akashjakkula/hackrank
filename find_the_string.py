def count_substring(string, sub_string):
    b=len(string)
    for i in range(0,b):
        a=string.find(sub_string)
        return (a[b-4])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
