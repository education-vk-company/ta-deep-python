#include <stdlib.h>
#include <stdio.h>

/*int sum(int *arr, int len)
{
    int res = 0;
    for (int i = 0; i < len; ++i)
    {
        res += arr[i];
    }
    return res;
}*/

struct Point {
    int x;
    int y;
};

int area(struct Point *p1, struct Point *p2)
{
    /*
    struct Point p3;
    p3.x + p3.y
    */
    return abs((p1->x - p2->x) * (p1->y - p2->y));
}
