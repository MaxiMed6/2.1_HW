import logging
import re
from datetime import datetime, timedelta


logging.basicConfig(
    filename='hb_test.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


logger = logging.getLogger()


def analyze_log(log_file):

    try:
        with open(log_file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        logger.error("Файл hblog.txt не найден.")
        print("Файл hblog.txt не найден.")
        return

    pattern = r'{[^}]*?Timestamp (\d{2}:\d{2}:\d{2})[^}]*?Key TSTFEED0300\|7E3E\|0400[^}]*?}'
    timestamp_strs = re.findall(pattern, content)

    if not timestamp_strs:
        logger.warning("Записи с ключом 'TSTFEED0300|7E3E|0400' не найдены.")
        print("Записи с ключом 'TSTFEED0300|7E3E|0400' не найдены.")

        with open('hb_test.log', 'w') as f:
            f.write("Анализ heartbeat для ключа TSTFEED0300|7E3E|0400\n")
            f.write("-" * 50 + "\n")
            f.write("Записи с ключом 'TSTFEED0300|7E3E|0400' не найдены.\n")
            f.write("-" * 50 + "\n")
        return

    print(f"Найдено {len(timestamp_strs)} записей.")


    timestamps = []
    for ts_str in timestamp_strs:
        try:
            ts_obj = datetime.strptime("1900-01-01 " + ts_str, "%Y-%m-%d %H:%M:%S")
            timestamps.append(ts_obj)
        except ValueError:
            continue

    timestamps.sort()

    with open('hb_test.log', 'w') as f:
        f.write("Анализ heartbeat для ключа TSTFEED0300|7E3E|0400\n")
        f.write("-" * 50 + "\n")

    issues_found = False
    for i in range(1, len(timestamps)):
        prev_ts = timestamps[i - 1]
        curr_ts = timestamps[i]


        if curr_ts >= prev_ts:
            delta = curr_ts - prev_ts
        else:
            delta = (curr_ts - prev_ts) + timedelta(days=1)

        delta_seconds = delta.total_seconds()


        prev_ts_str = prev_ts.strftime("%H:%M:%S")
        curr_ts_str = curr_ts.strftime("%H:%M:%S")


        if 31 < delta_seconds < 33:
            logger.warning(
                f"WARNING: Heartbeat {delta_seconds:.0f} секунд (между {prev_ts_str} и {curr_ts_str}) превышает 31 секунду.")
            issues_found = True
        elif delta_seconds >= 33:
            logger.error(
                f"ERROR: Heartbeat {delta_seconds:.0f} секунд (между {prev_ts_str} и {curr_ts_str}) критически велик (>=33 сек).")
            issues_found = True

    if not issues_found:
        with open('hb_test.log', 'a') as f:
            f.write("Нарушений heartbeat не выявлено.\n")

    with open('hb_test.log', 'a') as f:
        f.write("-" * 50 + "\n")

    print("Анализ завершен. Результаты записаны в 'hb_test.log'.")


if __name__ == "__main__":
    analyze_log('hblog.txt')