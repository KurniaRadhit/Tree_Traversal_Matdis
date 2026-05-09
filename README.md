# Tree Traversal — Matematika Diskrit

Implementasi algoritma **Tree Traversal** dalam bahasa Python. Tree traversal adalah proses mengunjungi setiap simpul (node) pada sebuah pohon (tree) tepat satu kali secara sistematis.

Algoritma tree traversal terbagi menjadi dua pendekatan utama: **DFS (Depth-First Search)** dan **BFS (Breadth-First Search)**.

---

## Struktur

```
tree-traversal/
├── DFS/
│   ├── pre_order.py     # Pre-order traversal
│   ├── in_order.py      # In-order traversal
│   ├── post_order.py    # Post-order traversal
│   └── dfs.py           # Gabungan ketiga DFS traversal
└── BFS/
    └── level_order.py   # Level-order traversal
```

---

## Contoh Tree

Seluruh file menggunakan contoh binary tree berikut:

```
            1
          /   \
         2     3
        / \   / \
       4   5 6   7
```

Tree ini dibangun pada blok `if __name__ == "__main__":` di setiap file menggunakan class `Node` yang memiliki tiga atribut: `value`, `left`, dan `right`.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

---

## DFS (Depth-First Search)

**DFS** adalah strategi penelusuran tree yang menjelajah ke arah **kedalaman** terlebih dahulu sebelum berpindah ke cabang lain. Dari root, algoritma terus menelusuri anak (child) sampai mencapai daun (leaf), lalu kembali (backtrack) untuk menelusuri cabang yang belum dikunjungi.

Pada implementasi di repo ini, DFS dilakukan secara **rekursif** — fungsi memanggil dirinya sendiri untuk subtree kiri dan kanan. Yang membedakan ketiga jenis DFS hanyalah **urutan kapan nilai node dimasukkan ke list hasil** (`hasil.append(node.value)`).

DFS terbagi menjadi tiga jenis: **Pre-order, In-order, dan Post-order**.

---

### 1. Pre-order Traversal

**Urutan:**
Root → Left → Right

**Artinya:**
- Kunjungi root dulu
- Traversal subtree kiri
- Traversal subtree kanan

**Implementasi:**
```python
def pre_order(node, hasil=None):
    if hasil is None:
        hasil = []
    if node is not None:
        hasil.append(node.value)        # Root dikunjungi pertama
        pre_order(node.left, hasil)     # lalu subtree kiri
        pre_order(node.right, hasil)    # terakhir subtree kanan
    return hasil
```

`hasil.append(node.value)` dipanggil **sebelum** rekursi ke kiri dan kanan, sehingga root selalu masuk ke list lebih dulu.

**Proses:**
1 → 2 → 4 → 5 → 3 → 6 → 7

**Hasil:**
`[1, 2, 4, 5, 3, 6, 7]`

**Karakteristik:**
- Root selalu diproses pertama
- Cocok untuk:
  - membuat copy/duplikasi tree
  - menyimpan struktur tree (serialisasi)

---

### 2. In-order Traversal

**Urutan:**
Left → Root → Right

**Artinya:**
- Traversal subtree kiri dulu
- Kunjungi root
- Traversal subtree kanan

**Implementasi:**
```python
def in_order(node, hasil=None):
    if hasil is None:
        hasil = []
    if node is not None:
        in_order(node.left, hasil)      # subtree kiri dulu
        hasil.append(node.value)        # baru root
        in_order(node.right, hasil)     # terakhir subtree kanan
    return hasil
```

Posisi `hasil.append(node.value)` berada di **tengah** — di antara rekursi kiri dan kanan.

**Proses:**
4 → 2 → 5 → 1 → 6 → 3 → 7

**Hasil:**
`[4, 2, 5, 1, 6, 3, 7]`

**Karakteristik:**
- Pada **Binary Search Tree (BST)**, hasil in-order akan urut **ascending** (terurut dari kecil ke besar)
- Sangat sering dipakai pada BST

---

### 3. Post-order Traversal

**Urutan:**
Left → Right → Root

**Artinya:**
- Traversal subtree kiri
- Traversal subtree kanan
- Root terakhir

