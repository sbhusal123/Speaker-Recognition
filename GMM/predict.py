'''
Audio file to be predicted is kept inside the predict folder.
'''

import os
import pickle
import numpy as np
from scipy.io.wavfile import read
import time
from ExtractFeature import ExtractFeature

def predict(audio_path):
    '''
    @:param:
    audio_path : Path to the audio which needs to be predicted

    return_type: String
                Returns the speaker thus detected by comparing to the model
    '''

    modelpath = "speakers_model/"

    ef = ExtractFeature

    # list of gmm_files available
    gmm_files = [os.path.join(modelpath, fname) for fname in
                os.listdir(modelpath) if fname.endswith('.gmm')]

    # name of the model of speaker = same as the name of speaker
    speakers = [fname.split("/")[-1].split(".gmm")[0] for fname in gmm_files]


    #list of existing models
    models   = [pickle.load(open(gmm_file,'rb')) for gmm_file in gmm_files] # rb stands for  reading the binary file


    # features of the file to be predicted
    feature = ef.extract_features(audio_path)

    score_of_individual_comparision = np.zeros(len(models))
    for i in range(len(models)):
        gmm = models[i]  # checking with each model one by one
        scores = np.array(gmm.score(feature))
        score_of_individual_comparision[i] = scores.sum()

    winner = np.argmax(score_of_individual_comparision)

    speaker_detected = speakers[winner]

    return speaker_detected



# This needs to be commented while accuracy testing because has coupling to that portion

base_path = "dataset/predict/"
file_name = "1.wav"


speaker_predicted =  predict(base_path+file_name)
print("Speaker predicted: "+ speaker_predicted)
