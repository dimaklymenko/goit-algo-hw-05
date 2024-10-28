from typing import Callable
import re


def generator_numbers(text: str):
    pattern = r'\b\d+(?:,\d{3})*(?:\.\d+)?\b'
    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable):
    total_sum = sum(generator_numbers(text))   
    return total_sum    


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")