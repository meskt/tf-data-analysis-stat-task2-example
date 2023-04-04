import pandas as pd
import numpy as np
from scipy.stats import chi2


chat_id = 1841341924 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = (x ** 2).mean()
    return np.sqrt(len(x) * loc / (38 * chi2.ppf(1 - alpha / 2, 2 * len(x)))), \
           np.sqrt(len(x) * loc / (38 * chi2.ppf(alpha / 2, 2 * len(x))))
