import os
from exif_utils import get_exif_data, extract_gps_location, save_exif_data_to_file
from location_utils import find_location_name
from file_utils import get_main_directory, construct_full_path

def main():
    main_directory = get_main_directory()
    
    image_filename = input("Enter the name of the image file (default: example.jpg): ")
    if not image_filename:
        image_filename = "example.jpg"
    
    image_path = construct_full_path(main_directory, image_filename)
    
    if not os.path.exists(image_path):
        print("Error: Image file not found.")
        return
    

    
if __name__ == "__main__":
    main()
