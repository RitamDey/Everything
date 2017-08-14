def is_legal(s1, s2, s3):
    if s3+s1 > s2 and s2+s3 > s1 and s1+s2 > s3:
        return True
    else:
        return False


if __name__ == '__main__':
    triangles = open('Day3_Input.txt').read().split('\n')[0:-1]
    total_sum = 0
    
    
    for triangle in triangles:
        # print(triangle.split())
        s1, s2, s3 = map(int, triangle.split())
        # print(is_legal(s1, s2, s3)); break
        if is_legal(s1, s2, s3):
           total_sum += 1
    print(total_sum)

