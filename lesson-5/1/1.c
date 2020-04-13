#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int sum(int *arr, int len)
{
    int res = 0;
    for (int i = 0; i < len; ++i)
    {
        res += arr[i];
    }
    return res;
}

int simple_function()
{
    static int i = 0;
    printf("Hello, world #%d\n", i);
    i += 1;
    return i;
}

void change_string(char *text)
{
    for (int i = 0; text != NULL && text[i] != '\0'; ++i)
    {
        text[i] += 1;
    }
}

char *alloc_str()
{
    return strdup("My allocated string");
}

void free_str(char *text)
{
    printf("Free memory\n");
    free(text);
}
