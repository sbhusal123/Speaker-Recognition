import mysql.connector
import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play
import time
import glob,os
import predict as pd


def insertIntoDB(attended_students,class_id):

    '''
    This functionality is for inserting the list of students who have attended class
    into the database.

    @param:
    attended_student: list of the students who have attended the class
    class_id : class_id for specific class attendance. To be provided by checking through the web-interface
               of the digital attendance.
    '''

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="smart_attendance"
    )

    mycursor = mydb.cursor()

    for student in attended_students:

        sql = "select id,name from attendance_student where name ='{}'".format(student)

        mycursor.execute(sql) #connection CRUD object

        myresult = mycursor.fetchall()

        for id,name in myresult:
            attended_student_id = id
            attended_student_name = name
            sql = "INSERT INTO attendance_attends (std_id_id,cl_id_id) VALUES ({}, {})".format(attended_student_id,class_id)
            mycursor.execute(sql)
            mydb.commit()

    mydb.close()


def recordSounnd(filename):

    '''
    Basically this method is for recording and saving sound to specific
    directory.

    @param:
    filename = name with which the file is to be saved for each student
    '''

    path = "dataset/predict/"
    samplerate = 44100  # Hertz
    duration = 5  # seconds

    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                    channels=2, blocking=True)

    sf.write(path+filename, mydata, samplerate)


def playSound(filename):
    '''
     playing sound while recording calling or initializing the application

    @param:
    filename = path + name of file to be played
    '''
    sound = AudioSegment.from_wav(filename)
    play(sound)


def rundemo():
    playSound("demo_audio/init.wav")
    playSound("demo_audio/student1.wav")

    print("Start speaking")
    recordSounnd("1.wav")
    for i in range(2,4):
        print(i)
        playSound("demo_audio/next.wav")
        recordSounnd(str(i)+".wav")


def appendToDb(class_id):
    recorded_audios_path = []
    student_attended = []

    recorded_files = os.listdir("dataset/predict")

    for files in recorded_files:
        recorded_audios_path.append("dataset/predict/"+files)


    for paths in recorded_audios_path:
        predict = pd.predict(paths)
        student_attended.append(predict)

    print(student_attended)

    insertIntoDB(student_attended, class_id)




''''
Demo setup:
1. Create a attendance class id in web-interface.
2. Then start recording the class attendance runing the method demo()
3. Then run append to DB using appendToDb(class_id) 
'''

rundemo()

class_id = 8
appendToDb(class_id)