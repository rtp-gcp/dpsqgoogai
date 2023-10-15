# Hackathon Deliverables

# General Info

## Project Name
RTP-GCP Project SAJ

## Elevator pitch
SQ and GOOG AI APIs WebApp

# Project Details

## Project Story

### About the project

#### Inspiration

The RTP-GCP usergroup located in Durham, North Carolina, USA meets each weekend to work together to learn how to use Google Cloud Platform.  We were excited to join this hackathon since DEVPOST hackathons are a great way to focus on learning a technology.  Considering we knew nothing about the squareup API, this also seemed like a great oppurtunity to expand our knowledge of that!

#### What it does

This app demonstrates how to build a GCP AppEngine WebApp that uses SQ and GOOG APIs to automate an online store front.  It does this by updating a SQ storefront with items for sale using AI generated product descriptions.  

#### How we built it

The hackathon entry was built in series of steps

###### Step 1

Requirements Analysis

Read the project rules and examine the project awards to determine the set of primary characteristics the submission should contain.  The following table was generated:

| Requirement  Description                      |  Source                      |   Notes                  
| ------------------------------------------| ---------------------- | ------------------- 
| Create an APP                                         | Project Rules             | App integrates to SQ app store
| New or updated                                      | Project Rules             | No prior knowledge so easy yes
| Image/Audio                                           | Project Rules              | Use API to upload image
| online experience                                   | Project Rules             | Simplify product listing
| online experience                                   | Project Rules             | Simplify invoice generation
| One SQ API                                             |                                     |                               
|  [ ] Terminal   option                                |  Project Rules            |                               
|  [ ] Subscriptions  option                        |  Project Rules            |                               
|  [x] Invoices   option                                |  Project Rules            |  Requires inventory item    
| One GOOG Foundation Model API      |                         |                                     |                                
| [x] Text   option                                        |  Project Rules            |  Use Vertex AI  API to generate text                  
| [ ] Chat  option                                         |  Project Rules            |                    
| GOOG Payments API                             |  Project Judges         |                               
| Idea                                                           |                                     |                                
| Quality                                                      | Judges & Criteria      |  #2 goal make it work well                             
| Implementation                                       | Judges & Criteria      |  #1 goal can we make it work                               
| Potential Value                                         | Judges & Criteria      |                                           
| Integrative Experience                           |  Judges & Criteria      |                                
| Potential Impact                                      | Judges & Criteria      |   
| Inventory API                                           | Derived Requirment  |   
| Automate Listing                                     | Derived Requirment  |    
| Automate Invoice                                    | Derived Requirment  |    
| GCP Webapp - Use AppEngine            | Derived Requirement |  Implement in python so all APIs are consistent across notebooks and app, ease of use for integration in samples


#### Challenges we ran into

* All of us are new to GenAI/LLM but we have some knowledge
* All of us are completely new to SQ online stores and their API.  Zero knowledge
* All of us are on a budget.  API usage costs money and time.  Try to use cheap methods
* Some of us have limited knowledge of GCP, none really in terms of Python web apps
* Contest requirements created long list of unknowns in terms of SQ squareup API
  - Invoice API requires use of Inventory API
  - Inventory API is a derived requirement
  - Image manipulation requires use of Inventory API
  - Inventory API requires Category API
  - Category API requires Upsert and Variation knowledge
  - While it makes sense, it does not come easily
  
* SQ Inventory Image API is documented wrong.  Docs and code are not in sync
    - See github issue [here](https://github.com/square/square-python-sdk/issues/121)
    - This was resolved but took time
* SQ API in general are tedious
  - Once we figured out how to use upsert I had to ask about modifying categories.  It turns out
when you upsert an item, all items must be reupdated otherwise they are erased.  ie. if you upload a portion of an item, attempt to upsert modifications to new characteristics, any missing characteristics are erased.  This means no partial updates in a series of small changes.  This was unexpected.
   - No ability to migrate items from in the library to visible in the online store.  Once again, spent considerable time trying to get this to work and finally found this out in the SQ discord chat.  The api should mention limitations to what can not be done.  Especially when visiblity is listed in the online UI and in the API.
   - Feels like the point of this hackathon is to crowdsource testing of the SQ API's and I am an unpaid participant.



#### Accomplishments that we're proud of

* We have something which meets requirements and works.  
* We started with nothing and worked together to have something worthy of a submission.
* We `#builtinpublic` and made a good `#opensource` example of how to use both company's APIs.


#### What we learned

We learned about:
* how to use GOOG Vertex AI in a notebook not hosted in AI Workbench or Collab
* SQ has an online store capabiity
* SQ has an API to manipulate the store
* keep our Python chops up to date

#### What's next for SAJ

If we win some money we will use the money towards updating the app and putting in SQ marketplace.  If not we will leave in GitHub so that others can use it as an idea of how to build a webapp that works with SQ and GOOG APIs.



## Built with

* python
* genai
* square
* google-cloud

## Project Media

TODO: Add PNG images 3:2 ratio 5MB max

## Video demo link

TODO: Add youtube link of demo

# Additional Info

## App Status

"Appears in project gallery"?

TODO:


## Testing instructions for application

TODO:


## Provide access to working application (test account, website, sandbox / production)

TODO: