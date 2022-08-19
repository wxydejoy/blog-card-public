虽然之前学过不少 python 的知识，但是还是没有系统的学习过一些基础知识，补一下。
参考书 [Python 基础教程(第 3 版)\_百度百科](https://baike.baidu.com/item/Python%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B%EF%BC%88%E7%AC%AC3%E7%89%88%EF%BC%89/49977580?fr=aladdin)

## 丑话说在前面

只记一下易错点和之前不会的点吧，个人向。

大量 复制粘贴 不喜勿看

## 快速上手：基础知识

### 数和表达式

```python
# 取余
10 % 3
# 整除
10 // 3
# 幂运算
2 ** 3

```

```python
>>> 10 // 3
3
>>> 10 // -3
-4
>>> -10 // 3
-4
>>> -10 // -3
3
```

对于整除运算，需要明白的一个重点是它向下圆整结果。因此在结果为负数的情况下，圆整后将离 0 更远。这意味着对于-10 // 3， 将向下圆整到-4，而不是向上圆整到-3。

```python
>>> 2 ** 3     # pow(2, 3)
8
>>> -3 ** 2
-9
>>> (-3) ** 2
9

```

请注意，乘方运算符的优先级比求负(单目减)高，因此`-3**2`等价于`-(3**2)`。如果你要计
算的是`(-3)**2`，必须明确指出。

十六进制、八进制和二进制

```python
0x10 # 十六进制
0o10 # 八进制
0b10 # 二进制
```

这些表示法都以 0 打头。

### 获取用户输入

```python
>>> input("The meaning of life: ")
The meaning of life: 42
'42'
```

这里在交互式解释器中执行了第一行(input( ))，它打印字符串"The meaning of life:"，
提示用户输入相应的信息。我输入 42 并按回车。这个数被 input(以文本或字符串的方式)返回， 并在最后一行被自动打印出来。

### cmath 和复数

```python
>>> (1 + 3j) * (9 + 4j)
(-3 + 31j)

```

### 保存并执行程序

在有些情况下，你希望能够像执行其他程序(如 Web 浏览器或文本编辑器)一样执行 Python 脚本，而无需显式地使用 Python 解释器。

UNIX 提供了实现这种目标的标准方式：让脚本的第一 行以字符序列#!(称为 pound bang 或 shebang)开始，并在它后面指定用于对脚本进行解释的程序 (这里是 Python)的绝对路径。

即便你对这一点不太明白，只需将下面的代码作为脚本的第一行， 就可在 UNIX 中轻松运行脚本：
`#!/usr/bin/env python `
不管 Python 库位于什么地方，这都将让你能够像运行普通程序一样运行脚本。
如果你安装了多个版本的 Python，可用更具体的可执行文件名(如 python3)替换 python。
要像普通程序一样运行脚本，还必须将其变成可执行的：
`$ chmod a+x hello.py `
现在，可以像下面这样来运行它(假定当前目录包含在执行路径中)：
`$ hello.py `
如果这不管用，请尝试使用`./hello.py`，这在当前目录(.)未包含在执行路径中时也管用(负责的系统管理员会告诉你执行路径是什么)。

如果你愿意，可对文件进行重命名并删除扩展名`.py`，使其看起来更像普通程序。

如果双击会如何呢 在 Windows 中，扩展名`.py`是让脚本像普通程序一样的关键所在。请尝试双击前一节保存的文件`hello.py`。如果正确地安装了`Python`，这将打开一个 DOS 窗口，其中包含提示信息 What is your name?。然而，这样运行程序存在一个问题：输入名字后，程序窗口将立即关闭，你根本来不及 看清结果。这是因为程序结束后窗口将立即关闭。尝试修改脚本，在末尾添加如下代码行： `input("Press <enter>")` 现在运行这个程序并输入名字后，DOS 窗口将包含如下内容：

`What is your name? Gumby Hello, Gumby! Press <enter>`

等你按回车键后，窗口将立即关闭，因为程序结束了。

### 字符串

```python
>>> "Hello, world!"
'Hello, world!'
```

在这个示例中，有一点可能让你颇感意外：Python 在打印字符串时，用单引号将其括起，而 我们使用的是双引号。这有什么差别吗？其实没有任何差别。

```python
>>> "Let's go!"
"Let's go!"
>>> '"Hello, world!" she said'
'"Hello, world!" she said'
```

第二个字符串包含双引号，因此必须使用单引号将整个字符串括起，原因和前面一样。实际上，并非必须这样做(这样做只是出于方便考虑)。可使用反斜杠(\)对引号进行转义，如 下所示

```Python
>>> 'Let\'s go!'
"Let's go!"
```

Python 打印所有的字符串时，都用引号将其括起。你可能通过前面的示例发现了这一点。

因为 Python 打印值时，保留其在代码中的样子，而不是你希望用户看到的样子。但如果你使用 print，结果将不同。

```Python

>>> "Hello,\nworld!"
'Hello,\nworld!'
>>> print("Hello,\nworld!")
Hello,
world!

```

通过两种不同的机制将值转换成了字符串。你可通过使用函数 str 和 repr① 直接使用这两种机制。使用 str 能以合理的方式将值转换为用户能够看懂的字符串。例如，尽可能将特殊字符编码 转换为相应的字符。然而，使用 repr 时，通常会获得值的合法 Python 表达式表示

```Python
>>> print(repr("Hello,\nworld!"))
'Hello,\nworld!'
>>> print(str("Hello,\nworld!"))
Hello, world!
```

1. 长字符串

要表示很长的字符串(跨越多行的字符串)，可使用三引号(而不是普通引号)。
print('''This is a very long string. It continues here.
And it's not over yet.
"Hello, world!" Still here.''')

还可使用三个双引号，如"""like this"""。

请注意，这让解释器能够识别表示字符串开始 和结束位置的引号，因此字符串本身可包含单引号和双引号，无需使用反斜杠进行转义

三个引号也是注释的一种写法。

2. 原始字符串

```python
>>> path = 'C:\nowhere'
>>> path
'C:\nowhere'

# 这好像没问题，但如果将其打印出来，就会出现问题。
>>> print(path)
C:
owhere

# 原始字符串用前缀r表示
>>> print(r'C:\nowhere')
C:\nowhere

#另外，原始字符串不能以单个反斜杠结尾。换而言之，原始字符串的最后一个字符不能是反斜杠，除非你对其进行转义(但进行转义时，用于转义的反斜杠也将是字符串的一部分)。
>>> print(r'C:\Program Files\foo\bar' '\\')
C:\Program Files\foo\bar\
```

3. Unicode、bytes 和 bytearray

每个 Unicode 字符都用一个码点(code point)表示，而码点是 Unicode 标准给每个字符指定的数字。

> > > "\u00C6"
> > > 'Æ'
> > > "\U0001F60A"
> > > '☺ '
> > > "This is a cat: \N{Cat}"
> > > 'This is a cat: '

Unicode 的理念很简单，却带来了一些挑战，其中之一是编码问题。在内存和磁盘中，所有对象都是以二进制数字(0 和 1)表示的(这些数字每 8 个为一组，即 1 字节)，字符串也不例外。 在诸如 C 等编程语言中，这些字节完全暴露，而字符串不过是字节序列而已。为与 C 语言互操作 以及将文本写入文件或通过网络套接字发送出去，Python 提供了两种类似的类型：不可变的 bytes 和可变的 bytearray。如果需要，可直接创建 bytes 对象(而不是字符串)，方法是使用前缀 b：

`>>> b'Hello, world!' b'Hello, world!' `

然而，1 字节只能表示 256 个不同的值，离 Unicode 标准的要求差很远。Python bytes 字面量只支持 ASCII 标准中的 128 个字符，而余下的 128 个值必须用转义序列表示，如\xf0 表示十六进制值 0xf0(即 240)。 唯一的差别好像在于可用的字母表规模，但实际上并非完全如此。乍一看，好像 ASCII 和 Unicode 定义的都是非负整数和字符之间的映射，但存在细微的差别：Unicode 码点是使用整数定义的，而 ASCII 字符是使用对应的数及其二进制编码定义的。

这一点好像无关紧要，原因之一是 整数 0 ～ 255 和 8 位二进制数之间的映射是固定的，几乎没有任何机动空间。问题是超过 1 字节后， 情况就不那么简单了：直接将每个码点表示为相应的二进制数可能不再可行。这是因为不仅存在字节顺序的问题(即便对整数值进行编码，也会遇到这样的问题)，而且还可能浪费空间：如果对于每个码点都使用相同数量的字节进行编码，就必须考虑到文本可能包含安那托利亚象形文字 或皇家亚兰字母。有一种 Unicode 编码标准是基于这种考虑的，它就是 UTF-32(32 位统一编码转换格式，Unicode Transformation Format 32 bits)，但如果你主要处理的是使用互联网上常见语言书写的文本，那么使用这种编码标准将很浪费空间。

然而，有一种非常巧妙的替代方式：不使用全部 32 位，而是使用变长编码，即对于不同的字符，使用不同数量的字节进行编码。这种编码方式主要出自计算机先锋 Kenneth Thompson 之手。 通过使用这种编码，可节省占用的空间，就像摩尔斯码使用较少的点和短线表示常见的字母，从 而减少工作量一样 ①。

具体地说，进行单字节编码时，依然使用 ASCII 编码，以便与较旧的系统兼容；但对于不在这个范围内的字符，使用多个字节(最多为 6 个)进行编码。

下面来使用 ASCII、 UTF-8 和 UTF-32 编码将字符串转换为 bytes。

```python
>>> "Hello, world!".encode("ASCII")
b'Hello, world!'
>>> "Hello, world!".encode("UTF-8")
b'Hello, world!'
>>> "Hello, world!".encode("UTF-32")
b'\xff\xfe\x00\x00H\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00,\x00\ x00\x00 \x00\x00\x00w\x00\x00\x00o\x00\x00\x00r\x00\x00\x00l\x00\x00\x00d\x00\x00\x00!\x00\ x00\x00'
```

从中可知，使用前两种编码的结果相同，但使用最后一种编码的结果长得多。再来看一个 示例：

```python
>>> len("How long is this?".encode("UTF-8"))
17
>>> len("How long is this?".encode("UTF-32"))
72
```

只要字符串包含较怪异的字符，ASCII 和 UTF-8 之间的差别便显现出来了：

```python
>>> "Hællå, wørld!".encode("ASCII") Traceback (most recent call last):

UnicodeEncodeError: 'ascii' codec can't encode character '\xe6' in position 1: ordinal not in range(128)
```

斯堪的纳维亚字母没有对应的 ASCII 编码。如果必须使用 ASCII 编码(这样的情况肯定会遇到)，可向 encode 提供另一个实参，告诉它如何处理错误。这个参数默认为 strict，但可将其指定为其他值，以忽略或替换不在 ASCII 表中的字符。

```python
>>> "Hællå, wørld!".encode("ASCII", "ignore")
b'Hll, wrld!'
>>> "Hællå, wørld!".encode("ASCII", "replace")
b'H?ll?, w?rld!'
>>> "Hællå, wørld!".encode("ASCII", "backslashreplace")
b'H\\xe6ll\\xe5, w\\xf8rld!'
>>> "Hællå, wørld!".encode("ASCII", "xmlcharrefreplace")
b'H&#230;ll&#229;, w&#248;rld!'
```

几乎在所有情况下，都最好使用 UTF-8。事实上，它也是默认使用的编码。

```python
>>> "Hællå, wørld!".encode()
b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!'
```

这相比于 Hello, world!，编码结果要长些；但使用 UTF-32 编码时，结果一样长。 可将字符串编码为 bytes，同样也可将 bytes 解码为字符串。

```python
>>> b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!'.decode()
'Hællå, wørld!'
```

与前面一样，默认编码也是 UTF-8。你可指定其他编码，但如果指定的编码不正确，将出现错误消息或得到一堆乱码。bytes 对象本身并不知道使用的是哪种编码，因此你必须负责跟踪这 一点。可不使用方法 encode 和 decode，而直接创建 bytes 和 str(即字符串)对象，如下所示：

```python
>>> bytes("Hællå, wørld!", encoding="utf-8")
b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!'
>>> str(b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!', encoding="utf-8")
'Hællå, wørld!'
```

这种方法更通用一些，在你不知道类似于字符串或 bytes 的对象属于哪个类时，使用这种方法也更管用。

一个通用规则是，不要做过于严格的假设。 编码和解码的最重要用途之一是，将文本存储到磁盘文件中。然而，Python 提供的文件读写机制通常会替你完成这方面的工作！

只要文件使用的是 UTF-8 编码，就无需操心编码和解码的问 题。

但如果原本正常的文本变成了乱码，就说明文件使用的可能是其他编码。

在这种情况下，对 导致这种问题的原因有所了解将大有裨益。

如果你想更详细地了解 Python 中的 Unicode，请参阅 在线文档中有关该主题的 HOWTO 部分 ①。

注意 源代码也将被编码，且默认使用的也是 UTF-8 编码。如果你想使用其他编码(例如，如果 你使用的文本编辑器使用其他编码来存储源代码)，可使用特殊的注释来指定。 # -*- coding: encoding name -*请将其中的 encoding name 替换为你要使用的编码(大小写都行)，如 utf-8 或 latin-1。
最后，Python 还提供了 bytearray，它是 bytes 的可变版。从某种意义上说，它就像是可修改 的字符串——常规字符串是不能修改的。然而，bytearray 其实是为在幕后使用而设计的，因此 作为类字符串使用时对用户并不友好。例如，要替换其中的字符，必须将其指定为 0 ～ 255 的值。 因此，要插入字符，必须使用 ord 获取其序数值(ordinal value)。

```python
>>> x = bytearray(b"Hello!")
>>> x[1] = ord(b"u")
>>> x
bytearray(b'Hullo!')

```

### 小结

本章介绍的内容很多，先来看看你都学到了什么，再接着往下讲。

- 算法：算法犹如菜谱，告诉你如何完成特定的任务。从本质上说，编写计算机程序就是 使用计算机能够理解的语言(如 Python)描述一种算法。这种对机器友好的描述被称为程序，主要由表达式和语句组成。
- 表达式：表达式为程序的一部分，结果为一个值。例如，2 + 2 就是一个表达式，结果为 4。简单表达式是使用运算符(如+或%)和函数(如 pow)将字面值(如 2 或"Hello")组 合起来得到的。通过组合简单的表达式，可创建复杂的表达式，如(2 + 2) \*(3 - 1)。表 达式还可能包含变量。
- 变量：变量是表示值的名称。通过赋值，可将新值赋给变量，如 x = 2。赋值是一种语句。
- - 语句：语句是让计算机执行特定操作的指示。这种操作可能是修改变量(通过赋值)、将 信息打印到屏幕上(如 print("Hello, world!"))、导入模块或执行众多其他任务。
- 函数：Python 函数类似于数学函数，它们可能接受参数，并返回结果(在第 6 章学习编写 自定义函数时，你将发现函数实际上可以在返回前做很多事情)。
- 模块：模块是扩展，可通过导入它们来扩展 Python 的功能。例如，模块 math 包含多个很有 用的函数。
- 程序：你通过练习学习了如何编写、保存和运行 Python 程序。 - 字符串：字符串非常简单。它们其实就是一段文本，其中的字符是用 Unicode 码点表示的。 然而，对于字符串，需要学习的知识有很多。本章介绍了很多表示字符串的方式，第 3 章 将介绍众多字符串用法。

```python

abs(number)                             # 返回指定数的绝对值
bytes(string, encoding[, errors])       # 对指定的字符串进行编码，并以指定的方式处理错误
cmath.sqrt(number)                      # 返回平方根；可用于负数
float(object)                           # 将字符串或数字转换为浮点数
help([object])                          # 提供交互式帮助
input(prompt)                           # 以字符串的方式获取用户输入
int(object)                             # 将字符串或数转换为整数
math.ceil(number)                       # 以浮点数的方式返回向上圆整的结果
math.floor(number)                      # 以浮点数的方式返回向下圆整的结果
math.sqrt(number)                       # 返回平方根；不能用于负数
pow(x, y[, z])                          # 返回x的y次方对z求模的结果
print(object,    )                      # 将提供的实参打印出来，并用空格分隔
repr(object)                            # 返回一个对象的字符串表示形式
round(number[, ndigits])                # 四舍五入为指定的精度，正好为5时舍入到偶数
str(object)                             # 将指定的值转换为字符串。用于转换bytes时，可指定编码和错误处理方式
```

## 列表和元组

索引 `tag[0]`

切片 `tag[32:-4]`

### 更大的步长

```PYTHON
在这个示例中，指定了另一个数。你可能猜到了，这显式地指定了步长。如果指定的步长大于1，将跳过一些元素。例如，步长为2时，将从起点和终点之间每隔一个元素

>>> numbers[0:10:1]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

提取一个元素显式地指定步长时，也可使用前述简写。例如，要从序列中每隔3个元素提取1个，只需提供步长4即可

>>> numbers[0:10:2]
[1, 3, 5, 7, 9]
numbers[3:6:3]
[4]

当然，步长不能为0，否则无法向前移动，但可以为负数，即从右向左提取元素。

```

### 乘法

将序列与数 x 相乘时，将重复这个序列 x 次来创建一个新序列：

```python
>>> 'python' * 5
'pythonpythonpythonpythonpython'
>>> [42] * 10
[42, 42, 42, 42, 42, 42, 42, 42, 42, 42]
```

None、空列表和初始化

空列表是使用不包含任何内容的两个方括号表示的。如果要创建一个可包含 10 个元素的列表，但没有任何有用的内容，可像前面那样使用`[42]*10`。但更准确的做法是使用`[0]*10`，这将创建一个包含 10 个零的列表。然而，在有些情况下，你可能想使用表示“什么都没有”的值，如表示还没有在列表中添加任何内容。在这种情况下，可使用 None。在 Python 中， None 表示什么都没有。因此，要将列表的长度初始化为 10，可像下面这样做：

```python
>>> sequence = [None] * 10
>>> sequence
[None, None, None, None, None, None, None, None, None, None]
```

### 列表： Python 的主力

```python

>>> list('Hello')
['H', 'e', 'l', 'l', 'o']

```

要将字符列表(如前述代码中的字符列表)转换为字符串，可使用下面的表达式：
`''.join(somelist)`

1. 给切片赋值
   切片是一项极其强大的功能，而能够给切片赋值让这项功能显得更加强大。

```python
>>> name = list('Perl')
>>> name
['P', 'e', 'r', 'l']
>>> name[2:] = list('ar')
>>> name
['P', 'e', 'a', 'r']
```

从上述代码可知，可同时给多个元素赋值。你可能认为，这有什么大不了的，分别给每个元
素赋值不是一样的吗？确实如此，但通过使用切片赋值，可将切片替换为长度与其不同的序列。

```python
>>> name = list('Perl')
>>> name[1:] = list('ython')
>>> name
['P', 'y', 't', 'h', 'o', 'n']
```

使用切片赋值还可在不替换原有元素的情况下插入新元素。

```python
>>> numbers = [1, 5]
>>> numbers[1:1] = [2, 3, 4]
>>> numbers
[1, 2, 3, 4, 5]
```

在这里，我“替换”了一个空切片，相当于插入了一个序列。你可采取相反的措施来删除切片。

```python
>>> numbers
[1, 2, 3, 4, 5]
>>> numbers[1:4] = []
>>> numbers
[1, 5]
```

你可能猜到了，上述代码与 del numbers[1:4]等效。现在，你可自己尝试执行步长**不为 1(乃至为负)**的切片赋值了。

### 列表方法

```python
append()
clear()
copy()
count()
extend()
index()
insert()
pop()  #从列尾删除一个元素，并返回该元素的值
remove()  #删除第一个值
reverse()  #反转列表中的元素
sort()  #排序列表中的元素 就地排序意味着对原来的列表进行修改，而不是创建一个新的列表。

```

#### copy()

方法 copy 复制列表。前面说过，常规复制只是将另一个名称关联到列表。

```python
>>> a = [1, 2, 3]
>>> b = a
>>> b[1] = 4
>>> a
[1, 4, 3]
```

要让 a 和 b 指向不同的列表，就必须将 b 关联到 a 的副本

```python
>>> a = [1, 2, 3]
>>> b = a.copy()
>>> b[1] = 4
>>> a
[1, 2, 3]
>>> b
[1, 4, 3]
```

#### Extend()

方法 extend 让你能够同时将多个值附加到列表末尾，为此可将这些值组成的序列作为参数提
供给方法 extend。换而言之，你可使用一个列表来扩展另一个列表。

```Python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6]
```

这可能看起来类似于拼接，但存在一个重要差别，那就是将修改被扩展的序列(这里是 a)。
在常规拼接中，情况是返回一个全新的序列。

```Python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> a + b
[1, 2, 3, 4, 5, 6]
>>> a
[1, 2, 3]
```

#### sort() 高级排序

方法 sort 接受两个可选参数： key 和 reverse。

方法 sort 接受两个可选参数： key 和 reverse。这两个参数通常是按名称指定的，称为关键字
参数，将在第 6 章详细讨论。参数 key 类似于参数 cmp：你将其设置为一个用于排序的函数。然而，
不会直接使用这个函数来判断一个元素是否比另一个元素小，而是使用它来为每个元素创建一个
键，再根据这些键对元素进行排序。因此，要根据长度对元素进行排序，可将参数 key 设置为函数 len。

```python
>>> x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
>>> x.sort(key=len)
>>> x
['add', 'acme', 'aerate', 'abalone', 'aardvark']
```

对于另一个关键字参数 reverse，只需将其指定为一个真值( True 或 False，将在第 5 章详细介绍)，以指出是否要按相反的顺序对列表进行排序。

### 元组：不可修改的序列 (元组)

```python
>>> tuple([1, 2, 3])
(1, 2, 3)
>>> tuple('abc')
('a', 'b', 'c')
>>> tuple((1, 2, 3))
(1, 2, 3)
```

### 小结

下面来回顾一下本章介绍的一些最重要的概念。

- 序列：序列是一种数据结构，其中的元素带编号(编号从 0 开始)。列表、字符串和元组
  都属于序列，其中列表是可变的(你可修改其内容)，而元组和字符串是不可变的(一旦
  创建，内容就是固定的)。要访问序列的一部分，可使用切片操作：提供两个指定切片起
  始和结束位置的索引。要修改列表，可给其元素赋值，也可使用赋值语句给切片赋值。

- 成员资格：要确定特定的值是否包含在序列(或其他容器)中，可使用运算符 in。将运
  算符 in 用于字符串时情况比较特殊——这样可查找子串。
- 方法：一些内置类型(如列表和字符串，但不包括元组)提供了很多有用的方法。方法
  有点像函数，只是与特定的值相关联。方法是面向对象编程的一个重要方面，这将在第 7
  章介绍。

## 字符串

### 设置字符串的格式 精简版

```python
# from c
>>> format = "Hello, s. s enough for ya?" % %
>>> values = ('world', 'Hot')
>>> format values %
'Hello, world. Hot enough for ya?'

# from shell

>>> from string import Template
>>> tmpl = Template("Hello, $who! $what enough for ya?")
>>> tmpl.substitute(who="Mars", what="Dusty")
'Hello, Mars! Dusty enough for ya?'

# new and improved
>>> "{}, {} and {}".format("first", "second", "third")
'first, second and third'
>>> "{0}, {1} and {2}".format("first", "second", "third")
'first, second and third'

>>> "{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to")
'to be or not to be'

>>> from math import pi
>>> "{name} is approximately {value:.2f}.".format(value=pi, name="π ")
'π is approximately 3.14.'

# 最后，在Python 3.6中，如果变量与替换字段同名，还可使用一种简写。在这种情况下，可使用f字符串——在字符串前面加上f。

>>> from math import e
>>> f"Euler's constant is roughly {e}."
"Euler's constant is roughly 2.718281828459045."

>>> "Euler's constant is roughly {e}.".format(e=e)
"Euler's constant is roughly 2.718281828459045."


```

### 设置字符串的格式 完整版

```python

>>> "{{ceci n'est pas une replacement field}}".format()
"{ceci n'est pas une replacement field}"
```

在格式字符串中，最激动人心的部分为替换字段。替换字段由如下部分组成，其中每个部分
都是可选的。

- 字段名：索引或标识符，指出要设置哪个值的格式并使用结果来替换该字段。除指定值
  外，还可指定值的特定部分，如列表的元素。
- 转换标志：跟在叹号后面的单个字符。当前支持的字符包括 r(表示 repr)、 s(表示 str)
  和 a(表示 ascii)。如果你指定了转换标志，将不使用对象本身的格式设置机制，而是使
  用指定的函数将对象转换为字符串，再做进一步的格式设置。
- 格式说明符：跟在冒号后面的表达式(这种表达式是使用微型格式指定语言表示的)。格
  式说明符让我们能够详细地指定最终的格式，包括格式类型(如字符串、浮点数或十六
  进制数)，字段宽度和数的精度，如何显示符号和千位分隔符，以及各种对齐和填充方式。
  下面详细介绍其中的一些要素。

#### 替换字段名

```python
>>> "{foo} {} {bar} {}".format(1, 2, bar=4, foo=3)
'3 1 4 2'

>>> "{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3)
'3 2 4 1'

>>> fullname = ["Alfred", "Smoketoomuch"]
>>> "Mr {name[1]}".format(name=fullname)
'Mr Smoketoomuch'
>>> import math
>>> tmpl = "The {mod.__name__} module defines the value {mod.pi} for π "
>>> tmpl.format(mod=math)
'The math module defines the value 3.141592653589793 for π '

```

#### 基本转换

```python
>>> print("{pi!s} {pi!r} {pi!a}".format(pi="π "))
π 'π ' '\u03c0'

# 上述三个标志( s、 r和a)指定分别使用str、 repr和ascii进行转换。
# 你还可指定要转换的值是哪种类型，更准确地说，是要将其视为哪种类型。例如，你可能提供一个整数，但将其作为小数进行处理。为此可在格式说明(即冒号后面)使用字符f(表示定点数)。

>>> "The number is {num}".format(num=42)
'The number is 42'
>>> "The number is {num:f}".format(num=42)
'The number is 42.000000'

>>> "The number is {num:b}".format(num=42)
'The number is 101010'

```

表 3-1 字符串格式设置中的类型说明符

| 类型 | 含义                                                                                              |
| ---- | ------------------------------------------------------------------------------------------------- |
| b    | 将整数表示为二进制数                                                                              |
| c    | 将整数解读为 Unicode 码点                                                                         |
| d    | 将整数视为十进制数进行处理，这是整数默认使用的说明符                                              |
| e    | 使用科学表示法来表示小数(用 e 来表示指数)                                                         |
| E    | 与 e 相同，但使用 E 来表示指数                                                                    |
| f    | 将小数表示为定点数                                                                                |
| F    | 与 f 相同，但对于特殊值( nan 和 inf)，使用大写表示                                                |
| g    | 自动在定点表示法和科学表示法之间做出选择。这是默认用于小数的说明符，但在默认情况下至少有 1 位小数 |
| G    | 与 g 相同，但使用大写来表示指数和特殊值                                                           |
| n    | 与 g 相同，但插入随区域而异的数字分隔符                                                           |
| o    | 将整数表示为八进制数                                                                              |
| s    | 保持字符串的格式不变，这是默认用于字符串的说明符                                                  |
| x    | 将整数表示为十六进制数并使用小写字母                                                              |
| X    | 与 x 相同，但使用大写字母                                                                         |
| %    | 将数表示为百分比值(乘以 100，按说明符 f 设置格式，再在后面加上%)                                  |

##### 宽度、精度和千位分隔符

```python
#宽度是使用整数指定的，如下所示：
>>> "{num:10}".format(num=3)
'         3'
>>> "{name:10}".format(name="Bob")
'Bob       '

#精度是使用小数指定的，如下所示：
>>> "Pi day is {pi:.2f}".format(pi=pi)
'Pi day is 3.14'

>>> "{pi:10.2f}".format(pi=pi)
' 3.14'

# 字符串
>>> "{:.5}".format("Guido van Rossum")
'Guido'


#　千位分隔符　　可使用逗号来指出你要添加千位分隔符
>>> 'One googol is {:,}'.format(10**100)
'One googol is 10,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000'

# 同时指定其他格式设置元素时，这个逗号应放在宽度和表示精度的句点之间①。
```

##### 符号、对齐和用 0 填充

在一栏中同时包含字符串和数时，你可能想修改默认对齐方式。在指定宽
度和精度的数前面，可添加一个标志。
这个标志可以是零、加号、减号或空格，其中零表示使用 0 来填充数字。

```python

>>> '{:010.2f}'.format(pi)
'0000003.14'
要指定左对齐、右对齐和居中，可分别使用<、 >和^。
>>> print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi))
3.14
  3.14
     3.14

#可以使用填充字符来扩充对齐说明符，这样将使用指定的字符而不是默认的空格来填充。
>>> "{:$^15}".format(" WIN BIG ")
'$$$ WIN BIG $$$'

# 还有更具体的说明符=，它指定将填充字符放在符号和数字之间。

>>> print('{0:10.2f}\n{1:10.2f}'.format(pi, -pi))
   3.14
   -3.14
>>> print('{0:10.2f}\n{1:=10.2f}'.format(pi, -pi))
   3.14
-  3.14

# 如果要给正数加上符号，可使用说明符+(将其放在对齐说明符后面)，而不是默认的-。如果将符号说明符指定为空格，会在正数前面加上空格而不是+。

>>> print('{0:-.2}\n{1:-.2}'.format(pi, -pi)) #默认设置
3.1
-3.1
>>> print('{0:+.2}\n{1:+.2}'.format(pi, -pi))
+3.1
-3.1
>>> print('{0: .2}\n{1: .2}'.format(pi, -pi))
 3.1
-3.1

# 需要介绍的最后一个要素是井号( #)选项，你可将其放在符号说明符和宽度之间(如果指定了这两种设置)。这个选项将触发另一种转换方式，转换细节随类型而异。例如，对于二进制、八进制和十六进制转换，将加上一个前缀。

>>> "{:b}".format(42)
'101010'
>>> "{:#b}".format(42)
'0b101010'

>>> "{:g}".format(42)
'42'
>>> "{:#g}".format(42)
'42.0000'

# 根据指定的宽度打印格式良好的价格列表

![](https://c.undf.top/images/others/Python_study.md/2022-08-15-19-01-22.png)

# result
# 这个程序的运行情况类似于下面这样：
Please enter width: 35
===================================
Item                          Price
-----------------------------------
Apples                         0.40
Pears                          0.50
Cantaloupes                    1.92
Dried Apricots (16 oz.)        8.00
Prunes (4 lbs.)               12.00
===================================

```

套娃哇！！666

### 字符串方法

字符串的方法太多了，这里只介绍一些最有用的。完整的字符串方法清单请参阅附录 B。这
里描述字符串的方法时，将列出其他相关的方法。

```python
# 字符串的方法
str.center(width[, fillchar]) # 方法center通过在两边添加填充字符(默认为空格)让字符串居中。
str.find(sub[, start[, end]]) # 方法find返回子字符串sub在字符串中第一次出现的索引，如果没有找到，则返回-1。
str.join(seq) # 方法join将序列seq中的元素用字符串str连接起来，返回连接后的字符串。 所合并序列的元素必须都是字符串
str.lower() # 方法lower将字符串转换为小写。
str.upper() # 方法upper将字符串转换为大写。
str.split(sep[, maxsplit]) # 方法split将字符串按照分隔符sep分割，返回分割后的字符串列表。
str.strip([chars]) # 方法strip删除字符串左右两边的空格。
str.replace(old, new[, max]) # 方法replace将字符串中的old子字符串替换为new子字符串，返回替换后的字符串。
str.splitlines([keepends]) # 方法splitlines将字符串按照行分割，返回分割后的字符串列表。
str.translate(table[, deletechars]) # 方法translate将字符串中的字符用表table中的对应字符替换，返回替换后的字符串。 方法translate与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。这个方法的优势在于能够同时替换多个字符，因此效率比replace高。
str.isdigit() # 方法isdigit判断字符串是否只包含数字字符。
str.isalpha() # 方法isalpha判断字符串是否只包含字母字符。
str.isalnum() # 方法isalnum判断字符串是否只包含字母和数字字符。
str.islower() # 方法islower判断字符串是否只包含小写字母。
str.isupper() # 方法isupper判断字符串是否只包含大写字母。 isalnum、 isalpha、 isdecimal、 isdigit、 isidentifier、 islower、 isnumeric、isprintable、 isspace、 istitle、 isupper。


```

#### trnaslate

```python
>>> table = str.maketrans('cs', 'kz')
如果愿意，可查看转换表的内容，但你看到的只是Unicode码点之间的映射。
>>> table
{115: 122, 99: 107}
创建转换表后，就可将其用作方法translate的参数。
>>> 'this is an incredible test'.translate(table)
'thiz iz an inkredible tezt'
```

### 小结

本章介绍了字符串的两个重要方面。

- 字符串格式设置：求模运算符( %)可用于将值合并为包含转换标志(如%s)的字符串，
  这让你能够以众多方式设置值的格式，如左对齐或右对齐，指定字段宽度和精度，添加
  符号(正号或负号)以及在左边填充 0 等。
- 字符串方法：字符串有很多方法， 有些很有用(如 split 和 join)，有些很少用到(如 istitle
  和 capitalize)。

## 字典 当索引行不通时

`phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}`

他的定义有点像结构体

```python
>>> items = [('name', 'Gumby'), ('age', 42)]
>>> d = dict(items)
>>> d
{'age': 42, 'name': 'Gumby'}
>>> d['name']
'Gumby'
# 还可使用关键字实参来调用这个函数，如下所示：
>>> d = dict(name='Gumby', age=42)
>>> d
{'age': 42, 'name': 'Gumby'}
```

### 特性

- 键的类型：字典中的键可以是整数，但并非必须是整数。字典中的键可以是任何不可变
  的类型，如浮点数(实数)、字符串或元组。
- 自动添加：即便是字典中原本没有的键，也可以给它赋值，这将在字典中创建一个新项。
  然而，如果不使用 append 或其他类似的方法，就不能给列表中没有的元素赋值。
- 成员资格：表达式 k in d(其中 d 是一个字典)查找的是键而不是值，而表达式 v in l(其
  中 l 是一个列表)查找的是值而不是索引。这看似不太一致，但你习惯后就会觉得相当自
  然。毕竟如果字典包含指定的键，检查相应的值就很容易。

> 将字符串格式设置功能用于字典

```python
>>> phonebook
{'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
>>> "Cecil's phone number is {Cecil}.".format_map(phonebook)
"Cecil's phone number is 3258."
```

### 字典方法

clear：清空字典中的所有项。
copy：返回一个字典的浅复制，而不是深复制。deepcopy：返回一个字典的深复制。
fromkeys：从指定的键值对创建一个新的字典。
get：返回指定键的值，如果值不在字典中返回默认值。方法 get 为访问字典项提供了宽松的环境。通常，如果你试图访问字典中没有的项，将引发错误。使用 get 来访问不存在的键时，没有引发异常，而是返回 None。你可指定“默认”值，这样将返回你指定的值而不是 None。

items：返回一个包含字典中的所有项的列表。

```python
>>> d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
>>> d.items()
dict_items([('url', 'http://www.python.org'), ('spam', 0), ('title', 'Python Web Site')])
```

返回值属于一种名为字典视图的特殊类型。字典视图可用于迭代(迭代将在第 5 章详细介绍)。
另外，你还可确定其长度以及对其执行成员资格检查。

视图的一个优点是不复制，它们始终是底层字典的反映，即便你修改了底层字典亦如此。

keys：返回一个包含字典中的所有键的列表。视图
pop：删除并返回字典中的一个项。`d.pop('x')`
popitem：随机删除并返回字典中的一个项。
setdefault：如果键不存在于字典中，则为它设置默认值。
update：将另一个字典的项添加到字典中。
values：返回一个包含字典中的所有值的列表。视图

### 小结

本章介绍了如下内容。

- 映射：映射让你能够使用任何不可变的对象(最常用的是字符串和元组)来标识其元素。
  Python 只有一种内置的映射类型，那就是字典。
- 将字符串格式设置功能用于字典：要对字典执行字符串格式设置操作，不能使用 format
  和命名参数，而必须使用 format_map。
- 字典方法：字典有很多方法，这些方法的调用方式与列表和字符串的方法相同。

## 条件、循环及其他语句

### 赋值魔法

1. 序列解包

```python
>>> x, y, z = 1, 2, 3
>>> print(x, y, z)
1 2 3

>>> x, y = y, x
>>> print(x, y)
2 1

>>> values = 1, 2, 3
>>> values
(1, 2, 3)
>>> x, y, z = values
>>> x
1


# 可使用星号运算符( *)来收集多余的值，这样无需确保值和变量的个数相同，如下例所示：

>>> a, b, *rest = [1, 2, 3, 4]
>>> rest
[3, 4]

# 还可将带星号的变量放在其他位置。
>>> name = "Albus Percival Wulfric Brian Dumbledore"
>>> first, *middle, last = name.split()
>>> middle
['Percival', 'Wulfric', 'Brian']


赋值语句的右边可以是任何类型的序列，但带星号的变量最终包含的总是一个列表。在变量和值的个数相同时亦如此。
>>> a, *b, c = "abc"
>>> a, b, c
('a', ['b'], 'c')

```

2. 链式赋值

```python

# 链式赋值是一种快捷方式，用于将多个变量关联到同一个值。这有点像前一节介绍的并行赋值，但只涉及一个值：
x = y = somefunction()
# 上述代码与下面的代码等价：
y = somefunction()
x = y
# 请注意，这两条语句可能与下面的语句不等价：
x = somefunction()
y = somefunction()
# 有关这方面的详细信息，请参阅5.4.6节介绍相同运算符( is)的部分。

```

3. 关键字 assert

```python

>>> age = 10
>>> assert 0 < age < 100
>>> age = -1
>>> assert 0 < age < 100
Traceback (most recent call last):
File "<stdin>", line 1, in ?
AssertionError
#如果知道必须满足特定条件，程序才能正确地运行，可在程序中添加assert语句充当检查点，这很有帮助。还可在条件后面添加一个字符串，对断言做出说明。
>>> age = -1
>>> assert 0 < age < 100, 'The age must be realistic'
Traceback (most recent call last):
File "<stdin>", line 1, in ?
AssertionError: The age must be realistic

```

4. 迭代字典

```python
# 要遍历字典的所有关键字，可像遍历序列那样使用普通的for语句。
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
print(key, 'corresponds to', d[key])
# 也可使用keys等字典方法来获取所有的键。如果只对值感兴趣，可使用d.values。你可能还
# 记得， d.items以元组的方式返回键值对。 for循环的优点之一是，可在其中使用序列解包。
for key, value in d.items():
print(key, 'corresponds to', value)
```

5. 并行迭代

有时候，你可能想同时迭代两个序列。假设有下面两个列表：

```python
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
```

如果要打印名字和对应的年龄，可以像下面这样做：

```python
for i in range(len(names)):
print(names[i], 'is', ages[i], 'years old')
```

i 是用作循环索引的变量的标准名称。一个很有用的并行迭代工具是内置函数 zip，它将两个
序列“缝合”起来，并返回一个由元组组成的序列。返回值是一个适合迭代的对象，要查看其内
容，可使用 list 将其转换为列表。

```python
>>> list(zip(names, ages))
[('anne', 12), ('beth', 45), ('george', 32), ('damon', 102)]
```

“缝合”后，可在循环中将元组解包。

```python
for name, age in zip(names, ages):
print(name, 'is', age, 'years old')
```

函数 zip 可用于“缝合”任意数量的序列。需要指出的是，当序列的长度不同时，函数 zip 将
在最短的序列用完后停止“缝合”。

```python
>>> list(zip(range(5), range(100000000)))
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
```

6. 迭代时获取索引

```python
index = 0
for string in strings:
if 'xxx' in string:
strings[index] = '[censored]'
index += 1
```

这个解决方案虽然可以接受，但看起来也有点笨拙。另一种解决方案是使用内置函数
enumerate。

```python
for index, string in enumerate(strings):
if 'xxx' in string:
strings[index] = '[censored]'
```

这个函数让你能够迭代索引 值对，其中的索引是自动提供的。

7. 循环中的 else 子句
   ```python
   from math import sqrt
   for n in range(99, 81, -1):
   root = sqrt(n)
   if root == int(root):
   print(n)
   break
   else:
   print("Didn't find it!")
   ```

在循环中使用 else 子句，可以在循环正常结束时执行，也可以在循环异常结束时执行。

### 列表推导式

```python
# 列表推导式是列表创建的另一种方式。
squares = [n ** 2 for n in range(10)]
print(squares)

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> [x*x for x in range(10) if x 3 == 0] %
[0, 9, 36, 81]

>>> [(x, y) for x in range(3) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

>>> girls = ['alice', 'bernice', 'clarice']
>>> boys = ['chris', 'arnold', 'bob']
>>> [b+'+'+g for b in boys for g in girls if b[0] == g[0]]
['chris+clarice', 'arnold+alice', 'bob+bernice']
# 这些代码将名字的首字母相同的男孩和女孩配对。

# 字典推导。

>>> squares = {i:"{} squared is {}".format(i, i**2) for i in range(10)}
>>> squares
{0: '0 squared is 0', 1: '1 squared is 1', 2: '2 squared is 4', 3: '3 squared is 9', 4: '4 squared is 16', 5: '5 squared is 25', 6: '6 squared is 36', 7: '7 squared is 49', 8: '8 squared is 64', 9: '9 squared is 81'}
# 在列表推导中， for前面只有一个表达式，而在字典推导中， for前面有两个用冒号分隔的表
# 达式。这两个表达式分别为键及其对应的值。

```

### 三人行

pass、 del 和 exec

pass 可以用来作为占位符，用于空语句块。

```python
>>> pass
```

del 可以用来删除一个对象的引用。

```python
>>> del var

# 这看似简单，但有时不太好理解。例如，在下面的示例中， x和y指向同一个列表：
>>> x = ["Hello", "world"]
>>> y = x
>>> y[1] = "Python"
>>> x
['Hello', 'Python']
# 你可能认为通过删除x，也将删除y，但情况并非如此。
>>> del x
>>> y
['Hello', 'Python']
#这是为什么呢？ x和y指向同一个列表，但删除x对y没有任何影响，因为你只删除名称x，而没有删除列表本身(值)。事实上，在Python中，根本就没有办法删除值，而且你也不需要这样
# 做，因为对于你不再使用的值， Python解释器会立即将其删除。

```

exec 可以用来执行一段代码。

```python
>>> exec("print('Hello, world!')")
Hello, world!

# eval

# exec执行一系列Python语句，而eval计算用字符串表示
# 的Python表达式的值，并返回结果( exec什么都不返回，因为它本身是条语句)。

>>> eval(input("Enter an arithmetic expression: "))
Enter an arithmetic expression: 6 + 18 * 2
42
```

### 小结

本章介绍了多种语句。

- 打印语句：你可使用 print 语句来打印多个用逗号分隔的值。如果 print 语句以逗号结尾，
  后续 print 语句将在当前行接着打印。
- 导入语句：有时候，你不喜欢要导入的函数的名称——可能是因为你已将这个名称用作
  他用。在这种情况下，可使用 import as 语句在本地重命名函数。
- 赋值语句：通过使用奇妙的序列解包和链式赋值，可同时给多个变量赋值；而通过使用
  增强赋值，可就地修改变量。
- 代码块：代码块用于通过缩进将语句编组。代码块可用于条件语句和循环中，还可用于
  函数和类定义中(这将在本书后面介绍)。
- 条件语句：条件语句根据条件(布尔表达式)决定是否执行后续代码块。通过使用 if/elif/
  else，可将多个条件语句组合起来。条件语句的一个变种是条件表达式，如 a if b else c。
- 断言：断言断定某件事(一个布尔表达式)为真，可包含说明为何必须如此的字符串。
  如果指定的表达式为假，断言将导致程序停止执行(或引发第 8 章将介绍的异常)。最好
  尽早将错误揪出来，免得它潜藏在程序中，直到带来麻烦。
- 循环：你可针对序列中的每个元素(如特定范围内的每个数)执行代码块，也可在条件
  为真时反复执行代码块。要跳过代码块中余下的代码，直接进入下一次迭代，可使用
  continue 语句；要跳出循环，可使用 break 语句。另外，你还可在循环末尾添加一个 else
  子句，它将在没有执行循环中的任何 break 语句时执行。
- 推导：推导并不是语句，而是表达式。它们看起来很像循环，因此我将它们放在循环中
  讨论。通过列表推导，可从既有列表创建出新列表，这是通过对列表元素调用函数、剔
  除不想要的函数等实现的。推导功能强大，但在很多情况下，使用普通循环和条件语句
  也可完成任务，且代码的可读性可能更高。使用类似于列表推导的表达式可创建出字典。
- pass、 del、 exec 和 eval： pass 语句什么都不做，但适合用作占位符。 del 语句用于删除变
  量或数据结构的成员，但不能用于删除值。函数 exec 用于将字符串作为 Python 程序执行。
  函数 eval 计算用字符串表示的表达式并返回结果。

## 抽象

#### 懒惰是一种美德

这里说的懒不是贬义词，而是说不做无谓的工作。

在有些语言(如 C++、 Pascal 和 Ada)中，经常需要给参数赋值并让这种修改影响函数外部的变
量。在 Python 中，没法直接这样做，只能修改参数对象本身。

#### 收集参数

参数前面的星号将提供的所有值都放在一个元组中，也就是将这些值收集起来。这样的行为
我们在 5.2.1 节见过：赋值时带星号的变量收集多余的值。它收集的是列表而不是元组中多余的值，
但除此之外，这两种用法很像。

```python
def print_params(*params):
    print(params)
>>> print_params(1, 2, 3)
(1, 2, 3)

def print_params_2(title, *params):
    print(title)
    print(params)

>>> print_params_2('Params:', 1, 2, 3)
Params:
(1, 2, 3)

```

与赋值时一样，带星号的参数也可放在其他位置(而不是最后)，但不同的是，在这种情况
下你需要做些额外的工作：使用名称来指定后续参数。

```python
>>> def in_the_middle(x, *y, z):
    print(x, y, z)

>>> in_the_middle(1, 2, 3, 4, 5, z=7)
1 (2, 3, 4, 5) 7
>>> in_the_middle(1, 2, 3, 4, 5, 7)
Traceback (most recent call last):

File "<stdin>", line 1, in <module>
TypeError: in_the_middle() missing 1 required keyword-only argument: 'z'

# 星号不会收集关键字参数。
>>> print_params_2('Hmm   ', something=42)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: print_params_2() got an unexpected keyword argument 'something'

# 要收集关键字参数，可使用两个星号。
>>> def print_params_3(**params):
    print(params)

>>> print_params_3(x=1, y=2, z=3)
{'z': 3, 'x': 1, 'y': 2}

如你所见，这样得到的是一个字典而不是元组。可结合使用这些技术。

def print_params_4(x, y, z=3, *pospar, **keypar):
print(x, y, z)
print(pospar)
print(keypar)

# 其效果与预期的相同。

>>> print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
1 2 3
(5, 6, 7)
{'foo': 1, 'bar': 2}
>>> print_params_4(1, 2)
1 2 3
()
{}
```

### 小结

本章介绍了抽象的基本知识以及函数。

- 抽象：抽象是隐藏不必要细节的艺术。通过定义处理细节的函数，可让程序更抽象。
- 函数定义：函数是使用 def 语句定义的。函数由语句块组成，它们从外部接受值(参数)，
  并可能返回一个或多个值(计算结果)。
- 参数：函数通过参数(调用函数时被设置的变量)接收所需的信息。在 Python 中，参数有
  两类：位置参数和关键字参数。通过给参数指定默认值，可使其变成可选的。
- 作用域：变量存储在作用域(也叫命名空间)中。在 Python 中，作用域分两大类：全局作
  用域和局部作用域。作用域可以嵌套。
- 递归：函数可调用自身，这称为递归。可使用递归完成的任何任务都可使用循环来完成，
  但有时使用递归函数的可读性更高。
- 函数式编程： Python 提供了一些函数式编程工具，其中包括 lambda 表达式以及函数 map、
  filter 和 reduce。

## 再谈抽象

### 对象魔法

- 多态：可对不同类型的对象执行相同的操作，而这些操作就像“被施了魔法”一样能够正常运行。
- 封装：对外部隐藏有关对象工作原理的细节。
- 继承：可基于通用类创建出专用类。

### 创建自定义类

```python
class Person:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))


class Student(Person):

class TalkingCalculator(Calculator, Talker):
      pass
```

### 深入探讨继承

要确定一个类是否是另一个类的子类，可使用内置方法 issubclass。

```python

>>> issubclass(SPAMFilter, Filter)
True
>>> issubclass(Filter, SPAMFilter)
False
```

如果你有一个类，并想知道它的基类，可访问其特殊属性**bases**。

```python
>>> SPAMFilter.__bases__
(<class __main__.Filter at 0x171e40>,)
>>> Filter.__bases__
(<class 'object'>,)
```

### 关于面向对象设计的一些思考

专门探讨面向对象程序设计的图书很多，虽然这并非本书的重点，但还是要提供一些指南。

- 将相关的东西放在一起。如果一个函数操作一个全局变量，最好将它们作为一个类的属
  性和方法。
- 不要让对象之间过于亲密。方法应只关心其所属实例的属性，对于其他实例的状态，让
  它们自己去管理就好了。
- 慎用继承，尤其是多重继承。继承有时很有用，但在有些情况下可能带来不必要的复杂
  性。要正确地使用多重继承很难，要排除其中的 bug 更难。
- 保持简单。让方法短小紧凑。一般而言，应确保大多数方法都能在 30 秒内读完并理解。
  对于其余的方法，尽可能将其篇幅控制在一页或一屏内。
  确定需要哪些类以及这些类应包含哪些方法时，尝试像下面这样做。

(1) 将有关问题的描述(程序需要做什么)记录下来，并给所有的名词、动词和形容词加
上标记。
(2) 在名词中找出可能的类。
(3) 在动词中找出可能的方法。
(4) 在形容词中找出可能的属性。
(5) 将找出的方法和属性分配给各个类。
有了面向对象模型的草图后，还需考虑类和对象之间的关系(如继承或协作)以及它们的职
责。为进一步改进模型，可像下面这样做。
(1) 记录(或设想)一系列用例，即使用程序的场景，并尽力确保这些用例涵盖了所有的功能。
(2) 透彻而仔细地考虑每个场景，确保模型包含了所需的一切。如果有遗漏，就加上；如果
有不太对的地方，就修改。不断地重复这个过程，直到对模型满意为止。
有了你认为行之有效的模型后，就可以着手编写程序了。你很可能需要修改模型或程序的某
些部分，所幸这在 Python 中很容易，请不用担心。只管按这里说的去做就好。(如果你需要更详
细的面向对象编程指南，请参阅第 19 章的推荐书目。)

### 小结

本章不仅介绍了有关 Python 语言的知识，还介绍了多个你可能一点都不熟悉的概念。下面来
总结一下。

- 对象：对象由属性和方法组成。属性不过是属于对象的变量，而方法是存储在属性中的
  函数。相比于其他函数，(关联的)方法有一个不同之处，那就是它总是将其所属的对象
  作为第一个参数，而这个参数通常被命名为 self。
- 类：类表示一组(或一类)对象，而每个对象都属于特定的类。类的主要任务是定义其
  实例将包含的方法。
- 多态：多态指的是能够同样地对待不同类型和类的对象，即无需知道对象属于哪个类就
  可调用其方法。
- 封装：对象可能隐藏(封装)其内部状态。在有些语言中，这意味着对象的状态(属性)
  只能通过其方法来访问。在 Python 中，所有的属性都是公有的，但直接访问对象的状态时
  程序员应谨慎行事，因为这可能在不经意间导致状态不一致。
- 继承：一个类可以是一个或多个类的子类，在这种情况下，子类将继承超类的所有方法。
  你可指定多个超类，通过这样做可组合正交(独立且不相关)的功能。为此，一种常见
  的做法是使用一个核心超类以及一个或多个混合超类。
- 接口和内省：一般而言，你无需过于深入地研究对象，而只依赖于多态来调用所需的方
  法。然而，如果要确定对象包含哪些方法或属性，有一些函数可供你用来完成这种工作。
- 抽象基类：使用模块 abc 可创建抽象基类。抽象基类用于指定子类必须提供哪些功能，却
  不实现这些功能。
- 面向对象设计：关于该如何进行面向对象设计以及是否该采用面向对象设计，有很多不
  同的观点。无论你持什么样的观点，都必须深入理解问题，进而创建出易于理解的设计。

## 异 常

_这是重点_

### 异常是什么

Python 使用异常对象来表示异常状态，并在遇到错误时引发异常。异常对象未被处理(或捕
获)时，程序将终止并显示一条错误消息( traceback)。

```python
>>> 1 / 0
Traceback (most recent call last):
File "<stdin>", line 1, in ?
ZeroDivisionError: integer division or modulo by zero
```

如果异常只能用来显示错误消息，就没多大意思了。但事实上，每个异常都是某个类(这里
是 ZeroDivisionError)的实例。你能以各种方式引发和捕获这些实例，从而逮住错误并采取措施，
而不是放任整个程序失败。

### 让事情沿你指定的轨道出错

正如你看到的，出现问题时，将自动引发异常。先来看看如何自主地引发异常，还有如何创
建异常，然后再学习如何处理这些异常。

#### 引发异常

引发异常的方法是使用 raise 语句。

```python
>>> raise Exception
Traceback (most recent call last):
File "<stdin>", line 1, in ?
Exception

>>> raise Exception('hyperdrive overload')
Traceback (most recent call last):
File "<stdin>", line 1, in ?
Exception: hyperdrive overload

```

| 类名              | 描述                                                             |
| ----------------- | ---------------------------------------------------------------- |
| Exception         | 几乎所有的异常类都是从它派生而来的                               |
| AttributeError    | 引用属性或给它赋值失败时引发                                     |
| OSError           | 操作系统不能执行指定的任务(如打开文件)时引发，有多个子类         |
| IndexError        | 使用序列中不存在的索引时引发，为 LookupError 的子类              |
| KeyError          | 使用映射中不存在的键时引发，为 LookupError 的子类                |
| NameError         | 找不到名称(变量)时引发                                           |
| SyntaxError       | 代码不正确时引发                                                 |
| TypeError         | 将内置操作或函数用于类型不正确的对象时引发                       |
| ValueError        | 将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适 |
| ZeroDivisionError | 在除法或求模运算的第二个参数为零时引发                           |

##### 创建自定义异常类

```python
class SomeCustomException(Exception): pass
```

#### 捕获异常

try/except 语句。

```python
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero!")


# 捕获多种异常
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero!")
except TypeError:
    print("That wasn't a number, was it?")

# 捕获多种异常的另一种方法

try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except (ZeroDivisionError, TypeError, NameError):
    print('Your numbers were bogus    ')

# 捕获对象

try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except (ZeroDivisionError, TypeError, NameError) as e:
    print('Your numbers were bogus     {}'.format(e))

# 一网打尽

try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except Exceptions as e: # 捕获所有异常
    print('Your numbers were bogus     {}'.format(e))
else: # 没有异常时执行
    print('OK, no errors')
finally: # 最后，还有finally子句，可用于在发生异常时执行清理工作。
    print('This always executes')


```

### 异常和函数

异常和函数有着天然的联系。如果不处理函数中引发的异常，它将向上传播到调用函数的地
方。如果在那里也未得到处理，异常将继续传播，直至到达主程序(全局作用域)。如果主程序
中也没有异常处理程序，程序将终止并显示栈跟踪消息。

### 异常之禅(异常与循环)

有时候，可使用条件语句来达成异常处理实现的目标，但这样编写出来的代码可能不那么自
然，可读性也没那么高。另一方面，有些任务使用 if/else 完成时看似很自然，但实际上使用
try/except 来完成要好得多。下面来看两个示例。

假设有一个字典，你要在指定的键存在时打印与之相关联的值，否则什么都不做。实现这种
功能的代码可能类似于下面这样

```python
def describe_person(person):
    print('Description of', person['name'])
    print('Age:', person['age'])
    if 'occupation' in person:
        print('Occupation:', person['occupation'])
```

如果你调用这个函数，并向它提供一个包含姓名 Throatwobbler Mangrove 和年龄 42(但不包
含职业)的字典，输出将如下：

```python

Description of Throatwobbler Mangrove
Age: 42

#如果你在这个字典中添加职业camper，输出将如下：

Description of Throatwobbler Mangrove
Age: 42
Occupation: camper
```

这段代码很直观，但效率不高(虽然这里的重点是代码简洁)，因为它必须两次查找
'occupation'键：一次检查这个键是否存在(在条件中)，另一次获取这个键关联的值，以便将
其打印出来。下面是另一种解决方案：

```python
def describe_person(person):
    print('Description of', person['name'])
    print('Age:', person['age'])
    try:
        print('Occupation:', person['occupation'])
    except KeyError: pass
```

在这里，函数直接假设存在'occupation'键。如果这种假设正确，就能省点事：直接获取并
打印值，而无需检查这个键是否存在。如果这个键不存在，将引发 KeyError 异常，而 except 子句
将捕获这个异常。

### 不那么异常的情况(警告)

```python

>>> from warnings import warn
>>> warn("I've got a bad feeling about this.")
__main__:1: UserWarning: I've got a bad feeling about this.
>>>

```

警告只显示一次。如果再次运行最后一行代码，什么事情都不会发生。
如果其他代码在使用你的模块，可使用模块 warnings 中的函数 filterwarnings 来抑制你发出
的警告(或特定类型的警告)，并指定要采取的措施，如"error"或"ignore"。

```python
>>> from warnings import filterwarnings
>>> filterwarnings("ignore")
>>> warn("Anyone out there?")
>>> filterwarnings("error")
>>> warn("Something is very wrong!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UserWarning: Something is very wrong!
```

如你所见，引发的异常为 UserWarning。发出警告时，可指定将引发的异常(即警告类别)，
但必须是 Warning 的子类。如果将警告转换为错误，将使用你指定的异常。另外，还可根据异常
来过滤掉特定类型的警告。

```PYTHON
>>> filterwarnings("error")
>>> warn("This function is really old   ", DeprecationWarning)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
DeprecationWarning: This function is really old
>>> filterwarnings("ignore", category=DeprecationWarning)
>>> warn("Another deprecation warning.", DeprecationWarning)
>>> warn("Something else.")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
UserWarning: Something else.
```

### 小结

本章介绍了如下重要主题。

- 异常对象：异常情况(如发生错误)是用异常对象表示的。对于异常情况，有多种处理
  方式；如果忽略，将导致程序终止。
- 引发异常：可使用 raise 语句来引发异常。它将一个异常类或异常实例作为参数，但你也
  可提供两个参数(异常和错误消息)。 如果在 except 子句中调用 raise 时没有提供任何参数，
  它将重新引发该子句捕获的异常。
- 自定义的异常类：你可通过从 Exception 派生来创建自定义的异常。
- 捕获异常：要捕获异常，可在 try 语句中使用 except 子句。在 except 子句中，如果没有指
  定异常类，将捕获所有的异常。你可指定多个异常类，方法是将它们放在元组中。如果
  向 except 提供两个参数，第二个参数将关联到异常对象。在同一条 try/except 语句中，可
  包含多个 except 子句，以便对不同的异常采取不同的措施。
- else 子句：除 except 子句外，你还可使用 else 子句，它在主 try 块没有引发异常时执行。
- finally：要确保代码块(如清理代码)无论是否引发异常都将执行，可使用 try/finally，
  并将代码块放在 finally 子句中。
- 异常和函数：在函数中引发异常时，异常将传播到调用函数的地方(对方法来说亦如此)。
- 警告：警告类似于异常，但(通常)只打印一条错误消息。你可指定警告类别，它们是
  Warning 的子类。

## 魔法方法、特性和迭代器

还是跟 C++一样

```python
# 重写普通方法和特殊的构造函数
class SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)
```

### INIT

#### 调用未关联的超类构造函数

本节介绍的方法主要用于解决历史遗留问题。在较新的 Python 版本中，显然应使用函数
super（这将在下一节讨论）。然而，很多既有代码使用的都是本节介绍的方法，因此你必须对
其有所了解。另外，这种方法也极具启迪意义，淋漓尽致地说明了关联方法和未关联方法之间
的差别。

```python
class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

```

在 SongBird 类中，只添加了一行，其中包含代码`Bird.__init__(self)。`先来证明这确实管用，
再解释这到底意味着什么。

```python
>>> sb = SongBird()
>>> sb.sing()
Squawk!
>>> sb.eat()
Aaaah
>>> sb.eat()
No, thanks!
```

这样做为何管用呢？对实例调用方法时，方法的参数 self 将自动关联到实例（称为关联的方
法），这样的示例你见过多个。然而，如果你通过类调用方法（如`Bird.__init__`），就没有实例
与其相关联。在这种情况下，你可随便设置参数 self。这样的方法称为未关联的。这就对本节的
标题做出了解释。
通过将这个未关联方法的 self 参数设置为当前实例，将使用超类的构造函数来初始化
SongBird 对象。这意味着将设置其属性 hungry。

#### 使用函数 super

在 Python3 中调用函数 super 时，可不提供任何参数（通常也应该这样做），而它将
像变魔术一样完成任务。

```python
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
        print('Aaaah    ')
        self.hungry = False
    else:
        print('No, thanks!')


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

# 这个新式版本与旧式版本等效：

>>> sb = SongBird()
>>> sb.sing()
Squawk!
>>> sb.eat()
Aaaah
>>> sb.eat()
No, thanks!
```

#### 使用函数 super 有何优点

在我看来，相比于直接对超类调用未关联方法，使用函数 super 更直观，但这并非其唯一
的优点。实际上，函数 super 很聪明，因此即便有多个超类，也只需调用函数 super 一次（条件
是所有超类的构造函数也使用函数 super）。另外，对于使用旧式类时处理起来很棘手的问题
（如两个超类从同一个类派生而来），在使用新式类和函数 super 时将自动得到处理。你无需知
道函数 super 的内部工作原理，但必须知道的是，使用函数 super 比调用超类的未关联构造函
数（或其他方法）要好得多。
函数 super 返回的到底是什么呢？通常，你无需关心这个问题，只管假定它返回你所需的
超类即可。实际上，它返回的是一个 super 对象，这个对象将负责为你执行方法解析。当你访
问它的属性时，它将在所有的超类（以及超类的超类，等等）中查找，直到找到指定的属性或
引发 AttributeError 异常。

### 元素访问

#### 基本的序列和映射协议

序列和映射基本上是元素（ item）的集合，要实现它们的基本行为（协议），不可变对象需
要实现 2 个方法，而可变对象需要实现 4 个。

- **len**(self)：这个方法应返回集合包含的项数，对序列来说为元素个数，对映射来说
  为键  值对数。如果**len**返回零（且没有实现覆盖这种行为的**nonzero**），对象在布
  尔上下文中将被视为假（就像空的列表、元组、字符串和字典一样）。
- **getitem**(self, key)：这个方法应返回与指定键相关联的值。对序列来说，键应该是
  0~n-1 的整数（也可以是负数，这将在后面说明），其中 n 为序列的长度。对映射来说，
  键可以是任何类型。
- **setitem**(self, key, value)：这个方法应以与键相关联的方式存储值，以便以后能够
  使用**getitem**来获取。当然，仅当对象可变时才需要实现这个方法。
- **delitem**(self, key)：这个方法在对对象的组成部分使用**del**语句时被调用，应
  删除与 key 相关联的值。同样，仅当对象可变（且允许其项被删除）时，才需要实现这个
  方法。
  对于这些方法，还有一些额外的要求。
- 对于序列，如果键为负整数，应从末尾往前数。换而言之， x[-n]应与 x[len(x)-n]等效。
- 如果键的类型不合适（如对序列使用字符串键），可能引发 TypeError 异常。
- 对于序列，如果索引的类型是正确的，但不在允许的范围内，应引发 IndexError 异常。

#### 从 list、 dict 和 str 派生

```python
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
#
>>> cl = CounterList(range(10))
>>> cl
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> cl.reverse()
>>> cl
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> del cl[3:6]
>>> cl
[9, 8, 7, 3, 2, 1, 0]
>>> cl.counter
0
>>> cl[4] + cl[2]
9
>>> cl.counter
2

```

### 其他魔法方法

特殊（魔法）名称的用途很多，前面展示的只是冰山一角。魔法方法大多是为非常高级的用
途准备的，因此这里不详细介绍。

### 特性

#### 函数 property

看不懂,再议

#### 静态方法和类方法

在 Python 2.4 中，引入了一种名为装饰器的新语法，
可用于像这样包装方法。（实际上，装饰器可用于包装任何可调用的对象，并且可用于方法和函
数。）可指定一个或多个装饰器，为此可在方法（或函数）前面使用运算符@列出这些装饰器（指
定了多个装饰器时，应用的顺序与列出的顺序相反）。

```python
class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')
    @classmethod
    def cmeth(cls):
        print('This is a class method of', cls)
# 定义这些方法后，就可像下面这样使用它们（无需实例化类）：
>>> MyClass.smeth()
This is a static method
>>> MyClass.cmeth()
This is a class method of <class '__main__.MyClass'>

```

在 Python 中，静态方法和类方法以前一直都不太重要，主要是因为从某种程度上说，总是可
以使用函数或关联的方法替代它们，而且早期的 Python 版本并不支持它们。因此，虽然较新的代
码没有大量使用它们，但它们确实有用武之地（如工厂函数），因此你或许应该考虑使用它们。

#### `__getattr__`、`__setattr__`等方法

可以拦截对对象属性的所有访问企图，其用途之一是在旧式类中实现特性（在旧式类中，函
数 property 的行为可能不符合预期）。要在属性被访问时执行一段代码，必须使用一些魔法方法。
下面的四个魔法方法提供了你需要的所有功能（在旧式类中，只需使用后面三个）。

- **getattribute**(self, name)：在属性被访问时自动调用（只适用于新式类）。
- **getattr**(self, name)：在属性被访问而对象没有这样的属性时自动调用。
- **setattr**(self, name, value)：试图给属性赋值时自动调用。
- **delattr**(self, name)：试图删除属性时自动调用。
  相比函数 property，这些魔法方法使用起来要棘手些（从某种程度上说，效率也更低），但
  它们很有用，因为你可在这些方法中编写处理多个特性的代码。然而，在可能的情况下，还是使
  用函数 property 吧。
  再来看前面的 Rectangle 示例，但这里使用的是魔法方法：

```python
class Rectangle:
    def __init__ (self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self. __dict__[name] = value
    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()
```

如你所见，这个版本需要处理额外的管理细节。对于这个代码示例，需要注意如下两点。

- 即便涉及的属性不是 size，也将调用方法**setattr**。因此这个方法必须考虑如下两种
  情形：如果涉及的属性为 size，就执行与以前一样的操作；否则就使用魔法属性**dict**。
  **dict**属性是一个字典，其中包含所有的实例属性。之所以使用它而不是执行常规属性
  赋值，是因为旨在避免再次调用**setattr**，进而导致无限循环。
- 仅当没有找到指定的属性时，才会调用方法**getattr**。这意味着如果指定的名称不是
  size，这个方法将引发 AttributeError 异常。这在要让类能够正确地支持 hasattr 和 getattr
  等内置函数时很重要。如果指定的名称为 size，就使用前一个实现中的表达式。

### 迭代器

本书前面粗略地提及了迭代器（和可迭代对象），本节将更详细地介绍。对于魔法方法，这
里只介绍**iter**，它是迭代器协议的基础。

#### 迭代器协议

迭代（ iterate）意味着重复多次，就像循环那样。本书前面只使用 for 循环迭代过序列和字典，
但实际上也可迭代其他对象：实现了方法**iter**的对象。

方法**iter**返回一个迭代器，它是包含方法**next**的对象，而调用这个方法时可不提供
任何参数。当你调用方法**next**时，迭代器应返回其下一个值。如果迭代器没有可供返回的值，
应引发 StopIteration 异常。你还可使用内置的便利函数 next，在这种情况下， next(it)与
it.**next**()等效。

这有什么意义呢？为何不使用列表呢？因为在很多情况下，使用列表都有点像用大炮打蚊
子。例如，如果你有一个可逐个计算值的函数，你可能只想逐个地获取值，而不是使用列表一次
性获取。这是因为如果有很多值，列表可能占用太多的内存。但还有其他原因：使用迭代器更通
用、更简单、更优雅。下面来看一个不能使用列表的示例，因为如果使用，这个列表的长度必须
是无穷大的！

这个“列表”为斐波那契数列，表示该数列的迭代器如下：

```python
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self
```

注意到这个迭代器实现了方法**iter**，而这个方法返回迭代器本身。在很多情况下，都在
另一个对象中实现返回迭代器的方法**iter**，并在 for 循环中使用这个对象。但推荐在迭代器
中也实现方法**iter**（并像刚才那样让它返回 self），这样迭代器就可直接用于 for 循环中。

首先，创建一个 Fibs 对象。

```python
>>> fibs = Fibs()
然后就可在for循环中使用这个对象，如找出第一个大于1000的斐波那契数。
>>> for f in fibs:
    if f > 1000:
    print(f)
    break

1597

```

这个循环之所以会停止，是因为其中包含 break 语句；否则，这个 for 循环将没完没了地执行。

#### 从迭代器创建序列

除了对迭代器和可迭代对象进行迭代（通常这样做）之外，还可将它们转换为序列。在可以
使用序列的情况下，大多也可使用迭代器或可迭代对象（诸如索引和切片等操作除外）。一个这
样的例子是使用构造函数 list 显式地将迭代器转换为列表。

```python
>>> class TestIterator:
        value = 0
        def __next__(self):
            self.value += 1
            if self.value > 10: raise StopIteration
            return self.value
        def __iter__(self):
            return self

>>> ti = TestIterator()
>>> list(ti)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### 生成器

生成器是一个相对较新的 Python 概念。由于历史原因，它也被称为简单生成器（ simple
generator）。生成器和迭代器可能是近年来引入的最强大的功能，但生成器是一个相当复杂的概
念，你可能需要花些功夫才能明白其工作原理和用途。虽然生成器让你能够编写出非常优雅的代
码，但请放心，无论编写什么程序，都完全可以不使用生成器。
生成器是一种使用普通函数语法定义的迭代器。生成器的工作原理到底是什么呢？通过示例
来说明最合适。下面先来看看如何创建和使用生成器，然后再看看幕后的情况。

#### 创建生成器

生成器创建起来与函数一样简单。你现在肯定厌烦了老套的斐波那契数列，所以下面换换口
味，创建一个将嵌套列表展开的函数。这个函数将一个类似于下面的列表作为参数：

`nested = [[1, 2], [3, 4], [5]]`

换而言之，这是一个列表的列表。函数应按顺序提供这些数字，下面是一种解决方案：160 第 9 章 魔法方法、特性和迭代器

```python
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
```

这个函数的大部分代码都很简单。它首先迭代所提供嵌套列表中的所有子列表，然后按顺序
迭代每个子列表的元素。倘若最后一行为 print(element)，这个函数将容易理解得多，不是吗？

在这里，你没有见过的是 yield 语句。包含 yield 语句的函数都被称为生成器。这可不仅仅是
名称上的差别，生成器的行为与普通函数截然不同。差别在于，*生成器不是使用 return 返回一个值，而是可以生成多个值，每次一个。*每次使用 yield 生成一个值后，函数都将冻结，即在此停
止执行，等待被重新唤醒。被重新唤醒后，函数将从停止的地方开始继续执行。
为使用所有的值，可对生成器进行迭代。

> > > nested = [[1, 2], [3, 4], [5]]
> > > for num in flatten(nested):
> > > ... print(num)
> > > ...
> > > 1
> > > 2
> > > 3
> > > 4
> > > 5
> > > 或
> > > list(flatten(nested))
> > > [1, 2, 3, 4, 5]

#### 递归式生成器

前一节设计的生成器只能处理两层的嵌套列表，这是使用两个 for 循环来实现的。如果要处
理任意层嵌套的列表，该如何办呢？例如，你可能使用这样的列表来表示树结构（也可以使用特
定的树类，但策略是相同的）。对于每层嵌套，都需要一个 for 循环，但由于不知道有多少层嵌套，
你必须修改解决方案，使其更灵活。该求助于递归了。

```python
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
```

调用 flatten 时，有两种可能性（处理递归时都如此）： 基线条件和递归条件。在基线条件下，
要求这个函数展开单个元素（如一个数）。在这种情况下， for 循环将引发 TypeError 异常（因为
你试图迭代一个数），而这个生成器只生成一个元素。

然而，如果要展开的是一个列表（或其他任何可迭代对象），你就需要做些工作：遍历所有
的子列表（其中有些可能并不是列表）并对它们调用 flatten，然后使用另一个 for 循环生成展开
后的子列表中的所有元素。这可能看起来有点不可思议，但确实可行。

```python
>>> list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))
[1, 2, 3, 4, 5, 6, 7, 8]
```

然而，这个解决方案存在一个问题。如果 nested 是字符串或类似于字符串的对象，它就属于
序列，因此不会引发 TypeError 异常，可你并不想对其进行迭代。

要处理这种问题，必须在生成器开头进行检查。要检查对象是否类似于字符串，最简单、最
快捷的方式是，尝试将对象与一个字符串拼接起来，并检查这是否会引发 TypeError 异常 ①。添加
这种检查后的生成器如下：

```python

def flatten(nested):
    try:
    # 不迭代类似于字符串的对象：
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

```

如你所见，如果表达式 nested + ''引发了 TypeError 异常，就忽略这种异常；如果没有引发
TypeError 异常，内部 try 语句中的 else 子句将引发 TypeError 异常，这样将在外部的 excpet 子句中
原封不动地生成类似于字符串的对象。明白了吗？
下面的示例表明，这个版本也可用于字符串：

> > > list(flatten(['foo', ['bar', ['baz']]]))
> > > ['foo', 'bar', 'baz']
> > > 请注意，这里没有执行类型检查：我没有检查 nested 是否是字符串，而只是检查其行为是否
> > > 类似于字符串，即能否与字符串拼接。对于这种检查，一种更自然的替代方案是，使用 isinstance
> > > 以及字符串和类似于字符串的对象的一些抽象超类，但遗憾的是没有这样的标准类。另外，即便
> > > 是对 UserString 来说，也无法检查其类型是否为 str。

#### 通用生成器

如果你按前面的例子做了，就差不多知道了如何使用生成器。你知道，生成器是包含关键字
yield 的函数，但被调用时不会执行函数体内的代码，而是返回一个迭代器。每次请求值时，都
将执行生成器的代码，直到遇到 yield 或 return。 yield 意味着应生成一个值，而 return 意味着生
成器应停止执行（即不再生成值；仅当在生成器调用 return 时，才能不提供任何参数）。

换而言之，生成器由两个单独的部分组成： 生成器的函数和生成器的迭代器。生成器的函数
是由 def 语句定义的，其中包含 yield。生成器的迭代器是这个函数返回的结果。用不太准确的话
说，这两个实体通常被视为一个，通称为生成器

```python
>>> def simple_generator():
yield 1
...
>>> simple_generator
<function simple_generator at 153b44>
>>> simple_generator()
<generator object at 1510b0>

