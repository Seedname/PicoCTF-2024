import piexif

exif_dict = piexif.load("Blast from the Past/original_modified.jpg")
exif_dict["ModifyDate"] = "1970:01:01 00:00:00"
exif_dict["DateTimeOriginal"] = "1970:01:01 00:00:00"
exif_dict["CreateDate"] = "1970:01:01 00:00:00"
exif_dict["SubSecTime"] = "1970:01:01 00:00:00.001"
exif_dict["SubSecTimeOriginal"] = "1970:01:01 00:00:00.001"
exif_dict["SubSecTimeDigitized"] = "1970:01:01 00:00:00.001"
# new_exif = adjust_exif(exif_dict)
exif_bytes = piexif.dump(exif_dict)
piexif.insert(exif_bytes, "Blast from the Past/original_modified.jpg")
