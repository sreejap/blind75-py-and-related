Here you go — a **clean, practical, interview-oriented Java → Python Cheat Sheet** plus **common pitfalls with examples + fixes**.
This is designed *exactly* for someone coding LeetCode / DSA in Python after years of Java.

---

# 🐍 **Java → Python Cheat Sheet (Everything You Need for Interviews)**

---

## ⭐ **1. Variables & Types**

### Java

```java
int x = 5;
String s = "hi";
```

### Python

```python
x = 5
s = "hi"
```

* No type declarations
* Types change at runtime
* Everything is an object

---

## ⭐ **2. Conditionals**

### Java

```java
if (x == 5) {
    ...
}
```

### Python

```python
if x == 5:
    ...
```

No parentheses required, no `{ }`.

---

## ⭐ **3. Loops**

### For-each loop

Java:

```java
for (int num : nums) {
    ...
}
```

Python:

```python
for num in nums:
    ...
```

### Range loop

Java:

```java
for (int i = 0; i < n; i++) {
    ...
}
```

Python:

```python
for i in range(n):
    ...
```

---

## ⭐ **4. Increment / Decrement**

Python **does NOT support** `++` or `--`.

Use:

```python
i += 1
i -= 1
```

---

## ⭐ **5. Lists (dynamic arrays)**

Java:

```java
List<Integer> list = new ArrayList<>();
list.add(10);
```

Python:

```python
arr = []
arr.append(10)
```

### Useful list operations:

```python
arr.reverse()
arr.pop()
arr[-1]          # last element
arr[::-1]        # reversed (creates new list)
len(arr)
```

---

## ⭐ **6. Dictionaries (like HashMap)**

Java:

```java
Map<Integer, String> map = new HashMap<>();
map.put(1, "a");
map.get(1);
```

Python:

```python
map = {}
map[1] = "a"
map.get(1)
```

Check existence:

```python
if key in map:
```

---

## ⭐ **7. Strings**

No char type in Python.
Everything is a string of length 1.

### Java

```java
char c = s.charAt(i);
```

### Python

```python
c = s[i]
```

Check digit:

```python
c.isdigit()
c.isalpha()
```

---

## ⭐ **8. Classes & `self`**

Java:

```java
class A {
    int x;
    void foo() { ... }
}
```

Python:

```python
class A:
    def __init__(self, x):
        self.x = x

    def foo(self):
        ...
```

**Remember:** `self` must be present.

---

## ⭐ **9. Recursion**

Similar to Java, but no type hints required.

```python
def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)
```

---

## ⭐ **10. Booleans**

Same as Java but lowercase:

```python
True, False
```

---

## ⭐ **11. `None` instead of `null`**

Java:

```java
return null;
```

Python:

```python
return None
```

---

# 🚨 **Biggest Pitfalls Java Developers Hit in Python**

---

## ❌ **1. Forgetting `self`**

Bad:

```python
class A:
    def foo():
        ...
```

Good:

```python
def foo(self):
```

---

## ❌ **2. Trying to use `++`**

Not allowed.

---

## ❌ **3. Calling an instance method like a static method**

You wrote earlier:

```python
Solution.lowestCommonAncestor(self, root, p, q)
```

This adds an extra `self` → error.

Correct:

```python
self.lowestCommonAncestor(root, p, q)
```

---

## ❌ **4. Using `is` instead of `==`**

Bad:

```python
if x is 5:
```

Good:

```python
if x == 5:
```

---

## ❌ **5. Mutable default arguments**

Bad:

```python
def foo(arr=[]):
```

Good:

```python
def foo(arr=None):
    if arr is None:
        arr = []
```

---

## ❌ **6. Misunderstanding slicing**

Python slices create new lists.

```python
arr2 = arr[::-1]   # new reversed list
```

---

## ❌ **7. Wrong indentation**

Python uses indentation instead of braces.

Must be **4 spaces** — no tabs.

---

## ❌ **8. Overusing classes because you're from Java**

Python solutions can be *simple functions*.
Only use classes when LeetCode forces it (like `Solution` wrapper).

---
