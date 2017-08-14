is_legal = lambda s1, s2, s3: s3+s1 > s2 and s2+s3 > s1 and s1+s2 > s3


triangles = open('Day3_Input.txt').read().split('\n')[0:-1]
total_sum = 0


for triangle in triangles:
    s1, s2, s3 = map(int, triangle.split())
    if is_legal(s1, s2, s3):
       total_sum += 1
print(total_sum)

