
```
Start
  │
  ▼
prime_generator(limit, current, divisor)
  │
  ├── Is current > limit?
  │       ├── Yes → Stop
  │       └── No →
  │
  ├── Is divisor * divisor > current?
  │       ├── Yes →
  │       │       • yield current (prime)
  │       │       • call prime_generator(limit, current + 1, 2)
  │       └── No →
  │             ├── Is current % divisor == 0?
  │             │       ├── Yes → call prime_generator(limit, current + 1, 2)
  │             │       └── No  → call prime_generator(limit, current, divisor + 1)
  │
  ▼
End
```

Execution Example for n = 10
```
Step    Current   Divisor   Action
1       2         2         divisor² > current → yield 2
2       3         2         divisor² > current → yield 3
3       4         2         divisible → skip to 5
4       5         2         divisor² > current → yield 5
5       6         2         divisible → skip to 7
6       7         2         divisor² > current → yield 7
7       8         2         divisible → skip to 9
8       9         2         not divisible → divisor=3 → divisible → skip to 10
9       10        2         divisible → skip to 11 → stop

Output: 2 3 5 7
```
```
prime_generator(10, 2, 2)
│
├── divisor*divisor > 2?  (4 > 2)  → yield 2
│   └── prime_generator(10, 3, 2)
│       ├── 4 > 3  → yield 3
│       │   └── prime_generator(10, 4, 2)
│       │       ├── 4 % 2 == 0  → skip to next
│       │       └── prime_generator(10, 5, 2)
│       │           ├── 4 > 5  → yield 5
│       │           │   └── prime_generator(10, 6, 2)
│       │           │       ├── 6 % 2 == 0  → skip to next
│       │           │       └── prime_generator(10, 7, 2)
│       │           │           ├── 4 > 7  → yield 7
│       │           │           │   └── prime_generator(10, 8, 2)
│       │           │           │       ├── 8 % 2 == 0  → skip to next
│       │           │           │       └── prime_generator(10, 9, 2)
│       │           │           │           ├── 4 > 9  → check next divisor
│       │           │           │           └── prime_generator(10, 9, 3)
│       │           │           │               ├── 9 % 3 == 0  → skip to next
│       │           │           │               └── prime_generator(10, 10, 2)
│       │           │           │                   ├── 10 % 2 == 0  → skip to next
│       │           │           │                   └── prime_generator(10, 11, 2)
│       │           │           │                       ├── current > limit  → stop
```

```
Flow Summary for n = 10
Start at (2, 2) → prime → go to (3, 2).
(3, 2) → prime → go to (4, 2).
(4, 2) → divisible → skip to (5, 2).
(5, 2) → prime → go to (6, 2).
(6, 2) → divisible → skip to (7, 2).
(7, 2) → prime → go to (8, 2).
(8, 2) → divisible → skip to (9, 2).
(9, 2) → not divisible → check (9, 3) → divisible → skip to (10, 2).
(10, 2) → divisible → skip to (11, 2) → stop.
```