# %%
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# %%
# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# %%
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# %%
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# %%
slide_elem.find('div', class_='content_title')

# %%
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# %%
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# %%
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# %%
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# %%
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# %%
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# %%
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# %%
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# %%
df.to_html()

# %%
# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
### Hemispheres
# 1. Use browser to visit the URL
url = 'https://marshemispheres.com/'

browser.visit(url)

# %%
# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# %%
# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Retrieve  full resolution image URL and title for each hemisphere image
#? Loop through the resolution image URL
for i in range(4):
    #? Find the elements on each loop
    browser.find_by_tag('h3')[i].click()
    html = browser.html
    hemi_soup = soup(html, 'html.parser')
    #? Find the image url
    img_url = hemi_soup.find('img', class_='wide-image')['src']
    #? Find the title
    title = hemi_soup.find('h2', class_='title').text
    #? Append the image url and title to the list
    hemisphere_image_urls.append({'title': title, 'img_url': img_url})
    #? Find the back button
    browser.back()

# %%
# # 2. Create a list to hold the images and titles.
# hemisphere_image_urls = []

# # 3. Write code to retrieve the image urls and titles for each hemisphere.
# for i in range(4):
#     # Browse through each article
#     browser.links.find_by_partial_text('Hemisphere')[i].click()

#     # Parse the HTML
#     html = browser.html
#     sphere_soup = soup(html,'html.parser')

#     # Scraping
#     title = sphere_soup.find('h2', class_='title').text
#     img_url = sphere_soup.find('li').a.get('href')

#     # Store findings into a dictionary and append to list
#     hemispheres = {}
#     hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
#     hemispheres['title'] = title
#     hemisphere_image_urls.append(hemispheres)

#     # Browse back to repeat
#     browser.back()

# # Quit browser
# browser.quit()

# %%
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


