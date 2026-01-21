# general

```
"Move#Hash#to#Front"

```

---

## **Step 1 — Initial Setup**

We have:

```
Input:  M  o  v  e  #  H  a  s  h  #  t  o  #  F  r  o  n  t
Index:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17

```

We create:

```
result = [""] * 18
left   = 0
right  = 17

```

---

## **Step 2 — Filling Process**

We scan **left to right** in the input string:

| Step | Char | Action | result after step | left | right |
| --- | --- | --- | --- | --- | --- |
| 1 | M | non-# → place at `right=17` | ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'M'] | 0 | 16 |
| 2 | o | non-# → place at `right=16` | ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'o', 'M'] | 0 | 15 |
| 3 | v | non-# → place at `right=15` | ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'v', 'o', 'M'] | 0 | 14 |
| 4 | e | non-# → place at `right=14` | ['', '', '', '', '', '', '', '', '', '', '', '', '', '', 'e', 'v', 'o', 'M'] | 0 | 13 |
| 5 | # | hash → place at `left=0` | ['#', '', '', '', '', '', '', '', '', '', '', '', '', '', 'e', 'v', 'o', 'M'] | 1 | 13 |
| 6 | H | non-# → place at `right=13` | ['#', '', '', '', '', '', '', '', '', '', '', '', '', 'H', 'e', 'v', 'o', 'M'] | 1 | 12 |
| 7 | a | non-# → place at `right=12` | ['#', '', '', '', '', '', '', '', '', '', '', '', 'a', 'H', 'e', 'v', 'o', 'M'] | 1 | 11 |
| 8 | s | non-# → place at `right=11` | ['#', '', '', '', '', '', '', '', '', '', '', 's', 'a', 'H', 'e', 'v', 'o', 'M'] | 1 | 10 |
| 9 | h | non-# → place at `right=10` | ['#', '', '', '', '', '', '', '', '', '', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M'] | 1 | 9 |
| 10 | # | hash → place at `left=1` | ['#', '#', '', '', '', '', '', '', '', '', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M'] | 2 | 9 |
| 11 | t | non-# → place at `right=9` | ['#', '#', '', '', '', '', '', '', '', 't', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M'] | 2 | 8 |
| 12 | o | non-# → place at `right=8` | ['#', '#', '', '', '', '', '', '', 'o', 't', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M'] | 2 | 7 |
| 13 | # | hash → place at `left=2` | ['#', '#', '#', '', '', '', '', '', 'o', 't', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M'] | 3 | 7 |
| 14 | F | non-# → place at `right=7` | ['#', '#', '#', '', '', '', '', 'F', 'o', 't', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M'] | 3 | 6 |
| 15 | r | non-# → place at `right=6` | ['#', '#', '#', '', '', '', 'r', 'F', 'o', 't', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M'] | 3 | 5 |
| 16 | o | non-# → place at `right=5` | ['#', '#', '#', '', '', 'o', 'r', 'F', 'o', 't', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M'] | 3 | 4 |
| 17 | n | non-# → place at `right=4` | ['#', '#', '#', '', 'n', 'o', 'r', 'F', 'o', 't', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M'] | 3 | 3 |
| 18 | t | non-# → place at `right=3` | ['#', '#', '#', 't', 'n', 'o', 'r', 'F', 'o', 't', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M'] | 3 | 2 |

---

## **Step 3 — After Loop**

```
result = ['#', '#', '#', 't', 'n', 'o', 'r', 'F', 'o', 't', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M']
left   = 3

```

---

## **Step 4 — Splitting**

```
hash_part = result[:left]
          = ['#', '#', '#']

non_hash_part = result[left:]        # ['t', 'n', 'o', 'r', 'F', 'o', 't', 'h', 's', 'a', 'H', 'e', 'v', 'o', 'M']
non_hash_part = non_hash_part[::-1]  # ['M', 'o', 'v', 'e', 'H', 'a', 's', 'h', 't', 'o', 'F', 'r', 'o', 'n', 't']

```

---

## **Step 5 — Combine**

```
final = hash_part + non_hash_part
      = ['#', '#', '#', 'M', 'o', 'v', 'e', 'H', 'a', 's', 'h', 't', 'o', 'F', 'r', 'o', 'n', '
```