#!/usr/bin/python

import datetime
import sys
import os, re,fileinput
import cx_Oracle
import csv

#ADW_OPTIMA_CONNECT='adwu_optima_ceex'
China_Files={}
Other_R_Files={}

print "{current_time} STEP010 : Checking the incoming parameters".format(datetime.datetime.now())
print "{current_time} STEP010 : Number of arguments passed {num_arg}".format(datetime.datetime.now(),len(sys.argv))
print "{current_time} STEP010 : Values of arguments passed {val_arg}".format(datetime.datetime.now(),sys.argv)

#Setting the global parameters

IN_REGION=sys.args[1]
IN_OBJECT_NAME=sys.args[2]
OPTIMA_FOLDER=sys.args[3]
WHICH_PRM_FY=sys.args[4]

# Setting HLD PARAMETER



   WHICH_PRM_FY.upper()
    if WHICH_PRM_FY == 'CURRENT':
        CONST_LOOP_DATA = "FY17/18^CURRENT_FY17/18"
    elif WHICH_PRM_FY == 'PREVIOUS':
        CONST_LOOP_DATA= "FY16/17^CURRENT_FY16/17"
    elif WHICH_PRM_FY == "NEXT":
        CONST_LOOP_DATA = "FY18/19^CURRENT_FY18/19"

    return CONST_LOOP_DATA

#check the fiscal year parameter and convert it into caps
def sql_files_assign(IN_REGION):

    for dirName,subDirName,fileList in os.walk("C:\\var"):
        #print ("Found Directory: %s" % dirName)
        #print subDirName
        for fn in fileList:
            CONST_OUTPUT_FILE_DIR =dirName
            file_path= os.path.join(dirName,fn)
            #print file_path
            if re.search(r'China',fn):
                China_Files[fn]=file_path
            else:
                Other_R_Files[fn]=file_path

        if IN_REGION == "AP":
            for fn in China_Files:
                if re.search ( r'AB_FFM', fn ):
                    LOG_SQL_AB_FFM = China_Files[fn]
                elif re.search ( r'AC', fn ):
                    LOG_SQL_AC = China_Files[fn]
                elif re.search ( r'AB', fn ):
                    LOG_SQL_AB = China_Files[fn]
        else:
            for fn in Other_R_Files:
                if re.search ( r'AB_FFM', fn ):
                    LOG_SQL_AB_FFM = Other_R_Files[fn]
                elif re.search ( r'AC', fn ):
                    LOG_SQL_AC = Other_R_Files[fn]
                elif re.search ( r'AB', fn ):
                    LOG_SQL_AB = Other_R_Files[fn]

    return LOG_SQL_AB_FFM,LOG_SQL_AC,LOG_SQL_AB,CONST_OUTPUT_FILE_DIR


#bus unit name
def fy_get(CONST_LOOP_DATA):
    FY_DATE=CONST_LOOP_DATA.split('^')
    FY=FY_DATE[0]
    FY_FILE=FY_DATE[1].replace('/','_')
    #Quaters:
    HY2=FY.split('/')[1]
    src=re.search(r'(\d+)',FY.split('/')[0])
    HY1=src.group()

    FY_MTHS=['JAS'+HY1, 'OND'+HY1, 'JFM'+HY2, 'AMJ'+HY2]
    print "FY MONTHS :{}".format(FY_MTHS)

    return  FY,FY_FILE,FY_MTHS



LOG_DATE=datetime.datetime.now("%Y%M%D")

def create_report(FY,FY_FILE,CONST_OUTPUT_FILE_DIR,FY_MTHS,LOG_SQL_AB_FFM,LOG_SQL_AB,LOG_SQL_AC):
    for QTR in FY_MTHS:
        if IN_REGION=="AP":
            if IN_OBJECT_NAME=="ACCOUNT_BRAND_FY_FFM":
                TEPOUT_FILE=CONST_OUTPUT_FILE_DIR+'/'+OPTIMA_FOLDER+'/'+'DATA_EXTRACT_'+IN_OBJECT_NAME+IN_REGION+OPTIMA_FOLDER+FY_FILE+LOG_DATE.csv
            else:
                TEPOUT_FILE = CONST_OUTPUT_FILE_DIR + '/' + OPTIMA_FOLDER + '/' + 'DATA_EXTRACT_' + IN_OBJECT_NAME + IN_REGION + OPTIMA_FOLDER + FY_FILE+QTR+LOG_DATE.csv
        else:
            TEPOUT_FILE = CONST_OUTPUT_FILE_DIR + '/' + OPTIMA_FOLDER + '/' + 'DATA_EXTRACT_' + IN_OBJECT_NAME + IN_REGION + OPTIMA_FOLDER + FY_FILE + QTR + LOG_DATE.csv

        print "Creating file: ", TEPOUT_FILE
        if IN_OBJECT_NAME=="ACCOUNT_BRAND_FY_FFM":
            LOG_SQL=LOG_SQL_AB_FFM
        elif IN_OBJECT_NAME=="ACCOUNT_BRAND_FY":
            LOG_SQL=LOG_SQL_AB
        elif IN_OBJECT_NAME=="ACTIVITY_COST":
            LOG_SQL=LOG_SQL_AC

        try:
            for line in fileinput.input ( LOG_SQL):
                new = line.replace ( '&v_BUS_UNIT_NAME',OPTIMA_FOLDER  )
                new1 = new.replace ( '&v_FY', FY )
                LOG_SQL_TMP1 = new1.replace ( '&v_QTR', QTR )
                LOG_SQL_TMP = "'''" + LOG_SQL_TMP1 + '\n' + "'''"

        except:
            print "ERROR: Failed to substitute the macros"

def Oracle_Connection(LOG_SQL_TMP,TEPOUT_FILE):
 try:
    connection=cx_Oracle.connect('adwu_optima_ceex','Wuopt_cex59','optax1u')
 except cx_Oracle.DatabaseError as e:
     error,=e.args
     if error.code==1017:
         print ("Invalid credentials")
     else:
         print("Database connection error %s".format(e))
 cur=connection.cursor
 try:
    cur.execute(LOG_SQL_TMP)
 except cx_Oracle.DatabaseError as e:
     error, = e.args
     print("Error in executing the statement: %s".format ( e ))
     print error.code
     print error.message
     print error.context
 csv_file = open (TEPOUT_FILE, 'wb' )
 csv_writer = csv.writer(csv_file )
 csv_writer.writerows( cur.fetchall() )
 cur.close()
 connection.close()
 csv_file.close()


if __name__ == '__main__':
    create_report(fy_get(assign_fy()))

