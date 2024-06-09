from zipfile import ZipFile

files_to_zip = ['os_join.py', 'shelf_delete.py', 'shutil_copy.py']
zip_name = 'multi_zip.zip'

with ZipFile(zip_name, 'w') as zipf:
    for file in files_to_zip:
        file_name = file.split('/')[-1]
        zipf.write(file, arcname=file_name)