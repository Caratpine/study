#include <stdio.h>

int main()
{
    int c;
    c = getchar();
    while (c != EOF) {
        putchar(c);
        int a;
        a = c != EOF;
        putchar(a);        
        c = getchar();
    }
}
