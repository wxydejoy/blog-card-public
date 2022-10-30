
## 因

目前 c++的学习主要是针对三个方向

- 基本语法
- 数据结构
- QT(能用就行的地步)

参考书:

- C++ Primer Plus（第 6 版）
- 数据结构、算法与应用 C++语言描述原书第 2 版
- Qt 5.9 C++开发指南 (王维波 栗宝鹃 侯春望)
- Qt5 开发及实例（第 3 版） (陆文周)

## 基本语法

## 数据结构

参照书前的学习计划安排自己的学习计划

![](https://image.wxydejoy.top/cundf/others/2022-07-04-20-31-15.png)
![](https://image.wxydejoy.top/cundf/others/2022-07-04-20-31-32.png)
p31

## QT

## C++ PrimerPlus

### 第一章 预备知识

一些原理，之前就已经学过，这里就不再详细记录。

![2](https://image.wxydejoy.top/cundf/others/2022-07-26-14-54-07.png)

### 第二章 开始学习

![](https://image.wxydejoy.top/cundf/others/C++PrimerPlus.md/2022-07-26-15-25-51.png)

![](https://image.wxydejoy.top/cundf/others/2022-07-26-15-16-12.png)

基本也没太多知识点，简单记一个吧。

![](https://image.wxydejoy.top/cundf/others/C++PrimerPlus.md/2022-07-26-15-57-46.png)

```cpp
using  std::cout; // namespace
using namespace std; // namespace
```

### 第三章 处理数据

![](https://image.wxydejoy.top/cundf/others/C++PrimerPlus.md/2022-07-26-16-08-35.png)

#### c++ 11 初始化方式

![](https://image.wxydejoy.top/cundf/others/C++PrimerPlus.md/2022-07-26-16-24-32.png)

这里第一次见，跑一下看看

```cpp
using namespace std; // namespace
int aaa = {7};
int bbb{7};
int ccc = {};
int ddd{};


cout << aaa << bbb << ccc << ddd << endl;
cout << sizeof(aaa) << sizeof(bbb) << sizeof(ccc) << sizeof(ddd)  << endl;

//result
7700
4444

```

看来是印刷错误

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-02-15-13-43.png)

#### 强制类型转换

```cpp
(int)aaa;    // c
int(aaa);   // c++
```

#### auto 声明

尽量少用

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-02-15-27-16.png)

### 复合类型

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-02-15-28-43.png)

#### 数组

##### 初始化规则

```cpp
int cards[5] = {1, 2, 3, 4, 5};     //ok
int cards[5];                       //ok
cards[5] = {1, 2, 3, 4, 5};         // error
cards = hands                       // error
```

##### C++11 初始化规则

```cpp
double cards[5]  {1.1, 2.2, 3.3, 4.4, 5.5};     //omit the space between = and {
int counts[5] {};     // there are no elements in the {}, so the elements are default initialized = 0
```


![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-02-18-19-01.png)


#### 字符串
##### c- style



书上写了一堆，总之就是不好用，所以有了新的


##### C++ style

`"string"`

字符串初始化与数组初始化类似，也可以省略 = 


#### 结构体



初始化与数组初始化类似，也可以省略 = ，不允许缩窄转换

#### 共用体

```cpp
union {
    int a;
    double b;
};
```

#### 枚举
```cpp

enum Color {
    RED,
    GREEN,
    BLUE
};


enum Color {
    RED = 1,
    GREEN = 2,
    BLUE = 3
};

```

#### 指针和自由存储空间

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-02-18-40-41.png)

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-02-18-40-53.png)

```cpp
int *p = new int;
delete p;

int *p = new int[10];
delete[] p;   // [] 是告诉编译器，释放整个数组，而不是单个元素

```

#### vector

```cpp
# include <vector>
vector<int> v;
v.push_back(1);
```
#### array
```cpp
# include <array>
array<int, 10> a;
```

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-02-18-49-53.png)

#### 小结

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-02-18-51-36.png)



### 循环和关系表达式

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-03-14-11-51.png)

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-03-14-15-55.png)

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-03-14-18-52.png)

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-03-14-21-39.png)

这个有点意思

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-03-14-24-41.png)


#### 小结

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-03-14-26-44.png)

### 分支语句和逻辑运算符
![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-04-12-00-36.png)

#### cctype
```cpp
#include <cctype>
isalpha('a'); // true
isalpha('1'); // false

isupper('A'); // true
isupper('1'); // false


```

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-04-12-03-13.png)

#### 简单文件输入输出  

```cpp
char word[20];
cin.getline(word, 20);
cout << word << endl;
```
在这种情况下，c将不断读取，直到遇到换行符（示例输入行少于20个字符）。所有字符都将被存储到数组wod中，并在末尾加上一个空字符。换行符被丢弃，输入队列中的下一个字符是下一行中的第一个字符。这里不需要进行任何转换。

##### write


```cpp
ofstream out;
out.open("test.txt"); 
//ofstream out("test.txt");

out << "Hello, world!" << endl;

out.close();
```
##### read

```cpp
ifstream in;
char word[20];
in.open("test.txt");
in >> word;
cout << word << endl;

in.close();
```

不得不说python和c++好像啊.


### 函数

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-05-15-03-03.png)


const

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-05-15-31-30.png)

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-05-15-31-32.png)



#### 函数指针
```cpp
int add(int a, int b) {
    return a + b;
}
int (*p)(int a, int b);
p = add;
p(1, 2);

```
#### 小结

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-05-15-38-34.png)

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-05-15-39-49.png)


### 函数探幽

并没有认真阅读,只是粗略了解

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-08-14-41-34.png)


