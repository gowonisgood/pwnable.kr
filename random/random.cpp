#include <stdio.h>
#include <stdlib.h>

int main()
{
	unsigned int rand = 0x6b8b4567;
	unsigned int key = rand ^ 0xcafebabe;

	printf("%0x\n", key);
	printf("%0d\n", key);

	printf("%0x\n", key ^ rand); //for check


}