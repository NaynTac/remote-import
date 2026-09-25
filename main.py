import sys
from url_hook import url_hook


# Добавляем хук
sys.path_hooks.append(url_hook)

# Добавялем новый путь импорта
sys.path.append("https://nayntac.github.io/remote-import/")