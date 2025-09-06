import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url = url, params = params)
data = response.json()

for i in range(2):
    photo_url = data['photos'] [i] ["img_src"]
    photo_response =requests.get(photo_url)

    file_name= f"mars_photo{i+1}.jpg"
    with open(file_name, "wb") as f:
        f.write(photo_response.content)
