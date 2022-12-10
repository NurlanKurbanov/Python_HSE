+ [hello world optional](#hello-world-optional)
+ [ones](#ones)
+ [selection of sequences of consecutive numbers](#selection-of-sequences-of-consecutive-numbers)
+ [diagonalSum](#diagonalsum)
+ [merge](#merge)
+ [sort of squares of elements](#sort-of-squares-of-elements)
+ [compress string](#compress-string)
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


## selection of sequences of consecutive numbers

 nums = [0,1,2,4,5,7] Output: ["0->2","4->5","7"]

```python
def f3(a):
    res = []
    if len(a) == 1:
        res.append(str(a[0]))
        return res

    i = 0
    while i < len(a):
        if a[i] == a[-1]:
            res.append(str(a[i]))
            return res
        else:
            for j in range(i + 1,len(a)):
                if (a[j] - a[i] == j - i) and j != len(a) - 1:
                   continue
                elif (a[j] - a[i] == j - i) and (j == len(a) - 1):
                    res.append('"' + str(a[i]) + '->' + str(a[j]))
                    i = j + 1
                else:
                    res.append('"' + str(a[i]) + '->' + str(a[j - 1]))
                    i = j
                    break

    return res
```


## diagonalSum

 diagonalSum of square matrix

```python
def diagonalSum(mat):
    n = len(mat)
    sum = 0
    for i in range(n):
        for j in range(n):
            if i == j or i + j + 1 ==n:
                sum += mat[i][j]
    return sum
```


## merge

 at the input two sorted arrays (lists), at the output get 1 sorted array

```python
def mergeS(first,second):
    i = 0
    j = 0
    res = []
    if len(first) == 0 and len(second) == 0:
        return res
    elif len(first) == 0:
        return second
    elif len(second) == 0:
        return first

    while True:
        if first[i] <= second[j]:
            res.append(first[i])
            i += 1
        else:
            res.append(second[j])
            j += 1
        if i == len(first) or j == len(second):
            break

    if i == len(first) and j != len(second):
        for k in range(j, len(second)):
            res.append(second[k])

    elif i != len(first) and j == len(second):
        for k in range(i, len(first)):
            res.append(first[k])

    return res
```


## sort of squares of elements

 Given a sorted list in non-decreasing order. Return the elements of this list squared in non-decreasing order

```python
def mergeS(first, second):
    i = 0
    j = 0
    res = []
    if len(first) == 0 and len(second) == 0:
        return res
    elif len(first) == 0:
        return second
    elif len(second) == 0:
        return first

    while True:
        if first[i] <= second[j]:
            res.append(first[i])
            i += 1
        else:
            res.append(second[j])
            j += 1
        if i == len(first) or j == len(second):
            break

    if i == len(first) and j != len(second):
        for k in range(j, len(second)):
            res.append(second[k])

    elif i != len(first) and j == len(second):
        for k in range(i, len(first)):
            res.append(first[k])

    return res


def square(s):
    pos = []
    neg = []
    for i in range(len(s)):
        if s[i] <= 0:
            neg.append(s[i]*s[i])
        if s[i] > 0:
            pos.append(s[i] * s[i])
    neg.reverse()
    return mergeS(neg,pos)
```


## compress string

 ["a","b","b","c","c","c"] -> ab2c3

```python
def compress(elems):
    i = 0
    s = ""
    while i < len(elems):
        j = i
        while j < len(elems):
            if elems[i] != elems[j]:
                s += elems[i]
                if (j - i) != 1:
                    s += str(j - i)
                i = j
                break
            j += 1
        if j == len(elems):
            s += elems[i]
            if (j - i) != 1:
                s += str(j - i)
            return s
```