**Implementasi:**
```python
def post_order(node, hasil=None):
    if hasil is None:
        hasil = []
    if node is not None:
        post_order(node.left, hasil)    # subtree kiri dulu
        post_order(node.right, hasil)   # lalu subtree kanan
        hasil.append(node.value)        # root paling akhir
    return hasil
```

`hasil.append(node.value)` baru dipanggil **setelah** kedua subtree selesai ditelusuri, sehingga root selalu masuk paling akhir.

**Proses:**
4 → 5 → 2 → 6 → 7 → 3 → 1

**Hasil:**
`[4, 5, 2, 6, 7, 3, 1]`

**Karakteristik:**
- Root selalu terakhir
- Cocok untuk:
  - menghapus tree (anak dihapus dulu, baru parent)
  - evaluasi expression tree

---

## BFS (Breadth-First Search)

**BFS** adalah strategi penelusuran yang menjelajah node **per level**, dari atas ke bawah dan kiri ke kanan. Berbeda dengan DFS yang langsung "menukik" ke kedalaman, BFS menyelesaikan satu level dulu sebelum lanjut ke level berikutnya.

BFS pada tree dikenal sebagai **Level-order traversal**.

---

### 4. Level-order Traversal

**Urutan:**
Berdasarkan level/baris dari atas ke bawah, kiri ke kanan

**Artinya:**
- Mulai dari root (level 0)
- Lanjut ke seluruh node di level 1
- Lanjut ke seluruh node di level 2
- Dan seterusnya sampai level terbawah

Karena BFS tidak bisa diimplementasikan dengan rekursi sederhana seperti DFS, kita menggunakan struktur data **Queue (antrian)** dengan prinsip **FIFO** (First In, First Out).

**Implementasi:**
```python
from collections import deque

def level_order(root):
    hasil = []
    if root is None:
        return hasil

    antrian = deque([root])
    while antrian:
        node = antrian.popleft()        # ambil node dari depan queue
        hasil.append(node.value)
        if node.left:
            antrian.append(node.left)   # masukkan anak kiri ke belakang
        if node.right:
            antrian.append(node.right)  # masukkan anak kanan ke belakang
    return hasil
```

**Cara kerja:**
1. Root dimasukkan ke dalam queue
2. Selama queue tidak kosong, ambil node paling depan (`popleft()`), masukkan nilainya ke list hasil
3. Tambahkan anak kiri dan kanan node tersebut ke belakang queue
4. Ulangi sampai queue kosong

`deque` digunakan dari modul `collections` karena operasi `popleft()` pada deque memiliki kompleksitas O(1), lebih efisien dibanding list biasa.

**Proses:**
1 → 2 → 3 → 4 → 5 → 6 → 7

**Hasil:**
`[1, 2, 3, 4, 5, 6, 7]`

**Karakteristik:**
- Traversal per tingkat (level demi level)
- Menggunakan Queue (antrian) dengan prinsip FIFO
- Disebut juga **Breadth-First Search (BFS)**
- Cocok untuk:
  - mencari shortest path (jarak terpendek dari root)
  - mencetak tree per level

---

## Perbandingan Singkat

| Traversal    | Pendekatan | Urutan              | Ciri Utama                     | Hasil pada Tree Contoh    |
|--------------|------------|---------------------|---------------------------------|----------------------------|
| Pre-order    | DFS        | Root → Left → Right | Root pertama                    | `[1, 2, 4, 5, 3, 6, 7]`    |
| In-order     | DFS        | Left → Root → Right | Bisa menghasilkan urutan BST    | `[4, 2, 5, 1, 6, 3, 7]`    |
| Post-order   | DFS        | Left → Right → Root | Root terakhir                   | `[4, 5, 2, 6, 7, 3, 1]`    |
| Level-order  | BFS        | Per level           | Menggunakan Queue / BFS         | `[1, 2, 3, 4, 5, 6, 7]`    |

---

## Cara Menjalankan

Pastikan Python 3 sudah terinstal, lalu jalankan masing-masing file:

```bash
# DFS
python DFS/pre_order.py
python DFS/in_order.py
python DFS/post_order.py
python DFS/dfs.py        

# BFS
python BFS/level_order.py
```
