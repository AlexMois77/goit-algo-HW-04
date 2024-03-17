from pathlib import Path

def get_cats_info(path):
    try:
        full_path = Path(path)# додаємо лінк - вказаний шлях до файлу

        if full_path.exists() and full_path.is_file(): # Перевіряємо чи є така дерікторія і чи є файл
        
            with open(full_path, "r", encoding='utf-8', errors='ignore') as fh: # відкриваємо файл 
                
                lines = [el.strip() for el in fh.readlines()] # Розділяємо на строки
                
                dict_total = {}
                cats_info  = []

                for el in lines:
                    id, name, age = el.split(',')   # висмикуємо данні про кошаків
                    dict_total["id"] = id           # закидаємо данні про кошаків: АйДі
                    dict_total["name"] = name       # закидаємо данні про кошаків: Ім'я
                    dict_total["age"] = age        # закидаємо данні про кошаків: на скільки досвідчений котик
                    cats_info.append(dict_total.copy()) # збираємо данні про кошаків в список
            return cats_info
        else:
            return "Перевірте вказаний шлях та ім'я файла (повинно бути: salary_file.txt)"
    except OSError as err:
        return f('Помилка доступу до файлу', {err})

print (get_cats_info("E:\piton_kurs\kurs2024\homework\HW4\cats_file.txt"))