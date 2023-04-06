import pandas as pd
import numpy as np
from scipy.stats import chi2


chat_id = 1841341924 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return (-min(-x) - 0.5) * 2 / 38 ** 2, \
        (-np.log(alpha) / len(x) - min(-x) - 0.5) * 2 / 38 ** 2
