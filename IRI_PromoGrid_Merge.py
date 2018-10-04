# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 11:26:46 2018

@author: Jason Weir
"""
#Importing dependencies
import json
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np

#Creating Private/ Public Key Creds to access relevant gsheets. Ensure that "pygsheets@pygsheets-186900.iam.gserviceaccount.com" is on the 'shared list' within each gsheet file.

json_key = json.load(open('creds.json')) # json credentials need to be saved in the working directory 
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'] # this is the scope where python will look to find data
credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope) # gets email and key from creds
file = gspread.authorize(credentials) # authenticate with Google before opening file

##############################
#Creating dfs and common variables
df = pd.DataFrame()

ws = 'S'
ww ='Woolworths'
cs ='Coles'
iga ='Supa IGA'
cw = 'Chemist Warehouse'
pl = 'Priceline'
ad= 'Aldi'

w16g ="Woolworths 2016 Prom Grid"
w17g ="Woolworths 2017 Prom Grid"
w18g ="Woolworths 2018 Prom Grid"
w19g ="Woolworths 2019 Prom Grid"

c16g ="Coles 2016 Prom Grid"
c17g ="Coles 2017 Prom Grid"
c18g ="Coles 2018 Prom Grid"
c19g ="Coles 2019 Prom Grid"

i16g ="Supa IGA 2016 Prom Grid"
i17g ="Supa IGA 2017 Prom Grid"
i18g ="Supa IGA 2018 Prom Grid"
i19g ="Supa IGA 2019 Prom Grid"

a17g ="ALDI 2017 Prom Grid"
a18g ="ALDI 2018 Prom Grid"
a19g ="ALDI 2019 Prom Grid"

cw16g ="Chemist Warehouse 2016 Prom Grid"
cw17g ="Chemist Warehouse 2017 Prom Grid"
cw18g ="Chemist Warehouse 2018 Prom Grid"
cw19g ="Chemist Warehouse 2019 Prom Grid"

p16g ="Priceline 2016 Prom Grid"
p17g ="Priceline 2017 Prom Grid"
p18g ="Priceline 2018 Prom Grid"
p19g ="Priceline 2019 Prom Grid"

wwc = "Woolworths Prom Grid Coding"
csc = "Coles Prom Grid Coding"
plc = "Priceline Prom Grid Coding"
igc = "Supa IGA Prom Grid Coding"
cwc = "Chemist Warehouse Prom Grid Coding"
adc = "ALDI Prom Grid Coding"

           ##   WOOLWORTHS  ##            ##   WOOLWORTHS  ##       ##   WOOLWORTHS  ##
###2016
w16oc = file.open(w16g).worksheet(ws) 
get_as_dataframe(w16oc)
data1 = get_as_dataframe(w16oc, evaluate_formulas=True,skiprows=1).assign(Year='2016').assign(Customer=ww)
###2017
w17oc = file.open(w17g).worksheet(ws) 
get_as_dataframe(w17oc)
data2 = get_as_dataframe(w17oc, evaluate_formulas=True,skiprows=1).assign(Year='2017').assign(Customer=ww)
##2018
w18oc = file.open(w18g).worksheet(ws) 
get_as_dataframe(w18oc)
data3 = get_as_dataframe(w18oc, evaluate_formulas=True,skiprows=1).assign(Year='2018').assign(Customer=ww)
###2019
w19oc = file.open(w19g).worksheet(ws) 
get_as_dataframe(w19oc)
data4 = get_as_dataframe(w19oc, evaluate_formulas=True,skiprows=1).assign(Year='2019').assign(Customer=ww)

#                                ##   COLES  ##       ##   COLES  ##    ##   COLES  ##
###2016
c16oc = file.open(c16g).worksheet(ws) 
get_as_dataframe(c16oc)
data5 = get_as_dataframe(c16oc, evaluate_formulas=True,skiprows=1).assign(Year='2016').assign(Customer=cs)
###2017
c17oc = file.open(c17g).worksheet(ws) 
get_as_dataframe(c17oc)
data6 = get_as_dataframe(c17oc, evaluate_formulas=True,skiprows=1).assign(Year='2017').assign(Customer=cs)
###2018
c18oc = file.open(c18g).worksheet(ws) 
get_as_dataframe(c18oc)
data7 = get_as_dataframe(c18oc, evaluate_formulas=True,skiprows=1).assign(Year='2018').assign(Customer=cs)
###2019
c19oc = file.open(c19g).worksheet(ws) 
get_as_dataframe(c19oc)
data8 = get_as_dataframe(c19oc, evaluate_formulas=True,skiprows=1).assign(Year='2019').assign(Customer=cs)

#                             ##   IGA  ##        ##   IGA  ##            ##   IGA  ##
####2016
i16oc = file.open(i16g).worksheet(ws) 
get_as_dataframe(i16oc)
data9 = get_as_dataframe(i16oc, evaluate_formulas=True,skiprows=1).assign(Year='2016').assign(Customer=iga)
###2017
i17oc = file.open(i17g).worksheet(ws) 
get_as_dataframe(i17oc)
data10 = get_as_dataframe(i17oc, evaluate_formulas=True,skiprows=1).assign(Year='2017').assign(Customer=iga)
###2018
i18oc = file.open(i18g).worksheet(ws) 
get_as_dataframe(i18oc)
data11 = get_as_dataframe(i18oc, evaluate_formulas=True,skiprows=1).assign(Year='2018').assign(Customer=iga)
###2019
i19oc = file.open(i19g).worksheet(ws) 
get_as_dataframe(i19oc)
data12 = get_as_dataframe(i19oc, evaluate_formulas=True,skiprows=1).assign(Year='2019').assign(Customer=iga)

                                ##   ALDI ##        ##   ALDI  ##            ##   ALDI  ##
###2017
a17oc = file.open(a17g).worksheet(ws) 
get_as_dataframe(a17oc)
data13 = get_as_dataframe(a17oc, evaluate_formulas=True,skiprows=1).assign(Year='2017').assign(Customer=ad)
###2018
a18oc = file.open(a18g).worksheet(ws) 
get_as_dataframe(a18oc)
data14 = get_as_dataframe(a18oc, evaluate_formulas=True,skiprows=1).assign(Year='2018').assign(Customer=ad)
###2019
a19oc = file.open(a19g).worksheet(ws) 
get_as_dataframe(a19oc)
data15 = get_as_dataframe(a19oc, evaluate_formulas=True,skiprows=1).assign(Year='2019').assign(Customer=ad)


## PRICELINE   ###               ## PRICELINE   ###                     ## PRICELINE   ###

p16oc = file.open(p16g).worksheet(ws) 
get_as_dataframe(p16oc)
data16 = get_as_dataframe(p16oc, evaluate_formulas=True,skiprows=1).assign(Year='2016').assign(Customer=pl)
data16 =pd.concat([data16[t].to_frame(c) for t in data16.columns for c in t.split(';')],1)
##2017
p17oc = file.open(p17g).worksheet(ws) 
get_as_dataframe(p17oc)
data17 = get_as_dataframe(p17oc, evaluate_formulas=True,skiprows=1).assign(Year='2017').assign(Customer=pl)
data17 =pd.concat([data17[t].to_frame(c) for t in data17.columns for c in t.split(';')],1)
##2018
p18oc = file.open(p18g).worksheet(ws) 
get_as_dataframe(p18oc)
data18 = get_as_dataframe(p18oc, evaluate_formulas=True,skiprows=1).assign(Year='2018').assign(Customer=pl)
data18 =pd.concat([data18[t].to_frame(c) for t in data18.columns for c in t.split(';')],1)
##2019
p19oc = file.open(p19g).worksheet(ws) 
get_as_dataframe(p19oc)
data19 = get_as_dataframe(p19oc, evaluate_formulas=True,skiprows=1).assign(Year='2019').assign(Customer=pl)
data19 =pd.concat([data19[t].to_frame(c) for t in data19.columns for c in t.split(';')],1)

## CHEMIST WAREHOUSE   ###               ## CHEMIST WAREHOUSE   ###                     ## CHEMIST WAREHOUSE   ###

cw16oc = file.open(cw16g).worksheet(ws) 
get_as_dataframe(cw16oc)
data20 = get_as_dataframe(cw16oc, evaluate_formulas=True,skiprows=1).assign(Year='2016').assign(Customer=cw)
data20 =pd.concat([data20[t].to_frame(c) for t in data20.columns for c in t.split(';')],1)
##2017
cw17oc = file.open(cw17g).worksheet(ws) 
get_as_dataframe(cw17oc)
data21 = get_as_dataframe(cw17oc, evaluate_formulas=True,skiprows=1).assign(Year='2017').assign(Customer=cw)
data21 =pd.concat([data21[t].to_frame(c) for t in data21.columns  for c in t.split(';')],1)
##2018
cw18oc = file.open(cw18g).worksheet(ws) 
get_as_dataframe(cw18oc)
data22 = get_as_dataframe(cw18oc, evaluate_formulas=True,skiprows=1).assign(Year='2018').assign(Customer=cw)
data22 =pd.concat([data22[t].to_frame(c) for t in data22.columns for c in t.split(';')],1)
##2019
cw19oc = file.open(cw19g).worksheet(ws) 
get_as_dataframe(cw19oc)
data23 = get_as_dataframe(cw19oc, evaluate_formulas=True,skiprows=1).assign(Year='2019').assign(Customer=cw)
data23 =pd.concat([data23[t].to_frame(c) for t in data23.columns for c in t.split(';')],1)

## appending DFs from Grocery together & Converting to relational format
frames = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16
          ,data17,data18,data19,data20,data21,data22,data23]
df = pd.concat(frames,sort=False)

df1= df.drop_duplicates(subset=['Promo Bundle','Customer','Year','Colgate Week'], keep='first')
df1.reset_index()
df1 = pd.melt(df1,id_vars=['Promo Bundle','Colgate Week','Year','Customer'])   
df1 = pd.pivot_table(df1,values='value',
                       index=    ['Promo Bundle','Year','Customer','variable'],
                       columns = ['Colgate Week'],aggfunc= 'first') 

df1.reset_index(inplace=True)
df1.drop(['Colgate Week'], axis=1, inplace = True)
## removing duplicate values & Removing non promoted weeks
df1 = df1[df1['Promo Bundle'] != 'Promo Bundle']
df1 = df1[df1['Promo Bundle'] != '-']
df1 = df1[~df1['variable'].str.contains('Un')]
df1 = df1[df1['Display'].notnull()]
df1.rename( columns={'variable': 'Colgate Week'}, inplace=True)
df1[['Colgate Week']] = df1[['Colgate Week']].apply(pd.to_numeric,errors ='coerce') 
df1[['Year']] = df1[['Year']].apply(pd.to_numeric,errors='coerce')

df1['Equivalent Single Price'] = df1['Equivalent Single Price'].astype('str')
df1['Equivalent Single Price'] = df1['Equivalent Single Price'].str.replace('Please Enter','')
df1['Equivalent Single Price'] = df1['Equivalent Single Price'].str.replace('nan','')
df1['Equivalent Single Price'] = df1['Equivalent Single Price'].str.replace('$','')
df1['Equivalent Single Price'] = df1['Equivalent Single Price'].str.strip()
df1[['Equivalent Single Price']] = df1[['Equivalent Single Price']].apply(pd.to_numeric,errors='coerce')
df1['Equivalent Single Price'] = df1['Equivalent Single Price'].apply(lambda x: round(x,2))

df1= df1.drop_duplicates(keep='first') 
df1.reset_index(inplace=True)

## PROM GRID CODING ###   ## PROM GRID CODING ###     ## PROM GRID CODING ###     ## PROM GRID CODING ###
                                                 ## PRICELINE
PLSCC = file.open(plc).worksheet(ws) 
get_as_dataframe(PLSCC)
data24 = get_as_dataframe(PLSCC, evaluate_formulas=True,skiprows=1,usecols=[0,1,2]).assign(Customer=pl)
                                               ##CHEMIST WAREHOUSE
CWHSCC = file.open(cwc).worksheet(ws)
get_as_dataframe(CWHSCC)
data25 = get_as_dataframe(CWHSCC, evaluate_formulas=True,skiprows=1,usecols=[0,1,2]).assign(Customer=cw)
                                                 ## WOOLWORTHS
WWSCC = file.open(wwc).worksheet(ws)
get_as_dataframe(WWSCC)
data26 = get_as_dataframe(WWSCC, evaluate_formulas=True,skiprows=1,usecols=[0,1,2]).assign(Customer=ww)
                                                    ## COLES
CSCC = file.open(csc).worksheet(ws)
get_as_dataframe(CSCC)
data27 = get_as_dataframe(CSCC, evaluate_formulas=True,skiprows=1,usecols=[0,1,2]).assign(Customer=cs)
                                                    ## IGA
igSCC = file.open(igc).worksheet(ws)
get_as_dataframe(igSCC)
data28 = get_as_dataframe(igSCC, evaluate_formulas=True,skiprows=1,usecols=[0,1,2]).assign(Customer=iga)
                                                    ## ALDI
ALCC = file.open(adc).worksheet(ws)
get_as_dataframe(ALCC)
data29 = get_as_dataframe(ALCC, evaluate_formulas=True,skiprows=1,usecols=[0,1,2]).assign(Customer=ad)

## appending DFs from CODING FILES together/ Converting to relational format & Cleaning Up
frames = [data24,data25,data26,data27,data28,data29]
df2 = pd.concat(frames,sort=False)
df2.reset_index(inplace=True)
df2 = df2[df2['Display'].notnull()]
df2['Display Quality'] = np.where((df2['Display Quality'].isnull()) ,'1.Shelf',df2['Display Quality']) 
df2['Display # of Stores'] = np.where((df2['Display # of Stores'].isnull()) ,0,df2['Display # of Stores'])
df2['Display # of Stores']= df2['Display # of Stores'].apply(pd.to_numeric,errors ='coerce')
df2= df2.drop_duplicates(keep='first') 
df2.reset_index(inplace=True) 

     ######### Merging Display Quality with Display on PROMO GRIDS  #################

dfm1= df1.merge(df2, how='left', left_on=['Customer','Display'], right_on=['Customer','Display'], indicator=True)

     ######### ISOLATING DISPLAY NOT CAPTURED ON THE CODING FILE FOR CDE REVIEW  #################

df3 = dfm1[dfm1['_merge']=='left_only']
df3 =df3[['Customer','Display','Year']]
df3= df3.drop_duplicates(subset=['Customer','Display','Year'], keep='first')
pcc = file.open("Promo Coding Misses").worksheet(ws) 
set_with_dataframe(pcc,df3,row=1)

## Drop uneeeded Cols
dfm1.reset_index(inplace=True)
dfm1.drop(['_merge'], axis=1, inplace = True)

      ######### Merging Product Info #################        ######### Merging Product Info #################

f1 = 'O:\My Drive\Colgate_Australia\Analytics_Development\Data_Governance\Master_Data\Product_Master_Data\OUTPUT CBP (AU) Product Master (PPG Level).csv'
df4 = pd.read_csv(f1)
dfm2= dfm1.merge(df4, how='left', left_on=['Promo Bundle'], right_on=['PPG Code+Name'], indicator=True)

     ######### ISOLATING PPGs NOT CAPTURED in PPG CODING FOR CDE REVIEW  #################

df5 = dfm2[dfm2['_merge']=='left_only']

df5 =df5[['Customer','Promo Bundle_x','Year']]
df5= df5.drop_duplicates(subset=['Customer','Promo Bundle_x','Year'], keep='first')
ppgc = file.open("PPG Coding Misses").worksheet(ws) 
set_with_dataframe(ppgc,df5,row=1)

## Drop uneeeded Cols

dfm2.drop(['_merge','Units per Case','Factory Origin','PPG Code+Name'], axis=1, inplace = True)

    ######### Merging Time Info #########     ######### Merging Time Info #########
    
f2 = 'O:\My Drive\Colgate_Australia\Analytics_Development\Data_Governance\Master_Data\Time_Master_Data\SOURCE Colgate Weeks Quarters Conversion.xlsx'
df6 = pd.read_excel(f2, usecols=[0,1,2,3,7,8])
df6 = df6.reindex(columns=['Year', 'Colgate Week','Colgate w/c Date', 'Quarter', 'Half','YTD/YTG'])
df6['Colgate Week'] = df6['Colgate Week'].apply(pd.to_numeric,errors='coerce')
df6['Year'] = df6['Year'].apply(pd.to_numeric,errors='coerce')
dfm3= dfm2.merge(df6, how='left',left_on=['Colgate Week','Year'], right_on=['Colgate Week','Year'])

## Drop uneeeded Cols
dfm3.drop(['index','index_x','index_y','level_0','Promo Bundle_y'], axis=1, inplace = True)
dfm3.rename( columns={'Promo Bundle_x': 'Promo Bundle'}, inplace=True)

    ######### Merging IRI/ CATALYTICS DATA #########     ######### Merging IRI/ CATALYTICS DATA #########

f6 = 'O:\My Drive\Colgate_Australia\Analytics_Development\Data_Governance\Master_Data\Sales_Master_Data\IRI_data\OUTPUT Promo Grid Actualised IRI Data.csv'
df7 = pd.read_csv(f6, usecols=[3,4,6,7,8,9,13,15,16,17,21,22,23])
#df7.to_csv('output4.csv')
dfm4= dfm3.merge(df7, how='outer',left_on=['Colgate Week','Year', 'Customer','Promo Bundle'], right_on=['Colgate Week','Year','Customer','PPG Code+Name'], suffixes=('_1x', '_1y'))
dfm4['Promo Bundle'] = np.where((dfm4['Promo Bundle'].isnull()),dfm4['PPG Code+Name'] ,dfm4['Promo Bundle'])

# Drop all IPH attributes
dfm4.drop(['PPG Code+Name','RRP','Category','Product Category','Sub Category','Brand','Sub Brand','Gender', 'Age',
           'Size','Uom','Size_Combined','PPG Code','Colgate w/c Date','Quarter','Half','YTD/YTG'], axis=1, inplace = True) # Drops unessesary PPG Code from IRI Data

##     Resetting Product Data AFTER IRI CONNECTION
dfm5= dfm4.merge(df4, how='left', left_on=['Promo Bundle'], right_on=['PPG Code+Name'], suffixes=('_x', '_y'))
dfm5.drop(['PPG Code+Name','Units per Case','Factory Origin'], axis=1, inplace = True) # Drops unessesary PPG Code from IRI Data
dfm5.rename( columns={'Promo Bundle_x':'Promo Bundle' ,'Promo Bundle_y': 'Promo Group'}, inplace=True)

#    Resetting Time Data AFTER IRI CONNECTION
dfm6= dfm5.merge(df6, how='left',left_on=['Colgate Week','Year'], right_on=['Colgate Week','Year'], suffixes=('', '_y'))

###    Resetting RRP data AFTER IRI CONNECTION
f9 = 'O:\My Drive\Colgate_Australia\Analytics_Development\Data_Governance\Master_Data\Pricing_Master_Data\SOURCE Pricing Master Data.xlsx'
df8 = pd.read_excel(f9,usecols = [5,6])
dfm7= dfm6.merge(df8, how='left', left_on=['Promo Bundle'], right_on=['PPG'], suffixes=('_x', '_y'))
dfm7.drop(['PPG'], axis=1, inplace = True) # Drops unessesary PPG Code from IRI Data

###    Removing uncoded PPGs AFTER IRI CONNECTION
dfm8 = dfm7[dfm7['Sub Category'].notnull()]

###    Creating RRP Price bands within Data
dfm9 = dfm8[['Sub Category','RRP']]
dfm9 = dfm9.drop_duplicates(keep='first') 
dfm9['RRP Percentile'] = dfm9.groupby(['Sub Category'])['RRP'].transform(lambda x: pd.qcut(x, 3,precision= int,labels =False,duplicates ='drop'))
dfm9['RRP Percentile'] = np.where((dfm9['RRP Percentile'].isnull()),1 ,dfm9['RRP Percentile'])

### Remerging RRP Bands with existing Dataset
dfm10= dfm8.merge(dfm9, how='left', left_on=['Sub Category','RRP'], right_on=['Sub Category','RRP'],copy =False)
dfm10 = dfm10.drop_duplicates(keep='first') 

### Filling in missing ESPs with ASP/Unit where a promo exists
dfm10['Equivalent Single Price'] = np.where((dfm10['Equivalent Single Price'].isnull()) & (dfm10['Display'].notnull()),
     dfm10['Asp/Unit'],dfm10['Equivalent Single Price'])

### Filling in missing ESPs with RRP/Unit where a promo exists And there is no ASP/Unit
dfm10['Equivalent Single Price'] = np.where((dfm10['Equivalent Single Price'].isnull()) & (dfm10['Display'].notnull()),
     dfm10['RRP'],dfm10['Equivalent Single Price'])

### Creating Discount % 
dfm10['%Disc']  = 0
dfm10['%Disc']  = np.where((dfm10['Asp/Unit'].isnull()) & (dfm10['Equivalent Single Price'].notnull()),
     ((dfm10['RRP']-dfm10['Equivalent Single Price'])/dfm10['RRP']),dfm10['%Disc']) #### Captures Future Discounts Based on ESP
dfm10['%Disc']  = np.where((dfm10['Asp/Unit'].notnull()) & (dfm10['Display'].notnull()),
     ((dfm10['RRP']-dfm10['Asp/Unit'])/dfm10['RRP']),dfm10['%Disc'])#### Captures past Discounts Based on ASP
dfm10['%Disc']= dfm10['%Disc'].apply(pd.to_numeric,errors ='coerce')
dfm10['%Disc'] = (dfm10['%Disc'].round(2))*100
dfm10['%Disc']  = np.where((dfm10['%Disc']<0)  & (dfm10['%Disc'].notnull()),0,dfm10['%Disc']) ## Removing discount where max ASP > RRP
dfm10['%Disc']  = np.where((dfm10['%Disc']>=90) & (dfm10['%Disc'].notnull()),0,dfm10['%Disc']) ## Removing discount where Disc > 90%
dfm10['%Disc']  = np.where((dfm10['Dist_Points']<=90) & (dfm10['Dist_Points'].notnull()) ,0,dfm10['%Disc']) ## Removes any discount in the IRI Data with Dist 90 stores and under

dfm10['%DiscLevel']  = pd.cut(dfm10['%Disc'], [0,28,40, 55, np.inf], labels=['Low','Medium','High','Very High'])
dfm10['%DiscLevel']  = np.where(dfm10['%DiscLevel'].isnull() ,'No Promo',dfm10['%DiscLevel'])

dfm10['%Disc(Normalised)'] = np.where(dfm10['%Disc']  <=13 ,dfm10['%Disc'],0)
dfm10['%Disc(Normalised)'] = np.where(dfm10['%Disc']  > 73 ,dfm10['%Disc'], dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=17) & (dfm10['%Disc']>13)) ,15,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=23) & (dfm10['%Disc']>17)) ,20,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=27) & (dfm10['%Disc']>23)) ,25,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=31) & (dfm10['%Disc']>27)) ,30,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=35) & (dfm10['%Disc']>31)) ,33,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=37) & (dfm10['%Disc']>35)) ,35,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=42) & (dfm10['%Disc']>37)) ,40,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=47) & (dfm10['%Disc']>42)) ,45,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=53) & (dfm10['%Disc']>47)) ,50,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=58) & (dfm10['%Disc']>53)) ,55,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=63) & (dfm10['%Disc']>58)) ,60,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=67) & (dfm10['%Disc']>63)) ,65,dfm10['%Disc(Normalised)'])
dfm10['%Disc(Normalised)'] = np.where(((dfm10['%Disc']<=73) & (dfm10['%Disc']>67)) ,70,dfm10['%Disc(Normalised)'])

## Ensuring that Promo grids line of with Catalytics

dfm10['Display'] = np.where((dfm10['%Disc(Normalised)']>20) & (dfm10['Display'].isnull() & (dfm10['Customer']=='Woolworths')) ,'Fixture',dfm10['Display'])
dfm10['Display'] = np.where((dfm10['%Disc(Normalised)']>20) & (dfm10['Display'].isnull() & (dfm10['Customer']!='Woolworths')) ,'Shelf',dfm10['Display'])

dfm10['Display Quality'] = np.where(((dfm10['Display']=='Shelf') | (dfm10['Display']=='Fixture')) ,'1.Shelf',dfm10['Display Quality'])

dfm10['Display # Shelves'] = np.where((dfm10['Display'].str.contains('helf') | (dfm10['Display'].str.contains('ixture'))) ,'0',dfm10['Display # Shelves'])
dfm10['Display # Shelves']= dfm10['Display # Shelves'].apply(pd.to_numeric,errors ='coerce')
  
dfm10['In-Store_Shopper'] = np.where((dfm10['%Disc']==0) & (dfm10['In-Store_Shopper'].notnull()) ,None,dfm10['In-Store_Shopper'])
dfm10['In-Store_Shopper'] = np.where((dfm10['In-Store_Shopper'].isnull() & dfm10['Display'].notnull()),'No' ,dfm10['In-Store_Shopper'])
              
dfm10['Display # of Stores'] = np.where((dfm10['%Disc']==0) & (dfm10['Display # of Stores'].notnull()) ,None,dfm10['Display # of Stores'])
     
dfm10['In-Store_Shopper_#'] = np.where((dfm10['%Disc']==0) & (dfm10['In-Store_Shopper_#'].notnull()) ,None,dfm10['In-Store_Shopper_#'])
dfm10['In-Store_Shopper_#'] = np.where((dfm10['Display'].notnull() & (dfm10['In-Store_Shopper_#'].isnull())) ,0,dfm10['In-Store_Shopper_#'])
dfm10['In-Store_Shopper_#'] = dfm10['In-Store_Shopper_#'].astype('str')    
dfm10['In-Store_Shopper_#'] = dfm10['In-Store_Shopper_#'].str.replace('Please Enter','')
dfm10['In-Store_Shopper_#'] = dfm10['In-Store_Shopper_#'].str.replace('nan','')
dfm10['In-Store_Shopper_#'] = dfm10['In-Store_Shopper_#'].str.replace('$','')
dfm10['In-Store_Shopper_#']=  dfm10['In-Store_Shopper_#'].apply(pd.to_numeric,errors ='coerce')  

dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('%%','%')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('off%','off')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('%O','% O')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('FF','ff')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('DD','Down Down')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('Down Down1','DD1')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('Down Down2','DD2')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('Doen','Down')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('1/2 price','Half Price')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('1/2 Price','Half Price')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('1/2Price','Half Price')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('1/2Price','Half Price')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('1./2 Price','Half Price')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('HP','Half Price')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace(' for ','for')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace(' 3 For 2','3for2')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('5..6','5.6')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('No Call out (EDLP) ','EDLP')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('Please Enter','')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('Shelf TPR','TPR')
dfm10['Mechanic'] = dfm10['Mechanic'].str.replace('Shelf Price (SFS)','TPR')

dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].isnull()) ,None,'TPR')
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('for')) ,'Multibuy',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('3f2')) ,'Multibuy',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('For')) ,'Multibuy',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('FOR')) ,'Multibuy',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('Multi')) ,'Multibuy',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('EDLP')) ,'EDLP',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('LDLP')) ,'EDLP',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('L1')) ,'EDLP',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('L2')) ,'EDLP',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('EDV')) ,'EDLP',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('Always')) ,'EDLP',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('Down Down')) ,'EDLP+',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('DD')) ,'EDLP+',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].str.contains('Dropped')) ,'EDLP+',dfm10['Mechanic Type'])
dfm10['Mechanic Type']  = np.where((dfm10['Mechanic'].isnull()) ,None,dfm10['Mechanic Type'])

dfm10['Catalogue'] = np.where((dfm10['%Disc']==0) & (dfm10['Catalogue'].notnull()) ,None,dfm10['Catalogue'])
dfm10['Catalogue'] = np.where((((dfm10['Catalogue'].isnull()) | (dfm10['Catalogue']=='No'))) & (dfm10['Catalogue Quality'].notnull()) ,dfm10['Catalogue Quality'],dfm10['Catalogue'])
dfm10['Catalogue'] = np.where((dfm10['Catalogue'].isnull()) & (dfm10['Display'].notnull()) ,'No',dfm10['Catalogue'])

dfm10['Catalogue Flag'] = np.where((dfm10['Catalogue'].str.contains('es')) | (dfm10['Catalogue'].str.contains('of')),'Yes','No')          
      

###### Cleaning Up Data to Drop into Tableau / Frequency Tracker & Weekly Summary File  #######

dfm10 = dfm10.sort_values(['Customer','Year','Category','Sub Category','Promo Bundle','Colgate Week'],  ## Sorting cells into better order
                                      ascending= True, kind ='quicksort',na_position = 'last')

dfm10= dfm10.drop_duplicates(keep='first')


dfm10.to_excel('OUTPUT AU Colgate Palmolive All Weeks & Promo Metrics.xlsx',index= True,merge_cells=False,startrow=2) ## Original unformatted 

#Capturing only promoted weeks & Sorting
dfm11 = dfm10[dfm10['Display'].notnull()].reset_index()
dfm11 = dfm11.sort_values(['Customer','Year','Category','Sub Category','Promo Bundle','Colgate Week'], 
                                      ascending= True, kind ='quicksort',na_position = 'last')

dfm11 = dfm11[['Category','Product Category','Sub Category','Brand','Sub Brand','Gender','Age','Size','Uom','Promo Bundle','Promo Group','Customer','Year','Quarter','Half','YTD/YTG','Colgate Week','Colgate w/c Date','Display','Equivalent Single Price','Mechanic','In-Store_Shopper','Display # Shelves','In-Store_Shopper_#',
 'Catalogue','Catalogue Flag','Mechanic Type','Display Quality','Display # of Stores','RRP','RRP Percentile','Asp/Unit','%DiscLevel','%Disc(Normalised)']]

dfm11.to_csv('OUTPUT AU Colgate Palmolive Promotional Execution (Data)(2).csv')
dfm11.to_excel('OUTPUT AU Colgate Palmolive Promotional Execution (Data).xlsx',merge_cells=False,startrow=0,sheet_name ='Sheet1')

########## Promotional Laydown Aggregated by Customer ##################
#Melting variables down to one column
dfm10 = dfm10[['Category','Sub Category','Promo Bundle',
               'PPG Code','Promo Group','Year','Customer','Colgate Week','Display','Equivalent Single Price',
               'Mechanic','In-Store_Shopper','Display # Shelves','In-Store_Shopper_#','Catalogue',
               'Mechanic Type','Display Quality','Display # of Stores','SkuCount','Value','Dist_Points',
               'Asp/Unit','%Disc(Normalised)','Mechanic Type']]

dfm10 =pd.melt(dfm10, id_vars=['Category','Sub Category','Promo Bundle',
               'PPG Code','Promo Group','Year','Customer','Colgate Week']
                     , var_name='Data Type', value_name='Value')

#Sorting Data by Subcat, Promo bundle, Prom Start Date
dfm10 = dfm10.sort_values(['Colgate Week','Customer','Year','Category','Sub Category','Promo Group','PPG Code','Data Type'], 
                                      ascending= False, kind ='quicksort',na_position = 'last')

#Pivoting Data so Instore dates are running above the top, thus replicating a normal prom grid
dfm10 = pd.pivot_table(dfm10,values='Value',
                             index=['Category','Sub Category','Promo Bundle',
               'PPG Code','Promo Group','Year','Customer','Data Type'],
                             columns = ['Colgate Week'],aggfunc='first' )  

#### Creating a Fancy formatted excel workbook for weekly calendar #########
dfm10 = dfm10.reset_index()
dfm10=dfm10[['Category','Sub Category','Promo Bundle','PPG Code','Promo Group','Year','Customer',
             'Data Type',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,
             33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]]

dfm10 = dfm10.sort_values(['Year','Sub Category','Promo Group','Customer'], 
                                      ascending= False, kind ='quicksort',na_position = 'last')

dfm10.to_excel('OUTPUT AU Colgate Palmolive Weekly Instore Execution(Data2).xlsx',index= True,merge_cells=False,startrow=2) ## Original unformatted 
