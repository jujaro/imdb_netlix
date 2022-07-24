import pandas as pd

imdb  = pd.read_html('https://www.imdb.com/chart/top/?ref_=nv_mv_250')[0]
imdb = imdb['Rank & Title'].str.extract('[0-9]+(.*)')[0].str.rsplit(' ',1,expand=True)[0].str.split(' ',1,expand=True)[1].str.strip()
print(imdb.head())

nf = pd.read_html('https://www.finder.com.au/netflix-movies')[0]
print(nf.head())

for p in set(nf.Title).intersection(set(imdb)):
    print(p)

