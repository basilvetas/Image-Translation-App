from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from config import API_KEY

def main():
    app = ClarifaiApp(api_key=API_KEY)
    model = app.models.get('dogBreeds')

    url = raw_input("URL of image: ")
    try:
        print model.predict_by_url(url)['outputs'][0]['data']['concepts'][0]
    except:
        print("try another one?")


if __name__ == '__main__':
    main()
