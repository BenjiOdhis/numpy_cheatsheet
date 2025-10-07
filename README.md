# 📘 NumPy Cheat Sheet for Machine Learning (Simplified Syntax Guide)

---

## 🧠 Core Array Creation Methods

### `np.array()` – Convert list or tuple into NumPy array

```python
np.array(data)
```

**data:** list, tuple, or nested lists → creates 1D, 2D, or 3D array.

> Example: `np.array([[1, 2, 3], [4, 5, 6]])`

---

### `np.zeros()` – Array of zeros

```python
np.zeros(shape)
```

**shape:** tuple → defines dimensions.

> Example: `np.zeros((2,3))` → 2×3 matrix of zeros

---

### `np.ones()` – Array of ones

```python
np.ones(shape)
```

**shape:** tuple → defines dimensions.

> Example: `np.ones((3,2))` → 3×2 matrix of ones

---

### `np.full()` – Array filled with a constant

```python
np.full(shape, fill_value)
```

**shape:** tuple of dimensions
**fill_value:** constant to fill

> Example: `np.full((2,3), 7)` → fills a 2×3 array with 7s

---

### `np.arange()` – Sequence with steps

```python
np.arange(start, stop, step)
```

**start:** beginning value
**stop:** end value (excluded)
**step:** interval between values

> Example: `np.arange(0,10,2)` → `[0,2,4,6,8]`

---

### `np.linspace()` – Evenly spaced numbers between two values

```python
np.linspace(start, stop, num)
```

**num:** number of samples

> Example: `np.linspace(0, 1, 5)` → `[0., 0.25, 0.5, 0.75, 1.]`

---

### `np.eye()` – Identity matrix

```python
np.eye(n)
```

**n:** size of the square matrix

> Example: `np.eye(3)` → 3×3 identity matrix

---

### `np.random.rand()` – Random floats in [0,1)

```python
np.random.rand(shape)
```

**shape:** dimensions of output

> Example: `np.random.rand(2,3)` → 2×3 random decimals

---

### `np.random.randint()` – Random integers in range

```python
np.random.randint(low, high, shape)
```

**low:** inclusive start
**high:** exclusive end
**shape:** array dimensions

> Example: `np.random.randint(0,10,(2,3))`

---

## ⚙️ Array Properties and Info

### `arr.shape` → returns (rows, columns)

### `arr.ndim` → number of dimensions

### `arr.size` → total number of elements

### `arr.itemsize` → bytes per element

### `arr.dtype` → data type

> Example:

```python
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)   # (2,3)
print(arr.ndim)    # 2
print(arr.size)    # 6
print(arr.itemsize) # 8
```

---

## 🔄 Array Operations (Used Heavily in ML)

### `np.reshape()` – Change shape

```python
np.reshape(arr, new_shape)
```

> Example: `np.reshape(arr, (3,2))`

### `np.flatten()` – Convert to 1D

```python
arr.flatten()
```

> Example: useful in neural networks to flatten feature maps

### `np.concatenate()` – Join arrays

```python
np.concatenate((arr1, arr2), axis=0)
```

> Example: stack rows or columns together

### `np.vstack()` / `np.hstack()` – Stack vertically/horizontally

> Example: `np.vstack([a,b])` or `np.hstack([a,b])`

### `np.split()` – Split into parts

```python
np.split(arr, num_sections, axis)
```

---

## 🧮 Mathematical & Statistical Methods

### Basic operations

* `np.add(a,b)` → elementwise addition
* `np.subtract(a,b)` → elementwise subtraction
* `np.multiply(a,b)` → elementwise multiplication
* `np.divide(a,b)` → elementwise division
* `np.dot(a,b)` → matrix multiplication
* `np.mean(a)` → average
* `np.median(a)` → median value
* `np.std(a)` → standard deviation
* `np.var(a)` → variance
* `np.min(a)`, `np.max(a)` → min/max values
* `np.sum(a, axis)` → sum over given axis

---

