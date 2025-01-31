# Todo list

## Base functionality

### High priority

- add basic functions
    - folder selector in the extension
    - option to create new folder in extension
    - delete bookmark option in the extension
    - move between folders (managed on the website)

- stop using XMLHttpRequest

- find a way to not need {'Access-Control-Allow-Origin': '*'} on every return



### Low priority

- add managing website

- if the user in on a site they have favorited, the extension's logo should change

- make bookmarks have thumbnails

- make extension connection secure (no idea how)


## Dilemma

- should duplicate bookmarks be alowed?




---

# Dev setup

## Create a virtual enviroment (recommended)

Run: `python -m venv .venv`


## Activate virtual enviroment

On linux run: `source .venv/bin/activate`

On windows run in cmd: `.\venv\Scripts\activate.bat`
(there is no `.\venv\Scripts\`, oops)


## Install requirements

Run: `pip install -r requirements.txt`




Create requirements with:
`pip freeze > requirements.txt`
