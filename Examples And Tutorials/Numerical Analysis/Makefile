clean:
	rm -rf *.run

trapezodial: trapezodial.c
	gcc -o trapezodial.run -lm trapezodial.c
	for i in {1..4}; do (echo "0 1"; echo "5") | ./trapezodial.run; done
	make clean

simpsons: simpsons-third.c
	gcc -o simpsons.run -lm simpsons-third.c
	for i in {1..4}; do (echo "0 1"; echo "5") | ./simpsons.run; done
	make clean

newton-forward: newton-forward.c
	gcc -o newton-forward.run -lm newton-forward.c
	#for i in {1..4}; do (echo "0 1"; echo "5") | ./newton-forward.run; done
	make clean

lagrange-interpolation: lagrange-interpolation.c
	gcc -o lagrange-interpolation.run -lm lagrange-interpolation.c
	(echo "5"; echo "25"; for i in {1..5}; do (echo "$i"; echo `echo $i^2 | bc`); done) | ./lagrange-interpolation.run
	make clean