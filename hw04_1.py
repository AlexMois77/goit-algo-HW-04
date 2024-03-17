from pathlib import Path

def total_salary(path):
    try: 
        full_path = Path(path) # додаємо лінк - вказаний шлях до файлу
        
        if full_path.exists() and full_path.is_file(): # Перевірка існування папки та файлу
            
            with open(full_path, "r", encoding='utf-8', errors='ignore') as fh: # відкриваємо файл 
                lines = [el.strip() for el in fh.readlines()] # Розділяємо на строки
                
                obj_query = {}
                total = 0
                average = 0
                count = 0
            
                for el in lines:
                    key, value = el.split(',')     # розділюємо працівників і зп по комі
                    total = total + int(value)     # сумуємо зп працівників
                    count += 1                     # сумуємо кількість працівників
                    obj_query.update({key: value}) # збираємо в словник ім'я і зп - хай буде
                average = int(total/count)         # середня зп
                korteg = (total, average)          # створюємо кортежик
                print(f"Загальна сума заробітної плати: {korteg[0]}, Середня заробітна плата: {korteg[1]}")
            return korteg
        else:
            return "Перевірте вказаний шлях та ім'я файла (повинно бути: salary_file.txt)"
    except OSError as err:
        return f('Помилка доступу до файлу', {err})

total_salary("E:\piton_kurs\kurs2024\homework\HW4\salary_file.txt")


