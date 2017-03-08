#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generate user play history
"""

# prepare workspace
import pandas as pd
import numpy as np
import json
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--input_actions', default='data/mars_tianchi_user_actions.csv')
parser.add_argument('--input_songs', default='data/mars_tianchi_songs.csv')
parser.add_argument('--history_type', default='artist')
parser.add_argument('--output_txt', default='data/artist_play_history.txt')
parser.add_argument('--output_json', default='data/artist_play_history_map.json')
args = parser.parse_args()


if __name__=="__main__":
  ### LOAD FILES 
  # load action data
  actions = pd.read_csv(args.input_actions, 
              names = ['user_id', 'song_id', 'gmt_create', 'action_type', 'Ds'])
  # Load song information
  song_info = pd.read_csv(args.input_songs,
              names = ['song_id', 'artist_id', 'publish_time', 'song_init_plays', 'lang', 'gender'])
                        
 
  ### CREATE CONVERSION MAPS
  # Create song_id -> artist_id map
  song_ids = song_info['song_id'].tolist()
  artist_ids = song_info['artist_id'].tolist()

  song_to_artist = {}
  for song, artist in zip(song_ids, artist_ids):
    song_to_artist[song] = artist

  # Create artist_id to idx map
  artist_ids_unique = np.unique(artist_ids)
  artist_to_idx = {artist_ids_unique[i]:i for i in xrange(len(artist_ids_unique))}

  # Create idx to artist_id
  idx_to_artist = {v: k for k, v in artist_to_idx.iteritems()}

  # Create song_id to idx map
  song_to_idx = {}
  unique_song_ids = np.unique(song_ids)
  artist_to_idx = {artist_ids_unique[i]:i for i in xrange(len(artist_ids_unique))}

  # Create idx to song map
  idx_to_song = {v: k for k, v in song_to_idx.iteritems()}

  ### GENERATE PLAY HISTORY
  #  We make the analogy between user play actions and text
  #
  # each user plays(writes) his/her own version of play histories(articles)
  # user plays(writes) song by song(word by word)
  # user plays(writes) different songs(words) in different mood
  # each continuous number of plays(paragraph) are common in theme
  #

  # sort actions by operation time only once
  actions_sorted = actions.sort_values(['user_id', 'gmt_create'])
 
  # We can achieve the effect below by just one line
  # which is, meanwhile, much much much faster!
  ###########################################
  #for row in actions_sorted.iterrows():
    ## row contains (index, Series), we only need Series
    #row_data = row[1]
    
    ## convert song_id to song_idx
    #song_id = row_data['song_id']
    #song_idx = song_to_idx[song_id]

    #play_history.append(song_idx)
  ############################################
  if args.history_type == 'song':
    play_history = actions_sorted['song_id'].map(lambda x: song_to_idx[x])
  elif args.history_type == 'artist':
    play_history = actions_sorted['song_id'].map(lambda x: artist_to_idx[song_to_artist[x]])
  else:
    raise 'history type must be artist or song'

  ### SAVE RESULTS
  # Dump a JSON file for the map
  json_data = {
    'artist_to_idx': artist_to_idx,
    'idx_to_artist': idx_to_artist,
    'song_to_idx': song_to_idx,
    'idx_to_song': idx_to_song,
  }
  with open(args.output_json, 'w') as f:
    json.dump(json_data, f)
   
  # finally, save history into file with satisfaction...
  with open(args.output_txt, 'w') as f:
    for item in play_history:
      f.write("%i " % item)
