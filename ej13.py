class Vector4D:
    def __init__(self, u, v, x, y):
        self.u = u
        self.v = v
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.u},{self.v},{self.x},{self.y})"

    def __add__(self, vector):
        u_sum = self.u + vector.u
        v_sum = self.v + vector.v
        x_sum = self.x + vector.x
        y_sum = self.y + vector.y
        return Vector4D(u_sum, v_sum, x_sum, y_sum)
    
    def __sub__(self, vector):
        u_sub = self.u - vector.u
        v_sub = self.v - vector.v
        x_sub = self.x - vector.x
        y_sub = self.y - vector.y
        return Vector4D(u_sub, v_sub, x_sub, y_sub)

    def __mul__(self, vector):
        u_mul = self.u * vector.u
        v_mul = self.v * vector.v
        x_mul = self.x * vector.x
        y_mul = self.y * vector.y
        return Vector4D(u_mul, v_mul, x_mul, y_mul)

    def __truediv__(self, escalar):
        u_div = self.u / escalar
        v_div = self.v / escalar
        x_div = self.x / escalar
        y_div = self.y / escalar
        return (u_div, v_div, x_div, y_div)

# Prueba
vector_1 = Vector4D(2, 4, 6, 8)
vector_2 = Vector4D(1, 2, 3, 4)

print("Vector_1 + Vector_2 =", vector_1 + vector_2)
print("Vector_1 * Vector_2 =", vector_1 * vector_2)
print("Vector_1 - Vector_2 =", vector_1 - vector_2)
print("Vector_2 / 2 =", vector_2 / 2)
