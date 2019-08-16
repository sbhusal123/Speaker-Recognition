import MakeModel as mm
from GetFiles import GetFiles
import sys

# to make it easier in the defense train through the command prompt i.e
# python train.py <speaker_name_directory>



def train(speaker_name):
    '''
    :param
    speaker_name : name of the speaker whose model is to be prepared
                   Actually it takes the folder name of the speaker's audio files.
    '''
    print("Training "+ speaker_name+"'s model")
    gf = GetFiles(dataset_path="dataset") #getting the training files of speaker
    pandas_frame = gf.getTrainFiles(flag="train", train_speaker_folder=speaker_name) #audios path pipelined in dataframe
    mm.makeModel(pandas_frame)
    print("Training finished.")



# speaker_name = "karan"
# train(speaker_name)

# name of the speaker passed as a command line argument
speaker_name = sys.argv[1]
train(speaker_name)