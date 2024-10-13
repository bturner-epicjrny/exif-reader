# exif-reader

A command line application that reads EXIF information from an image file or sidecar file (.XMP) associated to an image
file and prints it to the console.

## Specifications

- Command line application written in Python.

## Requirements

- Must accept command line parameter to path of image file.
- Use `argparse` package to process command line parameters.
- Use `pyexiv2` package for reading EXIF information.
- Must output all available metadata to the screen.
- Provide optional command line parameter to output value of a specific metadata tag.
- Gracefully handle errors.
- Provide unit tests.

## Setup

- On macOS, the *pyexiv2* package requires libinih. Install this library using the following command-line instruction:
    - `brew install inih`

## Instructions

### Launching the App

`python3 main.py filename` 
