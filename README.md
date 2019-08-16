# Speaker Recognition 
This is the extension of the work done by Atul-Anand-Jha in the implementation of MFCC(Mel's Frequency Cepestral Coefficient) and GMM(Gausian Mixture Model) which can be accessed from the following link and will be merged into his repository:
#### [Browse Repo](https://github.com/Atul-Anand-Jha/Speaker-Identification-Python) 

## 1. Algorithmic Details:
In the feature extraction, MFCC(Mel's Frequency cepestral Coefficient's) are used which emphasizes on extraction of  the low frequency components and their cepestral coefficients from the audio files. Precedure for feature extraction can be better described in the figure below:

### a. Feature Extraction
![MFCC Feature Extraction      Procedure](https://www.researchgate.net/profile/Ratnadeep_Deshmukh/publication/262794354/figure/fig1/AS:296064092524547@1447598588547/MFCC-Feature-Extraction.png)

Basically the frequency is calculated at the frame level by using windowing technique and the each frame of audio is converted into the ferquency domain representation using Discrete Fourier Transform. From those frequency of a frame, mel's cepestral coefficient (MCC) is calclated which is again conerted back into the logarthmic scale representation and finally converted back into the time domain representation using discrete fourier transform. Overall process of calculating a MFCC feature is done at the frequency domain.

### b.  Model Representation using Gausian Mixture Model
To represent the model of the each speaker, GMM i.e Gausian Mixture Model is used. Basically this particular technique relies on generalizing the Gaussians that arises from the each feature extracted from the audio files of a particular speaker during training phase.

![Gaussian Mixture Model Generalizing the individual Gaussians present in the feature array.](https://prateekvjoshi.files.wordpress.com/2013/06/multimodal.jpg)

The dotted line above can be infered as the feature present in the each speaker's audio file, while the solid line can be infered as being Generalized gaussian present in the feature space. 

# 2. Usage
Python Version: 3.7 or above
Libraries required can be found at [requirements.txt](https://github.com/sbhusal123/Speaker-Recognition-Digital-Attendance/blob/master/GMM/requirements.txt) file included in the repository. 
>pip install requirements.txt
## a. Training the speaker's audio file
>Audio File Supported:
>i. Audio file type: .wav
>ii. Channel: 2(stereo)

For the training and creating speaker's model, one needs to provide the individual speaker's file inside the dataset/train folder with the name of the speaker.
[Browse training folder's list](https://github.com/sbhusal123/Speaker-Recognition-Digital-Attendance/tree/master/GMM/dataset/train)

Then to generate the GMM model of the corresponding speaker's simply use:
> python train.py <speaker's file name>

The GMM model of each speaker is dumped at the [Speaker's Model folder](https://github.com/sbhusal123/Speaker-Recognition-Digital-Attendance/tree/master/GMM/speakers_model) using pickle.

> Tips: More is the data, more is the accuracy ;)

# b. Predicting 
For prediting simply record your sound and keep it inside the predict folder present inside the dataset folder [train folder](https://github.com/sbhusal123/Speaker-Recognition-Digital-Attendance/tree/master/GMM/dataset/predict) with name "1.wav". Then following command can be used to predict the speaker
> python predict.py

# 3. Accuracy 
For accuracy testing, one needs to provide the each speaker's audio file in the [test](https://github.com/sbhusal123/Speaker-Recognition-Digital-Attendance/tree/master/GMM/dataset/test) folder. Those audio files of speaker must be provided each indivudual's speaker's name.

> Caution: Make sure that the name of the speaker's folder is same as the training phase speaker's folder.

Then simply use the command below to test the accuracy of the model:
> python accuracy_test.py

# 4. Accuracy Measured 
For the accuracy testing precision, recall and f-score of each speaker's model was measured using confusion matrix. In the training folder an average of 10 minute audio was kept while 9 different audio files per speaker was used.

## In case of non-noisy data:
![Confusion Matrix Plot](https://github.com/sbhusal123/Speaker-Recognition-Digital-Attendance/blob/master/Accuracy%20Measures%20And%20Plot/With%20data%20free%20of%20errors/final_confusion_matrix.png?raw=true)

![Accuracy Thus Measured](https://github.com/sbhusal123/Speaker-Recognition-Digital-Attendance/blob/master/Accuracy%20Measures%20And%20Plot/With%20data%20free%20of%20errors/accuracy_statistical.png?raw=true)

## b. In case of noisy data:
![Confusion Matrix Plot](https://github.com/sbhusal123/Speaker-Recognition-Digital-Attendance/blob/master/Accuracy%20Measures%20And%20Plot/Result%20with%20noisy%20data/confusion_matrix_with_error.png?raw=true)

![Accuracy Thus Measured](https://github.com/sbhusal123/Speaker-Recognition-Digital-Attendance/blob/master/Accuracy%20Measures%20And%20Plot/Result%20with%20noisy%20data/recall_fscore_precision.png?raw=true)






