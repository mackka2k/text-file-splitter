import os
import shutil
from splitter import split_file

def test_split_file():
    # Setup
    test_file = "test_input_py.txt"
    test_content = [
        "# This is a comment\n",
        "line1\n",
        "line2\n",
        "\n",
        "line3\n",
        "# Another comment\n",
        "line4\n",
        "line5\n"
    ]
    
    with open(test_file, 'w', encoding='utf-8') as f:
        f.writelines(test_content)
        
    output_dir = "."
    chunk_size = 2
    
    try:
        print("Starting split_file test...")
        chunks_path = split_file(test_file, output_dir, chunk_size, lambda m, p: print(f"[{p*100:.0f}%] {m}"))
        
        # Verify
        if not os.path.exists(chunks_path):
            raise Exception("Chunks directory not created")
            
        files = sorted(os.listdir(chunks_path))
        print(f"Created files: {files}")
        
        expected_files = ["hosts_part_01_of_03.txt", "hosts_part_02_of_03.txt", "hosts_part_03_of_03.txt"]
        if files != expected_files:
            raise Exception(f"Expected files {expected_files}, but got {files}")
            
        # Verify contents of first chunk
        with open(os.path.join(chunks_path, files[0]), 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines != ["line1\n", "line2\n"]:
                raise Exception(f"Chunk 1 content mismatch: {lines}")
                
        # Verify contents of last chunk
        with open(os.path.join(chunks_path, files[2]), 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines != ["line5\n"]:
                raise Exception(f"Chunk 3 content mismatch: {lines}")
                
        print("Verification test PASSED!")
        
    finally:
        # Cleanup
        if os.path.exists(test_file):
            os.remove(test_file)
        # We'll keep hosts_chunks for a moment to let the user see it if they want, 
        # but normally we'd delete it in a test.
        # shutil.rmtree(chunks_path, ignore_errors=True)

if __name__ == "__main__":
    test_split_file()
