== cpp ==

a 的ascii 97

A 的ascii 65

cpp中新增了`bool`型变量

`^` 异或符号，按位

cpp中新增了三维数组，应该不常用

```cpp
//选择排序
void sort_ch(char a[]){
    int i,j,l,temp;
    for(i = 0; i < l-1; i++){
        for(j = i+1; i < l; j++){
            if(a[i] > a[j]){
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
}

//冒泡排序

void bubblesort(char a[],char l){
    char i,j,temp;
    for(i=0;i<l-1;i++){
        for(j = 0;j<l-i-1;j++)
            if(a[j+1] > a[j]){
                temp = a[j+1];
                a[j+1] = a[j];
                a[j] = temp;
            }
    }
}

```

函数指针，能看懂就行

递归函数--自己调用自己，但要有断点，以防死循环

函数重载--一个函数名根据输入的参数不同作出不同的反应

全局变量、外部变量、静态变量和局部变量。

内部函数，外部函数--了解

结构体，共用体，了解


## 类和对象

定义，对象

```cpp

class xxx{//xxx为类名
    private:
        //ssss
        char _a;//私有变量
        void aaa(void);//私有函数
    public:
        //sss
        xxx(char a);//构造函数      定义对象时自动调用
        ～xxx(char a);//析构函数    程序结束自动调用
        char _a;//公共变量
        void bbb(void);//公有函数
}

void xxx::aaa(void){

}

void xxx::bbb(void){


}

xxx a;//对象

```

好像也没什么新的，还行
