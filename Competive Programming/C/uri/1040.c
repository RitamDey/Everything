#include<stdio.h>

int main()
{
    float n1,n2,n3,n4;
    scanf("%f %f %f %f",&n1,&n2,&n3,&n4);
    double avg=(n1*2+n2*3+n3*4+n4)/(2+3+4+1);
    printf("Media: %.1f\n",avg);
    if(avg>=7.0)
	printf("Aluno aprovado.\n");
    else if(avg<5.0)
	printf("Aluno reprovado.\n");
    else
	{
	    printf("Aluno em exame.\n");
	    float lst;
	    scanf("%f",&lst);
	    printf("Nota do exame: %.1f\n",lst);
	    avg=(avg+lst)/2;
	    if(avg>=5.0)
		printf("Aluno aparovado.\n");
	    else
		printf("Aluno reprovado.\n");
	    printf("Media final: %.1f\n",avg);
	}

    return 0;
}
