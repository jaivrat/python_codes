import requests


image_folder = "/Users/jvsingh/work/github/python_codes/ml-python/pytorch_tut/images/"
files = ["sample_image_seven.png" , "my_image_five_test.png", "my_image_3_test.png"]

for file in files:
    print(f"Sending image {file} to server")
    filepath = image_folder + file
    resp = requests.post("http://localhost:5000/predict", 
                     files = {'file':open(filepath,'rb')})
    print(resp.text)
