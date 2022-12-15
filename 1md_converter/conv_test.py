import unittest
from main import *

class TestConverter(unittest.TestCase):
    def test_prepare_new_md_content_empty(self):
        old_md_content = None
        new_md_code = """## hello world optional
    
 depending on the input number, write hello world, its part or number
    
```python
def helloWorld(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print('hello world')
        elif i % 3 == 0:
            print('hello')
        elif i % 5 == 0:
            print('world')
        else:
            print(i)
```"""
        new_md_link ='+ [hello world optional](#hello-world-optional)'
        self.assertEqual(prepare_new_md_content(new_md_link, new_md_code, old_md_content), """+ [hello world optional](#hello-world-optional)
<!---md_file_delimiter--->

## hello world optional
    
 depending on the input number, write hello world, its part or number
    
```python
def helloWorld(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print('hello world')
        elif i % 3 == 0:
            print('hello')
        elif i % 5 == 0:
            print('world')
        else:
            print(i)
```""")

    def test_prepare_new_md_content(self):
        old_md_content = """+ [hello world optional](#hello-world-optional)
<!---md_file_delimiter--->

## hello world optional
    
 depending on the input number, write hello world, its part or number
    
```python
def helloWorld(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print('hello world')
        elif i % 3 == 0:
            print('hello')
        elif i % 5 == 0:
            print('world')
        else:
            print(i)
```
"""
        new_md_code = """## ones
    
 list consisting of 0 and 1. Find the length of the maximum continuous subsequence consisting of 1
    
```python
def ones(lst):
    k = 0
    max_seq = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            k += 1
        else:
            if max_seq < k:
                max_seq = k
            k = 0

    if max_seq < k:
        max_seq = k
    return max_seq
```
"""
        new_md_link = '+ [ones](#ones)'
        self.assertEqual(prepare_new_md_content(new_md_link, new_md_code, old_md_content),"""+ [hello world optional](#hello-world-optional)
+ [ones](#ones)
<!---md_file_delimiter--->

## hello world optional
    
 depending on the input number, write hello world, its part or number
    
```python
def helloWorld(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print('hello world')
        elif i % 3 == 0:
            print('hello')
        elif i % 5 == 0:
            print('world')
        else:
            print(i)
```


## ones
    
 list consisting of 0 and 1. Find the length of the maximum continuous subsequence consisting of 1
    
```python
def ones(lst):
    k = 0
    max_seq = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            k += 1
        else:
            if max_seq < k:
                max_seq = k
            k = 0

    if max_seq < k:
        max_seq = k
    return max_seq
```
""")


if __name__ == "__main__":
    unittest.main()