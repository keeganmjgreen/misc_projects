
import os

fnames_fname = 'fnames.txt'

old_fnames = []

cwd = os.getcwd()

for (dirpath, _, filenames) in os.walk(cwd):
    for filename in filenames:
        old_fnames.append((dirpath + '\\' + filename).replace(cwd + '\\', ''))

old_fnames.remove(os.path.basename(__file__))

old_fnames_f = open(fnames_fname, 'w')

for old_fname in old_fnames:
    old_fnames_f.write(old_fname + '\n')

old_fnames_f.close()

old_mtime = os.path.getmtime(fnames_fname)

os.system('subl' + ' ' + fnames_fname)

while True:
    new_mtime = os.path.getmtime(fnames_fname)
    if old_mtime != new_mtime:
        break

os.system('taskkill /F /IM sublime_text.exe')

new_fnames_f = open(fnames_fname, 'r')

for old_fname, new_fname in zip(old_fnames, new_fnames_f):
    os.rename(old_fname, new_fname[:-1])

new_fnames_f.close()

os.remove(fnames_fname)
