'''
Audio file to be predicted is kept inside the predict folder.
'''

import os
import pickle
import numpy as np
from scipy.io.wavfile import read
import time
import sys
from ExtractFeature import ExtractFeature

def testPredict(audio_path):
    '''
    @:param audio_path : Path to the audio which needs to be predicted

    @:return: Returns the speaker thus detected by comparing to the model
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



def predict(file_name):
    '''
    @param file_name : name of the file inside the dataset/predicted to be predicted
    @return: name of the speaker predicted
    '''
    speaker_predicted = testPredict(file_name)
    return speaker_predicted

if __name__ == "__main__":
    predict_dir_path = 'dataset/predict/'
    file_name = sys.argv[-1]
    predicted =  predict(predict_dir_path+file_name)
    print(predicted)


