
## Introduction

This repository contains data analysis scripts for Ali music trend prediction contest hosted in Ali TianChi, for contest details please see [here](https://tianchi.shuju.aliyun.com/competition/faq.htm?spm=5176.100068.5678.3.MJN8tJ&raceId=231531)

We provide following utilities for easy data inspection:

- Plot daily play/download/collect history of specific artist
- Plot daily play/download/collect history of specific user
- Plot word embedding of songs


## Prerequisite
### Data
Download contest data [here](https://tianchi.shuju.aliyun.com/competition/information.htm?spm=5176.100069.5678.2.b1xJxV&raceId=231531), and put `mars_tianchi_user_actions.csv`, `mars_tianchi_songs.csv` in `data` directory.

### Python
- Python 2.7
  - Jupyter notebook (for interactive environment)
  - numpy  (for numeric operation)
  - pandas (for data loading)
  - matplotlib (for plotting)
  - statsmodels (for time series decomposition)
  - sklearn (for TSNE)
  - json (for data storing)
  - h5py (for data storing)
To meet all python library requirements, you can simply use [Anaconda](https://www.continuum.io/downloads).

### Word2vec(optional)
This is needed for word embedding of songs, download it [here](https://github.com/dav/word2vec). Put the excutable `word2vec` in `external/word2vec/` after you sucessfully compile it.

## Utilities
### Plot artist daily information
run [artist_daily_info.ipynb](artist_daily_info.ipynb)

[artist_daily_info](assets/artist_daily_info.png)
[artist_daily_info_decomposition](assets/artist_daily_info_decomposition.png)

### Plot user daily information
run [user_daily_info.ipynb](user_daily_info.ipynb)

[user_daily_info](assets/user_daily_info.png)

### Plot word embedding of songs
run [create_embedding.sh](create_embedding.sh) and then [visualize_song_embedding.ipynb](visualize_song_embedding.ipynb)

[song_embedding](assets/tsne_color_artist_id_1500.png)

### analysis singer' identity"ali_music_analyses" 
run [analyse_singer_info.ipynb](analyse_singer_info.ipynb)
