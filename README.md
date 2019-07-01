# Python Learning Notes
### Tables of contents
1. [List](#list)
2. [Files I/O](#Files I/O)

##### Regular Expression
1. re.match() VS re.findall() VS re.search()
Let's see the example below:
```python
import re
str1 = 'this is a test for match and findall'
print(re.match(r'test', str1))
print(re.findall(r'test', str1))
```
The output:
```
None
['test']
```
That's because:
* `re.match()` will find the match from the beginning of a string, in this example 'test' does not match 
'this is xxxx'
* `re.search()` will find the first match from anywhere of a string, but only the first against your pattern.
* `re.findall()`will find the match from anywhere of a string. Note it returns a list of matched strings. If there are groups(surrounded by braces) in pattern, it
will return a list of tuples.
```python
import re

str1 = 'this is a test for group 5566 and groups in RE' \
       'another test for groups 68775' \
       'last test for groupsss 7787'
result_3_grp = re.findall(r'test (\w+) (\w*) (\d+)', str1)
result_no_grp = re.findall(r'test \w+ \w* \d+', str1)
result_1_grp = re.findall(r'test \w+ \w* (\d+)', str1)
print(result_3_grp)
print(result_no_grp)
print(result_1_grp)
```
Output:
```
[('for', 'group', '5566'), ('for', 'groups', '68775'), ('for', 'groupsss', '7787')]
['test for group 5566', 'test for groups 68775', 'test for groupsss 7787']
['5566', '68775', '7787']
```
* In other words, `re.match('pattern')` equals `re.findall('^pattern')`

2. 

##### Files I/O
1. Use `with` syntax, so that files can be automatically colsed.
```python
with open('data.txt', 'r') as f:
    for line in f:
        print(line)
```
2. Use iterator to output files.
```python
# Method 1:
for line in open('filename').readlines():
    print(line, end='')
```
```python
# Method 2:
for line in open('filename'):
    print(line, end='')
```
The results are the same, but the second method is preferred, it can save 
memory resources. The `open()`function returns a file object, which is an iterator.
