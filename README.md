# Change-Image-Format
python code to change format of image 

Python Imaging Library (PIL) to change the format of an image to PNG, JPEG, HEIC, or JPG.

The change_image_format() function takes the input image file path, the desired output file path, and the output format as parameters. It uses PIL's Image.open() method to open the image, and then saves it in the specified output format using the save() method.

When you run the code, it will prompt you to enter the path to the input image file, the path for the output image file, and the desired output format (either png, jpeg, heic, or jpg).

Please note that for HEIC format, additional dependencies might be required, such as the pyheif library or the installation of external tools like libheif. Make sure you have the necessary dependencies installed if you intend to convert to HEIC format.