```

对于生成器的函数返回的迭代器，可以像使用其他迭代器一样使用它

#### 生成器的方法

在生成器开始运行后，可使用生成器和外部之间的通信渠道向它提供值。这个通信渠道包含
如下两个端点。

- 外部世界：外部世界可访问生成器的方法 send，这个方法类似于 next， 但接受一个参数（要
  发送的“消息”，可以是任何对象）。
- 生成器：在挂起的生成器内部， yield 可能用作表达式而不是语句。换而言之，当生成器重新运行时， yield 返回一个值——通过 send 从外部世界发送的值。如果使用的是 next，
  yield 将返回 None。
  请注意，仅当生成器被挂起（即遇到第一个 yield）后，使用 send（而不是 next）才有意义。
  要在此之前向生成器提供信息，可使用生成器的函数的参数。

生成器还包含另外两个方法。
方法 throw：用于在生成器中（ yield 表达式处）引发异常，调用时可提供一个异常类型、一
个可选值和一个 traceback 对象。
方法 close：用于停止生成器，调用时无需提供任何参数。
方 法 close （ 由 Python 垃圾收 集 器在 需要 时 调用 ）也 是 基于 异常 的 ：在 yield 处 引 发
GeneratorExit 异常。因此如果要在生成器中提供一些清理代码，可将 yield 放在一条 try/finally
语句中。如果愿意，也可捕获 GeneratorExit 异常，但随后必须重新引发它（可能在清理后）、引
发其他异常或直接返回。对生成器调用 close 后，再试图从它那里获取值将导致 RuntimeError 异常。

### 八皇后问题

学习各种魔法方法后，该付诸应用了。本节将演示如何使用生成器来解决一个经典的编程
问题。

对于逐步得到结果的复杂递归算法，非常适合使用生成器来实现。要在不使用生成器的情况
下实现这些算法，通常必须通过额外的参数来传递部分结果，让递归调用能够接着往下计算。通
过使用生成器，所有的递归调用都只需生成其负责部分的结果。前面的递归版 flatten 就是这样
做的，你可使用这种策略来遍历图结构和树结构。
然而，在有些应用程序中，你不能马上得到答案。你必须尝试多次，且在每个递归层级中都
如此。打个现实生活中的比方吧，假设你要去参加一个很重要的会议。你不知道会议在哪里召开，
但前面有两扇门，而会议室就在其中一扇门的后面。你选择进入左边那扇门后，又看到两扇门。
你再次选择进入左边那扇门，但发现走错了。因此你往回走，并进入右边那扇门，但发现也走错
了。因此你继续往回走到起点，现在可以尝试进入右边那扇门。

#### 问题

这是一个深受大家喜爱的计算机科学谜题：你需要将 8 个皇后放在棋盘上，条件是任何一个
皇后都不能威胁其他皇后，即任何两个皇后都不能吃掉对方。怎样才能做到这一点呢？应将这些
皇后放在什么地方呢？
这是一个典型的回溯问题：在棋盘的第一行尝试为第一个皇后选择一个位置，再在第二行尝
试为第二个皇后选择一个位置，依次类推。在发现无法为一个皇后选择合适的位置后，回溯到前
一个皇后，并尝试为它选择另一个位置。最后，要么尝试完所有的可能性，要么找到了答案。
在前面描述的问题中，只有 8 个皇后，但这里假设可以有任意数量的皇后，从而更像现实世
界的回溯问题。如何解决这个问题呢？如果你想自己试一试，就不要再往下读了，因为马上就会
提供解决方案。

- 注意 对于这个问题，可找到效率高得多的解决方案。如果你想深入了解，在网上搜索就可找到大量的信息。

#### 状态表示

可简单地使用元组（或列表）来表示可能的解（或其一部分），其中每个元素表示相应行中
皇后所在的位置（即列）。因此，如果 state[0] == 3，就说明第 1 行的皇后放在第 4 列（还记得吧，
我们从 0 开始计数）。在特定的递归层级（特定的行），你只知道上面各皇后的位置，因此状态元
组的长度小于 8（即皇后总数）。

#### 检测冲突

先来做些简单的抽象。要找出没有冲突（即任何一个皇后都吃不到其他皇后）的位置组合，
首先必须定义冲突是什么。为何不使用一个函数来定义呢？
函数 conflict 接受（用状态元组表示的）既有皇后的位置，并确定下一个皇后的位置是否会
导致冲突。

```python
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False
```

参数 nextX 表示下一个皇后的水平位置（ x 坐标，即列），而 nextY 为下一个皇后的垂直位置（ y
坐标，即行）。这个函数对既有的每个皇后执行简单的检查：如果下一个皇后与当前皇后的 x 坐标
相同或在同一条对角线上，将发生冲突，因此返回 True；如果没有发生冲突，就返回 False。比
较难理解的是下面的表达式：
`abs(state[i] - nextX) in (0, nextY - i)`
如果下一个皇后和当前皇后的水平距离为 0（在同一列）或与它们的垂直距离相等（位于一
条对角线上），这个表达式就为真；否则为假。

#### 基线条件

八皇后问题解决起来有点棘手，但通过使用生成器并不太难。然而，如果你不熟悉递归，就
很难自己想出这里的解决方案。另外，这个解决方案的效率不是特别高，因此皇后非常多时，其
速度可能有点慢。
下面先来看基线条件：最后一个皇后。对于这个皇后，你想如何处理呢？假设你想找出所有
可能的解——给定其他皇后的位置，可将这个皇后放在什么位置（可能什么位置都不行）？可以
这样编写代码。

```python
def queens(num, state):
    if len(state) == num-1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos
