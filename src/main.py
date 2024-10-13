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
    img = None

    try:
        print(f"Processing file: {args.filename}...")

        # Attempt to open file using pyexiv2.
        img = pyexiv2.Image(filename=args.filename)
        mime_type = img.get_mime_type()

        print(f"File type: {mime_type}")

        # Output jpeg comment field value only if file mime type is jpeg.
        match mime_type:
            case 'image/jpeg':
                jpeg_comment = img.read_comment()
                print(f"Comment for JPEG: {'(None)' if jpeg_comment == '' else img.read_comment()}")
            case _:
                pass

        # Read metadata.
        exif = img.read_exif()
        iptc = img.read_iptc()
        xmp = img.read_xmp()

        print('\nEXIF metadata')
        print('--------------------------------------------------------------------------------')

        for exif_item in exif:
            print(f"{exif_item}: {exif[exif_item]}")
        print("\nDone processing EXIF metadata.")

        print('\nIPTC metadata')
        print('--------------------------------------------------------------------------------')
        for iptc_item in iptc:
            print(f"{iptc_item}: {iptc[iptc_item]}")
        print("\nDone processing IPTC metadata.")

        print('\nXMP metadata')
        print('--------------------------------------------------------------------------------')
        for xmp_item in xmp:
            print(f"{xmp_item}: {xmp[xmp_item]}")
        print("\nDone processing XMP metadata.")


    except RuntimeError as e:
        # Catch error(s).
        print(f"ERROR: Unable to open file {args.filename}!")
        print(f"Error details: {e}")

    finally:
        if img is not None:
            # Cleanup to avoid memory leaks.
            img.close()
            print("\nDone processing file.")


if __name__ == '__main__':
    # Run when script is executed directly.
    main()
