
def imageDistance(focal_length, object_distance):
    return 1 / (1/(focal_length)-1/(object_distance))

def magnification(object_distance, image_distance):
    return -(image_distance/object_distance)

def imageSize(object_size, magnification):
    return object_size * magnification