```

这段代码的意思是，如果只剩下最后一个皇后没有放好，就遍历所有可能的位置，并返回那
些不会引发冲突的位置。参数 num 为皇后总数，而参数 state 是一个元组，包含已放好的皇后的位
置。例如，假设总共有 4 个皇后，而前 3 个皇后的位置分别为 1、 3 和 0，如图 9-1 所示。（现在不用
关心白色的皇后。）
![](images/others/Python_study.md/2022-08-13-15-32-46.png)

从该图可知，每个皇后都占据一行，而皇后的位置是从 0 开始编号的（ Python 中通常如此）。

`>>> list(queens(4, (1, 3, 0)))`

代码的效果很好。这里使用 list 旨在让生成器生成所有的值。在这个示例中，只有一个位置
符合条件。在图 9-1 中，在这个位置放置了一个白色皇后。（请注意，颜色没有什么特殊含义，不
是程序的一部分。）

#### 递归条件

现在来看看这个解决方案的递归部分。处理好基线条件后，可在递归条件中假设来自更低层级（编号更大的皇后）的结果都是正确的。因此，只需在函数 queens 的前述实现中给 if 语句添加
一个 else 子句。
你希望递归调用返回什么样的结果呢？你希望它返回当前行下面所有皇后的位置，对吧？假
设位置是以元组的方式返回的，因此需要修改基线条件，使其返回一个（长度为 1 的）元组，但
这将在后面处理。
因此，对于递归调用，向它提供的是由当前行上面的皇后位置组成的元组。对于当前皇后的
每个合法位置，递归调用返回的是由下面的皇后位置组成的元组。为了让这个过程不断进行下去，
只需将当前皇后的位置插入返回的结果开头，如下所示：

```python
...
else:
    for pos in range(num):
        if not conflict(state, pos):
            for result in queens(num, state + (pos,)):
                yield (pos,) + result

