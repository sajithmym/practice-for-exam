import scipy.sparse as sparse

data = [1, 2, 3, 4]
row = [0, 0, 1, 2]
col = [0, 1, 1, 0]

matrix = sparse.csr_matrix((data, (row, col)))
