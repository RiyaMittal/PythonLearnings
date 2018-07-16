import cx_Oracle,csv

x='''SELECT
		'Account'
       || ','
       || 'Account ID'
       || ','
       || 'Category '
       || ','
       || 'Category ID'
       || ','
       || 'Brand'
       || ','
       || 'Brand ID'
       || ','
       || 'Fund Class'--Added by Marcin Puszkarski, QMR11.1 CES Reporting
       || ','
       || 'Quarter Name' --Added by Marcin Puszkarski, QMR11.1 CES Reporting
       || ','
       || 'Month Name'
       || ','
       || 'Base SU'
       || ','
       || 'Incremental SU'
       || ','
       || 'Total Volume (SU)'
       || ','
       || 'GIV'
       || ','
       || 'NIV'
       || ','
       || 'D-NOS'
       || ','
       || 'SLOG'
       || ','
       || 'MDA Fixed LOR'
       || ','
       || 'MDA Fixed Expense'
       || ','
       || 'MDA Variable LOR'
       || ','
       || 'MDA Variable Expense'
       || ','
       || 'Balance vs Expected Spending'
     || ','
     || 'Total Adjustments'
     || ','
     || 'Total Fund Transfers'
     || ','
     || 'Total Fund Forecasted'
     || ','
     || 'Forecasted Available (by Fund)'
FROM DUAL
UNION ALL
SELECT TRANSLATE (REPLACE
(   CHR (8)
|| ACCOUNT
|| CHR (8)
|| ','
||CHR (8)
|| ACCOUNT_ID
|| CHR (8)
|| ','
||CHR (8)
|| CATEGORY
|| CHR (8)
|| ','
||CHR (8)
|| CATEGORY_ID
|| CHR (8)
|| ','
||CHR (8)
|| BRAND
|| CHR (8)
|| ','
||CHR (8)
|| BRAND_ID
|| CHR (8)
|| ','
||CHR (8)
|| FUND_CLASS_CODE --Added by Marcin Puszkarski, QMR11.1 CES Reporting
|| CHR (8)
|| ','
||CHR (8)
|| QTR_NAME --Added by Marcin Puszkarski, QMR11.1 CES Reporting
|| CHR (8)
|| ','
||CHR (8)
|| MONTH_NAME
|| CHR (8)
|| ','
||
BASE_SU
|| ','
||
INC_SU
|| ','
||
TOTAL_SU
|| ','
||
GIV
|| ','
||
NIV
|| ','
||
NOS
|| ','
||
SLOG
|| ','
|| ESTMT_FIXED_MDA_LOR
|| ','
|| ESTMT_FIXED_MDA_EXPENSE
|| ','
|| ESTMT_VARIABLE_MDA_LOR
|| ','
|| ESTMT_VARIABLE_MDA_EXPENSE
|| ','
|| BALANCE
|| ','
||  ADJ
|| ','
||
TNSFR
|| ','
||
TOT
|| ','
||
AVA
,
'""',
'""""'
),
CHR (8),
'""'
       )
FROM (select  BUS_UNIT_NAME,
	     FISC_YR_ABBR_NAME,
	     ACCOUNT,
	     ACCOUNT_ID,
	     CATEGORY,
	     CATEGORY_ID,
	     BRAND,
	     BRAND_ID,
	     FUND_CLASS_CODE, --Added by Marcin Puszkarski, QMR11.1 CES Reporting
	     QTR_NAME, --Added by Marcin Puszkarski, QMR11.1 CES Reporting
	     MONTH_NAME,
	     BASE_SU,
	     INC_SU,
	     TOTAL_SU,
	     GIV,
	     NIV,
	     NOS,
	     SLOG,
	     ESTMT_FIXED_MDA_LOR,
	     ESTMT_FIXED_MDA_EXPENSE,
	     ESTMT_VARIABLE_MDA_LOR,
	     ESTMT_VARIABLE_MDA_EXPENSE,
	     BALANCE,
	     ADJ,
	     TNSFR,
	     TOT,
	     AVA from OPT_ACCT_BRAND_FY_TSP_S_VW) TEMP
	WHERE BUS_UNIT_NAME =  'Ukraine'
    AND FISC_YR_ABBR_NAME = 'FY17/18'
    ---AND QTR_NAME = 'AMJ17'
    and ROWNUM<10
    '''


connection = cx_Oracle.connect ( 'adwu_optima_ceex', 'Wuopt_cex59', 'optax1u' )
cur = connection.cursor()
cur.arraysize = 1000
print "starting execution"
cur.execute(x)
csv_file = open('output.csv','wb')
csv_writer = csv.writer(csv_file)
csv_writer.writerows(cur.fetchall())
print "Write complete"
csv_file.close()
cur.close()
connection.close()

