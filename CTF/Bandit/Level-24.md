# Bandit Level 24 → Level 25


## Question
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.


## Answer
This is the first level where we need to use write a malicious script, here a bruteforcing script.

My take was like
```
def main():
    res = ""
    for i0 in range(0, 9):
        for i1 in range(0, 9):
            for i2 in range(0, 9):
                for i3 in range(0, 9):
                    res = str(i0) + str(i1) + str(i2) + str(i3)
                    print("UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ", res)


main()
```

I know it's not the best script (maybe the worst) but it get's the job done