## 🧩 Useful ML/DS-Oriented Functions

### `np.unique()` – unique elements

```python
np.unique(arr)
```

### `np.argmax()` / `np.argmin()` – indices of max/min

```python
np.argmax(arr)
```

> Used in classification for picking the most likely class.

### `np.where()` – conditional filter

```python
np.where(arr > 0.5, 1, 0)
```

> Replace values based on condition.

### `np.clip()` – limit values to a range

```python
np.clip(arr, 0, 1)
```

> Common for normalizing outputs.

### `np.transpose()` / `arr.T` – swap rows/columns

> Used in linear algebra and gradient calculations.

### `np.dot()` / `@` operator – matrix multiplication

> Core operation in neural networks.

### `np.linalg.inv()` – matrix inverse

### `np.linalg.det()` – determinant

### `np.linalg.eig()` – eigenvalues/eigenvectors

> Essential in linear algebra and PCA.

---

## 🧮 Randomness and Sampling in ML

### `np.random.seed()` – fix randomness for reproducibility

```python
np.random.seed(42)
```

### `np.random.shuffle()` – shuffle elements

### `np.random.choice()` – random selection from array

---

## ⚡ Quick Reference Summary

| Category       | Function                                                                           | Purpose                            |
| -------------- | ---------------------------------------------------------------------------------- | ---------------------------------- |
| Array Creation | `np.array`, `np.zeros`, `np.ones`, `np.full`, `np.arange`, `np.linspace`, `np.eye` | Build arrays & matrices            |
| Random         | `np.random.rand`, `np.random.randn`, `np.random.randint`, `np.random.choice`       | Generate random data               |
| Shape Ops      | `np.reshape`, `np.flatten`, `np.concatenate`, `np.split`, `np.transpose`           | Manage dimensions                  |
| Math           | `np.add`, `np.multiply`, `np.mean`, `np.std`, `np.dot`                             | Compute statistics & algebra       |
| Logic          | `np.where`, `np.clip`, `np.unique`, `np.argmax`                                    | Conditional & classification tasks |
| Linear Algebra | `np.linalg.inv`, `np.linalg.det`, `np.linalg.eig`, `np.linalg.norm`                | Core ML math                       |

---

🧾 **Tip:** In ML pipelines, these methods appear constantly for tasks like:

* Preprocessing datasets
* Feature normalization
* Matrix multiplications in neural networks
* Random initialization of weights
* Statistical summaries

---

✨ *Created for ML learners who want simple, readable syntax explanations of essential NumPy functions.*
# 🧭 60-Day Integrated Python (ML) + C++ (DSA) Roadmap

This plan combines **Python for Machine Learning** and **C++ for Data Structures & Algorithms**, structured into a 60-day learning path. It includes daily focus areas, milestone goals, GitHub push recommendations, and suggested resources like **W3Schools** for quick reference.

---

## 📚 Recommended Resources

