#include <stdio.h>

<<<<<<< HEAD
int main()
{
 int pk,pu,a;
 float up,tp=0.0;
 for(a=1;a<=2&&scanf("%i %i %f",&pk,&pu,&up);a++)//You shoyldn't declare a here because it seems for this problem URI Online Judge doesn't use C99 or C11 standard
  tp+=pu*up;
 printf("VALOR A PAGAR: R$ %.2f\n",tp);
 return 0;
=======
int main(void) {
	int pk,pu,a;
	float up,tp=0.0;
	for(a=1;a<=2&&scanf("%i %i %f",&pk,&pu,&up);a++)//You shoyldn't declare a here because it seems for this problem URI Online Judge doesn't use C99 or C11 standard
	 tp+=pu*up;
	printf("VALOR A PAGAR: R$ %.2f\n",tp);
	return 0;
>>>>>>> 3e91c6b2088573d3b9d89fc51897ba2ab4e1ad58
}

