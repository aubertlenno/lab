#include <stdio.h>

int main(void){


    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);

    return 0;
}
int max_of_four(int a, int b, int c, int d){

    if(a>b && a>c && a>d){
        printf("%d\n", a);
    }else if(b>a && b>c && b>d){
        printf("%d\n", b);
    }else if(c>a && c>b && c>d){
        printf("%d\n", c);
    }else if(d>a && d>b && d>c){
        printf("%d\n", d);
    }

    return 0;
}