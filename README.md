# Python Learning Notes
### Tables of contents
1. [List](#list)
2. [Files I/O](#Files I/O)

###### Files I/O
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
The results are the same, but the second method - a file object iterator is preferred, which can save 
memory resources. The `open()`function returns a file object, which is an iterator.
