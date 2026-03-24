import math
import sys


def validate_matrix(matrix):
    if not matrix or not matrix[0]:
        raise ValueError("矩阵不能为空")
    column_count = len(matrix[0])
    for row in matrix:
        if len(row) != column_count:
            raise ValueError("矩阵每一行的列数必须一致")


def matrix_shape(matrix):
    return len(matrix), len(matrix[0])


def zeros(rows, cols):
    return [[0.0 for _ in range(cols)] for _ in range(rows)]


def identity(size):
    result = zeros(size, size)
    for i in range(size):
        result[i][i] = 1.0
    return result


def transpose(matrix):
    rows, cols = matrix_shape(matrix)
    result = zeros(cols, rows)
    for i in range(rows):
        for j in range(cols):
            result[j][i] = float(matrix[i][j])
    return result


def matmul(a, b):
    a_rows, a_cols = matrix_shape(a)
    b_rows, b_cols = matrix_shape(b)
    if a_cols != b_rows:
        raise ValueError("矩阵乘法维度不匹配")

    result = zeros(a_rows, b_cols)
    for i in range(a_rows):
        for k in range(a_cols):
            aik = a[i][k]
            if abs(aik) < 1e-15:
                continue
            for j in range(b_cols):
                result[i][j] += aik * b[k][j]
    return result


def matvec(matrix, vector):
    rows, cols = matrix_shape(matrix)
    if cols != len(vector):
        raise ValueError("矩阵与向量乘法维度不匹配")

    result = [0.0 for _ in range(rows)]
    for i in range(rows):
        total = 0.0
        for j in range(cols):
            total += matrix[i][j] * vector[j]
        result[i] = total
    return result


def dot(a, b):
    if len(a) != len(b):
        raise ValueError("向量维度不匹配")
    total = 0.0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total


def norm(vector):
    return math.sqrt(dot(vector, vector))


def scalar_multiply_vector(vector, scalar):
    return [value * scalar for value in vector]


def subtract_vectors(a, b):
    if len(a) != len(b):
        raise ValueError("向量维度不匹配")
    return [a[i] - b[i] for i in range(len(a))]


def copy_matrix(matrix):
    return [row[:] for row in matrix]


def columns_to_matrix(columns):
    if not columns:
        return []
    row_count = len(columns[0])
    result = zeros(row_count, len(columns))
    for j, column in enumerate(columns):
        for i, value in enumerate(column):
            result[i][j] = value
    return result


def matrix_columns(matrix):
    rows, cols = matrix_shape(matrix)
    result = []
    for j in range(cols):
        result.append([matrix[i][j] for i in range(rows)])
    return result


def diagonal_matrix(diagonal):
    size = len(diagonal)
    result = zeros(size, size)
    for i in range(size):
        result[i][i] = diagonal[i]
    return result


def gram_schmidt_add(candidate, basis, tolerance=1e-10):
    vector = candidate[:]
    for base in basis:
        projection = dot(vector, base)
        vector = subtract_vectors(vector, scalar_multiply_vector(base, projection))

    vector_norm = norm(vector)
    if vector_norm <= tolerance:
        return None
    return scalar_multiply_vector(vector, 1.0 / vector_norm)


