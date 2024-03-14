import pyexiv2
import subprocess

# subprocess.run(["exiftool(-k).exe", "-AllDates=1970:01:01 00:00:00", "original.jpg"], shell=True)

img = pyexiv2.Image("original.jpg")

img.modify_exif({
    'Exif.Image.DateTime': '1970:01:01 00:00:00',
    'Exif.Photo.DateTimeOriginal': '1970:01:01 00:00:00.001',
    'Exif.Photo.DateTimeDigitized': '1970:01:01 00:00:00.001',
    'Exif.Photo.SubSecTimeDigitized': '001',
})
