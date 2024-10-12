#!/usr/bin/env python

import argparse


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





if __name__ == '__main__':
  # Run when script is executed directly.
  main()