```

这里的 for pos 和 if not conflict 部分与前面相同，因此可以稍微简化一下代码。另外，还
可给参数指定默认值。

```python
def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result
```

如果你觉得这些代码难以理解，用自己的话来描述其作用可能会有所帮助。另外，你可能还
记得(pos,)中的逗号必不可少（不能仅用圆括号将 pos 括起），这样得到的才是元组。
生成器 queens 提供了所有的解（即所有合法的皇后位置组合）。

```python
>>> list(queens(3))
[]
>>> list(queens(4))
[(1, 3, 0, 2), (2, 0, 3, 1)]
>>> for solution in queens(8):
... print solution
...
(0, 4, 7, 5, 2, 6, 1, 3)
(0, 5, 7, 2, 6, 3, 1, 4)
...
(7, 2, 0, 5, 1, 4, 6, 3)
(7, 3, 0, 2, 5, 1, 6, 4)
>>>

# 如果运行queens时将参数num设置为8，将快速显示大量的解。下面看看有多少个解。

>>> len(list(queens(8)))
92
```

### 小结

本章介绍的内容很多，下面来总结一下。

- 新式类和旧式类： Python 类的工作方式在不断变化。较新的 Python 2 版本有两种类，其中
  旧式类正在快速退出舞台。新式类是 Python 2.2 引入的，提供了一些额外的功能，如支持
  函数 super 和 property，而旧式类不支持。要创建新式类，必须直接或间接地继承 object
  或设置**metaclass**。
- 魔法方法： Python 中有很多特殊方法，其名称以两个下划线开头和结尾。这些方法的功能
  各不相同，但大都由 Python 在特定情况下自动调用。 例如**init**是在对象创建后调用的。
- 构造函数：很多面向对象语言中都有构造函数，对于你自己编写的每个类，都可能需要
  为它实现一个构造函数。构造函数名为**init**，在对象创建后被自动调用。
- 重写：类可重写其超类中定义的方法（以及其他任何属性），为此只需实现这些方法即可。
  要调用被重写的版本，可直接通过超类调用未关联版本（旧式类），也可使用函数 super
  来调用（新式类）。
- 序列和映射：要创建自定义的序列或映射，必须实现序列和映射协议指定的所有方法，
  其中包括**getitem**和**setitem**等魔法方法。通过从 list（或 UserList）和 dict（或
  UserDict）派生，可减少很多工作量。
- 迭代器：简单地说， 迭代器是包含方法**next**的对象，可用于迭代一组值。没有更多的
  值可供迭代时，方法**next**应引发 StopIteration 异常。 可迭代对象包含方法**iter**，
  它返回一个像序列一样可用于 for 循环中的迭代器。通常，迭代器也是可迭代的，即包含
  返回迭代器本身的方法**iter**。
- 生成器： 生成器的函数是包含关键字 yield 的函数，它在被调用时返回一个生成器，即一
  种特殊的迭代器。要与活动的生成器交互，可使用方法 send、 throw 和 close。
- 八皇后问题：八皇后问题是个著名的计算机科学问题，使用生成器可轻松地解决它。这
  个问题要求在棋盘上放置 8 个皇后，并确保任何两个皇后都不能相互攻击。

### 预告

至此，你学习了 Python 语言的大部分知识，但为何本书后面还有这么多章呢？因为需要学习
的知识还有很多，大都是关于 Python 如何以各种方式与外部联系的。另外，还有测试、扩展、打
包和一些具体项目。本书还远没有到结束的时候。

## 开箱即用

### 模块

#### 模块就是程序

模块并不是用来执行操作（如打印文本）的，而是用于定义
变量、函数、类等。鉴于定义只需做一次，因此导入模块多次和导入一次的效果相同。

#### 模块是用来下定义的

一个包含有条件地执行的测试代码的模块

```python
# hello4.py
def hello():
    print("Hello, world!")
