import os
import math
from typing import List, Callable, Optional

def split_file(
    input_file: str,
    output_dir: str,
    chunk_size: int,
    progress_callback: Optional[Callable[[str, float], None]] = None
) -> str:
    """
    Splits a text file into smaller chunks, filtering out comments and empty lines.
    
    Args:
        input_file: Path to the input text file.
        output_dir: Directory where the 'hosts_chunks' folder will be created.
        chunk_size: Number of lines per chunk.
        progress_callback: Optional function(status_message, progress_percentage) for updates.
        
    Returns:
        The path to the created chunks directory.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    if progress_callback:
        progress_callback("Reading input file...", 0.1)

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if progress_callback:
        progress_callback("Filtering lines...", 0.2)

    # Filter out empty lines and comments (lines starting with #)
    filtered_lines = [
        line for line in lines 
        if line.strip() and not line.strip().startswith('#')
    ]
    
    total_lines = len(filtered_lines)
    if total_lines == 0:
        raise ValueError("No valid lines found in the input file.")

    num_chunks = math.ceil(total_lines / chunk_size)
    
    chunks_dir = os.path.join(output_dir, "hosts_chunks")
    os.makedirs(chunks_dir, exist_ok=True)

    if progress_callback:
        progress_callback(f"Found {total_lines} valid lines. Creating {num_chunks} chunks...", 0.3)

    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = min(start_idx + chunk_size, total_lines)
        chunk_content = filtered_lines[start_idx:end_idx]

        chunk_filename = f"hosts_part_{i + 1:02}_of_{num_chunks:02}.txt"
        chunk_path = os.path.join(chunks_dir, chunk_filename)

        with open(chunk_path, 'w', encoding='utf-8') as f:
            f.writelines(chunk_content)

        if progress_callback:
            # Progress from 0.3 to 1.0
            progress = 0.3 + ((i + 1) / num_chunks) * 0.7
            progress_callback(f"Created: {chunk_filename} ({len(chunk_content)} lines)", progress)

    return chunks_dir
