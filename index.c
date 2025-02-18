#include<stdio.h>

int main(){
    
    int x ,y ,z ,w;

    printf("enter the number1:");
    scanf("%d", &x);

    printf("enter the number2:");
    scanf("%d" ,&y);

    printf("enter the number3:");
    scanf("%d", &w);

    z = x + y + w;

    printf("result: %d\n", z);
    
    return 0;
} 