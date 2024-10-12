#!/usr/bin/env python

import argparse
import os


def main():
  parser = argparse.ArgumentParser(
    prog='EXIF Reader',
    description='Read EXIF metadata from image/sidecar file and output it to the console.',
  )
  # Add positional parameter for path to image file/sidecar file.
  parser.add_argument(
    'filename', 
    help='Path to image file.')
  
  args = parser.parse_args()

  print(f"Processing file: {args.filename}...")

  # Verify provided filename exists in file system.
  print(f"Provided filename exists in file system: {file_path_valid(args.filename)}")
  



def file_path_valid(filename):
  """Tests if provided provided file exists.

  Args: 
    filename (string): Path to file.

  Returns: 
    bool: True if file exists.
  """
  is_valid_file = os.path.isfile(filename)
  return is_valid_file





if __name__ == '__main__':
  # Run when script is executed directly.
  main()
