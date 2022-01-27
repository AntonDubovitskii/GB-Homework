"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates
"""

import os
import shutil

project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'my_project')
templ_dir = os.path.join(project_dir, 'templates')

# При помощи os.wolk() обходятся все пути и отбираются те, что оканчиваются на 'templates', это и есть нужные
# директории. Далее они копируются при помощи shutil.copytree() в корень проекта. Благодаря параметру dirs_exist_ok=True
# конфликтов не происходит
for dir, folders, files in os.walk(project_dir):
    if dir.endswith('templates'):
        shutil.copytree(dir, templ_dir, dirs_exist_ok=True)




