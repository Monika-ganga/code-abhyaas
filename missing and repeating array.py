a = [1, 2, 3, 4, 4, 6, 7]
n = len(a)
v = n * (n + 1) / 2
u = n * (n + 1) * (2 * n + 1) / 6
sum1 = 0
sum2 = 0

for i in range(len(a)):
    sum1 += a[i]

for j in range(len(a)):
    sum2 += a[j] * a[j]

x_minus_y = sum1 - v
x_squared_minus_y_squared = sum2 - u
x_plus_y = x_squared_minus_y_squared / (x_minus_y)

# Calculate x and y
x = (x_plus_y + x_minus_y) / 2
y = (x_plus_y - x_minus_y) / 2

print("x =", x)
print("y =", y)

