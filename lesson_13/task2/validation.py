import os
import json
import logging
from pathlib import Path



logging.basicConfig(
    filename='json__veliksar.log',
    level=logging.ERROR ,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


folder_path = Path(__file__).parent
print(folder_path)


if not os.path.exists(folder_path):
    print("Папка не знайдена!")
else:
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    json.load(file)
                print(f"{filename} - валідний JSON")
            except json.JSONDecodeError as e:
                logging.error(f"{filename} - невалідний JSON: {str(e)}")
                print(f"{filename} - невалідний JSON")
            except Exception as e:
                logging.error(f"{filename} - помилка: {str(e)}")
                print(f"{filename} - помилка")