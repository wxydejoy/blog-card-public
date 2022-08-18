==一些c语言的常识==
## 类的封装

我封装的第一个类，WXY类
```c
// Created on wxydejoy.
#include <stdio.h>
class WXY {
    public:
        WXY(unsigned int age){
            __age = age;
        }
        void on(void){
            add();
            printf("%d",__age);
        }

    private:
        unsigned int __age;
        void add(void){
            __age += 1;
        }
};

int main() {

    /*
    int a = 0,i;
    for(i=1;i<5;i++){
        switch(i){
            case 0:
            case 3: a+=2;
            case 1:
            case 2: a+=3;
            
            default: a+=5;
        }
    }*/
    WXY www = WXY(3);
    www.on();
    //printf("%d",a);
    return 0;
}

```
## 易错点

1. 指针相关
    `int a = 11; int *b = &a;  // *b == 11`
    只有在定义的时候可以这样写，定义后不能这样写。
2. 判断相关
    `switch`不加`break`会把后面所有的都执行一遍
    ```c
    int main() {    
        int a = 0,i;    
        printf("%d",a);    
        for(i=1;i<5;i++){        
            switch(i){          
            case 0:
            case 3: a+=2; 
            case 1:
            case 2: a+=3;
            default: a+=5;
            }
        }    
        return 0;
    }
    // a =31.  
    //. 1 - +3+5
    //. 2 - +3+5
    //. 3 - +2+3+5
    //. 4 - +5
    ```

## 常用数据类型

| 类型   | 符号 | 关键字               | 位数 | 范围             |
| ------ | ---- | -------------------- | ---- | ---------------- |
| 整型   | 有   | `(signed)int`        | 16   | -32768~32767     |
| 整型   | 有   | `(signed)shot`       | 16   | -32768~32767     |
| 整型   | 有   | `(signed)long`       | 32   | -2^16~2^16-1     |
| 整型   | 无   | `unsigned int`       | 16   | 0~65535          |
| 整型   | 无   | `unsigned short int` | 16   | 0~65535          |
| 整型   | 无   | `unsigned  long int` | 32   | 0~2^32-1         |
| 实型   | 有   | `float`              | 32   | 3.4e-38~3.4e38   |
| 实型   | 有   | `double`            | 64   | 1.7e-308~1.7e308 |
| 字符型 | 有   | `char`               | 8    | -128~127         |
| 字符型 | 无   | `unsigned char`      | 8    | 0~255            |


## 指针

总结地来说， 变量为了表示数据而生， 指针为了传递数据为生。 

一般与系统位数相同

- 关于 * 和 & 的谜题

[原文链接](http://c.biancheng.net/view/1991.html)

假设有一个 int 类型的变量 a，pa 是指向它的指针，那么`*&a`和`&*pa`分别是什么意思呢？

`*&a`可以理解为`*(&a)`，`&a`表示取变量 a 的地址（等价于 pa），`*(&a)`表示取这个地址上的数据（等价于 *pa），绕来绕去，又回到了原点，`*&a`仍然等价于 a。

`&*pa`可以理解为`&(*pa)`，`*pa`表示取得 pa 指向的数据（等价于 a），`&(*pa)`表示数据的地址（等价于 &a），所以`&*pa`等价于 pa。

- 对星号`*`的总结

在我们目前所学到的语法中，星号`*`主要有三种用途：

- 表示乘法，例如`int a = 3, b = 5, c;  c = a * b;`，这是最容易理解的。
- 表示定义一个指针变量，以和普通变量区分开，例如`int a = 100;  int *p = &a;`。
- 表示获取指针指向的数据，是一种间接操作，例如`int a, b, *p = &a;  *p = 100;  b = *p;`。

## 结构体

```c
//defind
struct name{
	int a;
    float b;
};//分号前可以定义一个结构体  }sonname; 或者另外定义，另外name可以不写(我称之为一次性结构体)
//example
struct name sonname1;
//逐个访问
name1.a = 3;
name1.b = 0.5;
```
- 注意

需要注意的是，结构体是一种自定义的数据类型，是创建变量的模板，不占用内存空间；结构体变量才包含了实实在在的数据，需要内存空间来存储。

**结构体指针要用->不能用点**

### 共用体

个人定义：数据的不同显示形式。

```c
//defind
union 共用体名{
    成员列表
};
//分号前可以定义一个结构体  }sonname; 
//或者另外定义，另外name可以不写(我称之为一次性共用体)
//example
struct name sonname1;
//逐个访问
name1.a = 3;
name1.b = 0.5;
```

- 注意

共用体 data 中，成员 f 占用的内存最多，为 8 个字节，所以 data 类型的变量（也就是 a、b、c）也占用 8 个字节的内存，请看下面的演示：

```c
#include <stdio.h>
union data{    
    int n;    
    char ch;    
    short m;
};
int main(){    
    union data a;    
    printf("%d, %d\n", sizeof(a), sizeof(union data) );
    a.n = 0x40;
    printf("%X, %c, %hX\n", a.n, a.ch, a.m);
    a.ch = '9';
    printf("%X, %c, %hX\n", a.n, a.ch, a.m);
    a.m = 0x2059;    printf("%X, %c, %hX\n", a.n, a.ch, a.m);
    a.n = 0x3E25AD54;    printf("%X, %c, %hX\n", a.n, a.ch, a.m);
    return 0;
}
```

运行结果：

```c
4, 4
40, @, 40
39, 9, 39
2059, Y, 2059
3E25AD54, T, AD54
```

这段代码不但验证了共用体的长度，还说明共用体成员之间会相互影响，修改一个成员的值会影响其他成员。

- 结构体与共用体的区别与联系

1、结构体每一位成员都用来表示一种具体事务的属性，共用体成员可以表示多种属性（同一存储空间可以存储不同类型的数据）。

2、结构体总空间大小，等于各成员总长度，共用体空间等于最大成员占据的空间。

3、共用体不能赋初值而结构体可以。

## 枚举变量 

变量的值只能未定义常量中的一个，例如

```c
enum day{mon,tue,wed}workday;//workday 与结构体类似，都是声明一个变量
```

