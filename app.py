from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_images_from_cian(address):
    search_url = f"https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=1&address={address}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    images = []
    for img in soup.find_all('img', {'alt': 'фотография объекта'}):
        img_url = img.get('src')
        if img_url:
            images.append(img_url)

    return images


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        address = request.form['address']
        images = get_images_from_cian(address)
        return render_template('index.html', images=images, address=address)
    return render_template('index.html', images=None)


if __name__ == '__main__':
    app.run(debug=True)