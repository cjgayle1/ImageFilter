# ImageFilter

This was a fun project for me to experiment with NumPy and some other Python libaries I wanted to try out,
including some basic ML.
The initial idea came from the famous Obama hope picture. I wanted to create a program that could edit
the RGB values of an image and put a filter similar to that one on it. This ended up working and I created
a few more sample filters for it that work as well but the possibilites are as many as there are colors.

Essientially what the code does is process an image into RGB values, classifies those values into a specified number
of categories based on similarity of value, then it changes the RGB values of each classified category into that of 
the pre-selected color values of the filter.
