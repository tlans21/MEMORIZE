#include<stdio.h>

int main(){
    int count = 0;
    char str[] = "Data Structure!";

    for(int i = 0; str[i] != '\0'; i++){
        printf("%c", str[i]);
    }

    char str1[100];
    printf("�Է����ּ���: ");
    gets(str1);

    printf("", str1);

    for(int i = 0; str1[i] != '\0'; i++){
        count++;
    }

    printf("�Էµ� ���ڿ��� ���̴� %d �Դϴ�.", count);
}
