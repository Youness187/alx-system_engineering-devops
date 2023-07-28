#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * main - Creates five zombie processes.
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	int c = 0;

	while (c < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			c++;
		}
		else
			exit(0);
	}
	if (pid != 0)
	{
		while (1)
			sleep(1);
	}
	return (0);
}

