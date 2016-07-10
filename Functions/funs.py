#returns all objects in an image using Google Cloud Vision API
def start_img(img):

#gets the list of images that need to be removed
def get_remove_list():


#returns whether
def test_img(img, list):
    for i in range(len(list)):
        if i == img:
            return True
    return False


#returns all the logos in an image that need to be removed
def get_all_logos(input):
    imgs = start_img(input)
    output = []
    for img in imgs:
        if test_img(img, get_remove_list):
            output.append(img)

    return output
