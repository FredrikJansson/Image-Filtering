try:
    from PIL import ImageFilter
    from PIL import Image
except:
    raise ImportError("Pillow is required.")


def square_picture(file_name, out_name="out"):
    with Image.open(file_name) as img:
        # Convert to RBGA.
        #img = im.convert("RGBA")

        # Apply filter.
        img = img.filter(ImageFilter.FIND_EDGES)

        # Get data.
        datas = img.getdata()

        # Convert black pixels to transparent.
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        img.save(out_name + ".png", "PNG")


if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args < 2:
        raise KeyError
    if args == 2:
        square_picture(sys.argv[1])
    else:
        square_picture(sys.argv[1], sys.argv[2])