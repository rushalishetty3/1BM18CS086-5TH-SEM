#include <fcntl.h>
 #include <sys/stat.h>
 #include <sys/types.h>
 #include <unistd.h>
 #include <stdio.h>
 #define MAX_BUF 1024 
 int main(int argc, char *argv[])
{
 int fd;
 /* A temp FIFO file is not created in reader */
 char *myfifo = argv[1]; 
 char buf[MAX_BUF];
 /* open, read, and display the message from the FIFO */
 fd = open(myfifo, O_RDONLY);
 printf("File opened\n");
 read(fd, buf, MAX_BUF); 
 printf("Reader: %s\n", buf);
 close(fd);
 printf("File closed\n");
 return 0;
}
