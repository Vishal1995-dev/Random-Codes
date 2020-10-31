#include<stdio.h>
#include<stdlib.h>
#include<sys/ipc.h>
#include<sys/types.h>
#include<unistd.h>
#include<fcntl.h>

int main()
{
	int ret=0;
	char arr[20]={'\0'};
	int fd[2]={0,0};   //fd[1]-write and fd[0]-read
	pipe(fd);		//unnamed pipe
	
	ret=fork();
	
	if(ret==0)
	{
		close(fd[1]);
		read(fd[0],arr,10);
		printf("Child receives 1st 10 bytes data %s\n",arr);
		read(fd[0],arr,10);
		printf("Child receives 2nd 10 bytes data %s\n",arr);
	}
	else
	{
		close(fd[0]);
		write(fd[1],"Name:Vishal Bhandari",20);
		printf("Parent writes data in pipe\n");
	}
	return 0;
}
