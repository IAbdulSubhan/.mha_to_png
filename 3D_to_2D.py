# Install this library first
# !pip install SimpleITK numpy

import os
import SimpleITK as sitk
import matplotlib.pyplot as plt

# Specify the path to the folder
specific_folder = "../../3D to 2D"

# Get a list of all folders inside the specific folder
folders = [folder for folder in os.listdir(specific_folder) if os.path.isdir(os.path.join(specific_folder, folder))]

# Print the list of folders
print("Folders in the specific folder:")
for folder in folders:
    # Assuming the path to the folder containing .mha files
    
    input_folder = specific_folder+"/"+folder

    # Get a list of all image files in the folder
    image_files = [file for file in os.listdir(input_folder) if file.endswith('.mha')]
    # Loop through each image file
    for image_file in image_files:
        # Construct the full path to the image
        image_path = os.path.join(input_folder, image_file)

        # Read the image using SimpleITK
        image = sitk.ReadImage(image_path)

        # Convert the image to a NumPy array for easier manipulation
        image_array = sitk.GetArrayFromImage(image)

        # Create a folder with the complete image name
        image_name = os.path.splitext(image_file)[0]  # remove the extension
        output_folder = os.path.join(input_folder, image_name)
        os.makedirs(output_folder, exist_ok=True)

        # Save 2D slices inside the created folder
        for i in range(image_array.shape[0]):
            plt.imshow(image_array[i, :, :], cmap='gray')
            plt.title(f"Slice {i}")

            # Save the image to the output folder
            image_filename = f"slice_{i}.png"
            image_path = os.path.join(output_folder, image_filename)
            plt.savefig(image_path)

            # Close the plot to avoid displaying the images in the loop
            plt.close()

        print(f"2D slices saved for {image_file} in {output_folder}")

# Print a message indicating the process is complete
print("All 2D slices saved.")
