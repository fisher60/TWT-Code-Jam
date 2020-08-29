def get_images(topic):
    from bs4 import BeautifulSoup
    import requests
    import re
    import random
    import requests
    from pathlib import Path
    from PIL import Image
    from io import BytesIO

    location = str(Path(__file__).parent.absolute())
    url = f"https://unsplash.com/s/photos/{topic}"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    Images = [x.get('src') for x in soup.find_all('img', alt=True) if "w=1000" in x.get('src')]
    chosen_images = set([random.choice(Images) for x in range(15)])
    images = list(chosen_images)[:3]
#    my_images = []
    for i,x in enumerate(images):
        r = requests.get(x)
        with open(location+ r"/images/image{}.jpg".format(i),"wb") as f:
            f.write(r.content)
        im = Image.open(location + r"/images/image{}.jpg".format(i))
        im = im.resize((650,325))
        im.save(location+r"/images/image{}.jpg".format(i))
#        my_images.append(Image.open(BytesIO(response.content)))
#    print(my_images)
#    image1,image2,image3 = images
#    return images
if __name__ == "__main__":
    r = requests.get(image1)
    with open(location+ r"\images\image1.jpg","wb") as f:
        f.write(r.content)

    r = requests.get(image2)
    with open(location+ r"\images\image2.jpg","wb") as f:
        f.write(r.content)

    r = requests.get(image3)
    with open(location+ r"\images\image3.jpg","wb") as f:
        f.write(r.content)
