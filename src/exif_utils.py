import exifread

def get_exif_data(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)
    return tags

def extract_gps_location(exif_data):
    if 'GPS GPSLatitude' in exif_data and 'GPS GPSLongitude' in exif_data:
        latitude = exif_data['GPS GPSLatitude']
        longitude = exif_data['GPS GPSLongitude']
        return latitude, longitude
    else:
        print("GPS data not found in the image EXIF.")
        return None, None

def save_exif_data_to_file(exif_data, output_file):
    with open(output_file, 'w') as f:
        for tag, value in exif_data.items():
            f.write(f"{tag}: {value}\n")
