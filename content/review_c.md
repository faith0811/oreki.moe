Title: 复习了一下c语言
Date: 2015-11-10 18:43:54
Category: UselessSkill

今天复习了一下c语言。一直以来我都以为
```
int *a = 3;
```
是对的。但是事实上这个好像是不对的。

还是Python好用 不用考虑那么多问题。

附上复习的结果。

```
#include<stdio.h>
#include<stdlib.h>

typedef struct {
  char *test_char;
  int test_int;
} test;


int main(int arg, char* argv[]){
  test *aaa = malloc(sizeof(test));
  aaa->test_char = malloc(1024);
  aaa->test_char[0] = 30;
  printf("%d", aaa->test_char[0]);
  free(aaa);
  int * b = malloc(100);
  printf("%d", aaa->test_char[0]);
}
```
看起来好像哪里不太对 不管了。