def jacobi_eigen_decomposition(matrix, tolerance=1e-12, max_sweeps=100):
    validate_matrix(matrix)
    size, cols = matrix_shape(matrix)
    if size != cols:
        raise ValueError("Jacobi 方法只适用于方阵")

    a = copy_matrix(matrix)
    eigenvectors = identity(size)

    for _ in range(max_sweeps):
        max_value = 0.0
        p = 0
        q = 1 if size > 1 else 0

        for i in range(size):
            for j in range(i + 1, size):
                value = abs(a[i][j])
                if value > max_value:
                    max_value = value
                    p, q = i, j

        if max_value < tolerance:
            break

        app = a[p][p]
        aqq = a[q][q]
        apq = a[p][q]

        if abs(apq) < tolerance:
            continue

        tau = (aqq - app) / (2.0 * apq)
        if tau >= 0:
            t = 1.0 / (tau + math.sqrt(1.0 + tau * tau))
        else:
            t = -1.0 / (-tau + math.sqrt(1.0 + tau * tau))

        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c

        for k in range(size):
            if k == p or k == q:
                continue

            akp = a[k][p]
            akq = a[k][q]
            a[k][p] = c * akp - s * akq
            a[p][k] = a[k][p]
            a[k][q] = s * akp + c * akq
            a[q][k] = a[k][q]

        a[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
        a[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
        a[p][q] = 0.0
        a[q][p] = 0.0

        for k in range(size):
            vip = eigenvectors[k][p]
            viq = eigenvectors[k][q]
            eigenvectors[k][p] = c * vip - s * viq
            eigenvectors[k][q] = s * vip + c * viq

    eigenvalues = [a[i][i] for i in range(size)]
    return eigenvalues, eigenvectors


def sort_eigensystem_descending(eigenvalues, eigenvectors):
    columns = matrix_columns(eigenvectors)
    pairs = list(zip(eigenvalues, columns))
    pairs.sort(key=lambda item: item[0], reverse=True)

    sorted_values = [pair[0] for pair in pairs]
    sorted_vectors = [pair[1] for pair in pairs]
    return sorted_values, columns_to_matrix(sorted_vectors)


def svd(matrix, tolerance=1e-10):
    validate_matrix(matrix)
    a = [[float(value) for value in row] for row in matrix]
    m, n = matrix_shape(a)
    k = min(m, n)

    ata = matmul(transpose(a), a)
    eigenvalues, eigenvectors = jacobi_eigen_decomposition(ata)
    eigenvalues, eigenvectors = sort_eigensystem_descending(eigenvalues, eigenvectors)

    singular_values = []
    v_columns = matrix_columns(eigenvectors)
    selected_v_columns = []
    u_columns = []

    for i in range(k):
        eigenvalue = eigenvalues[i]
        if eigenvalue < 0.0 and abs(eigenvalue) < tolerance:
            eigenvalue = 0.0
        if eigenvalue < 0.0:
            raise ValueError("A^T A 出现明显负特征值，数值过程不稳定")

        sigma = math.sqrt(eigenvalue)
        singular_values.append(sigma)
        selected_v_columns.append(v_columns[i])

        if sigma > tolerance:
            left_vector = matvec(a, v_columns[i])
            left_vector = scalar_multiply_vector(left_vector, 1.0 / sigma)
            left_vector = gram_schmidt_add(left_vector, u_columns, tolerance)
            if left_vector is None:
                raise ValueError("构造 U 时出现线性相关，数值过程不稳定")
            u_columns.append(left_vector)

    while len(u_columns) < k:
        for row_index in range(m):
            candidate = [0.0 for _ in range(m)]
            candidate[row_index] = 1.0
            extra = gram_schmidt_add(candidate, u_columns, tolerance)
            if extra is not None:
                u_columns.append(extra)
                break
        else:
            raise ValueError("无法补全 U 的正交基")

    u = columns_to_matrix(u_columns[:k])
    vt = transpose(columns_to_matrix(selected_v_columns))
    sigma_matrix = diagonal_matrix(singular_values)
    return u, sigma_matrix, vt


def reconstruction_error(original, u, sigma, vt):
    recovered = matmul(matmul(u, sigma), vt)
    rows, cols = matrix_shape(original)
    error = 0.0
    for i in range(rows):
        for j in range(cols):
            diff = original[i][j] - recovered[i][j]
            error += diff * diff
    return math.sqrt(error), recovered


def print_matrix(name, matrix, precision=6):
    print(name)
    for row in matrix:
        print("  [" + ", ".join(f"{value:.{precision}f}" for value in row) + "]")
    print()


def parse_matrix(text):
    rows = []
    for row_text in text.strip().split(";"):
        row_text = row_text.strip()
        if not row_text:
            continue
        row = [float(value) for value in row_text.replace(",", " ").split()]
        rows.append(row)

    validate_matrix(rows)
    return rows


def main():
    if len(sys.argv) > 1:
        matrix = parse_matrix(sys.argv[1])
    else:
        matrix = [
            [1.0, 0.0],
            [0.0, 2.0],
            [1.0, 1.0],
        ]

    u, sigma, vt = svd(matrix)
    error, recovered = reconstruction_error(matrix, u, sigma, vt)

    print_matrix("A =", matrix)
    print_matrix("U =", u)
    print_matrix("Sigma =", sigma)
    print_matrix("V^T =", vt)
    print_matrix("U * Sigma * V^T =", recovered)
    print(f"重构误差(Frobenius范数): {error:.12f}")


if __name__ == "__main__":
    main()
