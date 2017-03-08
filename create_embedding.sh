#! /bin/sh

###################
# Prepare Workspace
###################
# Stop if error
set -e 

###################
# OPTIONS
###################
# Experiment options
stage=0
history_type="artist"
embedding_size=20

if [ $stage -le 1 ]; then
echo "Prepare play history..."
python scripts/generate_play_history.py --input_actions "data/mars_tianchi_user_actions.csv" \
                                        --input_songs "data/mars_tianchi_songs.csv" \
                                        --history_type $history_type \
                                        --output_json "data/${history_type}_play_history_map.json" \
                                        --output_txt "data/${history_type}_play_history.txt" 
fi

if [ $stage -le 2 ]; then
echo "Train embedding..."
./external/word2vec/word2vec -train data/${history_type}_play_history.txt \
                             -output data/${history_type}_vec.txt \
                             -size $embedding_size \
                             -window 5 \
                             -sample 1e-4 \
                             -negative 5 \
                             -hs 0 \
                             -binary 0 \
                             -cbow 1 \
                             -iter 5
fi
