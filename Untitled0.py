
# In[146]:

import pandas as pd
import datetime
from datetime import date
import dicom
pd.set_option('max_rows',5000)
pd.set_option('max_columns',5000)


# In[206]:

a.head(3)


# Out[206]:

#         koreanName  subjectName subjectInitial group sex  age  \
#     NaN       이성주2          NaN            LSJ   NOR   M   26   
#     NaN        조인영          NaN            JIY   NOR   F   24   
#     NaN       이영은2          NaN            LYE   NOR   F   22   
#     
#                          DOB             scanDate  timeline studyName  \
#     NaN  1984-03-08 00:00:00  2010-10-30 00:00:00  baseline       ToL   
#     NaN  1986-08-12 00:00:00  2010-11-05 00:00:00  baseline       ToL   
#     NaN  1988-03-21 00:00:00  2010-11-05 00:00:00  baseline       ToL   
#     
#          patientNumber T1Number DTINumber DKINumber RESTNumber REST2Number  \
#     NaN            NaN      208        65       151       4060         NaN   
#     NaN            NaN      208        65       151       4060         NaN   
#     NaN            NaN      208        65       151       4060         NaN   
#     
#         folderName  backUpBy    note  
#     NaN  NOR01_LSJ       NaN    뒤에 2  
#     NaN  NOR02_JIY       NaN     NaN  
#     NaN  NOR03_LYE       NaN  이름뒤에 2  

# In[133]:

pwd


# Out[133]:

#     u'/Volumes/CCNC_3T/KangIk/2014_05_DKI_project/FEP07_KHJ/T1/dicom'

## Implement into backUp script

# In[180]:

b = getDicomInfoAuto('/Volumes/CCNC_3T/KangIk/2014_05_DKI_project/FEP07_KHJ/T1/dicom/1.3.12.2.1107.5.2.32.35413.2011021811585514137740077.dcm')


# Out[180]:

#     KWEON^HYEOK JU A
#     1994-02-19 00:00:00
#     M
#     72131118
#     2011-02-18 00:00:00
#     16
# 

# In[183]:

b


# Out[183]:

