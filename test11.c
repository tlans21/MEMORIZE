#include<sys/types.h>
#include<sys/socket.h>
#include<stdio.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<unistd.h>

int main(void)
{
    pid_t pid, ret;
    int status = 0;
    char in_buf[256];
    char *argv[]
    int j = 0;
    while (1)
    {
        printf("$ ");
        fgets(in_buf, 256, stdin);
        /*
          fgets 는 키보드 입력 문자열 뒤에 \n\0 를 포함해서 in_buf에 저장함.
          \n 을 제외해야 정상적인 입력 문자열을 확보할 수 있음.
          다음은 \n 자리에 '\0' 를 대체하기 위한 코드임.
        */
        in_buf[strlen(in_buf)-1]='\0';

        
        if((pid = fork()) > 0)
        {
            ret = waitpid(pid, &status, 0);
            /* waitpid로 기다린 자식 프로세스의 종료 상태는 status 에 반환됨
               이를 확인하기 위해서는 WIFEXITED, WEXITSTATUS 등의 매크로를 이용해야 함.
               WIFEXITED 는 자식 프로세스의 정상 종료 여부를 나타냄.
               WEXITSTATUS 는 자식 프로세스가 정상 종료되었을 때 반환한 상태 값.
            */
            printf("Child Process Exited : %d, %d, %d", ret, WIFEXITED(status), WEXITSTATUS(status));
        }
        else if(pid == 0)
        {
            //printf("Executing : %s", in_buf);

            token = strtok(in_buf, " ");
            while(token){
                argv[j++] = token;
                token = strtok(in_buf, " ");
                }
                argv[j] = (char *)0;
                execvp(argv[0], argv);
        else
            printf("fail to fork\n");
    }
    return 0;
}
