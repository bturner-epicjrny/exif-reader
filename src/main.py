#!/usr/bin/env python

import argparse
import pyexiv2


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

  try:
    # Attempt to open file using pyexiv2.
    img = pyexiv2.Image(filename=args.filename)
  except RuntimeError as e:
    # Catch error(s).
    print(f"ERROR: Unable to open file {args.filename}!")
    print(f"Error details: {e}")







if __name__ == '__main__':
  # Run when script is executed directly.
  main()
