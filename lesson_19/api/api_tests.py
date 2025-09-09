import requests
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_PATH = os.path.join(BASE_DIR, "mars", "mars_photo1.jpg")
print(BASE_DIR)
print(IMAGE_PATH)

class Image:
    def __init__ (self, base_url = "http://127.0.0.1:8080"):
        self.base_url = base_url
        self.filename = None


    def image_upload(self):
        with open(IMAGE_PATH, "rb") as image_file:
            files = {"image": image_file }
            response = requests.post(f"{self.base_url}/upload", files = files)
            if response.status_code == 201:
                data = response.json()
                self.filename = data['image_url'].split('/')[-1]
                print(self.filename)
                print(f"успешно загружено: {data['image_url']}")
                return data["image_url"]
            else:
                print(f"произошло ошибка: {response.text}")
                return None


    def image_get(self):
        headers = {"Content-Type": "text"}
        response = requests.get(f"{self.base_url}/image/{self.filename}", headers = headers)
        if response.status_code == 200:
            data = response.json()
            print(f"info: {data["image_url"]}")
            return data["image_url"]
        else:
            print(f"Error: {response.text}")
            return None


    def image_delete(self):
        response = requests.delete(f"{self.base_url}/delete/{self.filename}")
        if response.status_code == 200:
            data = response.json()
            print(f"info: {data["message"]}")
            return data["message"]
        else:
            print(f"Error: {response.text}")
            return None







if __name__ == "__main__":
    img = Image()
    img.image_upload()
    img.image_get()
    img.image_delete()