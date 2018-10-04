# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:51:50 2017

@author: Jason Weir
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:13:32 2017

@author: Jason Weir
"""
import pandas as pd     #importing Pandas package to tranform data structures
import numpy as np  

# File names of IRI Master DATA Files

#  CBP Master DATA File (This will be used to track 'future' skus and assign correct PPG Coding to bundles)

FileName6 = '..\Product_Master_Data\SOURCE CBP (AU) Product Data (Sku Level).xlsx'

CBPSkiprow = 27

###Loading CBP Data (No zeros to filter out)
df6 = pd.read_excel(FileName6,'Opr CBR',skiprows=CBPSkiprow,dtype={'EAN/UPC''EAN - Consumer Unit''Unnamed: 3':str})

df6 = df6[['Category','Product Category','Sub Category','Brand / Equity','Sub Brand','Variant','Size','Consumer Lifestage','Product Planning Group','Unnamed: 1','Product', 'Unnamed: 3','EAN - Consumer Unit','Created on', 'Gender','Converted Cs Factor', 'Focus Factory']]

df6.rename(columns={'Brand / Equity' : 'Brand','Unnamed: 1':'Promo Bundle','Product Planning Group' :'PPG Code',
                    'Unnamed: 3':'CP Sku Code','EAN - Consumer Unit':'EAN','Consumer Lifestage' :'Age','Converted Cs Factor':'Units per Case','Focus Factory':'Factory Origin','Product':'SAP Product Name'}, inplace=True)
                        
df6                     = df6[df6.Brand != 'Sard']
df6                     = df6[df6.Brand != 'Spree']
df6                     = df6[df6.Brand != 'Hurricane']
df6                     = df6[df6.Brand != 'Fab']
df6                     = df6[df6.Brand != 'Dynamo/Dinamo']
df6                     = df6[df6.Brand != 'Cold Power']

df6['Age']              = np.where(df6['Variant'].str.contains("Kids") ,'Child','Adult')
df6['Gender']           = np.where(df6['Sub Brand'].str.contains(" Men") ,'Mens','Unisex')
df6['Created on']       = pd.to_datetime(df6['Created on'],format ='%d.%m.%Y',errors='coerce')  

df6['Size']             = np.where((df6['SAP Product Name'].str.contains('4 PACK') & (df6['Size'].str.contains('#'))) ,'4 pk',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('4PK') & (df6['Size'].str.contains('#'))) ,'4 pk',df6['Size'])  
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('700ML')& (df6['Size'].str.contains('#'))),'700 ml',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('475ML')& (df6['Size'].str.contains('#'))),'475 ml',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('80x6') & (df6['Size'].str.contains('#'))),'80 pk',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('80g') & (df6['Size'].str.contains('#'))),'80 gm',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('250 ml')& (df6['Size'].str.contains('#'))),'250 ml',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('250ml')& (df6['Size'].str.contains('#'))),'250 ml',df6['Size'])  
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('250ML')& (df6['Size'].str.contains('#'))),'250 ml',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('250M')& (df6['Size'].str.contains('#'))),'250 ml',df6['Size'])   
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('250mL')& (df6['Size'].str.contains('#'))),'250 ml',df6['Size'])     
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('500ml') & (df6['Size'].str.contains('#'))),'500 ml',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('500mL') & (df6['Size'].str.contains('#'))),'500 ml',df6['Size'])   
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('500ML') & (df6['Size'].str.contains('#'))),'500 ml',df6['Size']) 
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('900ML') & (df6['Size'].str.contains('#'))),'900 ml',df6['Size'])      
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('375ML') & (df6['Size'].str.contains('#'))),'375 ml',df6['Size'])         
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('160g')& (df6['Size'].str.contains('#'))),'320 gm',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('190g')& (df6['Size'].str.contains('#'))),'190 gm',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('80G')& (df6['Size'].str.contains('#'))),'80 gm',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('110g')& (df6['Size'].str.contains('#'))),'110 gm',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('100GM')& (df6['Size'].str.contains('#'))),'100 gm',df6['Size']) 
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('100G ')& (df6['Size'].str.contains('#'))),'100 gm',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('100g')& (df6['Size'].str.contains('#'))),'100 gm',df6['Size']) 
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('120g')& (df6['Size'].str.contains('#'))),'120 gm',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains(' 110G')& (df6['Size'].str.contains('#'))),'110 gm',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('400ML')& (df6['Size'].str.contains('#'))),'400 ml',df6['Size'])  
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('200ML')& (df6['Size'].str.contains('#'))),'200 ml',df6['Size'])   
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('48ML')& (df6['Size'].str.contains('#'))),'48 ml',df6['Size'])    
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('1PK') & (df6['Size'].str.contains('#'))) ,'1 pk',df6['Size'])     
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('2PK') & (df6['Size'].str.contains('#'))) ,'2 pk',df6['Size'])    
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('56G')& (df6['Size'].str.contains('#'))),'56 gm',df6['Size'])   
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('850ml')& (df6['Size'].str.contains('#'))),'48 ml',df6['Size'])  
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('2L')& (df6['Size'].str.contains('#'))),'2 L',df6['Size'])   
   

df6['Size']             = np.where((df6['Promo Bundle'].str.contains(" Pallet ")),'1',df6['Size'])    
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('1pk')& (df6['Size'].str.contains('#'))),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('2pk')& (df6['Size'].str.contains('#'))),'2 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('4 Pack')& (df6['Size'].str.contains('#'))),'4 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('Single')& (df6['Size'].str.contains('#'))),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('3pk')& (df6['Size'].str.contains('#'))),'3 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('4pk')& (df6['Size'].str.contains('#'))),'4 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('6pk')& (df6['Size'].str.contains('#'))),'6 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('1L')& (df6['Size'].str.contains('#'))),'1 L',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('1 Lt')& (df6['Size'].str.contains('#'))),'1 L',df6['Size']) 
   
   
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('A5E-')),'1 pk',df6['Size'])   
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('A6E-')),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('A8E-')),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('A8F-')),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('A9E-')),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('A9N-')),'137 mt',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('A9O-')),'137 mt',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('AAA-')),'100 mt',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('AAC-')),'25 Mt',df6['Size'])      
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('AX5-')),'2 L',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('-Costco ')),'Display Pallet',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('-Coscto ')),'Display Pallet',df6['Size'])      
df6['Size']             = np.where((df6['Promo Bundle'].str.contains(" Prepack ")),'Display Pallet',df6['Size']) 
df6['Size']             = np.where((df6['SAP Product Name'].str.contains(' COSTCO ')),'Display Pallet',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("ADE-")),'48 ml',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("ADI-")),'750 ml',df6['Size'])   
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('A8D-')),'1 pk',df6['Size'])  
df6['Size']             = np.where((df6['Promo Bundle'].str.contains('AWP-')),'850 ml',df6['Size'])  



df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AFB-")),'500 ml',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AH3-")),'350 ml',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AH7-")),'350 ml',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AH8-")),'350 ml',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AHB-")),'350 ml',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AM0-")),'1.5 L',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AMZ-")),'1 L',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("ASO-")),'15 Kg',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AB5-")),'180 gm',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("ABI-")),'360 gm',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("ABK-")),'900 gm',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AB0-")),'400 gm',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AB6-")),'360 gm',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A1K-")),'220 gm',df6['Size']) 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A36-")),'220 gm',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("ADZ-")),'420 ml',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AEG-")),'500 ml',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AHH-")),'700 ml',df6['Size'])

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AFR-")),'400 ml',df6['Size'])
    
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("PO (1F)S'GEL MILK&HONEY 1L TWN PALLET")),'Dispaly Pallet',df6['Size'])   
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("PO SG CHERRY BLOSSOM 1L WAVE x12 (SRP)")),'1 L',df6['Size'])     
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("COLD POWER SENSITIVE 2L TL x6")),'2 L',df6['Size'])    
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("COLD POWER SENSITIVE F/L 2L x 6")),'2 L',df6['Size'])       
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("PO SW LHW AB DFNC PMP 250mLx24 (4XSRP)")),'250 ml',df6['Size'])    
   
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("PALM LHW ANTI-BAC 1L TWIN x 3")),'2 L',df6['Size'])    
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("PALM LHW MLK & HNY 1L TWIN x 3")),'2 L',df6['Size']) 
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("PON LHW SEA MNRLS RFL 1L TWIN x 3")),'2 L',df6['Size']) 
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("PON LHW LIME REFILL 1L TWIN x 3")),'2 L',df6['Size']) 

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("PO LHW AB LIME REFILL 1L TRIPLE x 4")),'3 L',df6['Size'])    
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("PO LHW ALOE VERA REFILL 1L TRIPLE x 4")),'3 L',df6['Size']) 

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("COLD POWER & CUDDLY 3.6KG X3")),'3.6 Kg',df6['Size']) 

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("FAB SUNSHINE FRESH O/F 500g x 12")),'500 gm',df6['Size']) 

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("DYNAMO WITH SARD ULTRA F/L 900ml x 8")),'900 ml',df6['Size']) 

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("Duraphat Varnsh Single Dose x600 (12x50)")),'10 ml',df6['Size']) 
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CUDDLY COLLECTIONS CHERRY 900ML X8 (SRP)")),'900 ml',df6['Size']) 
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CUDDLY COLLECTIONS JASMINE 900ML X8(SRP)")),'900 ml',df6['Size']) 


df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTP OPTIC WHITE (SRP) 110g x 72")),'110 gm',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A27-")),'240 gm',df6['Size']) 

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("COL TP TOTAL PUMP 120g x 24 (SRP)")),'120 gm',df6['Size']) 

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTP OPTIC WHITE (SRP) 160g x 72")),'160 gm',df6['Size']) 

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTP OPTIC WHITE (SRP) 140g x 72")),'140 gm',df6['Size']) 

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("COLGATE GRF TWIN 175G x 36")),'350 gm',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A18-")),'1 pk',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A4B-")),'1 pk',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A4I-")),'6 pk',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A4L-")),'1 pk',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A4N-")),'2 pk',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A4U-")),'1 pk',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A4W-")),'1 pk',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A5G-")),'1 pk',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A65-")),'1 pk',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A66-")),'2 pk',df6['Size']) 

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A8E-")),'1 pk',df6['Size'])
 
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AA5-")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AAN-")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB PRO CLINICAL C350 x 2")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB PRO CLINICAL C600 x 2")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB PRO CLINICAL C200 x 2")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB PRO CLINICAL A1500 x 2")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A0K-")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A68-")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A9S-")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A67-")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A6Z-")),'2 pk',df6['Size'])

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A9T-")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1224955")),'40 pk',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AU00310A")),'40 pk',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AJAX SnW WIPES D/BLENDS 40x10(SRP)")),'40 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB PRO CLINICAL T/CLEAN 2PK REFILL X 20")),'2 pk',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB PRO CLINICAL 360 WHITE 2PK REFIL X20")),'2 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CPTB MINIONS INTERACTIVE 1PK X 6")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTBM FLOSS TIP MED 1PK (SRP) x 96")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTBM FLOSS TIP SOFT 1PK (SRP) x 96")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTBM 360 Charcoal UHX 1PK_SPC*96")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB SLIM SOFT UCH PERSONALISED X 144")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB PRO CLINICAL 150 X 12")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB PRO CLINICAL BLACK C250+ X 2")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB PRO CLINICAL C250+ x 2")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB PRO CLINICAL WHITENING C350 x 2")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTB PRO CLINICAL A1500 x 2")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("COL TP TOTAL PUMP 120g x 24 (SRP)")),'120 gm',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("COL TP (Aldi) TRIPLE ACTION 160g TWINx18")),'320 gm',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CLG WTNG+T/TAR 120g TWIN x 18 (Aldi)")),'240 gm',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("COL TP WHIT TARTAR CTR 120g Twin x18 SRP")),'240 gm',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CLG T/P TOTAL PROOF 100g x 72 (SRP)")),'100 gm',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTP OPTIC WHITE (SRP) 110g x 72")),'110 gm',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTBM 360 Charcoal UHX 1PK_SPC*96")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTBM EXTRA_CLEAN FH M 2PK SPC*144")),'2 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTBM CAVITY PROTECTION  SOFT 1pk x96_SPC")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTBM CAVITY PROTECTION MED 1pk x 96_spc")),'1 pk',df6['Size'])

df6['Promo Bundle']    = np.where((df6['CP Sku Code'].str.contains("1225638")),'A2O-Colgate Optic White (Prem) TP 85gm',df6['Promo Bundle'])



df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTBM SLIM SOFT 12 CH X 2PK_SPC x 192")),'2 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("CTBPWR 360 Opt White Soft Twin Refill x6")),'2 pk',df6['Size'])

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A6K-Colgate Pro Clinical C 250")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("POC TB TOTAL PROF UCH X 72")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['SAP Product Name'].str.contains("Duraphat Varnsh Single Dose x600 (12x50)")),'10 ml',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("SANITISER CHECK OUT TRAY X 2")),'Display Pallet',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("PO SW LHW AB DFNC PMP 250mLx24 (4XSRP)")),'250 ml',df6['Size'])
df6['Size']             = np.where((df6['SAP Product Name'].str.contains("AJAX SnW WIPES D/BLENDS 40x10(SRP)")),'40 pk',df6['Size'])


df6['Size']             = np.where((df6['SAP Product Name'].str.contains('KIT 2mm X 72')),'6 pk',df6['Size'])  
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('KIT 4mm X 72')),'6 pk',df6['Size'])   
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('KIT 5mm X 72')),'6 pk',df6['Size'])  
df6['Size']             = np.where((df6['SAP Product Name'].str.contains('KIT 6mm X 72')),'6 pk',df6['Size']) 

df6['Size']             = np.where((df6['CP Sku Code'].str.contains('1224368')),'1 pk',df6['Size'])  
df6['Size']             = np.where((df6['CP Sku Code'].str.contains('183900529')),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains('1225656')),'1 L',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225470")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225469")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225724")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225342")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225341")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1224840")),'375 ml',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AU00384A")),'475 ml',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225665")),'900 ml',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225667")),'900 ml',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225019")),'2 pk',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225018")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225017")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1507117")),'250 ml',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("183902001")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1052169")),'2 pk',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225443")),'270 gm',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1223571")),'10 pk',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225771")),'120 gm',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1537827")),'320 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225770")),'100 gm',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1224737")),'103 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1224871")),'103 gm',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225291")),'95 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225459")),'95 gm',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225293")),'140 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225461")),'140 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225528")),'140 gm',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225077")),'110 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225079")),'110 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225078")),'110 gm',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225207")),'Display Pallet',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225595")),'320 gm',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AU00534A")),'Display Pallet',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("733853")),'10 ml',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225474")),'1.5 L',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1224837")),'1.5 L',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AU00524A")),'Display Pallet',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AU00509A")),'Display Pallet',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AU00533A")),'Display Pallet',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AU00504A")),'2 L',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("1225595")),'240 gm',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("TH02771A")),'120 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("TH02957A")),'200 gm',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A29-")),'115 gm',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A1S-")),'200 gm',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A1R-")),'220 gm',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A1N-")),'115 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("TH02958A")),'200 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("TH02813A")),'200 gm',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A1M-")),'40 gm',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A0I-")),'40 gm',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A0H-")),'130 gm',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A6A-")),'2 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A69-")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A84-")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A84-")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AU00605A")),'675 ml',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AU00610A")),'675 ml',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("AKY-")),'1.3 L',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A5V-")),'1 pk',df6['Size'])
df6['Size']             = np.where((df6['Promo Bundle'].str.contains("A5W-")),'1 pk',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("CN07302A")),'170 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("TH02047A")),'190 gm',df6['Size'])

df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AU00602A")),'85 gm',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("AU00618A")),'25 Mt',df6['Size'])
df6['Size']             = np.where((df6['CP Sku Code'].str.contains("TH03071A")),'180 gm',df6['Size'])


df6['Promo Bundle'] = np.where((df6['EAN'].str.contains("9300632085507")),'A2B-Colgate Total (Premium) TP 170/190gm',df6['Promo Bundle'])
df6['Promo Bundle'] = np.where((df6['EAN'].str.contains("9300632085187")),'A2A-Colgate Total (Premium) TP 100/110gm',df6['Promo Bundle'])
df6['Promo Bundle'] = np.where((df6['EAN'].str.contains("9300632083473")),'A2I-Colgate Optic White (Base) TP 95gm',df6['Promo Bundle'])


df6['Uom']              =df6['Size'].str.split(' ').str[1]
df6['Size']             =df6['Size'].str.split(' ').str[0]

df6['Uom']             = np.where(df6['Uom'].str.contains("GR") ,'gm',df6['Uom'])
df6['Uom']             = np.where(df6['Uom'].str.contains("ML") ,'ml',df6['Uom'])
df6['Uom']             = np.where(df6['Uom'].str.contains("PC") ,'pk',df6['Uom'])
df6['Uom']             = np.where(df6['Uom'].str.contains("LT") ,'L' ,df6['Uom'])
df6['Uom']             = np.where(df6['Uom'].str.contains("ME") ,'ml',df6['Uom'])
df6['Uom']             = np.where(df6['Uom'].str.contains("MR") ,'Mt',df6['Uom'])
df6['Uom']             = np.where(df6['Uom'].str.contains("CT") ,'pk',df6['Uom'])
df6['Uom']             = np.where(df6['Uom'].str.contains("KG") ,'Kg',df6['Uom'])
df6['Uom']             = np.where(df6['Uom'].str.contains("MM") ,'ml',df6['Uom'])
df6['Uom']             = np.where(df6['Uom'].str.contains("mt") ,'Mt',df6['Uom'])
df6['Uom']             = np.where(df6['Uom'].str.contains("Pallet") ,'Unit/Pallet',df6['Uom'])

df6['Size']            = np.where((df6['Size'].str.contains("Display")),'1',df6['Size'])

df6['Promo Bundle']    = np.where((df6['CP Sku Code'].str.contains('1225527')),'A2N-Colgate Optic White (Base) TP 140gm',df6['Promo Bundle'])


df6['Size_Combined']   =df6['Size'] +df6['Uom'] 
df6['Manufacturer']    ='Colgate Palmolive' 

df6['Promo Bundle1']   = df6['Promo Bundle'].str[4:]
df6['PPG Code']        = df6['PPG Code'].str[9:]
df6['PPG Code+Name']   = df6['Promo Bundle']

df6.rename(columns={'Promo Bundle' : 'PPG Name','Promo Bundle1' :'Promo Bundle'  }, inplace=True)




df6   = df6[['Category','Manufacturer','Product Category','Sub Category','Brand','Sub Brand','Variant','Gender' ,'Age','Size' ,'Uom','Size_Combined','PPG Name','PPG Code','Promo Bundle','PPG Code+Name', 'EAN','Created on','CP Sku Code','SAP Product Name','Units per Case','Factory Origin' ]]

#df6   = df6.reindex(columns=['Category','Product Category','Sub Category','Brand','Sub Brand','Variant','Gender' ,'Age','Size' ,'Uom','Promo Bundle', 'EAN','Created on','CP Sku Code','SAP Product Name'])

df6 =  df6.sort_values(['Created on' ], ascending=[False], inplace=False)


df6.to_csv('OUTPUT CBP (AU) Product Master (CP Sku Level).csv',index= False) ### Producing Cleaned CP Sku Level Output



df6grouped = df6.groupby(['EAN'],as_index=False).first()  ### Grouping at EAN level

df6grouped   = df6grouped[['Category','Product Category','Sub Category','Manufacturer','Brand','Sub Brand','Variant','Gender' ,'Age','Size' ,'Uom','Size_Combined','PPG Code','Promo Bundle','PPG Code+Name', 'EAN','Created on','SAP Product Name','Units per Case' ,'Factory Origin']]

df6grouped =  df6grouped.sort_values(['Category','Product Category','Sub Category','Brand','Sub Brand','Variant','Gender' ,'Age','Size' ,'Uom','PPG Code','Promo Bundle', 'EAN','SAP Product Name' ,'Units per Case'], ascending=[True,False,False,False,False,False,False,False,False,False,True,True,True,True,True], inplace=False)
df6grouped =  df6grouped[df6grouped.EAN != '#']    


df6grouped.to_csv('OUTPUT CBP (AU) Product Master (EAN Level).csv',index= False)

df6grouped2 = df6.groupby(['PPG Code'],as_index=False).first()  ### Grouping at EAN level

df6grouped2   = df6grouped2[['Category','Product Category','Sub Category','Brand','Manufacturer','Sub Brand','Gender' ,'Age','Size' ,'Uom','Size_Combined','PPG Code','Promo Bundle','PPG Code+Name','Units per Case' ,'Factory Origin']]
df6grouped2                    = df6grouped2[df6grouped2['PPG Code'] != '#']  
df6grouped2.to_csv('OUTPUT CBP (AU) Product Master (PPG Level).csv',index= False)