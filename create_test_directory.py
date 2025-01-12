import os

def create_test_directory():
    os.makedirs("test_dir/subdir", exist_ok=True)
    
    open("test_dir/file1.txt", "w").close()
    open("test_dir/file2.jpg", "w").close()
    open("test_dir/file3.pdf", "w").close()
    
    open("test_dir/subdir/file4.docx", "w").close()
    open("test_dir/subdir/file5.png", "w").close()
    
    print("Test directory and files created!")

if __name__ == "__main__":
    create_test_directory()
