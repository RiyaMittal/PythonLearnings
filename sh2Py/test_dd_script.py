#!/usr/bin/python

import datetime
import sys
import os, re, fileinput
import cx_Oracle
import csv

# ADW_OPTIMA_CONNECT='adwu_optima_ceex'
China_Files = {}
Other_R_Files = {}
global LOG_SQL_AB_FFM
global LOG_SQL_AC
global LOG_SQL_AB


print "{0} STEP010 : Checking the incoming parameters".format(datetime.datetime.now())
print "{0} STEP010 : Number of arguments passed {1}".format( datetime.datetime.now(),len(sys.argv))

print "{0} STEP010 : Values of arguments passed {1}".format( datetime.datetime.now(), sys.argv)

# Setting the global parameters

IN_REGION = sys.argv[1]
IN_OBJECT_NAME = sys.argv[2]
OPTIMA_FOLDER = sys.argv[3]
WHICH_PRM_FY = sys.argv[4]

# Setting HLD PARAMETER


WHICH_PRM_FY.upper ()
if WHICH_PRM_FY == 'CURRENT':
    CONST_LOOP_DATA = "FY17/18^CURRENT_FY17/18"
elif WHICH_PRM_FY == 'PREVIOUS':
    CONST_LOOP_DATA = "FY16/17^CURRENT_FY16/17"
elif WHICH_PRM_FY == "NEXT":
    CONST_LOOP_DATA = "FY18/19^CURRENT_FY18/19"



# check the fiscal year parameter and convert it into caps
for dirName, subDirName, fileList in os.walk ( "C:\\var" ):
        # print ("Found Directory: %s" % dirName)
        # print subDirName
        for fn in fileList:
            CONST_OUTPUT_FILE_DIR = dirName
            file_path = os.path.join ( dirName, fn )
            print file_path
            if re.search(r'sqlin$',fn):
                if re.search ( r'China', fn ):
                    China_Files[fn] = file_path
                else:
                    Other_R_Files[fn] = file_path

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

print "China Files",China_Files
print "Other R Files",Other_R_Files


# bus unit name
FY_DATE = CONST_LOOP_DATA.split ( '^' )
FY = FY_DATE[0]
FY_FILE = FY_DATE[1].replace ( '/', '_' )
# Quaters:
HY2 = FY.split ( '/' )[1]
src = re.search ( r'(\d+)', FY.split ( '/' )[0] )
HY1 = src.group ()

FY_MTHS = ['JAS' + HY1, 'OND' + HY1, 'JFM' + HY2, 'AMJ' + HY2]
print "FY MONTHS :{}".format ( FY_MTHS )

#LOG_DATE = datetime.datetime.now()
print "CONST_OUTPUT_FILE_DIR  ",CONST_OUTPUT_FILE_DIR

for QTR in FY_MTHS:
        if IN_REGION == "AP":
            if IN_OBJECT_NAME == "ACCOUNT_BRAND_FY_FFM":
                TEPOUT_FILE = CONST_OUTPUT_FILE_DIR + '/' + OPTIMA_FOLDER + '/' + 'DATA_EXTRACT_' + IN_OBJECT_NAME +'_'+ IN_REGION+'_'+ OPTIMA_FOLDER + FY_FILE+'.csv'
            else:
                TEPOUT_FILE = CONST_OUTPUT_FILE_DIR + '/' + OPTIMA_FOLDER + '/' + 'DATA_EXTRACT_' + IN_OBJECT_NAME +'_'+ IN_REGION+'_'+ OPTIMA_FOLDER + FY_FILE + QTR +'.csv'
        else:
            TEPOUT_FILE = CONST_OUTPUT_FILE_DIR + '/' + OPTIMA_FOLDER + '/' + 'DATA_EXTRACT_' + IN_OBJECT_NAME +'_'+ IN_REGION+'_'+ OPTIMA_FOLDER + FY_FILE + QTR +'.csv'

        print "Creating file: ", TEPOUT_FILE
        if IN_OBJECT_NAME == "ACCOUNT_BRAND_FY_FFM":
            LOG_SQL = LOG_SQL_AB_FFM
        elif IN_OBJECT_NAME == "ACCOUNT_BRAND_FY":
            LOG_SQL = LOG_SQL_AB
        elif IN_OBJECT_NAME == "ACTIVITY_COST":
            LOG_SQL = LOG_SQL_AC

        #print "LOG_SQL",LOG_SQL
        #newquery = "'''\n" + LOG_SQL + "\n'''"
        #print "newquery", newquery

        with open(LOG_SQL,'r') as fh:
            file_text_sql=fh.read()
        #print "jkjk",file_text_sql
        #filtered = filter ( lambda x: not re.match ( r'^\n*$', x ), file_text_sql )
        newquery = "'''" + file_text_sql     + "\n'''"
        new = newquery.replace ( '&v_BUS_UNIT_NAME', OPTIMA_FOLDER )
        new1 = new.replace ( '&v_FY', FY )
        LOG_SQL_TMP1 = new1.replace ( '&v_QTR', QTR )
        # filtered = filter ( lambda x: not re.match ( r'^\n*$', x ), LOG_SQL_TMP1 )
        #print filtered
        # print LOG_SQL_TMP1
#             new = newquery.replace('&v_BUS_UNIT_NAME', OPTIMA_FOLDER)
#             new1 = new.replace('&v_FY',FY)
#             LOG_SQL_TMP1 = new1.replace('&v_QTR',QTR)
#             print LOG_SQL_TMP1
#             #newquery = "'''\n" + LOG_SQL_TMP1 + "\n'''"
#             #print newquery
#                 #LOG_SQL_TMP = "'''" + LOG_SQL_TMP1 + '\n' + "'''"
#             #print "Statement Executing: {LOG_SQL_TMP}".format(LOG_SQL_TMP)
#         except Exception as e:
#             s=str(e)
#             #error, = e.args
#             print "ERROR CODE : {}".format(e)
#
try:
   connection = cx_Oracle.connect( 'adwu_optima_ceex', 'Wuopt_cex59', 'optax1u' )
except cx_Oracle.DatabaseError as e:
   error, = e.args
   if error.code == 1017:
        print ("Invalid credentials")
   else:
        print("Database connection error {}".format(error.code))
finally:
    print "connection successfull"
cur = connection.cursor()
try:
   print LOG_SQL_TMP1
   cur.execute(LOG_SQL_TMP1)
except cx_Oracle.DatabaseError as e:
   error, = e.args
   print("Error in executing the statement: {}".format(e))
   print "Error Code:",error.code
   print "Error Message:",error.message
   print "Error Context: ",error.context
print TEPOUT_FILE
csv_file = open(TEPOUT_FILE,'wb')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(cur.fetchone())
csv_writer.writerows(cur.fetchall())
cur.close()
connection.close()
csv_file.close()


