from pathlib import Path
import os
import pestuary

data_directory = 'data'

datasets = [
    {
        "name": "bodemkwaliteit.csv",
        "url": "https://maps.amsterdam.nl/open_geodata/excel.php?KAARTLAAG=BODEMKWALITEIT&THEMA=bodemkwaliteit"
    }
]

for dataset in datasets:
    Path(data_directory).mkdir(exist_ok=True)
    name = dataset['name']
    url = dataset['url']
    pestuary.utils.download_dataset_from_url(name, url, data_directory=data_directory)

    resp = pestuary.contentApi.content_add_post(data=os.path.join(data_directory, name), filename=name)
    print(resp)
