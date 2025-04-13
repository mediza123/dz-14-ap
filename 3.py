def append_to_file(text, filename):
    # Добавляем текст в файл
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    
    # Читаем файл и выводим четные строки
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        even_lines = [line.strip() for i, line in enumerate(lines, 1) if i % 2 == 0]
        print('\n'.join(even_lines))