def test():
    hello()
if __name__ == '__main__':
    test()


```

#### 让模块可用

1. 将模块放在正确的位置
2. 告诉解释器到哪里去查找 办法之一是直接修改 sys.path，但这种做法不常见。标准做法是将模块所在的目录包含在环境变量 PYTHONPATH 中。

#### 包

为组织模块，可将其编组为包（ package）。包其实就是另一种模块，但有趣的是它们可包含其他模块。

| 文件/目录                    | 描述                   |
| ---------------------------- | ---------------------- |
| ~/python/                    | PYTHONPATH 中的目录    |
| ~/python/drawing/            | 包目录（包 drawing）   |
| ~/python/drawing/**init**.py | 包代码（模块 drawing） |
| ~/python/drawing/colors.py   | 模块 colors            |
| ~/python/drawing/shapes.py   | 模块 shapes            |

```python
import drawing # (1) 导入drawing包
import drawing.colors # (2) 导入drawing包中的模块colors
from drawing import shapes # (3) 导入模块shapes
```

- 如果要打印的数据结构太大，一行容纳不下，可使用模块 pprint 中的函数 pprint（而不是普通 print 语句）。 pprint 是个卓越的打印函数，能够更妥善地打印输出。

### 探索模块

绍一些标准库模块前，先来说说如何探索模块。这是一种很有用的技能， 因为在你的 Python
程序员职业生涯中，将遇到很多很有用的模块，而这里无法一一介绍。当前的标准库很大，足以
编写专著来论述（市面上也确实有这样的专著），而且还在不断增大。每个新 Python 版本都新增
了模块，通常还会对一些既有模块进行细微的修改和改进。另外，你在网上肯定会找到一些很有
用的模块。如果能快速而轻松地理解它们，编程工作将有趣得多。

#### 模块包含什么

要探索模块，最直接的方式是使用 Python 解释器进行研究。为此，首先需要将模块导入。假
设你听说有一个名为 copy 的标准模块。

> > > import copy
> > > 没有引发异常，说明确实有这样的模块。但这个模块是做什么用的呢？它都包含些什么呢？

1. 使用 dir()要查明模块包含哪些东西，可使用函数 dir，它列出对象的所有属性（对于模块，它列出所有的函数、类、变量等）。
2. 变量**all**
   为何要提供它呢？旨在定义模块的公有接口。具体地说，它告诉解释器从这个模块导入所有的名称意味着什么。因此，如果你使用如下代码：from copy import \*将只能得到变量**all**中列出的 4 个函数。要导入 PyStringMap，必须显式地：导入 copy 并使用 copy.PyStringMap； 或者使用 from copy import PyStringMap。
3. help()
4. **doc**模块的文档字符串。

#### 阅读源代码

1. **file**模块的存放路径。

### 标准库

一些深受欢迎的模块

#### sys

| 函数/变描   | 述                                               |
| ----------- | ------------------------------------------------ |
| argv        | 命令行参数，包括脚本名                           |
| exit([arg]) | 退出当前程序，可通过可选参数指定返回值或错误消息 |
| modules     | 一个字典，将模块名映射到加载的模块               |
| path        | 一个列表，包含要在其中查找模块的目录的名称       |
| platform    | 一个平台标识符，如 sunos5 或 win32               |
| stdin       | 标准输入流——一个类似于文件的对象                 |
| stdout      | 标准输出流——一个类似于文件的对象                 |
| stderr      | 标准错误流——一个类似于文件的对象                 |

#### os

| 函数/变量       | 描述                          |
| --------------- | ----------------------------- | ------ | -------------- |
| environ         | 包含环境变量的映射            |
| system(command) | 在子 shell 中执行操作系统命令 |
| sep             | 路径中使用的分隔符            |
| pathsep         | 分隔不同路径的分隔符          |
| linesep         | 行分隔符（                    | '\n'、 | '\r'或'\r\n'） |
| urandom(n)      | 返回 n 个字节的强加密随机数据 |

#### fileinput

| 函数           | 描述                           |
| -------------- | ------------------------------ | ---------- | ------------------------ |
| input([files[, | inplace[,                      | backup]]]) | 帮助迭代多个输入流中的行 |
| filename()     | 返回当前文件的名称             |
| lineno()       | 返回（累计的）当前行号         |
| filelineno()   | 返回在当前文件中的行号         |
| isfirstline()  | 检查当前行是否是文件中的第一行 |
| isstdin()      | 检查最后一行是否来自 sys.stdin |
| nextfile()     | 关闭当前文件并移到下一个文件   |
| close()        | 关闭序列                       |

#### 集合、堆和双端队列

1. 集合

```python
>>> set(range(10))
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

可使用序列（或其他可迭代对象）来创建集合，也可使用花括号显式地指定。请注意，不能
仅使用花括号来创建空集合，因为这将创建一个空字典。

相反，必须在不提供任何参数的情况下调用 set。集合主要用于成员资格检查，因此将忽略重复的元素：
与字典一样，集合中元素的排列顺序是不确定的，因此不能依赖于这一点。

除成员资格检查外，还可执行各种标准集合操作（你可能在数学课上学过），如并集和交集，
为此可使用对整数执行按位操作的运算符（参见附录 B）。例如，要计算两个集合的并集，可对其
中一个集合调用方法 union，也可使用按位或运算符|

```python
>>> a = {1, 2, 3}
>>> b = {2, 3, 4}
>>> a.union(b)
{1, 2, 3, 4}
>>> a | b
{1, 2, 3, 4}

# 还有其他一些方法和对应的运算符，这些方法的名称清楚地指出了其功能：
>>> c = a & b
>>> c.issubset(a)
True
>>> c <= a
True
>>> c.issuperset(a)
False
>>> c >= a
False
>>> a.intersection(b)
{2, 3}
>>> a & b
{2, 3}
>>> a.difference(b)
{1}
>>> a - b
{1}
>>> a.symmetric_difference(b)
{1, 4}
>>> a ^ b
{1, 4}
>>> a.copy()
{1, 2, 3}
>>> a.copy() is a
False

```

集合是可变的，因此不能用作字典中的键。另一个问题是，集合只能包含不可变（可散列）
的值，因此不能包含其他集合。由于在现实世界中经常会遇到集合的集合，因此这可能是个问题。
所幸还有 frozenset 类型，它表示不可变（可散列）的集合

```python
>>> a = set()
>>> b = set()
>>> a.add(b)
Traceback (most recent call last):
File "<stdin>", line 1, in ?
TypeError: set objects are unhashable
>>> a.add(frozenset(b))
```

构造函数 frozenset 创建给定集合的副本。在需要将集合作为另一个集合的成员或字典中的
键时， frozenset 很有用

2. 堆
   另一种著名的数据结构是堆（ heap），它是一种优先队列。优先队列让你能够以任意顺序添
   加对象，并随时（可能是在两次添加对象之间）找出（并删除）最小的元素。相比于列表方法 min，
   这样做的效率要高得多。

实际上， Python 没有独立的堆类型，而只有一个包含一些堆操作函数的模块。这个模块名为
heapq（其中的 q 表示队列），它包含 6 个函数（如表 10-5 所示），其中前 4 个与堆操作直接相关。必
须使用列表来表示堆对象本身。

| 函 数               | 描 述                           |
| ------------------- | ------------------------------- | --------------------------- |
| heappush(heap,x)    | 将 x 压入堆中                   |
| heappop(heap)       | 从堆中弹出最小的元素            |
| heapify(heap)       | 让列表具备堆特征                |
| heapreplace(heap,x) | 弹出最小的元素，并将 x 压入堆中 |
| nlargest(n,         | iter)                           | 返回 iter 中 n 个最大的元素 |
| nsmallest(n,iter)   | 返回 iter 中 n 个最小的元素     |

函数 heappush 用于在堆中添加一个元素。请注意，不能将它用于普通列表，而只能用于使用
各种堆函数创建的列表。原因是元素的顺序很重要（虽然元素的排列顺序看起来有点随意，并没
有严格地排序）。

```python
>>> from heapq import *
>>> from random import shuffle
>>> data = list(range(10))
>>> shuffle(data)
>>> heap = []
>>> for n in data:
... heappush(heap, n)
...
>>> heap
[0, 1, 3, 6, 2, 8, 4, 7, 9, 5]
>>> heappush(heap, 0.5)
>>> heap
[0, 0.5, 3, 6, 1, 8, 4, 7, 9, 5, 2]

```

元素的排列顺序并不像看起来那么随意。它们虽然不是严格排序的，但必须保证一点：位置
i 处的元素总是大于位置 i // 2 处的元素（反过来说就是小于位置 2 _ i 和 2 _ i + 1 处的元素）。
这是底层堆算法的基础，称为堆特征（ heap property）。

```python
>>> heappop(heap)
0
>>> heappop(heap)
0.5
>>> heappop(heap)
1
>>> heap
[2, 5, 3, 6, 9, 8, 4, 7]

```

函数 heapify 通过执行尽可能少的移位操作将列表变成合法的堆（即具备堆特征）。如果你的
堆并不是使用 heappush 创建的，应在使用 heappush 和 heappop 之前使用这个函数。

```python
>>> heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
>>> heapify(heap)
>>> heap
[0, 1, 5, 3, 2, 7, 9, 8, 4, 6]

```

函数 heapreplace 用得没有其他函数那么多。它从堆中弹出最小的元素，再压入一个新元素。
相比于依次执行函数 heappop 和 heappush，这个函数的效率更高。

```python
>>> heapreplace(heap, 0.5)
0
>>> heap
[0.5, 1, 5, 3, 2, 7, 9, 8, 4, 6]
>>> heapreplace(heap, 10)
0.5
>>> heap
[1, 2, 5, 3, 6, 7, 9, 8, 4, 10]
```

至此，模块 heapq 中还有两个函数没有介绍： nlargest(n, iter)和 nsmallest(n, iter)， :分
别用于找出可迭代对象 iter 中最大和最小的 n 个元素。这种任务也可通过先排序（如使用函数
sorted）再切片来完成，但堆算法的速度更快，使用的内存更少（而且使用起来也更容易）。

3. 双端队列（及其他集合）

在需要按添加元素的顺序进行删除时，双端队列很有用。在模块 collections 中，包含类型
deque 以及其他几个集合（ collection）类型。
与集合（ set）一样，双端队列也是从可迭代对象创建的，它包含多个很有用的方法。

```python
>>> from collections import deque
>>> q = deque(range(5))
>>> q.append(5)
>>> q.appendleft(6)
>>> q
deque([6, 0, 1, 2, 3, 4, 5])
>>> q.pop()
5
>>> q.popleft()
6
>>> q.rotate(3)
>>> q
deque([2, 3, 4, 0, 1])
>>> q.rotate(-1)
>>> q
deque([3, 4, 0, 1, 2])

```

双端队列很有用，因为它支持在队首（左端）高效地附加和弹出元素，而使用列表无法这样做。
另外，还可高效地旋转元素（将元素向右或向左移，并在到达一端时环绕到另一端）。双端队列对
象还包含方法 extend 和 extendleft，其中 extend 类似于相应的列表方法，而 extendleft 类似于
appendleft。请注意，用于 extendleft 的可迭代对象中的元素将按相反的顺序出现在双端队列中。

#### time

模块 time 包含用于获取当前时间、操作时间和日期、从字符串中读取日期、将日期格式化为
字符串的函数。

| 函数              | 描述                               |
| ----------------- | ---------------------------------- |
| asctime([tuple])  | 将时间元组转换为字符串             |
| localtime([secs]) | 将秒数转换为表示当地时间的日期元组 |
| mktime(tuple)     | 将时间元组转换为当地时间           |
| sleep(secs)       | 休眠（什么都不做）secs 秒          |

strptime(string[,format])将字符串转换为时间元组
time() | 当前时间（从新纪元开始后的秒数，以 UTC 为准）

#### random

| 函数                           | 描述                                        |
| ------------------------------ | ------------------------------------------- |
| random()                       | 返回一个 0~1（含）的随机实数                |
| getrandbits(n)                 | 以长整数方式返回 n 个随机的二进制位         |
| uniform(a,b)                   | 返回一个 a~b（含）的随机实数                |
| randrange([start],stop,[step]) | 从 range(start,stop,step)中随机地选择一个数 |
| choice(seq)                    | 从序列 seq 中随机地选择一个元素             |
| shuffle(seq[,random])          | 就地打乱序列 seq                            |
| sample(seq,n)                  | 从序列 seq 中随机地选择 n 个值不同的元素    |