#     {'age': 16,
#      'dicomRead': (0008, 0000) Group Length                        UL: 994
#     (0008, 0008) Image Type                          CS: ['ORIGINAL', 'PRIMARY', 'M', 'NORM', 'DIS2D', 'FM', 'FIL']
#     (0008, 0012) Instance Creation Date              DA: '20110218'
#     (0008, 0013) Instance Creation Time              TM: '115856.140000'
#     (0008, 0016) SOP Class UID                       UI: MR Image Storage
#     (0008, 0018) SOP Instance UID                    UI: 1.3.12.2.1107.5.2.32.35413.2011021811585514137740077
#     (0008, 0020) Study Date                          DA: '20110218'
#     (0008, 0021) Series Date                         DA: '20110218'
#     (0008, 0022) Acquisition Date                    DA: '20110218'
#     (0008, 0023) Content Date                        DA: '20110218'
#     (0008, 0030) Study Time                          TM: '115324.171000'
#     (0008, 0031) Series Time                         TM: '115855.531000'
#     (0008, 0032) Acquisition Time                    TM: '115459.020000'
#     (0008, 0033) Content Time                        TM: '115856.140000'
#     (0008, 0050) Accession Number                    SH: '1102180001'
#     (0008, 0060) Modality                            CS: 'MR'
#     (0008, 0070) Manufacturer                        LO: 'SIEMENS'
#     (0008, 0080) Institution Name                    LO: 'S.N.U.H 3.0T'
#     (0008, 0081) Institution Address                 ST: 'Street StreetNo,Seoul /1D0BB1/,District,KR,ZIP'
#     (0008, 0090) Referring Physician's Name          PN: '11105'
#     (0008, 1010) Station Name                        SH: 'MEDPC'
#     (0008, 1030) Study Description                   LO: 'Research study^research study'
#     (0008, 103e) Series Description                  LO: 'TFL3D_208_SLAB'
#     (0008, 1040) Institutional Department Name       LO: 'Department'
#     (0008, 1048) Physician(s) of Record              PN: 'SIM^KEUM SUK'
#     (0008, 1050) Performing Physician's Name         PN: ''
#     (0008, 1070) Operators' Name                     PN: 'KSS'
#     (0008, 1090) Manufacturer's Model Name           LO: 'TrioTim'
#     (0008, 1140)  Referenced Image Sequence   3 item(s) ---- 
#        (0008, 0000) Group Length                        UL: 94
#        (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
#        (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.32.35413.2011021811540662719838497
#        ---------
#        (0008, 0000) Group Length                        UL: 94
#        (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
#        (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.32.35413.2011021811540794482638507
#        ---------
#        (0008, 0000) Group Length                        UL: 94
#        (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
#        (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.32.35413.2011021811540596822838492
#        ---------
#     (0010, 0000) Group Length                        UL: 88
#     (0010, 0010) Patient's Name                      PN: 'KWEON^HYEOK JU A'
#     (0010, 0020) Patient ID                          LO: '72131118'
#     (0010, 0030) Patient's Birth Date                DA: '19940219'
#     (0010, 0040) Patient's Sex                       CS: 'M'
#     (0010, 1010) Patient's Age                       AS: '016Y'
#     (0010, 1030) Patient's Weight                    DS: '77'
#     (0018, 0000) Group Length                        UL: 400
#     (0018, 0020) Scanning Sequence                   CS: ['GR', 'IR']
#     (0018, 0021) Sequence Variant                    CS: ['SP', 'MP']
#     (0018, 0022) Scan Options                        CS: 'IR'
#     (0018, 0023) MR Acquisition Type                 CS: '3D'
#     (0018, 0024) Sequence Name                       SH: 'tfl3d1_ns'
#     (0018, 0025) Angio Flag                          CS: 'N'
#     (0018, 0050) Slice Thickness                     DS: '1'
#     (0018, 0080) Repetition Time                     DS: '1670'
#     (0018, 0081) Echo Time                           DS: '1.89'
#     (0018, 0082) Inversion Time                      DS: '900'
#     (0018, 0083) Number of Averages                  DS: '1'
#     (0018, 0084) Imaging Frequency                   DS: '123.234603'
#     (0018, 0085) Imaged Nucleus                      SH: '1H'
#     (0018, 0086) Echo Number(s)                      IS: '1'
#     (0018, 0087) Magnetic Field Strength             DS: '3'
#     (0018, 0089) Number of Phase Encoding Steps      IS: '255'
#     (0018, 0091) Echo Train Length                   IS: '1'
#     (0018, 0093) Percent Sampling                    DS: '100'
#     (0018, 0094) Percent Phase Field of View         DS: '100'
#     (0018, 0095) Pixel Bandwidth                     DS: '271'
#     (0018, 1000) Device Serial Number                LO: '35413'
#     (0018, 1020) Software Version(s)                 LO: 'syngo MR B17'
#     (0018, 1030) Protocol Name                       LO: 'TFL3D_208_SLAB'
#     (0018, 1251) Transmit Coil Name                  SH: 'Body'
#     (0018, 1310) Acquisition Matrix                  US: [0, 256, 256, 0]
#     (0018, 1312) In-plane Phase Encoding Direction   CS: 'ROW'
#     (0018, 1314) Flip Angle                          DS: '9'
#     (0018, 1315) Variable Flip Angle Flag            CS: 'N'
#     (0018, 1316) SAR                                 DS: '0.15121144636717'
#     (0018, 1318) dB/dt                               DS: '0'
#     (0018, 5100) Patient Position                    CS: 'HFS'
#     (0019, 0000) Private Creator                     UL: 204
#     (0019, 0010) Private tag data                    LO: 'SIEMENS MR HEADER'
#     (0019, 1008) [CSA Image Header Type]             CS: 'IMAGE NUM 4'
#     (0019, 1009) [CSA Image Header Version ??]       LO: '1.0'
#     (0019, 100b) [SliceMeasurementDuration]          DS: '232685'
#     (0019, 100f) [GradientMode]                      SH: 'Normal'
#     (0019, 1011) [FlowCompensation]                  SH: 'No'
#     (0019, 1012) [TablePositionOrigin]               SL: [0, 0, -1283]
#     (0019, 1013) [ImaAbsTablePosition]               SL: [0, 0, -1248]
#     (0019, 1014) [ImaRelTablePosition]               IS: ['0', '0', '35']
#     (0019, 1015) [SlicePosition_PCS]                 FD: [96.86592925, -158.42889543, 119.49976199]
#     (0019, 1017) [SliceResolution]                   DS: '1'
#     (0019, 1018) [RealDwellTime]                     IS: '7200'
#     (0020, 0000) Group Length                        UL: 442
#     (0020, 000d) Study Instance UID                  UI: 1.2.410.200003.1037.1.0.72131118.20110218.112900.1102180001.1
#     (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.32.35413.2011021811585177562839189.0.0.0
#     (0020, 0010) Study ID                            SH: '1102180001'
#     (0020, 0011) Series Number                       IS: '2'
#     (0020, 0012) Acquisition Number                  IS: '1'
#     (0020, 0013) Instance Number                     IS: '198'
#     (0020, 0032) Image Position (Patient)            DS: ['96.865929251629', '-158.42889542589', '154.49976199482']
#     (0020, 0037) Image Orientation (Patient)         DS: ['0.02956607291768', '0.99956282810648', '9.2819653e-009', '-0.0531693338709', '0.00157270521355', '-0.9985842721243']
#     (0020, 0052) Frame of Reference UID              UI: 1.3.12.2.1107.5.2.32.35413.2.20110218115324312.0.0.0
#     (0020, 1040) Position Reference Indicator        LO: ''
#     (0020, 1041) Slice Location                      DS: '93.145752848251'
#     (0028, 0000) Group Length                        UL: 172
#     (0028, 0002) Samples per Pixel                   US: 1
#     (0028, 0004) Photometric Interpretation          CS: 'MONOCHROME2'
#     (0028, 0010) Rows                                US: 256
#     (0028, 0011) Columns                             US: 256
#     (0028, 0030) Pixel Spacing                       DS: ['0.9765625', '0.9765625']
#     (0028, 0100) Bits Allocated                      US: 16
#     (0028, 0101) Bits Stored                         US: 12
#     (0028, 0102) High Bit                            US: 11
#     (0028, 0103) Pixel Representation                US: 0
#     (0028, 0106) Smallest Image Pixel Value          US: 0
#     (0028, 0107) Largest Image Pixel Value           US: 101
#     (0028, 1050) Window Center                       DS: '32'
#     (0028, 1051) Window Width                        DS: '86'
#     (0028, 1055) Window Center & Width Explanation   LO: 'Algo1'
#     (0029, 0000) Private Creator                     UL: 65610
#     (0029, 0010) Private tag data                    LO: 'SIEMENS CSA HEADER'
#     (0029, 0011) Private tag data                    LO: 'SIEMENS MEDCOM HEADER2'
#     (0029, 1008) [CSA Image Header Type]             CS: 'IMAGE NUM 4'
#     (0029, 1009) [CSA Image Header Version]          LO: '20110218'
#     (0029, 1010) [CSA Image Header Info]             OB: Array of 9460 bytes
#     (0029, 1018) [CSA Series Header Type]            CS: 'MR'
#     (0029, 1019) [CSA Series Header Version]         LO: '20110218'
#     (0029, 1020) [CSA Series Header Info]            OB: Array of 55996 bytes
#     (0029, 1160) [Series Workflow Status]            LO: 'com'
#     (0032, 0000) Group Length                        UL: 48
#     (0032, 1032) Requesting Physician                PN: 'SIM^KEUM SUK'
#     (0032, 1060) Requested Procedure Description     LO: 'MRI Research - KJS(C'
#     (0040, 0000) Group Length                        UL: 192
#     (0040, 0244) Performed Procedure Step Start Date DA: '20110218'
#     (0040, 0245) Performed Procedure Step Start Time TM: '115324.234000'
#     (0040, 0253) Performed Procedure Step ID         SH: '16254439'
#     (0040, 0254) Performed Procedure Step Descriptio LO: 'MRI Research - KJS(C'
#     (0040, 0275)  Request Attributes Sequence   1 item(s) ---- 
#        (0040, 0000) Group Length                        UL: 62
#        (0040, 0007) Scheduled Procedure Step Descriptio LO: 'MRI Research - KJS(C'
#        (0040, 0009) Scheduled Procedure Step ID         SH: '16254439'
#        (0040, 1001) Requested Procedure ID              SH: '1102180001'
#        ---------
#     (0051, 0000) Private Creator                     UL: 268
#     (0051, 0010) Private tag data                    LO: 'SIEMENS MR HEADER'
#     (0051, 1008) [CSA Image Header Type]             CS: 'IMAGE NUM 4'
#     (0051, 1009) [CSA Image Header Version ??]       LO: '1.0'
#     (0051, 100a) [Unknown]                           LO: 'TA 03:52'
#     (0051, 100b) [AcquisitionMatrixText]             LO: '256*256'
#     (0051, 100c) [Unknown]                           LO: 'FoV 250*250'
#     (0051, 100d) [Unknown]                           SH: 'SP L93.1'
#     (0051, 100e) [Unknown]                           LO: 'Sag>Tra(3.1)>Cor(1.7)'
#     (0051, 100f) [CoilString]                        LO: 'T:HEA;HEP'
#     (0051, 1011) [PATModeText]                       LO: 'p2'
#     (0051, 1012) [Unknown]                           SH: 'TP H35'
#     (0051, 1013) [PositivePCSDirections]             SH: '+LPH'
#     (0051, 1016) [Unknown]                           LO: 'p2 M/NORM/DIS2D/FM/FIL'
#     (0051, 1017) [Unknown]                           SH: 'SL 1.0'
#     (0051, 1019) [Unknown]                           LO: 'A1/IR'
#     (7fe0, 0000) Group Length                        UL: 131084
#     (7fe0, 0010) Pixel Data                          OW: Array of 131072 bytes,
#      'dob': datetime.datetime(1994, 2, 19, 0, 0),
#      'name': 'KWEON^HYEOK JU A',
#      'patientId': '72131118',
#      'scanDate': datetime.datetime(2011, 2, 18, 0, 0),
#      'sex': 'M'}

