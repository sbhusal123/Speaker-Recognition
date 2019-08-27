from GetFiles import GetFiles
import predict as pred
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


def getActualPredictedList():
    '''
    @return pd-frame : list of the actual and predicted list for confusion matrix calculation
    '''
    data_frame_row = []

    gf = GetFiles(dataset_path="dataset")
    testing_files =  gf.getTestFiles()

    for index, row in testing_files.iterrows():
        audio_path = row["audio_path"]
        predicted = pred.testPredict(audio_path)

        actual = row["actual"]
        data_frame_row.append([actual, predicted])

    actual_predicted = pd.DataFrame(data_frame_row,columns = ['actual','predicted'])

    return actual_predicted


def showAccuracyPlotAndMeasure():
    actual_pred = getActualPredictedList()

    actual = actual_pred["actual"].tolist()
    predicted = actual_pred["predicted"].tolist()
    labels  = actual_pred["actual"].unique().tolist()
    cm = confusion_matrix(actual, predicted, labels) #confusion matrix in matrix form

    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(cm)
    plt.title('Confusion matrix of Recognition Model')
    fig.colorbar(cax)
    ax.set_xticklabels([''] + labels)
    ax.set_yticklabels([''] + labels)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
    display_numeric_accuracy(actual, predicted,labels) # displays the precision recall and fscore

def display_numeric_accuracy(actual,predicted,labels):
    '''
    @param list actual : actual label for the speaker's audio
    @param list predicted : predicted label by the GMM classifier
    @param list labels : name of the distinct speaker
    '''
    print(classification_report(actual, predicted, target_names=labels))


showAccuracyPlotAndMeasure()