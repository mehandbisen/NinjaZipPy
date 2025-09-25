import argparse
from .zip_utils import zip_file, unzip_file

def main():
    parser = argparse.ArgumentParser(description="NinjaZipPy: zip/unzip .7z files")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- Zip command ---
    zip_parser = subparsers.add_parser("zip", help="Compress files/folders into .7z archive")
    zip_parser.add_argument("source", help="File or folder to compress")
    zip_parser.add_argument("-o", "--output", required=True, help="Output .7z archive path")

    # --- Unzip command ---
    unzip_parser = subparsers.add_parser("unzip", help="Extract .7z archive")
    unzip_parser.add_argument("archive", help="Archive to extract")
    unzip_parser.add_argument("-d", "--dest", required=True, help="Destination folder")

    args = parser.parse_args()

    if args.command == "zip":
        zip_file(args.source, args.output)
    elif args.command == "unzip":
        unzip_file(args.archive, args.dest)
