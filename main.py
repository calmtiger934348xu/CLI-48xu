#!/usr/bin/env python3
"""
dirstat - simple CLI tool to get statistics of a directory.
Usage: python dirstat.py [path]
"""

import os, argparse, sys

def dir_stats(path):
    total_files = 0
    total_dirs = 0
    total_size = 0
    for root, dirs, files in os.walk(path):
        total_dirs += len(dirs)
        total_files += len(files)
        for f in files:
            try:
                total_size += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total_files, total_dirs, total_size

def main():
    parser = argparse.ArgumentParser(description="Directory statistics")
    parser.add_argument('path', nargs='?', default='.', help='Directory path')
    args = parser.parse_args()
    if not os.path.isdir(args.path):
        sys.exit(f"Error: {args.path} is not a directory")
    files, dirs, size = dir_stats(args.path)
    print(f"Path: {args.path}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")
    print(f"Total size: {size} bytes")

if __name__ == "__main__":
    main()