#!/usr/bin/env python3
# generated with AI

import argparse
import glob
import os
import re
import time
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple

def read_files(input_dir: str) -> str:
    """Read all files from input directory and concatenate their content."""
    content = []
    for file_path in glob.glob(os.path.join(input_dir, '*')):
        with open(file_path, 'r', encoding='utf-8') as f:
            content.append(f.read())
    return ' '.join(content)

def extract_words(text: str) -> List[str]:
    """Extract Roman Pali words using regex pattern."""
    # Include both standard Latin and Pali special characters
    pattern = r'[a-zA-ZāīūṁṃṇḍḷṛṣśṭñṅĀĪŪṀṂṆḌḶṚṢŚṬÑṄ]+'
    words = re.findall(pattern, text)
    return [word.lower() for word in words if len(word) > 1]

def count_words(words: List[str]) -> List[Tuple[str, int]]:
    """Count word frequencies and return sorted list of (word, count) tuples."""
    counter = Counter(words)
    return sorted(counter.items(), key=lambda x: (-x[1], x[0]))

def generate_txt_file(word_counts: List[Tuple[str, int]], output_file: str):
    """Generate text file with word frequencies."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for idx, (word, count) in enumerate(word_counts, 1):
            f.write(f"{idx} {word} {count}\n")

def generate_csv_file(word_counts: List[Tuple[str, int]], output_file: str, limit: int = 180000):
    """Generate CSV file for Android keyboard dictionary."""
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write("_id,word,frequency,locale,appid,shortcut\n")
        
        # Write data
        for idx, (word, count) in enumerate(word_counts[:limit], 1):
            # Calculate frequency
            freq = min(count + 100, 250)
            f.write(f"{idx},{word},{freq},,0,\n")

def main():
    parser = argparse.ArgumentParser(description='Word frequency analyzer')
    parser.add_argument('input_dir', help='Directory containing input files')
    parser.add_argument('--txt-output', default='topword.txt', help='Output TXT file path')
    parser.add_argument('--csv-output', default='user_dict.csv', help='Output CSV file path')
    args = parser.parse_args()

    # Ensure input directory exists
    if not os.path.isdir(args.input_dir):
        print(f"Error: Input directory '{args.input_dir}' does not exist")
        return

    print("|----------------------------|")
    print("|         Script 1           |")
    print("|    Generating TXT file     |")
    print("|----------------------------|")
    
    start_time = time.time()
    
    # Process files
    content = read_files(args.input_dir)
    words = extract_words(content)
    word_counts = count_words(words)
    
    # Generate output files
    generate_txt_file(word_counts, 'topword.txt')
    
    print(f"Time elapsed: {time.time() - start_time:.2f} seconds\n")

    print("|----------------------------|")
    print("|         Script 2           |")
    print("|    Generating CSV file     |")
    print("|----------------------------|")
    
    start_time = time.time()
    
    generate_csv_file(word_counts, args.csv_output)
    
    print(f"Time elapsed: {time.time() - start_time:.2f} seconds\n")

    print("|----------------------------|")
    print("|         Done all           |")
    print("|----------------------------|")

if __name__ == '__main__':
    main()