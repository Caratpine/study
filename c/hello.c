#include <stdio.h>
#include <string.h>

#define TEST "hello world"

int count_one_bits(unsigned value)
{
    int ones;

    for (ones = 0; value != 0; value = value >> 1) {
        if (value % 2 != 0) {
            ones = ones + 1;
        }
    }

    return ones;
}

int main()
{
    for (float y = 1.5f; y > -1.5f; y -= 0.1f) {
            for (float x = -1.5f; x < 1.5f; x += 0.05f) {
                        float a = x * x + y * y - 1;
                        putchar(a * a * a - x * x * y * y * y <= 0.0f ? '*' : ' ');
                               }
                   putchar('\n');
                      }
}
