'''
This portion consists of feature extraction process.
    While developing be cautious so that the list of features can be tested

    Feature extraction approaches to be dealed:
    1. MFECC (must )
    2. Trasfer Learning (if possible)
    3. Other criteria to be explored
'''


'''
 extracts 40 dimensional MFCC & delta MFCC features
'''

import numpy as np
from sklearn import preprocessing
import python_speech_features as mfcc
from scipy.io.wavfile import read
from sklearn.metrics import precision_recall_fscore_support as score



class ExtractFeature:

    @classmethod #classmethod is the decorator
    def __calculate_delta(self,array):
        """Calculate and returns the delta of given feature vector matrix"""

        rows, cols = array.shape
        deltas = np.zeros((rows, 20)) #20 columns
        N = 2
        for i in range(rows):
            index = []
            j = 1
            while j <= N:
                if i - j < 0:
                    first = 0
                else:
                    first = i - j
                if i + j > rows - 1:
                    second = rows - 1
                else:
                    second = i + j
                index.append((second, first))
                j += 1
            deltas[i] = (array[index[0][0]] - array[index[0][1]] + (2 * (array[index[1][0]] - array[index[1][1]]))) / 10
        return deltas

    @classmethod
    def extract_features(self,audio_path):
        """extract 20 dim mfcc features from an audio, performs CMS and combines
        delta to make it 40 dim feature vector"""

        '''
        @:param
        audio_path: path of the audio file 
                    in the implementation this is stored in the pandas frame as audio_path key.
                    
        rate: singnal rate of the audio file
              Can be determined using
              sr,audio = read(source + path).
              sr = signal rate
              
        Returns the MFCC feature and the delta of the audio thus provided.
        '''

        mfcc_feature = np.asarray

        rate, audio = read(audio_path)
        mfcc_feature = mfcc.mfcc(audio, rate, 0.025, 0.01, 20, nfft=1200, appendEnergy=True)
        mfcc_feature = preprocessing.scale(mfcc_feature) # feature is preprocessed
        delta = self.__calculate_delta(mfcc_feature)
        combined = np.hstack((mfcc_feature, delta))
        return combined




# ef = ExtractFeature()
#
# audio_path = "dataset/train/karan/Karan_17.wav"

# ef.extract_features(audio_path)