from ninjazippy.zip_utils import zip_files, unzip_files
import os

def main():
    # Create a sample file
    with open("hello.txt", "w") as f:
        f.write("Hello, NinjaZipPy!")

    # Test zipping
    zip_files("hello.txt", "test_archive.7z")
    print("✅ File zipped into test_archive.7z")

    # Test unzipping
    unzip_files("test_archive.7z", "output_dir")
    print("✅ File unzipped into output_dir/")

    # Check result
    if os.path.exists("output_dir/hello.txt"):
        print("🎉 Success! Unzipped file found.")

if __name__ == "__main__":
    main()
