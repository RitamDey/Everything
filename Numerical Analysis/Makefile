clean:
	rm -rf *.run

trapezodial: trapezodial.c
	gcc -o trapezodial.run -lm trapezodial.c
	for i in {1..4}; do (echo "0 1"; echo "5") | ./trapezodial.run; done

simpsons: simpsons-third.c
	gcc -o simpsons.run -lm simpsons-third.c
	for i in {1..4}; do (echo "0 1"; echo "5") | ./simpsons.run; done

newton-forward: newton-forward.c
	gcc -o newton-forward.run -lm newton-forward.c
	#for i in {1..4}; do (echo "0 1"; echo "5") | ./newton-forward.run; done