# In[179]:

def getDicomInfoAuto(firstDicomAddress):
    
    try:
        df = dicom.read_file(firstDicomAddress)
        dob =  df.PatientBirthDate
        sex = df.PatientSex
        pID = df.PatientID
        date = df.StudyDate
        age,dob,date=calculate_age(dob,date) 
        name = df.PatientName
        
        print name
        print dob
        print sex
        print pID
        print date
        print age 
        
        return {'name':name,
                'dob':dob,
                'sex':sex,
                'patientId':pID,
                'scanDate':date,
                'age':age,
                'dicomRead':df}
    
    except:
        dicom.read_file(firstDicomAddress,force=True)
        print 'cannot properly read dicom file'
        


# In[177]:

def calculate_age(born,scanDate):
    j= str(int(scanDate))
    i = str(int(born))
    
    today = datetime.datetime(year=int(j[:4]), month=int(j[4:6]), day=int(j[6:8]))
    born = datetime.datetime(year=int(i[:4]), month=int(i[4:6]), day=int(i[6:8]))
    
    try: 
        birthday = born.replace(year=today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1,born,today
    else:
        return today.year - born.year,born,today


# In[160]:

b = getDicomInfoAuto('/Volumes/CCNC_3T/KangIk/2014_05_DKI_project/FEP07_KHJ/T1/dicom/1.3.12.2.1107.5.2.32.35413.2011021811585514137740077.dcm')


# Out[160]:

#     19940219
#     M
#     72131118
#     20110218
#     16
# 

## Editing the database file

# In[215]:

efile = pd.ExcelFile('/Users/admin/Workbook1.xlsx')
a = efile.parse(efile.sheet_names[0])


# In[217]:

scanDateList = []
for i in a.scanDate:
    try:
        if type(i) == float:
            j=str(int(i))
            #print j
            #print j[:4], j[4:6], j[6:8]
            b = datetime.datetime(year=int(j[:4]), month=int(j[4:6]), day=int(j[6:8]))
            #print b
            scanDateList.append(b)
        else:
            scanDateList.append(i)
    except:
        scanDateList.append(i)


# In[218]:

a = a.reset_index()
a.scanDate = pd.Series(pd.to_datetime(scanDateList)).reindex_like(a)


# In[223]:

a = a.drop('index',axis=1)


# Out[223]:


    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)

    <ipython-input-223-3acd47447363> in <module>()
    ----> 1 a = a.drop('index',axis=1)
    

    /Users/admin/anaconda/lib/python2.7/site-packages/pandas/core/generic.pyc in drop(self, labels, axis, level)
        402                 new_axis = axis.drop(labels, level=level)
        403             else:
    --> 404                 new_axis = axis.drop(labels)
        405             dropped = self.reindex(**{axis_name: new_axis})
        406             try:


    /Users/admin/anaconda/lib/python2.7/site-packages/pandas/core/index.pyc in drop(self, labels)
       1305         mask = indexer == -1
       1306         if mask.any():
    -> 1307             raise ValueError('labels %s not contained in axis' % labels[mask])
       1308         return self.delete(indexer)
       1309 


    ValueError: labels ['index'] not contained in axis


