#include <stdio.h>

int main(void) {
int n,f;
scanf("%d", &n);
for (int i=0; i<n; i++)
{
	int cas[1000]={0};
	int sum=0;
	double count=0;
	double avg=0;
	scanf("%d",&f);
	for (int j=0; j<f; j++)
	{
		scanf("%d", &cas[j]);
		sum += cas[j];
	}
	avg = (double)sum/f;
	for (int k=0; k<f; k++)
	{
		if(avg < cas[k])
		count++;
	}
	count = count*100/f;
	printf("%.3f%\n", count);
}
}