#### shelve 和 json

1. 一个潜在的陷阱
   至关重要的一点是认识到 shelve.open 返回的对象并非普通映射，如下例所示：

```python
>>> import shelve
>>> s = shelve.open('test.dat')
>>> s['x'] = ['a', 'b', 'c']
>>> s['x'].append('d')
>>> s['x']
['a', 'b', 'c']

```

'd'到哪里去了呢？
这很容易解释：当你查看 shelf 对象中的元素时，将使用存储版重建该对象，而当你将一个
元素赋给键时，该元素将被存储。在上述示例中，发生的事情如下。

- 列表['a', 'b', 'c']被存储到 s 的'x'键下。
- 获取存储的表示，并使用它创建一个新列表，再将'd'附加到这个新列表末尾，但这个修
  改后的版本未被存储！
- 最后，再次获取原来的版本——其中没有'd'。
  要正确地修改使用模块 shelve 存储的对象，必须将获取的副本赋给一个临时变量，并在修改
  这个副本后再次存储 ①：

```python
>>> temp = s['x']
>>> temp.append('d')
>>> s['x'] = temp
>>> s['x']
['a', 'b', 'c', 'd']

```

还有另一种避免这个问题的办法：将函数 open 的参数 writeback 设置为 True。这样，从 shelf
对象读取或赋给它的所有数据结构都将保存到内存（缓存）中，并等到你关闭 shelf 对象时才将
它们写入磁盘中。如果你处理的数据不多，且不想操心这些问题，将参数 writeback 设置为 True
可能是个不错的主意。在这种情况下，你必须确保在处理完毕后将 shelf 对象关闭。为此，一种
办法是像处理打开的文件那样，将 shelf 对象用作上下文管理器，这将在下一章讨论。

#### re

| 函数                               | 描述                                   |
| ---------------------------------- | -------------------------------------- |
| compile(pattern[,flags])           | 根据包含正则表达式的字符串创建模式对象 |
| search(pattern,string[,flags])     | 在字符串中查找模式                     |
| match(pattern,string[,flags])      | 在字符串开头匹配模式                   |
| split(pattern,string[,maxsplit=0]) | 根据模式来分割字符串                   |

findall(pattern,string) 返回一个列表，其中包含字符串中所有与模式匹配的子串
sub(pat,repl,string[,count=0]) | 将字符串中与模式 pat 匹配的子串都替换为 repl
escape(string) | 对字符串中所有的正则表达式特殊字符都进行转义

#### 其他有趣的标准模块

- argparse：在 UNIX 中，运行命令行程序时常常需要指定各种选项（ 开关）， Python 解释器
  就是这样的典范。这些选项都包含在 sys.argv 中，但要正确地处理它们绝非容易。模块
  argparse 使得提供功能齐备的命令行界面易如反掌。
- cmd：这个模块让你能够编写类似于 Python 交互式解释器的命令行解释器。你可定义命令，
  让用户能够在提示符下执行它们。或许可使用这个模块为你编写的程序提供用户界面？
- csv： CSV 指的是逗号分隔的值（ comma-seperated values），很多应用程序（如很多电子表
  格程序和数据库程序）都使用这种简单格式来存储表格数据。这种格式主要用于在不同
  的程序之间交换数据。模块 csv 让你能够轻松地读写 CSV 文件，它还以非常透明的方式处
  理 CSV 格式的一些棘手部分。
- datetime：如果模块 time 不能满足你的时间跟踪需求，模块 datetime 很可能能够满足。
  datetime 支持特殊的日期和时间对象，并让你能够以各种方式创建和合并这些对象。相比
  于模块 time，模块 datetime 的接口在很多方面都更加直观。
- difflib：这个库让你能够确定两个序列的相似程度，还让你能够从很多序列中找出与指
  定序列最为相似的序列。例如，可使用 difflib 来创建简单的搜索程序。
- enum：枚举类型是一种只有少数几个可能取值的类型。很多语言都内置了这样的类型，如
  果你在使用 Python 时需要这样的类型，模块 enum 可提供极大的帮助。
- functools：这个模块提供的功能是，让你能够在调用函数时只提供部分参数（部分求值，
  partial evaluation），以后再填充其他的参数。在 Python 3.0 中，这个模块包含 filter 和 reduce。
- hashlib：使用这个模块可计算字符串的小型“签名”（数）。计算两个不同字符串的签名
  时，几乎可以肯定得到的两个签名是不同的。你可使用它来计算大型文本文件的签名，
  这个模块在加密和安全领域有很多用途 ①。
- itertools：包含大量用于创建和合并迭代器（或其他可迭代对象）的工具，其中包括可
  以串接可迭代对象、创建返回无限连续整数的迭代器（类似于 range，但没有上限）、反复
  遍历可迭代对象以及具有其他作用的函数。
- logging：使用 print 语句来确定程序中发生的情况很有用。要避免跟踪时出现大量调试输
  出，可将这些信息写入日志文件中。这个模块提供了一系列标准工具，可用于管理一个
  或多个中央日志，它还支持多种优先级不同的日志消息。
- statistics：计算一组数的平均值并不那么难，但是要正确地获得中位数，以确定总体标
  准偏差和样本标准偏差之间的差别，即便对于偶数个元素来说，也需要费点心思。在这
  种情况下，不要手工计算，而应使用模块 statistics！
- timeit、 profile 和 trace：模块 timeit（和配套的命令行脚本）是一个测量代码段执行时
  间的工具。这个模块暗藏玄机，度量性能时你可能应该使用它而不是模块 time。模块
  profile（和配套模块 pstats）可用于对代码段的效率进行更全面的分析。模块 trace 可帮
  助你进行覆盖率分析（即代码的哪些部分执行了，哪些部分没有执行），这在编写测试代
  码时很有用。

### 小结

本章介绍了模块：如何创建模块、如何探索模块以及如何使用 Python 标准库中的一些模块。

- 模块：模块基本上是一个子程序，主要作用是定义函数、类和变量等。模块包含测试代
  码时，应将这些代码放在一条检查 name == '**main**'的 if 语句中。如果模块位于环境变
  量 PYTHONPATH 包含的目录中，就可直接导入它；要导入存储在文件 foo.py 中的模块，可使
  用语句 import foo。
- 包：包不过是包含其他模块的模块。包是使用包含文件**init**.py 的目录实现的。
- 探索模块：在交互式解释器中导入模块后，就可以众多不同的方式对其进行探索，其中
  包括使用 dir、查看变量**all**以及使用函数 help。文档和源代码也是获取信息和洞见的
  极佳来源。
- 标准库： Python 自带多个模块，统称为标准库。本章介绍了其中的几个。
- sys：这个模块让你能够访问多个与 Python 解释器关系紧密的变量和函数。
- os：这个模块让你能够访问多个与操作系统关系紧密的变量和函数。
- fileinput：这个模块让你能够轻松地迭代多个文件或流的内容行。
- sets、 heapq 和 deque：这三个模块提供了三种很有用的数据结构。内置类型 set 也实现
  了集合。
- time：这个模块让你能够获取当前时间、操作时间和日期以及设置它们的格式。
- random：这个模块包含用于生成随机数，从序列中随机地选择元素，以及打乱列表中元
  素的函数。
- shelve：这个模块用于创建永久性映射，其内容存储在使用给定文件名的数据库中。
- re：支持正则表达式的模块。
  如果你想更深入地学习模块，再次建议浏览“Python 库参考手册”，它读起来真的很有趣。

## 文件

### 打开文件

```python
>>> f = open('somefile.txt', 'r')
>>> f.read()
'Hello World!'
>>> f.close()
```

文件模式

| 值  | 描述                                   |
| --- | -------------------------------------- |
| 'r' | 读取模式（默认值）                     |
| 'w' | 写入模式                               |
| 'x' | 独占写入模式                           |
| 'a' | 附加模式                               |
| 'b' | 二进制模式（与其他模式结合使用）       |
| 't' | 文本模式（默认值，与其他模式结合使用） |
| '+' | 读写模式（与其他模式结合使用）         |

通常， Python 使用通用换行模式。在这种模式下，后面将讨论的 readlines 等方法能够识别所有合法的换行符（ '\n'、 '\r'和'\r\n'）。如果要使用这种模式，同时禁止自动转换，可将关键字参数 newline 设置为空字符串，如 open(name, newline='')。如果要指定只将'\r'或'\r\n'视为合法的行尾字符，可将参数 newline 设置为相应的行尾字符。这样，读取时不会对行尾字符进行转换，但写入时将把'\n'替换为指定的行尾字符。

### 小结

- 类似于文件的对象：类似于文件的对象是支持 read 和 readline（可能还有 write 和 writelines）等方法的对象。
- 打开和关闭文件：要打开文件，可使用函数 open，并向它提供一个文件名。如果要确保即便发生错误时文件也将被关闭，可使用 with 语句。
- 模式和文件类型：打开文件时，还可指定模式，如'r'（读取模式）或'w'（写入模式）。通过在模式后面加上'b'，可将文件作为二进制文件打开，并关闭 Unicode 编码和换行符替换。
- 标准流：三个标准流（模块 sys 中的 stdin、 stdout 和 stderr）都是类似于文件的对象，它们实现了 UNIX 标准 I/O 机制（ Windows 也提供了这种机制）。
- 读取和写入：要从文件或类似于文件的对象中读取，可使用方法 read；要执行写入操作，可使用方法 write。
- 读取和写入行：要从文件中读取行， 可使用 readline 和 readlines；要写入行， 可使用 writelines。
- 迭代文件内容：迭代文件内容的方法很多，其中最常见的是迭代文本文件中的行，这可通过简单地对文件本身进行迭代来做到。还有其他与较旧 Python 版本兼容的方法，如使用readlines。

## 图形用户界面

`import tkinter as tk`

同样，下面来复习一下本章介绍的内容。
- 图形用户界面（ GUI）： GUI有助于让应用程序对用户更友好。并非所有的程序都需要GUI，
但只要程序需要与用户交互， GUI就可能很有帮助。
- Tkinter： Tkinter是一个跨平台的Python GUI工具包，成熟而且使用广泛。
布局：通过指定组件的几何属性，很容易对其进行定位，但要确保它们在父窗口的大小
发生变化时做出正确的反应，就必须使用布局管理器。
- 事件处理： GUI工具包中用户触发事件执行的操作。要发挥作用，程序可能需要响应某些
事件，否则用户将无法与之交互。在Tkinter中，要给组件添加事件处理程序，可使用方
法bind。

## 数据库支持

### Python 数据库 API

#### 全局变量
变量名 | 描述
----|---
apilevel | 使用的Python | DB | API版本
threadsafety | 模块的线程安全程度如何
paramstyle | 在SQL查询中使用哪种参数风格

#### 异常
异常 | 超类 | 描述
---|----|---
StandardError | 所有异常的超类
Warning | StandardError | 发生非致命问题时引发
Error | StandardError | 所有错误条件的超类
InterfaceError | Error | 与接口（而不是数据库）相关的错误
DatabaseError | Error | 与数据库相关的错误的超类
DataError | DatabaseError | 与数据相关的问题，如值不在合法的范围内
OperationalError | DatabaseError | 数据库操作内部的错误
IntegrityError | DatabaseError | 关系完整性遭到破坏，如键未通过检查
InternalError | DatabaseError | 数据库内部的错误，如游标无效
ProgrammingError | DatabaseError | 用户编程错误，如未找到数据库表
NotSupportedError | DatabaseError | 请求不支持的功能，如回滚

#### 连接和游标

参数名 | 描述 | 是否可选
----|----|-----
dsn | 数据源名称，具体含义随数据库而异 | 否
user | 用户名 | 是
password | 用户密码 | 是
host | 主机名 | 是
database | 数据库名称 | 是

##### 游标对象方法

名称 | 描述
---|---
callproc(name[,params]) | 使用指定的参数调用指定的数据库过程（可选）
close() | 关闭游标。关闭后游标不可用
execute(oper[,params]) | 执行一个SQL操作——可能指定参数
executemany(oper,pseq) | 执行指定的SQL操作多次，每次都序列中的一组参数
fetchone() | 以序列的方式取回查询结果中的下一行；如果没有更多的行，就返回None
fetchmany([size]) | 取回查询结果中的多行，其中参数size的值默认为arraysize
fetchall() | 以序列的序列的方式取回余下的所有行
nextset() | 跳到下一个结果集，这个方法是可选的
setinputsizes(sizes) | 用于为参数预定义内存区域
setoutputsize(size[,col]) | 为取回大量数据而设置缓冲区长度

##### 游标对象的属性

名称 | 描述
---|---
description 由结果列描述组成的序列（只读）
rowcount | 结果包含的行数（只读）
arraysize fetchmany返回的行数，默认为1

#### 类型

名称 | 描述
---|---
Date(year,month,day) | 创建包含日期值的对象
Time(hour,minute,second) | 创建包含时间值的对象
Timestamp(y,mon,d,h,min,s) | 创建包含时间戳的对象
DateFromTicks(ticks) | 根据从新纪元开始过去的秒数创建包含日期值的对象
TimeFromTicks(ticks) | 根据从新纪元开始过去的秒数创建包含时间值的对象
imestampFromTicks(ticks) | 根据从新纪元开始过去的秒数创建包含时间戳的对象
Binary(string) | 创建包含二进制字符串值的对象
STRING | 描述基于字符串的列（如CHAR）
BINARY | 描述二进制列（如LONG或RAW）
NUMBER | 描述数字列
DATETIME | 描述日期/时间列
ROWID | 描述行ID列

### SQLite 和 PySQLite

前面说过，可用的SQL数据库引擎有很多，它们都有相应的Python模块。这些数据库引擎大
都作为服务器程序运行，连安装都需要有管理员权限。为降低Python DB API的使用门槛，我选
择了一个名为SQLite的小型数据库引擎。它不需要作为独立的服务器运行，且可直接使用本地文
件，而不需要集中式数据库存储机制。

### 小结

- Python DB API：这个API定义了一个简单的标准化接口，所有数据库包装器模块都必须
遵循它，这让编写使用多个不同数据库的程序更容易。
- 连接：连接对象表示到SQL数据库的通信链路，使用方法cursor可从连接获得游标。你还
可使用连接对象来提交或回滚事务。使用完数据库后，就可将连接关闭了。
- 游标：游标用于执行查询和查看结果。可逐行取回查询结果，也可一次取回很多（或全
部）行。
- 类型和特殊值： DB API指定了一组构造函数和特殊值的名称。构造函数用于处理日期和
时间对象，还有二进制数据对象；而特殊值用于表示关系型数据库的类型，如STRING、
NUMBER和DATETIME。
- SQLite：这是一个小型的嵌入式SQL数据库，标准Python发行版中包含其Python包装器，
即模块sqlite3。这个数据库速度快、易于使用，且不要求搭建专门的服务器。

## 网络编程

### 几个网络模块

#### 模块 socket


```python
# 代码清单14-1 最简单的服务器
import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()

# 代码清单14-2 最简单的客户端
import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
print(s.recv(1024))
```
#### 模块 urllib 和 urllib2
1. 打开远程文件

```python
>>> from urllib.request import urlopen
>>> webpage = urlopen('http://www.python.org')
```
urlopen返回的类似于文件的对象支持方法close、 read、 readline和readlines，还支持迭
代等。


2. 获取远程文件

函数urlopen返回一个类似于文件的对象，可从中读取数据。如果要让urllib替你下载文件，
并将其副本存储在一个本地文件中，可使用urlretrieve。这个函数不返回一个类似于文件的对
象，而返回一个格式为(filename, headers)的元组，其中filename是本地文件的名称（由urllib
自动创建），而headers包含一些有关远程文件的信息（这里不会介绍headers，如果你想更深入地
了解它，请在有关urllib的标准库文档中查找urlretrieve）。如果要给下载的副本指定文件名，
可通过第二个参数来提供。
urlretrieve('http://www.python.org', 'C:\\python_webpage.html')


#### 其他模块

