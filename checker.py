from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
 
def get_exif_data(image):
    exif_data = {}
    exif = Image.open(image)._getexif()
    if exif:
        for tag, value in exif.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                for info in value:
                    exif_data[GPSTAGS.get(info, info)] = value[info]
 
    return exif_data
 
def if_exist(data):
    if 'GPSLatitude' and 'GPSLongitude' and 'GPSAltitude' in data:
        return True
    else:
        return False

def check(file_names):
    valid = list()
    not_valid = list()
    for image in file_names:
        if image.endswith(('.jpg', '.JPG')):
            exif_data = get_exif_data(image)
            if if_exist(exif_data):
                valid.append(image)
            else:
                not_valid.append(image)
        else:
            not_valid.append(image)
    return valid, not_valid