from sys import stdin

while True:
    print(
        eval(
            compile(input(),filename=stdin)
        )
    )

