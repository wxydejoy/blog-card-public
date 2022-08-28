
import os
import shutil

# 将目录下的guide.md改名为README.md  如果READme.md存在则删除
def rename_file(path):
    if os.path.exists(path + '/README.md'):
        os.remove(path + '/README.md')
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == 'guide.md':
                os.rename(os.path.join(root, file), os.path.join(root, 'README.md'))



# 遍历目录并生成docsify 的 _sidebar.md
def generate_sidebar(path):
    with open(path + '/_sidebar.md', 'w') as f:
        f.write('# 导航\n')
        f.write('\n')
        for root, dirs, files in os.walk(path):
            for file in files:
                if file == 'README.md':
                    f.write('- [{}]({})\n'.format(os.path.basename(root), os.path.join(root, file)))

# 将 每个 子文件夹 内 的 除了 README.md  之外的 .md 格式 文件 拼接成 一个 .md 文件 并删除原来的文件
def generate_markdown(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == 'README.md':
                continue
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r',encoding = "utf-8") as f:
                    content = f.read()
                with open(os.path.join(root, 'a.md'), 'a',encoding = "utf-8") as f:
                    f.write(content)
                os.remove(os.path.join(root, file))
    




rename_file('.')
#generate_sidebar('./latex-cookbook-main')

