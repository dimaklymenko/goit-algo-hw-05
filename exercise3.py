import sys
import re
from collections import Counter


def parse_log_line(line: str) -> dict:
    parts = line.split(maxsplit=3)
    if len(parts) < 4:
        return {}
    return {"Дата" : parts[0], "Час" : parts[1] , "Рівень" : parts[2], "Повідомлення" : parts[3]}

def load_logs(file_path: str) -> list:
    parsed_logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed_log = parse_log_line(line.strip())
                if parsed_log:
                    parsed_logs.append(parsed_log)            
        return parsed_logs
    except Exception as e:
        print(f'{e}')


def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return [log for log in logs if log["Рівень"] == level]


def count_logs_by_level(logs: list) -> dict:
    counts = Counter(log["Рівень"] for log in logs)
    return dict(counts)


def display_log_counts(counts: dict):
    print(f"{'Рівень':<10} | {'Кількість':<10}")
    print("-" * 22)
    for level, count in counts.items():
        print(f"{level:<10} | {count:<10}")


file_path = 'logs.txt'
logs = load_logs(file_path)
filtered_logs = filter_logs_by_level(logs, "ERROR")
counts = count_logs_by_level(logs)
display_log_counts(counts)
print(filtered_logs)



# if __name__ == "__main__":

#     file_path = sys.argv[1]
#     log_level = sys.argv[2] if len(sys.argv) > 2 else None

#     logs = load_logs(file_path)
    
#     if log_level:
#         filtered_logs = filter_logs_by_level(logs, log_level)
#         for log in filtered_logs:
#             print(f"{log['Рівень']}: {log['Повідомлення']}")
#     else:
#         log_counts = count_logs_by_level(logs)
#         display_log_counts(log_counts)

