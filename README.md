# Localized and Personalized Search Engine for COVID-19

## Motivation:
Throughout the COVID-19 pandemic, people’s needs have evolved due to a myriad of closures and stay-at-home orders. Local services have had to adapt themselves to this everyday and this information changes at a fast pace. All of this new and dynamic information is difficult to sift through and not always straightforward to find.


## Goal:
- Our goal is to crawl, aggregate, index and search/retrieve information from local news sources in Baltimore and report back relevant and personalized results to the user.
  - To achieve this, we built a search engine to retrieve relevant articles. We expanded our search engine to simulate user personalization based on the user’s profile, which can be mimicked through topics the user is biased towards, that are incorporated as a string of bias terms at run time. This allows us to retrieve results personalized to the user needs.


## Datasets - Evaluation:
To find an appropriate system for real-world data, we considered 4 labelled datasets ([CACM](http://ir.dcs.gla.ac.uk/resources/test_collections/cacm/), [CISI](https://www.kaggle.com/dmaso01dsta/cisi-a-dataset-for-information-retrieval/version/1), [Medline](http://www.trec-cds.org/2017.html), [Cranfield](http://ir.dcs.gla.ac.uk/resources/test_collections/cran/)) and conducted experiments on this data:
- **CACM:** abstracts and queries from Communications of ACM journal
- **CISI:** documents and queries from Centre for Inventions and Scientific Information
- **Medline:** collection of articles and queries from Medline journals
- **Cranfield:** commonly used IR dataset with aerodynamics journals articles, queries, and relevance judgements

## Datasets - Deployment:
- Then, we selected the best performing permutations from evaluation on development data to deploy on our COVID-19 news data.
- We crawled COVID-19 related articles from Baltimore Sun, CBS Baltimore, and WBALTV since they provide access to focused local information relevant to Baltimore.
- Note: CBS and WBALTV local news source spiders based on [RISJbot](https://github.com/pmyteh/RISJbot)

## Approach:
- **Web crawling and scraping**
  - Scrape a set of websites to create a corpus of documents
- **Preprocessing**
  - **Structured:** Stemming and Stop Words Removal
  - **Unstructured:** Acronyms, Emoticons, Spell Check, Contractions
- **Vectorization and Scoring**
  - **Word embeddings:** (Word2Vec, GloVe, FastText, Doc2Vec, OneHot)
  - **Word embeddings to Sentence embeddings Weighting Schemes:** Mean, TF-IDF, Smooth Inverse Frequency, Unsupervised Smooth Inverse Frequency.
  - **Similarity:** Cosine, Dice, Jaccard or anything from scipy.spatial.distance.
- **Query Optimization**
  - Personalize user queries using a modified Rocchio relevance feedback mechanism

## Outcomes:
- Personalized search engine for local Baltimore news.
- Web scraper for popular Baltimore news/business websites.
- Find the best
  - Word/Sentence embedding
  - Ways to personalize any query
  - Ways to handle unstructured text

## Running instructions:

Install all the packages this search engine requires to run using:
```
pip install -r requirements.txt
```

### Scraping data

1. `$ scrapy crawl <news source>`: Runs the scrapy spider on news site. Choose from: `['cbs', 'wbaltv']`
2. Process the jsonl output into CSV and document-format required by data loader.
  ```
  $ cd data/local_news_data
  $ python process.py
  ```
