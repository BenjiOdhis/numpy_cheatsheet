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
