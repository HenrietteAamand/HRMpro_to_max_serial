from filewriter import *
from max_dataobj_class import *
import json
import serial

Testperson_nummer = '1'
Fasenummer = '1'
Navn_på_fase = 'test'

filename_maxdata = 'Testperson_' + Testperson_nummer + "_Fase_" + Fasenummer + "_" + Navn_på_fase + "_maxdata" #Testperson_1_Fase_1_stilhed_maxdata 
#full_path_maxdata = '/Users/sisselraahede/Documents/Au_Digital_design/Kandidat/Praktik/Isobel/Lydindhold/Max/Soundscape komposition/GenerativeCompositionAbleton'
full_path_maxdata = ''
max_obj = Max_dataobj_class()

fw = WriteJSON_class(full_path_maxdata, filename_maxdata, max_obj.Get_Empty_JSON())

# Her mangler noget seriel kommunikation...
hr = 0
timestamp = 0
flag = 0
com = serial.Serial('COM17',baudrate=115200, timeout = 3)

while(True):
    output = com.readline()
    print(output)
    max_obj.UpdateJSON(hr, timestamp)
    fw.SaveLineToFile(json.loads(max_obj.toJSON()))