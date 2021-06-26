from scipy import io
mat_file = io.loadmat('numbers.mat')  # 파일명
numbers = mat_file['numbers']
