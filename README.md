**Kerbbonize-py-002**

# Description
Kerbbonize, a program utilizing ***Python Tkinter, CustomTkinter, and PIL*** made to effortly transform all instances of a color of a pixel into a transparent background. providing an output image that is a frame for all event promotions of a school organization during their DP blasts. 

Please note that while the program excels at creating the frames, image layering behind the frame is still a work-in-progress. 

## Function that changes all instance of pixel color to transparent
Revolves around comparing RGBA values of a pixel from (0, 0, 0, 0). Tolerance can be adjusted to smoothen out edges of transformed pixels. Through testing, a value of 120 was determined without adversely affecting the image. ValueError also exists when image has no alpha channel, hence, code is adjusted to have alpha value = 255 as default value.

```python

    print("Changing all instances with color {} to transparent".format(pixel_color))
    transparent_color = (0, 0, 0, 0)  # RGBA Format
    target_color = pixel_color

    width, height = image.size

    # tolerance from RGB values (0-255)
    tolerance = 120

    # get RGB from RGBA
    tr, tg, tb = target_color[:3]

    for i in range(width):
        for j in range(height):
            try:
                cr, cg, cb, _ = image.getpixel((i, j))  # pixel color at (i, j) with format RGBA
            except ValueError:
                cr, cg, cb = image.getpixel((i, j))[:3]

            if (abs(cr - tr) <= tolerance and abs(cg - tg) <= tolerance and abs(cb - tb) <= tolerance):
                image.putpixel((i, j), transparent_color)  # change if pixel color is within tolerance
```
## Sample Input and Output
![image](https://github.com/kerbs001/Kerbbonize-py-002/assets/155122597/a69e24e5-071a-4ade-bbd6-00751628c4e8)

![Frame_No BG](https://github.com/kerbs001/Kerbbonize-py-002/assets/155122597/45b798a7-8be3-4b50-a669-b3c4683c7998)

## Development Update

