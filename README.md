# exif-reader

A command line application that reads EXIF information from an image file or sidecar file (.XMP) associated to an image file and prints it to the console. 

## Specifications
- Command line application written in Python. 


## Requirements
- Must accept command line parameter to path of image file.
- Use `pyexiv2` package for reading EXIF information. 
- Must output all available metadata to the screen.
- Provide optional command line parameter to output value of a specific metadata tag. 
- Gracefully handle errors.
- Provide unit tests. 

## Instructions

### Launching the App
`python3 main.py`
