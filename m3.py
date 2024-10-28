import sys
import re
from collections import Counter

def parse_log_line(line: str) -> dict:
    """
    Парсить рядок логу, повертаючи словник з рівнем логування та самим повідомленням.
    
    """
    parts = line.split(maxsplit=3)
    if len(parts) < 4:
        return {}
    log_pattern = re.compile(r'(?P<level>INFO|ERROR|DEBUG|WARNING): (?P<message>.+)')
    match = log_pattern.search(line)
    if match:
        return {"level": match.group("level"), "message": match.group("message")}
    return {"date" : parts[0], "time" : parts[1] , "level" : parts[2], "message" : parts[3]}

def load_logs(file_path: str) -> list:
    """
    Завантажує лог-файл та повертає список розпарсених рядків логу.
    """
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line.strip())
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Фільтрує логи за певним рівнем логування.
    """
    level = level.upper()
    return [log for log in logs if log["level"] == level]

def count_logs_by_level(logs: list) -> dict:
    """
    Підраховує кількість записів для кожного рівня логування.
    """
    counts = Counter(log["level"] for log in logs)
    return dict(counts)

def display_log_counts(counts: dict):
    print("\n Кількість записів для кожного рівня логування:")
    print(f"{'Рівень':<10} | {'Кількість':<10}")
    print("-" * 23)
    for level, count in counts.items():
        print(f"{level:<10} | {count:<10}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Вкажіть шлях до файлу логів як перший аргумент.")
        sys.exit(1)

    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        for log in filtered_logs:
            print(f"{log['level']}: {log['message']}")
    else:
        log_counts = count_logs_by_level(logs)
        display_log_counts(log_counts)

