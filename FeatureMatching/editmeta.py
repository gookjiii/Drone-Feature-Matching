import json
import piexif.helper
import cv2
from PIL import Image

#convert png to jpg
png_img = cv2.imread('D:/CyberIntellect/FeatureMatching/images/res.png')
cv2.imwrite('D:/CyberIntellect/FeatureMatching/images/res.jpg', png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

#getData
content = list()
with open('D:/CyberIntellect/FeatureMatching/images/res.pgw') as f:
    [content.append(line.strip()) for line in f.readlines()]

userdata = {
    'Horisontal pixel distribution': content[0],
    'Y screw/rotation': content[2],
    'X screw/rotation': content[4],
    'Vertical pixel distribution': content[6],
    'X coordinate for center of top left pixel': content[8],
    'Y coordinate for center of top left pixel': content[10]
}

gps_ifd = {
            piexif.GPSIFD.GPSLatitude: 1,
            piexif.GPSIFD.GPSLongitude:2
            }
img_ifd = {
            piexif.ImageIFD.DefaultScale
            }

filename = 'D:/CyberIntellect/FeatureMatching/images/res.jpg'
exif_dict = piexif.load(filename)

exif_dict["Exif"][piexif.ExifIFD.UserComment] = piexif.helper.UserComment.dump(
    json.dumps(userdata),
    encoding="unicode"
)

piexif.insert(
    piexif.dump(exif_dict), filename
)

img = Image.open(filename)
exif = img.info['exif']

exif_dict['GPS'][piexif.GPSIFD.GPSAltitude] = (140, 1)
exif_bytes = piexif.dump(exif_dict)
img.save(filename , exif=exif_bytes)