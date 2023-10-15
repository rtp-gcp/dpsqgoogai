# dpsqgoogai
DEVPOST Square Google Fintech AI Hackathon


This is a project for a [DEVPOST](https://devpost.com) hackathon.

It demos 

* Square (SQ) Online Store operations and relationship to developer APIs

* Square's squareup API for python
    * for creating items to list in SQ online store (storefront webapp)
    * Provides samples in python for 
        * creating an item to sell
        * associating an image for a item listing
        * listing items
        * how to use the sandbox versus production environments
        * Endpoints used
            * category  TODO: get real names
            * inventory
            * invoice
            * orders
        
* Google Cloud Platform (GOOG/GCP) Vertex GenAI API for python
    * for automated test descriptions of item variations
    * Provides samples in python for
        * shows how to use the API outside of a collab or Vertex AI notebook
        * creating automated text of specified topic and brevity

* Google Cloud Platform Python based Webapp using App Engine Microservice

    The goal was to use this as the webapp for submitting to SQ Apps marketplace.
    However, this capability is unfinished.  Currently, its just a webapp that demos
    use of the invoice API.
    * Lists selected columns of the invoices created by the store listing


## Guide to the project

* [Deliverables.md] contains text for the hackathon project submission
* [notebooks] contains jupyter notebooks for prototyping code using: 
    - [squareup API docs](https://developer.squareup.com/docs) 
    - [squareup API explorder](https://developer.squareup.com/explorer/square)
    - [vertex API](https://cloud.google.com/python/docs/reference/aiplatform/latest)
* [webapp] contains code for the [webapp](https://devpost-goog-sq.uc.r.appspot.com/)
* [docs] contains notes on various components
* [secrets] contains encrypted API keys and such

