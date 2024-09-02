# -*- coding: utf-8 -*-

import os

# Ҫ���������
insert_content = """---
comments: true
---

"""

# ��ȡ��ǰĿ¼
current_directory = os.getcwd()

# ������ǰĿ¼�µ������ļ�
for filename in os.listdir(current_directory):
    if filename.endswith('.md'):
        file_path = os.path.join(current_directory, filename)

        try:
            # ��ȡ�ļ�����
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_content = file.read()

            # ����������
            new_content = insert_content + existing_content

            # д���ļ�
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

            print(f"�ļ� {filename} �Ѹ��¡�")
        except UnicodeDecodeError:
            print(f"�ļ� {filename} ������ UTF-8 ������ַ�����������")

print("���пɴ���� .md �ļ��Ѹ��¡�")