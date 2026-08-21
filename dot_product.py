import os
import math
os.system('cls')

# menghitung dot product

# 1. definisikan vector
vector_a = [2, 4, 6]
vector_b = [3, 6, 9]

# 2. Cara menghitung dot product
dot = sum([a * b for a, b in zip(vector_a, vector_b)])
print(dot)

# menghitung panjang vector
panjang_vector_a = math.sqrt(sum([a**2 for a in vector_a]))
panjang_vector_b = math.sqrt(sum([b**2 for b in vector_a]))

# menghitung cosine_similiarity
cosine_similiarity = dot / (panjang_vector_a * panjang_vector_b)
print(cosine_similiarity)
