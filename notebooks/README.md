# README

##  github codespaces setup

These are notes on how to setup a vs code installation using github codespaces for use with 
jupyter/inotebooks

### workflow

1. start a githubcodespace via a git repo
2. using settings icon in lower left, select themes
3. in terminal create the venv
    
    This varies for notebooks and webapps.  In this case I'll show how to do it for the notebooks
    1. `cd notebooks`
    2. `mkdir nbenv`
    3. `cd nbenv` 
    5.  `python -m venv nbenv`
    6.  `source nbenv/bin/activate`
        - at this point you should notice your prompt has a prefix of `(nbenv)` meaning the venv is operational
    7.  `pip install --upgrade pip`
    8.  `python -m pip install numpy`
        - just to test that you can install `numpy`
    9. `cd ..`
        - For now, there is just one requirements.txt and its above this dir
    9. `python install -r requirements.txt`
        - this installs the common identified modules for the notebooks in this venv
    7. `add .gitignore for nbenv`
        - this is so that git does not try to CM your modules
        - `echo nbenv/nbenv/ >> .gitignore`
4. Install jupyter notebooks in vscode
    1. click extensions in left sidebar
    2. type jupyter<CR>
    3. select jupyter from microsoft
5. Setup python inpreter for the VS Code workspace
    1. cmd shift p to bring up command window
    2. type `Python: Select Interpreter`
    3. click the use existing option 
    3. Use browse capability to browse to `notebooks/nbenv/bin/python3`
6. In the file menu, create a new notebook
    1. click explorer on left sidebar
    2. click notebooks in the file explorer
        - We want to create the notebook in this folder
    3. click the add file button at the top of the explorer to add a new file
        - name it `foo.ipynb`
        - click the new file and it should bring up a blank python jupyter notebook
6. Test notebook setup
    1. Use this code for the first cell

        ```
        from pprint import pprint
        foo={"id": 1,"name": "Leanne Graham","username": "Bret","email": "Sincere@april.biz","address": {  "street": "Kulas Light",  "suite": "Apt. 556",  "city": "Gwenborough",  "zipcode": "92998-3874",  "geo": {    "lat": "-37.3159",    "lng": "81.1496"  }},"phone": "1-770-736-8031 x56442","website": "hildegard.org","company": {  "name": "Romaguera-Crona",  "catchPhrase": "Multi-layered client-server neural-net",  "bs": "harness real-time e-markets"}}
        pprint(foo)

        import pandas as pd
        df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
        print(df)
        ```
7. On right hand side, it will say in the menu bar, `Select Kernel`
    1. click the `Select Kernel` button
    2. click `nbenv` which is recommended
8. Within github codespaces, the python env file is in top level of gitrepo.  
    1. Put `.env` at top level
    2. place api key in this file
    3. add to `.gitignore`




## vs code multiple tabs

```
Within your settings, under workbench, set:

"workbench.editor.enablePreview": false,
"workbench.editor.enablePreviewFromQuickOpen": false
This will allow you to open the files with a single click, as opposed to double-clicking. It may seem minute, but it was incredibly annoying to have to double-click every single file.
```


# Creating service accounts for these notebooks


## Authentication

### Set and create
```
$ SERVICE_ACCOUNT_ID=jams-devpost
$ gcloud iam service-accounts create $SERVICE_ACCOUNT_ID  \
    --description="A custom service account for Vertex custom training with Tensorboard" \
    --display-name="Vertex AI Custom Training"
```
## Authorization

### cloud storage

```
$ PROJECT_ID=$(gcloud config get-value core/project)
$ gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member=serviceAccount:$SERVICE_ACCOUNT_ID@$PROJECT_ID.iam.gserviceaccount.com \
    --role="roles/storage.admin"
```

### App engine

App Engine default service account	
Editor

```
$ gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member=serviceAccount:$SERVICE_ACCOUNT_ID@$PROJECT_ID.iam.gserviceaccount.com \
    --role="roles/appengine.appAdmin"
```


### Vertex AI

```
$ gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member=serviceAccount:$SERVICE_ACCOUNT_ID@$PROJECT_ID.iam.gserviceaccount.com \
    --role="roles/aiplatform.serviceAgent"
 ```
    

## create the json key

```
$ gcloud iam service-accounts keys create ~/path/to/your-key-file.json --iam-account SERVICE_ACCOUNT_NAME@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

