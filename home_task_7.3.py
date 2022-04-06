import os, shutil

root = os.path.join(os.getcwd(), 'my_project')
root_temp = os.path.join(os.getcwd(), 'my_project', 'templates')
if not os.path.exists(root_temp):
    os.mkdir(root_temp)

for roots, dirs, files in os.walk(root):
    if str(files).rsplit('.', maxsplit=1)[-1].lower()[:-2] == 'html':
        if not os.path.exists(os.path.join(root_temp, str(roots).split('templates')[-1][1:])):
            os.makedirs(os.path.join(root_temp, str(roots).split('templates')[-1][1:]))
        for file in files:
            src_file = os.path.join(roots, file)
            dst_folder = os.path.join(root_temp, str(roots).split('templates')[-1][1:])
            if not os.path.exists(os.path.join(dst_folder, file)):
                shutil.copy(src_file, dst_folder)
