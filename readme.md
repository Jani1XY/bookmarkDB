# Todo list

## Base functionality

### High priority

- add basic functions
    - folder selector in the extension
    - option to create new folder in extension
    - move between folders (managed on the website)
    - add confirmation when pressing delete on extension

- website displays every bookmark

- find a way to not need {'Access-Control-Allow-Origin': '*'} on every return



### Low priority

- add managing website

- if the user in on a site they have favorited, the extension's logo should change

- make bookmarks have thumbnails

- make extension connection secure (no idea how)



---

# Dev setup

## Create a virtual enviroment (recommended)

Run: `python -m venv .venv`


## Activate virtual enviroment

On linux run: `source .venv/bin/activate`

On windows run in cmd: `.\venv\Scripts\activate.bat`


## Install requirements

Run: `pip install -r requirements.txt`




Create requirements with:
`pip freeze > requirements.txt`
