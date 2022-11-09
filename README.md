# 📹 Youtube Video Downloader

This is open source project in Python using [Streamlit](https://streamlit.io/) to download and convert videos from Youtube.

<img width="583" alt="screenshot" src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7c83ebed-4213-4ac2-b360-4594411cdb37/Capture_decran_2022-11-05_a_15.02.09.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221105T142658Z&X-Amz-Expires=86400&X-Amz-Signature=ab64dc4a717aea77c04500f546f9d0b628c99954bd87eb1beb9ffe7080b7e941&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Capture%2520d%25E2%2580%2599e%25CC%2581cran%25202022-11-05%2520a%25CC%2580%252015.02.09.png%22&x-id=GetObject">


## Installation

We recommended to install it and all its dependencies, inside a virtual environnement and through the Python Package Index.

Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.
### Creating a virtual environment
```bash
  virtualenv env
  source env/bin/activate
```
### Install dependencies
```bash
  pip install streamlit
  pip install -r requirements.txt  
```
### Run
```bash
  streamlit run app.py
```

The video/audio downloaded will be stored in the same folder