![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-08-14-42-58.png)

#### 引用变量
```cpp
int a = 1;
int &b = a;
b = 2;
cout << a << endl;
// 2
```

何时使用

![](https://image.wxydejoy.top/cundf/others/C++学习.md/X.png)

#### 默认参数
```cpp
int add(int a, int b = 0) {
    return a + b;
}
add(1);
```
类似python的默认参数,准确的说是python类似c++.

#### 函数重载
```cpp
int add(int a, int b);
int add(int a, int b, int c);
```
何时使用
![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-08-16-06-00.png)

#### 函数模板
```cpp
template <typename T>
T add(T a, T b) {
    return a + b;
}
//use add<int>(1, 2);
add<int>(1, 2);
```

模板可以与函数重载结合使用.


#### 小结

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-08-16-09-23.png)


### 内存模型和名称空间

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-11-18-31-53.png)

和C语言一样，C++也允许甚至鼓励程序员将组件函数放在独立的文件中。第1章介绍过，可以单独编译这些文件，然后将它们链接成可执行的程序。（通常，C++编译器既编译程序，也管理链接器。）如果只修改了一个文件，则可以只重新编译该文件，然后将它与其他文件的编译版本链接。这使得大程序的管理更便捷。另外，，大多数C++环境都提供了其他工具来帮助管理。.例如，UNIX和Linux系统都具有make程序，可以跟踪程序依赖的文件以及这些文件的最后修改时间。运行makc时，如果它检测到上次编译后修改了源文件，make将记住重新构建程序所需的步骤。大多数集成开发环境（包括：Embarcadero C+Builder,Microsoft Visual C+、.Apple.Xcode和Freescale CodeWarrior)都在Project菜单中提供了类似的工具。

#### .H文件

* 函数原型。
* 使用#define或const定义的符号常量。
* 结构声明。
* 类声明。
* 模板声明。
* 内联函数。

#### .CPP文件

* 函数定义。
* 使用#define或const定义的符号常量。
* 结构定义。
* 类定义。
* 模板定义。
* 内联函数。
* 等等

#### 存储特性 作用域和链接性  

全局变量 局部变量 作用域

四种存储特性
- 自动存储特性 (默认)
- 静态存储特性 (static)
- 线程存储特性 (thread_local)
- 动态存储特性 (new,delete)

作用域和链接

作用域(scope)描述了名称在文件（翻译单元）的多大范围内可见。

例如，函数中定义的变量可在该函数中使用，但不能在其他函数中使用：而在文件中的函数定义之前定义的变量则可在所有函数中使用。

链接性(linkage)描述了名称如何在不同单元间共亨。

链接性为外部的名称可在文件间共享，链接性为内部的名称只能由一个文件中的函数共享。自动变量的名称没有链接性，因为它们不能共享。


C++变量的作用域有多种。
- 作用域为局部的变量只在定义它的代码块中可用。代码块是由花括号括起的一系列语句。例如函数体就是代码块，但可以在函数体中嵌入其他代码块。
- 作用域为全局（也叫文件作用域)的变量在定义位置到文件结尾之间都可用。
- 自动变量的作用域为局部，静态变量的作用域是全局还是局部取决于它是如何被定义的。在函数原型作用域(function prototype scope)中使用的名称只在包含参数列表的括号内可用（这就是为什么这些名称是什么以及是否出现都不重要的原因）。在类中声明的成员的作用域为整个类（参见第10章）。在名称空间中声明的变量的作用域为整个名称空间（由于名称空间已经引入到C++语言中，因此全局作用域是名称空间作用域的特例)。C++函数的作用域可以是整个类或整个名称空间（包括全局的），但不能是局部的（因为不能在代码块内定义函数，如果函数的作用域为局部，则只对它白己是可见的，因此不能被其他函数调用。这样的函数将无法运行)。不同的C++存储方式是通过存储持续性、作用域和链接性来描述的。下面来看看各种C++存储方式的这些特征。首先介绍引入名称空间之前的情况，然后看一看名称空问带来的影响。


#### 名称空间

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-11-18-47-23.png)

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-11-18-47-50.png)

1. using 声明 和 using 编译指令

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-11-18-50-18.png)

由于using声明将名称添加到局部声明区域中，因此这个示例避免了将另一个局部变量也命名为fetch。另外，和其他局部变量一样，fetch也将覆盖同名的全局变量。在函数的外面使用usig声明时，将把名称添加到全局名称空间中：

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-11-18-51-21.png)

using声明使一个名称可用，而using编译指令使所有的名称都可用。usig编译指令由名称空间名和它前面的关键字using namespace组成，它使名称空间中的所有名称都可用，而不需要使用作用域解析运算符：一

`using namespace std;`

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-11-18-52-55.png)

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-11-18-54-40.png)

- 一般使用using声明来替代using编译指令，因为using声明更易读。安全

### 对象和类

#### this 指针

#### 对象数组

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-13-16-18-11.png)

![](https://image.wxydejoy.top/cundf/others/C++学习.md/2022-08-13-16-18-18.png)

### 使用类

![](https://image.wxydejoy.top/cundf/others/cpp_study.md/2022-08-14-19-54-05.png)
#### 友元
1. 友元函数
2. 友元类
3. 友元成员函数

这里只介绍 友元函数

![](https://image.wxydejoy.top/cundf/others/cpp_study.md/2022-08-14-19-57-52.png)

说实话 看不懂
截个图吧

![](https://image.wxydejoy.top/cundf/others/cpp_study.md/2022-08-14-20-01-03.png)

![](https://image.wxydejoy.top/cundf/others/cpp_study.md/2022-08-14-20-01-12.png)