* **W3Schools** → For Python & C++ syntax refreshers, quick lookups, and basic examples.
  🔗 [https://www.w3schools.com](https://www.w3schools.com)
* **LeetCode / Codeforces / GeeksforGeeks** → For C++ DSA practice.
* **Kaggle / DataWars** → For Data Analysis & ML practice.
* **GitHub** → Maintain daily commits for accountability.

---

## 🗓️ Phase 1 (Days 1–10): Python Foundations

**Goal:** Build strong programming fundamentals.

**Focus Areas:**

* Variables, loops, conditionals, and functions
* Lists, tuples, sets, dictionaries
* File handling and comprehensions
* Basic OOP (classes, objects)

**Parallel C++ DSA:**

* Syntax, loops, functions, arrays
* Pointers and references

**Daily Routine Example:**

* 🐍 2 hours Python (practice small scripts)
* ⚙️ 1 hour C++ problem-solving (simple loops/arrays)

**Milestone:**
✅ Confident with basic syntax, can write simple algorithms in both Python and C++.

---

## 🧮 Phase 2 (Days 11–20): NumPy & Core DSA

**Goal:** Learn numerical computing and essential data structures.

**Python (NumPy):**

* Array creation: `np.array`, `np.zeros`, `np.ones`, `np.arange`
* Array attributes: `.shape`, `.size`, `.dtype`
* Slicing, reshaping, broadcasting
* Basic linear algebra (`np.dot`, `np.linalg.inv`)

**C++ DSA:**

* Structures, classes, vectors, strings
* Sorting algorithms and searching

**Resources:**

* W3Schools → NumPy & C++ STL basics
* Practice daily problems on LeetCode (Array/Vector category)

**Milestone:**
✅ Efficient with NumPy and comfortable manipulating arrays.
✅ Able to implement search/sort algorithms manually.

---

## 🧱 Phase 3 (Days 21–30): Pandas + Intermediate DSA

**Goal:** Learn how to clean, analyze, and summarize tabular data.

**Python (Pandas):**

* DataFrames and Series basics
* Import/export CSVs
* Filtering, sorting, grouping, merging
* Handling missing values
* Descriptive stats and `.corr()`

**C++ DSA:**

* Linked lists, stacks, and queues
* Object-oriented patterns and STL containers (`map`, `set`)

**Practice:**

* Analyze sample CSV datasets from Kaggle or DataWars.
* Solve 1–2 LeetCode DSA problems daily.

**Milestone:**
✅ Can perform full EDA (Exploratory Data Analysis).
✅ Understand core data structures thoroughly.

---

## 📊 Phase 4 (Days 31–45): DataWars + Advanced DSA

**Goal:** Apply analysis & visualization to real datasets and learn advanced logic in C++.

**Python / ML:**

* Work on 2–3 DataWars challenges.
* Focus on cleaning, visualizing, and documenting findings.
* Learn scikit-learn basics (`train_test_split`, `fit`, `predict`).

**C++ DSA:**

* Trees, recursion, graphs
* STL: priority_queue, unordered_map
* Recursion & dynamic programming basics

**Daily Routine:**

* 🐍 2.5 hrs on DataWars or notebook projects
* ⚙️ 1.5 hrs on C++ problem sets

**Milestone:**
✅ Submitted first DataWars project.
✅ Implemented recursive and tree-based solutions in C++.

---

## 🤖 Phase 5 (Days 46–60): Kaggle & Advanced ML Integration

**Goal:** Transition to full ML workflows.

**Python / ML:**

* Beginner Kaggle competitions (Titanic, House Prices)
* Feature engineering and evaluation metrics
* Model improvement techniques
* Visualization & documentation for GitHub portfolio

**C++ DSA:**

* Master dynamic programming
* Participate in one Codeforces or LeetCode contest weekly

**Milestone:**
✅ Completed a Kaggle beginner competition.
✅ Achieved consistent problem-solving rhythm in C++ contests.

---

## 🧾 Summary (Flexible Path Version)

For learners who prefer flexibility over strict timelines:

| Stage | Focus                     | Key Tools        | Outcome                                      |
| ----- | ------------------------- | ---------------- | -------------------------------------------- |
| 1️⃣   | **Programming basics**    | Python, C++      | Foundational understanding of syntax & logic |
| 2️⃣   | **Numerical computing**   | NumPy            | Efficient data manipulation                  |
| 3️⃣   | **Data analysis**         | Pandas           | Confident with data cleaning and EDA         |
| 4️⃣   | **Problem-solving**       | C++ STL, DSA     | Strong algorithmic reasoning                 |
| 5️⃣   | **Practical application** | DataWars, Kaggle | Real-world experience & ML readiness         |

💡 *Adjust pace as needed — the key is consistent practice and GitHub documentation, not rigid timing.*

---

🏁 **Final Tip:** Use W3Schools daily as a quick reference for both languages — short examples there save debugging time. Combine it with consistent GitHub commits and platform practice (DataWars, Kaggle, LeetCode) to form a well-rounded coding + ML portfolio.
