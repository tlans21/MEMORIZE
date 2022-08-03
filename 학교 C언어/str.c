#include<stdio.h>

int main(){
    int count = 0;
    char str[] = "Data Structure!";

    for(int i = 0; str[i] != '\0'; i++){
        printf("%c", str[i]);
    }

    char str1[100];
    printf("입력해주세요: ");
    gets(str1);

    printf("", str1);

    for(int i = 0; str1[i] != '\0'; i++){
        count++;
    }

    printf("입력된 문자열의 길이는 %d 입니다.", count);
}
