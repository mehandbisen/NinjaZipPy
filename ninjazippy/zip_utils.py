import os
import py7zr

def zip_file(input_path: str, output_archive: str):
    """Compress a file or folder into a .7z archive."""
    with py7zr.SevenZipFile(output_archive, 'w') as archive:
        if os.path.isdir(input_path):
            archive.writeall(input_path, arcname=os.path.basename(input_path))
        else:
            archive.write(input_path, arcname=os.path.basename(input_path))

def unzip_file(archive_path: str, output_dir: str):
    """Extract a .7z archive into a folder."""
    with py7zr.SevenZipFile(archive_path, 'r') as archive:
        archive.extractall(path=output_dir)
