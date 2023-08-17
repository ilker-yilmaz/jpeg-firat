import os
import shutil


def create_directories(base_directory, folder_name):
    plt_save_directory = os.path.join(base_directory, folder_name, f"compressed-{folder_name}-plt")
    compressed_image_directory = os.path.join(base_directory, folder_name, f"compressed-{folder_name}-images")
    excel_file_directory = os.path.join(base_directory, folder_name, f"compressed-{folder_name}")

    os.makedirs(plt_save_directory, exist_ok=True)
    os.makedirs(compressed_image_directory, exist_ok=True)

    return plt_save_directory, compressed_image_directory, excel_file_directory


base_directory = "C:/Users/ilker/Desktop/deneme"
source_directory = os.path.join(base_directory, "pnomoni")

for i, filename in enumerate(os.listdir(source_directory)):
    if filename.startswith("image-"):
        folder_name = "compressed-"+filename.split("-")[1].split(".")[0]

        plt_save_directory, compressed_image_directory, excel_file_directory = create_directories(base_directory,
                                                                                                  folder_name)

        img_path = os.path.join(source_directory, filename)

        # Move image to the compressed image directory
        new_img_path = os.path.join(compressed_image_directory, filename)
        shutil.copy(img_path, new_img_path)

        # Perform additional operations (e.g., compression) on the image if needed

        # Create a new Excel file or perform other operations in the excel_file_directory

        print(f"Processed image {filename} in folder {folder_name}")


