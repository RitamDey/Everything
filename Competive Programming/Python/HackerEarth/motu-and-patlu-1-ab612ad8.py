def scores(icecreams, n_icecreams):
    motu_score = 1
    patlu_score = 1
    
    motu_pos = 0
    patlu_pos = n_icecreams - 1
    
    
    motu_height = icecreams[motu_pos]
    patlu_height = 2 * icecreams[patlu_pos]
    
    while motu_pos < patlu_pos:
        if motu_pos == patlu_pos:
            motu_score += 1
            motu_pos += 1
        
        diff = motu_height - patlu_height
        
        if diff < 0:
            motu_score += 1
            motu_pos += 1
        elif diff > 0:
            patlu_score += 1
            patlu_pos -= 1
        else:
            patlu_score += 1
            motu_score += 1
            
            motu_pos += 1
            patlu_pos -= 1
    
    return motu_score, patlu_score


if __name__ == "__main__":
    for _ in range(int(input())):
        n_icecreams = int(input())
        icecreams = list(map(int, input().split()))

        result = scores(icecreams, n_icecreams)

        print(result[0], result[1])

        if result[0] > result[1]:
            print("Motu")
        elif result[0] < result[1]:
            print("Patlu")
        else:
            print("Tie")

