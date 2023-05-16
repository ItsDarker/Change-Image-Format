from PIL import Image

def change_image_format(input_path, output_path, output_format):
    try:
        # Open the image
        image = Image.open(input_path)
        # Save the image in the desired format
        image.save(output_path, format=output_format)
        print(f"Image saved as {output_path}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
input_file = input("Enter the path to the input image: ")
output_file = input("Enter the path for the output image: ")
output_format = input("Enter the desired output format (png, jpeg, heic, jpg): ")

change_image_format(input_file, output_file, output_format)
