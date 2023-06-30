# Web Scraping using nimbleway api and openai api

Solution to nimbleway's coding challenge

## Installation and running

```bash
pip -r requirements.txt
python run.py
```

## Challenges

- **Open AI api token limit** : open ai gpt-3.5-turbo model has a limit of 4096 token which in case of webscrape which involves a lot of text is not enough. Any normal html page even exceed 32k token limit.
- **Converting html**: I tried converting html to json as it has less characters than html. but maintaining order was hard be it finding xpath back to original html.

## Approach

- **Converting html to json**: each tag as key and attributes and array of inner_html as values.
- **Removing unnecessary tags and attributes** :
  - Removing all script tags
  - Removing all style tags
  - Removing all comments
  - Removing all iframes
  - Include only `class`, `id`, `src`, `href` attributes
  - Remove common styling classes `i.e col-*, row-*`
- **Shortening class names** : Convert class names to shorter 4 character hashesh of alphanumeric values
- Removing necessary attributes, if it exceeds 12k token limit (bare html sometime still exceeds 12k token limit)
  > the goal was to get xpath from the bare html pattern
  - src
  - class
  - text_value
- **Remove foreign urls**: removing all urls which are not from the same domain as the url provided for anchor tags
- **Creating json out of just anchor tags**: List of all anchor tags with their attributes and inner_html ( just a reduced version to comply with 12k token limit)
  > even with this some websites exceed 12k token limit `e.g. https://www.ebay.com/b/Animal-Collectibles/1335/bn_1853571` which has 22k token with just anchor tags

## Improvements

- **Chunking**: spliting html into chunks of level from root node to leaf node
- **Toggle modle based on token size**: if token size exceeds 3k then use `gpt-3.5-turbo-16k` else use `gpt-3.5-turbo`
- **Extracting text from html**: using `beautifulsoup` to extract text from html and using that text to get product details from openai api
  > limitaion: expensive
- Using Chunking and sending html bare with text to get xpath to product detail element tag `also include some wild card characters to get more accurate xpath /*/`
  > limitaion: coehrsion between chunk html

**Thank's nimblyway for this challenge, got to learn a lot of things while doing this challenge regarding openai api**
