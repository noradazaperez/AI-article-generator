import google.generativeai as palm

API_KEY = 'AIzaSyDJLl-f-jRe28WVcN0NkI7n2e5BF243ViM'
palm.configure(api_key=API_KEY)

model_list = [_ for _ in palm.list_models()]
for model in model_list:
    print(model.name)