# In[224]:

a.to_excel('/Users/admin/prac_scanDate.xlsx','Sheet1')


# In[225]:

df = pd.ExcelFile('/Users/admin/database.xlsx')
database = df.parse(df.sheet_names[0])


# In[226]:

database.scanDate=a.scanDate


# In[233]:

database[database.scanDate=='NaT']


# Out[233]:

#         koreanName  subjectName subjectInitial      group  sex  age  \
#     273        최유리          NaN            CYR        GHR    F   18   
#     477        C18          NaN            KDY    SNU_NOR    M   19   
#     478        C19          NaN            BHW    SNU_NOR    M   22   
#     479        C20          NaN            KJB    SNU_NOR    M   23   
#     480        C21          NaN            LJY    SNU_NOR    F   22   
#     481        C22          NaN            LJW    SNU_NOR    M   22   
#     482        C23          NaN            KSJ    SNU_NOR    M   22   
#     483        C24          NaN            IYS    SNU_NOR    F   20   
#     484        C25          NaN            RJY    SNU_NOR    M   19   
#     485        C26          NaN            PJH    SNU_NOR    M   19   
#     486        C27          NaN            LSH    SNU_NOR    F   19   
#     487        C28          NaN            KCH    SNU_NOR    M   22   
#     488        C29          NaN            KSD    SNU_NOR    M   22   
#     489        C30          NaN            LJJ    SNU_NOR    M   20   
#     490        C31          NaN            KHP    SNU_NOR    M   20   
#     491        C32          NaN            LJH    SNU_NOR    M   21   
#     492        C33          NaN            JHS    SNU_NOR    M   20   
#     493        C34          NaN            SGR    SNU_NOR    F   20   
#     494        C35          NaN            AJH    SNU_NOR    M   23   
#     495        C36          NaN            LDH    SNU_NOR    M   23   
#     496        C37          NaN            PJI    SNU_NOR    M   24   
#     497        C38          NaN            YKH    SNU_NOR    M   23   
#     498        T01          NaN            IKB    SNU_SPD    M   24   
#     513        T16          NaN            CKW    SNU_SPD    M   16   
#     518        T21          NaN            ANG    SNU_SPD    F   27   
#     519        T22          NaN             PI    SNU_SPD    M   27   
#     520        T23          NaN            KSH    SNU_SPD    M   23   
#     521        T24          NaN            PCY    SNU_SPD    M   24   
#     522        T25          NaN             TK    SNU_SPD    M   24   
#     523        T26          NaN            YJG    SNU_SPD    M   25   
#     524        T27          NaN             SK    SNU_SPD    F   24   
#     525        T28          NaN            SSH    SNU_SPD    F   23   
#     526        T29          NaN            HSA    SNU_SPD    F   19   
#     527        T30          NaN             YJ    SNU_SPD    F   18   
#     528        T31          NaN             HS    SNU_SPD    M   26   
#     529        김진훈          NaN            KJH  BADUK_PRO    M   21   
#     590        홍영인          NaN            HYI    SNU_NOR    남   31   
#     622        홍영인          NaN            HYI    SNU_NOR    남   31   
#     637        NaN          NaN            NaN    reCheck  NaN  NaN   
#     638        NaN          NaN            NaN    reCheck  NaN  NaN   
#     639        NaN          NaN            NaN    reCheck  NaN  NaN   
#     640        NaN          NaN            NaN    reCheck  NaN  NaN   
#     641        김대현  KimDaeHyeon            KDH        UMO    M   25   
#     642        임세락      ImSeRak            ISR        DNO    M   18   
#     
#                          DOB scanDate   timeline     studyName  patientNumber  \
#     273  1996-06-25 00:00:00      NaT   baseline          fMRI       44607261   
#     477  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     478  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     479  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     480  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     481  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     482  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     483  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     484  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     485  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     486  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     487  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     488  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     489  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     490  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     491  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     492  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     493  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     494  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     495  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     496  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     497  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     498  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     513  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     518  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     519  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     520  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     521  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     522  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     523  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     524  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     525  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     526  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     527  1970-01-01 00:00:00      NaT   baseline            BM            NaN   
#     528  1991-02-16 00:00:00      NaT   baseline            BM            NaN   
#     529  1991-02-16 00:00:00      NaT   baseline         baduk       44093204   
#     590  1982-01-31 00:00:00      NaT   baseline  oxytocin SNU            NaN   
#     622  1982-01-31 00:00:00      NaT  follow up  oxytocin SNU            NaN   
#     637                  NaN      NaT        NaN           NaN            NaN   
#     638                  NaN      NaT        NaN           NaN            NaN   
#     639                  NaN      NaT        NaN           NaN            NaN   
#     640                  NaN      NaT        NaN           NaN            NaN   
#     641           1988-06-11      NaT   baseline           NaN       45719763   
#     642           1995-09-29      NaT   baseline           NaN       45707272   
#     
#         T1Number DTINumber DKINumber RESTNumber REST2Number         folderName  \
#     273      208        65       151       4060         NaN          GHR29_CYR   
#     477      208        65       151       4060         150          CON19_KDY   
#     478      208        65       151       4060         150          CON20_BHW   
#     479      208        65       151       4060         150          CON21_KJB   
#     480      208        65       151       4060         150          CON22_LJY   
#     481      208        65       151       4060         150          CON23_LJW   
#     482      208   missing   missing       4060         150          CON24_KSJ   
#     483      208        65       151       4060         150          CON25_IYS   
#     484      208        65       151       4060         150          CON26_RJY   
#     485      208        65       151       4060         150          CON27_PJH   
#     486      208        65       151       4060         150          CON28_LSH   
#     487      208        65       151       4060         150          CON29_KCH   
#     488      208   missing   missing       4060         150          CON30_KSD   
#     489      208        65       151       4060         150          CON31_LJJ   
#     490      208        65       151       4060         150          CON32_KHP   
#     491      208        65       151       4060         150          CON33_LJH   
#     492      208        65       151       4060         150          CON34_JHS   
#     493      208        65       151       4060         150          CON35_SGR   
#     494      208        65       151       4060         150          CON36_AJH   
#     495      208        65       151       4060         150          CON37_LDH   
#     496      208        65       151       4060         150          CON38_PJI   
#     497      208        65       151       4060         150          CON39_YKH   
#     498      208        65       151       4060         150  Schizotypal40_IKB   
#     513      208        65       151       4060         150  Schizotypal55_CKW   
#     518      208        65       151       4060         150  Schizotypal60_ANG   
#     519      208        65       151       4060         150   Schizotypal61_PI   
#     520      208        65       151       4060         150  Schizotypal62_KSH   
#     521      208        65       151       4060         150  Schizotypal63_PCY   
#     522      208        50       151       4060         150   Schizotypal64_TK   
#     523      208        65       151       4060         150  Schizotypal65_YJG   
#     524      208        65       151       4060         150   Schizotypal66_SK   
#     525      208        65       151       4060         150  Schizotypal67_SSH   
#     526      208        65       151       4060         150  Schizotypal68_HSA   
#     527      208        65       151       4060         150   Schizotypal69_YJ   
#     528      208        65       151       4060         150   Schizotypal70_HS   
#     529      416       NaN       NaN       8120        3132    BADUK_PRO01_KJH   
#     590      208        65       NaN        149         NaN           HC03_HYI   
#     622      NaN       NaN       NaN        150         NaN        fu_HC03_HYI   
#     637      NaN       NaN       NaN        NaN         NaN          CHR73_CKI   
#     638      NaN       NaN       NaN        NaN         NaN          GHR31_JJA   
#     639      NaN       NaN       NaN        NaN         NaN          NOR75_LSK   
#     640      NaN       NaN       NaN        NaN         NaN          SPR09_JYS   
#     641      208        65       151       4060         NaN          UMO59_KDH   
#     642      208        65       151       4060         NaN          DNO35_ISR   
#     
#         backUpBy             note  
#     273      NaN         oxytocin  
#     477      NaN              NaN  
#     478      NaN              NaN  
#     479      NaN              NaN  
#     480      NaN              NaN  
#     481      NaN              NaN  
#     482      NaN              NaN  
#     483      NaN              NaN  
#     484      NaN              NaN  
#     485      NaN              NaN  
#     486      NaN              NaN  
#     487      NaN              NaN  
#     488      NaN              NaN  
#     489      NaN              NaN  
#     490      NaN              NaN  
#     491      NaN              NaN  
#     492      NaN              NaN  
#     493      NaN              NaN  
#     494      NaN              NaN  
#     495      NaN              NaN  
#     496      NaN              NaN  
#     497      NaN              NaN  
#     498      NaN              NaN  
#     513      NaN              NaN  
#     518      NaN              NaN  
#     519      NaN              NaN  
#     520      NaN              NaN  
#     521      NaN              NaN  
#     522      NaN  육안으로 확인 시 이상 없음  
#     523      NaN              NaN  
#     524      NaN              NaN  
#     525      NaN              NaN  
#     526      NaN              NaN  
#     527      NaN              NaN  
#     528      NaN              NaN  
#     529      NaN              NaN  
#     590      NaN              NaN  
#     622      NaN              fu_  
#     637      NaN              NaN  
#     638      NaN              NaN  
#     639      NaN              NaN  
#     640      NaN              NaN  
#     641   kangik              NaN  
#     642   kangik              NaN  
