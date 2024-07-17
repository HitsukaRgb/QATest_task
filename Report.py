

def wright_log_file(text: str, path=None) -> str:
    """Функция записи в файл логов"""
    if not path:
        path = "webcalculator.log"
    with open(path, "a", encoding="utf-8") as file:
        file.write(text + "\n")
    return text
