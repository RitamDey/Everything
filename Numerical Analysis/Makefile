clean:
	rm -rf trapezodial

trapezodial: trapezodial.c
	gcc -o trapezodial -lm trapezodial.c
	for i in {1..4}; do (echo "0 1"; echo "5") | ./trapezodial; done

simpsons: simpsons-third.c
	gcc -o simpsons -lm simpsons-third.c
	for i in {1..4}; do (echo "0 1"; echo "5") | ./simpsons; done

