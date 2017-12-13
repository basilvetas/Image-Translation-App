from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


def main():
    app = ClarifaiApp(api_key='c5c78def8d574935aebbfd8da2c22ed3')
    model = app.models.get('dogBreeds')

    url = raw_input("URL of image: ")
    try:
        print model.predict_by_url(url)['outputs'][0]['data']['concepts'][0]
    except:
        print("try another one?")


if __name__ == '__main__':
    main()
