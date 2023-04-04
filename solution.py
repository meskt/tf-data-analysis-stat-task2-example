import pandas as pd
import numpy as np
from scipy.stats import chi2


chat_id = 1841341924 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    size = len(x)
    return np.sqrt(2*size / ((x**2).mean()*38**2 * chi2.ppf(q=1 - alpha / 2, df=2 * size))), \
           np.sqrt(2*size / ((x**2).mean()*38**2 * chi2.ppf(q=alpha / 2, df=2 * size)))
