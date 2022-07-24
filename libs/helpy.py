# Animals photos' urls

image_urls = [
    "https://user-images.githubusercontent.com/70684994/179326921-0a70f671-2f7e-4af7-b17a-642c81293940.jpeg",
    "https://user-images.githubusercontent.com/70684994/179327013-973f27b9-b3ce-4310-8f40-ce8cd5b66296.jpg",
    "https://user-images.githubusercontent.com/70684994/179327217-905907b0-5355-4db8-bfe1-2ebddea97bf0.jpeg",
    "https://user-images.githubusercontent.com/70684994/179327277-e941d449-db8d-4a42-804e-da3270372cdc.jpg",
    "https://user-images.githubusercontent.com/70684994/179327356-ab0eb452-e87a-4218-a5d1-389e0510f024.jpeg"
]

animals = [
    'Cat',
    'Dog',
    'Bird',
    'Livestock',
    'Other'
]

animal_photos = dict()
for i, j in zip(image_urls, animals):
    animal_photos[j] = i



# Buttons that used in third page to search and add new record.

class BUTTON:
    def __init__(self, click):
        self.click = click

    def isNew(self, newClick):
        if (self.click == newClick):
            return False
        elif ((newClick == 0) | (newClick == None)):
            return False
        else:
            self.click = newClick
            return True


# Animal count calculater (actually its filter the target value)
def animal_counts(df, animal):
    # I used here try-except bc; after datepicker selected , if there is no data for a animal type, this mean it is equal to 0
    try:
        return df[df['animal_type'] == animal].iloc[0,1]
    except:
        return 0