模块 | 描述
---|---
asynchat | 包含补充asyncore的功能（参见第24章）
asyncore | 异步套接字处理程序（参见第24章）
cgi | 基本的CGI支持（参见第15章）
Cookie | Cookie对象操作，主要用于服务器
cookielib | 客户端Cookie支持
email | 电子邮件（包括MIME）支持
ftplib | FTP客户端模块
gopherlib | Gopher客户端模块
httplib | HTTP | 客户端模块
imaplib | IMAP4客户端模块
mailbox | 读取多种邮箱格式
mailcap | 通过mailcap文件访问MIME配置
mhlib | 访问MH邮箱
nntplib | NNTP客户端模块（参见第23章）
poplib | POP客户端模块
robotparser | 解析Web服务器robot文件
SimpleXMLRPCServer | 一个简单的XML-RPC服务器（参见第27章）
smtpd | SMTP服务器模块
smtplib | SMTP客户端模块
telnetlib | Telnet客户端模块
urlparse | 用于解读URL
xmlrpclib | XML-RPC客户端支持（参见第27章）


### SocketServer 及相关的类

模块SocketServer是标准库提供的服务器框架的基石，这个框架包括
BaseHTTPServer、 SimpleHTTPServer、 CGIHTTPServer、 SimpleXMLRPCServer和DocXMLRPCServer等服
务器，它们在基本服务器的基础上添加了各种功能。


等等...

- 套接字和模块socket：套接字是让程序（进程）能够通信的信息通道，这种通信可能需要
通过网络进行。模块socket让你能够在较低的层面访问客户端套接字和服务器套接字。服
务器套接字在指定的地址处监听客户端连接，而客户端套接字直接连接到服务器。
- urllib和urllib2：这些模块让你能够从各种服务器读取和下载数据，为此你只需提供指
向数据源的URL即可。模块urllib是一种比较简单的实现，而urllib2功能强大、可扩展
性极强。这两个模块都通过诸如urlopen等函数来完成工作。
- 框架SocketServer：这个框架位于标准库中，包含一系列同步服务器基类，让你能够轻松
地编写服务器。它还支持使用CGI的简单Web（ HTTP）服务器。如果要同时处理多个连
接，必须使用支持分叉或线程化的混合类。
- select和poll：这两个函数让你能够在一组连接中找出为读取和写入准备就绪的连接。这
意味着你能够以循环的方式依次为多个连接提供服务，从而营造出同时处理多个连接的
假象。另外，相比于线程化或分叉，虽然使用这两个函数编写的代码要复杂些，但解决
方案的可伸缩性和效率要高得多。
- Twisted：这是Twisted Matrix Laboratories开发的一个框架，功能丰富而复杂，支持大多数
主要的网络协议。虽然这个框架很大且其中使用的一些成例看起来宛如天书，但其基本
用法简单而直观。框架Twisted也是异步的，因此效率和可伸缩性都非常高。对很多自定
义网络应用程序来说，使用Twisted来开发很可能是最佳的选择。


## Python和Web
本章讨论Python Web编程的一些方面。 Web编程涉及的范围极广，为激发你的学习兴趣，这里挑选了其中三个重要的主题：屏幕抓取、 CGI和mod_python。

### 屏幕抓取

屏幕抓取是通过程序下载网页并从中提取信息的过程。这种技术很有用，在网页中有你要在
程序中使用的信息时，就可使用它。当然，如果网页是动态的，即随时间而变化，这就更有用了。
如果网页不是动态的，你可手工下载一次并提取其中的信息。（当然，最理想的情况是，可通过
Web服务来获取这些信息，这将在本章后面讨论。）

```python
from urllib.request import urlopen
import re
p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = urlopen('http://python.org/jobs').read().decode()
for url, name in p.findall(text):
print('{} ({})'.format(name, url))
```

正则表达式一点都不容易理解。如果HTML代码和查询都更复杂，正则表达式将更难以理解和维护。

它对付不了独特的HTML内容，如CDATA部分和字符实体（如&amp;）。遇到这样的东西时，这个程序很可能束手无策。

#### Tidy 和 XHTML 解析

Python标准库为解析HTML和XML等结构化格式提供了强大的支持（参见“Python库参考手
册”中的Structured Markup Processing Tools部分）。 XML和XML解析将在第22章更深入地讨论，
这里只介绍处理XHTML所需的工具。 XHTML是HTML 5规范描述的两种具体语法之一，也是一
种XML格式。这里介绍的大部分内容也适用于HTML。

### 小结

- 屏幕抓取：指的是自动下载网页并从中提取信息。程序Tidy及其库版本是很有用的工具，可用来修复格式糟糕的HTML，然后使用HTTML解析器进行解析。另一种抓取方式是使
用Beautiful Soup，即便面对混乱的输入，它也可以处理。
- CGI：通用网关接口是一种创建动态网页的方式，这是通过让Web服务器运行、与客户端程序通信并显示结果而实现的。模块cgi和cgitb可用于编写CGI脚本。 CGI脚本通常是在HTML表单中调用的。
- Flask：一个简单的Web框架，让你能够将代码作为Web应用发布，同时不用过多操心Web部分。
- Web应用框架：要使用Python开发复杂的大型Web应用， Web应用框架必不可少。对简单的项目来说， Flask是不错的选择；但对于较大的项目，你可能应考虑使用Django或TurboGears。
- Web服务： Web服务之于程序犹如网页之于用户。你可以认为， Web服务让你能够以更抽象的方式进行网络编程。常用的Web服务标准包括RSS（以及与之类似的RDF和Atom）、XML-RPC和SOAP。


## 测试基础

### 先测试再编码
要避免代码在开发途中被淘汰，必须能够应对变化并具备一定的灵活性，因此为程序的各个
部分编写测试至关重要（这称为单元测试），而且是应用程序设计工作的重要组成部分。极限编
程先锋引入了“测试一点点，再编写一点点代码”的理念。这种理念与直觉不太相符，却很管用，
胜过与直觉一致的“编写一点点代码，再测试一点点”的做法。

#### 准确的需求说明

#### 做好应对变化的准备

#### 测试四步曲
(1) 确定需要实现的新功能。可将其记录下来，再为之编写一个测试。
(2) 编写实现功能的框架代码，让程序能够运行（不存在语法错误之类的问题），但测试依然无法通过。测试失败是很重要的，因为这样你才能确定它可能失败。如果测试有错误，导致在任
何情况下都能成功（这样的情况我遇到过很多次），那么它实际上什么都没有测试。不断重复这
个过程：确定测试失败后，再试图让它成功。
(3) 编写让测试刚好能够通过的代码。在这个阶段，无需完全实现所需的功能，而只要让测试能够通过即可。这样，在整个开发阶段，都能够让所有的测试通过（首次运行测试时除外），即便是刚着手实现功能时亦如此。
(4) 改进（ 重构）代码以全面而准确地实现所需的功能，同时确保测试依然能够成功。提交代码时，必须确保它们处于健康状态，即没有任何测试是失败的。测试驱动编程倡导者都是这么说的。我有时会在当前正在编写的代码处留下一个失败的测试，作为提醒自己的待办事项或未完事项。然而，与人合作开发时，这种做法真的很糟糕。在任何情况下，都不应将存在失败测试的代码提交到公共代码库。

### 测试工具

你可能觉得，编写大量测试来确保程序的每个细节都没问题很繁琐。好消息是标准库可助你
一臂之力。有两个杰出的模块可替你自动完成测试过程。
- unittest：一个通用的测试框架。
- doctest：一个更简单的模块，是为检查文档而设计的，但也非常适合用来编写单元测试。
下面先来看看doctest，从它开始是个非常不错的选择。

#### 性能分析

- 测试驱动编程：大致而言，测试驱动编程意味着先测试再编码。有了测试，你就能信心
满满地修改代码，这让开发和维护工作更加灵活。
- 模块doctest和unittest：需要在Python中进行单元测试时，这些工具必不可少。模块
doctest设计用于检查文档字符串中的示例，但也可轻松地使用它来设计测试套件。为让
测试套件更灵活、结构化程度更高，框架unittest很有帮助。
- PyChecker和PyLint：这两个工具查看源代码并指出潜在（和实际）的问题。它们检查代
码的方方面面——从变量名太短到永远不会执行的代码段。你只需编写少量的代码，就可将它们加入测试套件，从而确保所有修改和重构都遵循了你采用的编码标准。
- 性能分析：如果你很在乎速度，并想对程序进行优化（仅当绝对必要时才这样做），应首
先进行性能分析：使用模块profile或cProfile来找出代码中的瓶颈。

## 扩展Python

Python什么都能做，真的是这样。这门语言功能强大，但有时候速度有点慢。例如，如果要
编写模拟某种核反应的程序或为下一部《星球大战》电影渲染图形，企图使用Python来编写这样
的高性能代码可能不是很好的选择。 Python的目标是易于使用以及帮助提高开发速度，这种灵活
性是以牺牲效率为代价的。对大多数常见的编程任务来说， Python无疑足够快，但如果你真的很
在乎速度， C、 C++、 Java和Julia等语言通常要快好几个数量级。

### 鱼和熊掌兼得

对于坚信速度至上的读者，我并不鼓励你只使用C语言进行开发。虽然只使用C语言能提高
程序本身的速度，但肯定会降低编程速度。因此你需要考虑哪一点更重要：是快速编写好程序，
还是很久以后终于编写出了一个速度极快的程序。如果Python的速度足以满足需求，使用C等低
级语言带来的痛苦将让这样的选择毫无意义（除非还有其他需求，比如程序将在不适合使用
Python的嵌入式设备中运行）。
本章讨论确实需要进一步提升速度的情形。在这种情况下，最佳的解决方案可能不是完全转
向C语言（或其他中低级语言），我建议你采用下面的方法（这可满足众多的速度至上需求）。
(1) 使用Python开发原型（有关原型开发的详细信息，请参阅第19章）。
(2) 对程序进行性能分析以找出瓶颈（有关测试，请参阅第16章）。
(3) 使用C（或者C++、 C#、 Java、 Fortran等）扩展重写瓶颈部分。
这样得到的架构（包含一个或多个C语言组件的Python框架）将非常强大，因为它兼具这两
门语言的优点。关键在于选择正确的工具来完成每项任务，这样既能获得使用高级语言（ Python）
开发复杂系统的好处，又能使用低级语言（ C）来开发较小（还可能较简单）但速度至关重要的
组件。

如果编码前就知道系统的哪部分将是瓶颈，可以（而且可能应该）在设计原型时就确保可轻
松地替换这些关键部分。对于这个观点，可能使用下面的提示来阐述更合适。

最终你可能发现并不需要使用C扩展来替换这些瓶颈（这可能是因为运行程序的计算机的速
度更高了），但至少存在选择的空间。
扩展能够找到用武之地的另一种常见情形是遗留代码。你可能想重用一些代码，但这些代码
是使用其他语言（如C）编写的。在这种情况下，可将这些代码“包装”起来（编写一个提供合
适接口的小型C语言库），并使用这个包装器来创建Python扩展。
在接下来的几节中，我将简要地介绍如何扩展Python的经典C语言实现（为此可手工编写所
有的代码，也可使用工具SWIG），以及如何扩展其他两种实现： Jython和IronPython。另外，还
将讨论访问外部代码的其他方式。

### 小结
扩展Python是个庞大的主题，本章只对其做了蜻蜓点水式的介绍，涉及的内容如下。
- 扩展理念： Python扩展的主要用途有两个——利用既有（遗留）代码和提高瓶颈部分的速
度。从头开始编写代码时，请尝试使用Python建立原型，找出其中的瓶颈并在需要时使用
扩展来替换它们。预先将潜在的瓶颈封装起来大有裨益。
- Jython和IronPython：对这些Python实现进行扩展很容易，使用底层语言（对于Jython，
为Java；对于IronPython，为C#和其他.NET语言）以库的方式实现扩展后，就可在Python
中使用它们了。
- 扩展方法：有很多用于扩展代码或提高其速度的工具，有的让你更轻松地在Python程序中
嵌入C语言代码，有的可提高数字数组操作等常见运算的速度，有的可提高Python本身的
速度。这样的工具包括SWIG、 Cython、 Weave、 NumPy、 ctypes和subprocess。
- SWIG： SWIG是一款自动为C语言库生成包装代码的工具。包装代码自动处理Python C
API，使你不必自己去做这样的工作。使用SWIG是最简单、最流行的扩展Python的方式
之一。
- 使用Python/C API：可手工编写可作为共享库直接导入到Python中的C语言代码。为此，
必须遵循Python/C API：对于每个函数，你都需要负责完成引用计数、提取参数以及创建
返回值等工作；另外，还需编写将C语言库转换为模块的代码，包括列出模块中的函数以
及创建模块初始化函数。

## 程序打包

本章重点介绍Setuptools，因为这是每个Python程序员都要用到的工具。实际上， Setuptools
并非只能用于创建基于脚本的Python安装程序，还可用于编译扩展。另外，通过将其与扩展py2exe
和py2app结合起来使用，还可创建独立的Windows和macOS可执行程序。


### 小结
至此，你知道了如何创建带GUI安装程序的专业级软件或自动生成.tar.gz文件。现对本章介
绍的概念总结如下。
- Setuptools： Setuptools工具包让你能够编写安装脚本。根据约定，这种安装脚本被命名
为setup.py。使用这种脚本，可安装模块、包和扩展。
- Setuptools的命令：可使用多个命令来运行setup.py脚本，如build、 build_ext、 install、
sdist和bdist。
- 编译扩展：可使用Setuptools来自动编译C语言扩展，并让Setuptools自动确定Python安装
位置以及该使用哪个编译器。还可让它自动运行SWIG。
- 可执行的二进制文件： Setuptools扩展py2exe可用来从Python程序创建可执行的Windows
二进制文件以及其他一些文件（可使用安装程序方便地安装）。无需单独安装Python解释
器，就可运行这些.exe文件。在macOS中，扩展py2app提供了与py2exe类似的功能。


## 趣味编程

### 配置

### 日志

```python
import logging
logging.basicConfig(level=logging.INFO, filename='mylog.log')
logging.info('Starting program')
logging.info('Trying to divide 1 by 0')
print(1 / 0)
```
### 如果你已不胜其烦

你可能认为： “这些是挺好，但编写简单的小程序时，我绝不会在这些方面花费太多精力。
配置、测试和日志，这些听起来真的很烦。”
你说得没错，编写简单的程序时确实不需要这些东西。即便开发的项目很大，刚开始也可能
并不需要所有这些东西。我要说的是，你至少需要某种测试程序的方式（这在第16章讨论过），
虽然它可能不是基于自动化单元测试的。例如，如果你要编写一个自动制作咖啡的程序，必须得
有个咖啡壶才能测试这个程序是否管用。
在后面介绍项目的章节中，我不会编写完整的测试套件和复杂的日志工具，而只是通过一些
简单的测试用例来证明程序管用，仅此而已。如果你发现某个项目的核心理念很有趣，应再进一
步，尝试对其进行改进和扩展；而在改进和扩展的过程中，你就必须考虑本章提及的问题。例如，
添加配置机制是否是个好主意？是不是需要编写更完整的测试套件？如何做完全由你决定。

### 如果你想深入学习

- Andrew Hunt和David Thomas的著作《程序员修炼之道》。
- Martin Fowler等的著作《重构》 ①。
- 四人组Erich Gamma、 Richard Helm、 Ralph Johnson和John Vlissides的著作《设计模式》。
- Kent Beck的著作《测试驱动开发》。
- Eric S. Raymond的著作《 UNIX编程艺术》 ②。
- Thomas H. Cormen等的著作《算法导论》。
- 高德纳的著作《计算机程序设计艺术》（卷1~卷3） ③。
- Peter Van Roy和Seif Haridi的著作Concepts, Techniques, and Models of Computer Programming。
就算不详细阅读这些著作（我反正没有详细阅读），随便翻翻也将让你深受启迪。


### 小结

本章介绍了一些通用的Python编程原则和技巧，我将它们统称为“有趣的编程”。下面是其
中一些要点。
- 灵活性：设计和编程时，应以灵活性为目标。随着对所面临问题了解得越来越深入，你
应心甘情愿乃至随时准备修改程序的方方面面，不要固守最初的想法。
- 原型设计：要深入了解问题和可能的实现方案，一个重要的技巧是编写程序的简化版本，
以了解它是如何工作的。使用Python编写原型非常容易，使用众多其他语言编写一个原型
所需的时间足以让你用Python编写多个原型。即便如此，除非万不得已，否则不要推倒重
来，因为重构通常是更佳的解决方案。
- 配置：通过提取程序中的常量，可让以后修改程序变得更容易。通过将这些常量放在配
置文件中，让用户能够配置程序，使其按自己希望的方式行事。通过使用环境变量和命
令行选项，可进一步提高程序的可配置性。
- 日志：日志对找出程序存在的问题或监视其行为大有裨益。你可自己动手使用print语句
实现简单的日志，但最安全的做法是使用标准库中的模块logging。

## 至此 结束