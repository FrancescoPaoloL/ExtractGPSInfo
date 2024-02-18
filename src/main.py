import os
from exif_utils import get_exif_data, extract_gps_location, save_exif_data_to_file
from location_utils import find_location_name
from file_utils import get_main_directory, construct_full_path

def main():
    main_directory = get_main_directory()
    
    image_filename = input("Enter the name of the image file (default: test.jpg): ")
    if not image_filename:
        image_filename = "test.jpg"
    
    image_path = construct_full_path(main_directory, image_filename)
    
    if not os.path.exists(image_path):
        print("Error: Image file not found.")
        return
    
    exif_data = get_exif_data(image_path)
    
    latitude, longitude = extract_gps_location(exif_data, image_filename)
    
    if latitude is not None and longitude is not None:
        location_name = find_location_name(latitude.values[0], longitude.values[0])
        print("Location:", location_name)
    else:
        print(f"No GPS data found in {image_filename}")
    

    save_file = input("Do you want to save the extracted EXIF data to a file? (y/n): ").lower()
    if save_file.strip() == 'y':
        output_filename = input(f"Enter the name of the output file (default: {image_filename}_exif_data.txt): ")
        if not output_filename:
            output_filename = f"{image_filename}_exif_data.txt"
        
        output_file = construct_full_path(main_directory, output_filename)
        
        save_exif_data_to_file(exif_data, output_file)
        print(f"EXIF data saved to {output_file}")
    else:
        print("EXIF data not saved.")

    
if __name__ == "__main__":
    main()
