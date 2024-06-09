from zipfile import ZipFile

with ZipFile('my_zip.zip', 'w') as zipf:
    zipf.write('file.txt', arcname='mohit/kumar/file.txt')