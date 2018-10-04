# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:13:32 2017

@author: Jason Weir
"""
import pandas as pd     #importing Pandas package to tranform data structures
import numpy as np      #importing Numpy package to wrangle and clean data
# File names of IRI Master DATA Files

f1 = 'O:\My Drive\Colgate_Australia\Analytics_Development\Data_Governance\Master_Data\Product_Master_Data\SOURCE IRI AUNZ Fabric Conditioners Product Master.xlsx'
f2 = 'O:\My Drive\Colgate_Australia\Analytics_Development\Data_Governance\Master_Data\Product_Master_Data\SOURCE IRI AUNZ Household Cleaners Product Master.xlsx'
f3 = 'O:\My Drive\Colgate_Australia\Analytics_Development\Data_Governance\Master_Data\Product_Master_Data\SOURCE IRI AUNZ Manual Dish Care Product Master.xlsx'
f4 = 'O:\My Drive\Colgate_Australia\Analytics_Development\Data_Governance\Master_Data\Product_Master_Data\SOURCE IRI AUNZ Oral Care Product Master.xlsx'
f5 = 'O:\My Drive\Colgate_Australia\Analytics_Development\Data_Governance\Master_Data\Product_Master_Data\SOURCE IRI AUNZ Personal Care Product Master.xlsx'

IRISkiprow = 1

### Loading HOME CARE  ####

df1 = pd.read_excel(f1,'Sheet1',skiprows=IRISkiprow,dtype={'EAN''Size':str})

df1.rename(columns={'Packsize':'Size Range', 
                    'Fragrance':'Variant', 
                    'Washes':'# Uses',
                    'Packtype':'Pack Intention',
                    'Subcategory':'Packtype',
                    'Bonuspack':'Bonus Pack',
                    'Subbrand':'Sub Brand',
                    }, inplace=True)

df1['Category']         = 'Home Care'
df1['Product Category'] = 'Fabric Conditioner'
df1['Sub Category']     = 'Fabric Conditioner'
df1['Age']              = 'Adult'
df1['Form']             = np.where(df1['Size Range'].str.contains(" Sheets") ,'Sheets','Liquid')
df1['Sub Segment']      = 'Still to be added'
df1['Multi Pack']       = 'Single_Pack'


######################################################################################

df_filtered2 = pd.read_excel(f2,'Sheet1',skiprows=IRISkiprow,dtype={'EAN''Size':str}).assign(Include ='Yes')
#df_filtered2 = df2[df2['Sum 4 Periods'] != 0.0]
df_filtered2 = df_filtered2.drop(['Market', 'Groups Total', 'Level', 
                                  'Total', 'Gst', 'Client','Woolworths Commodity'
                                  ,'Coles Commodity','Woolworths Reference',
                                  'Metcash Reference','Progressive NZ Reference'
                                  ,'Standard Launched In','Standard Totals' 
                                  ,'Environmental','Bathroom Subsegment', 'Launched In Cal Qtr'
                                  ,'Woolworths Assortment Code','Colesrange','Wwrange','Global'
                                  ,'Antibacterial','Wipes Packsizes','Pack_config','Product.1'], axis=1) ## Droping unessesary columns

df_filtered2['Category']         = 'Home Care'
df_filtered2['Product Category'] = 'Cleaners'
df_filtered2['Sub Category']     = 'Cleaners'  ## Adding nesseseary columns
df_filtered2['Age']              = 'Adult'
df_filtered2['Sub Segment']      = 'Still to be added'
df_filtered2['Multi Pack']       = np.where(df_filtered2['Product'].str.contains(" 2x") ,'Multi-Pack','Standard-Pack')
df_filtered2['Bonus Pack']        = 'Standard Pack'

df_filtered2.rename(columns={'Packsize':'Size Range', 'Fragrance':'Variant','Primary_refill':'Pack Intention','Bonuspack':'Bonus Pack','Subbrand':'Sub Brand',
                             'Sum 4 Periods': 'Units','Sum 4 Periods.1': '$ASP','Sum 4 Periods.2':'Base Price'}, inplace=True)

##########################################################################################

df_filtered3 = pd.read_excel(FileName3,'Sheet1',skiprows=IRISkiprow,dtype={'EAN''Size':str}).assign(Include ='Yes')
#df_filtered3 = df3[df3['Sum 4 Periods'] != 0.0]
df_filtered3 = df_filtered3.drop(['Market', 'Groups Total', 'Level', 
                                  'Total', 'Gst', 'Client','Woolworths Commodity'
                                  ,'Coles Commodity','Woolworths Reference',
                                  'Metcash Reference','Progressive NZ Reference'
                                  ,'Standard Launched In','Standard Totals' 
                                  ,'Environmental', 'Launched In Cal Qtr'
                                  ,'Colesrange','Antibacterial',
                                  'Cp_subcategory','Colesrange'
                                  ,'Wwrange','Woolworths Subcommodity','Coles Subcommodity','Product.1'], axis=1) ## Droping unessesary columns

df_filtered3.rename(columns={'Packsize':'Size Range', 'Fragrance':'Variant','Bonuspack':'Bonus Pack','Subsegment' :'Sub Segment','Subbrand':'Sub Brand',
                             'Sum 4 Periods': 'Units','Sum 4 Periods.1': '$ASP','Sum 4 Periods.2':'Base Price'}, inplace=True)

df_filtered3['Category']         = 'Home Care'
df_filtered3['Product Category'] = 'Dish'
df_filtered3['Sub Category']     = 'Dish Hand'
df_filtered3['Age']              = 'Adult'
df_filtered3['Multi Pack']       = 'Standard Pack'
df_filtered3['Pack Intention']   = np.where(df_filtered3['Product'].str.contains(" Rfl") ,'Refill','Primary')

##############################################################################################

df_filtered5 = pd.read_excel(FileName5,'Sheet1',skiprows=IRISkiprow,dtype={'EAN''Size':str})
#df_filtered5 = df5[df5['Sum 4 Periods'] != 0.0]
df_filtered5 = df_filtered5.drop(['Market', 'Groups Total', 'Level', 
                                  'Total', 'Gst', 'Client','Woolworths Commodity'
                                  ,'Coles Commodity','Woolworths Reference',
                                  'Metcash Reference','Progressive NZ Reference'
                                  ,'Standard Launched In','Standard Totals' 
                                  ,'Woolworths Assortment Code'
                                  ,'Hairtype','Product.1',
                                  'Wool_com','Coles Code','Price'], axis=1) ## Droping unessesary columns

df_filtered5.rename(columns={'Packsize':'Size Range', 'Category' : 'Product Category' ,'Subcategory' : 
                            'Sub Category','Subsegment' :'Sub Segment','Subbrand':'Sub Brand',
                             'Sum 4 Periods': 'Units','Sum 4 Periods.1': '$ASP','Sum 4 Periods.2':'Base Price'}, inplace=True)

df_filtered5['Category']         = 'Personal Care'
df_filtered5['Age']              = 'Adult'
df_filtered5['Multi Pack']       =  np.where(df_filtered5['Bonus Pack'].str.contains("Normal Pack") ,'Single-Pack','Multi-Pack')
df_filtered5['Multi Pack']       =  np.where(df_filtered5['Size Range'].str.contains("Bar Single Packs") ,'Single_Pack',df_filtered5['Multi Pack'] )
df_filtered5['Multi Pack']       =  np.where(df_filtered5['Size Range'].str.contains("Bar Twin Packs") ,'Multi_Pack',df_filtered5['Multi Pack'] )
df_filtered5['Multi Pack']       =  np.where(df_filtered5['Size Range'].str.contains("Bar Three Packs") ,'Multi_Pack',df_filtered5['Multi Pack'] )
df_filtered5['Multi Pack']       =  np.where(df_filtered5['Size Range'].str.contains("Bar Four Packs") ,'Multi_Pack',df_filtered5['Multi Pack'] )
df_filtered5['Multi Pack']       =  np.where(df_filtered5['Size Range'].str.contains("Bar Five Packs") ,'Multi_Pack',df_filtered5['Multi Pack'] )
df_filtered5['Multi Pack']       =  np.where(df_filtered5['Size Range'].str.contains("Bar Six Packs") ,'Multi_Pack',df_filtered5['Multi Pack'] )
df_filtered5['Multi Pack']       =  np.where(df_filtered5['Size Range'].str.contains("Bar Eight Packs") ,'Multi_Pack',df_filtered5['Multi Pack'] )

df_filtered5['Variant']          = 'Still to be added'

df_filtered5['Uom']              = 'Still to be added'
df_filtered5['Uom']              = np.where(df_filtered5['Size Range'].str.contains("ml") ,'ml',df_filtered5['Uom'] )
df_filtered5['Uom']              = np.where(df_filtered5['Product'].str.contains("pk") ,'pk',df_filtered5['Uom'] )
df_filtered5['Uom']              = np.where(df_filtered5['Product'].str.contains("0g") ,'gm',df_filtered5['Uom'] )
df_filtered5['Uom']              = np.where(df_filtered5['Product'].str.contains("6pc") ,'pk',df_filtered5['Uom'] )
df_filtered5['Uom']              = np.where(df_filtered5['Product'].str.contains("3pc") ,'pk',df_filtered5['Uom'] )
df_filtered5['Uom']              = np.where(df_filtered5['Size Range'].str.contains("Bar Single Packs") ,'gm',df_filtered5['Uom'] )
df_filtered5['Uom']              = np.where(df_filtered5['Size Range'].str.contains("Bar Twin Packs") ,'gm',df_filtered5['Uom'] )
df_filtered5['Uom']              = np.where(df_filtered5['Size Range'].str.contains("Bar Three Packs") ,'gm',df_filtered5['Uom'] )
df_filtered5['Uom']              = np.where(df_filtered5['Size Range'].str.contains("Bar Four Packs") ,'gm',df_filtered5['Uom'] )
df_filtered5['Uom']              = np.where(df_filtered5['Size Range'].str.contains("Bar Five Packs") ,'gm',df_filtered5['Uom'] )
df_filtered5['Uom']              = np.where(df_filtered5['Size Range'].str.contains("Bar Six Packs") ,'gm',df_filtered5['Uom'] )
df_filtered5['Uom']              = np.where(df_filtered5['Size Range'].str.contains("Bar Eight Packs") ,'gm',df_filtered5['Uom'] )


df_filtered5['Form']             =  np.where(df_filtered5['Sub Category'].str.contains("Bar Soap") ,'Solid','Liquid')
df_filtered5['Pack Intention']   =  np.where(df_filtered5['Product'].str.contains(" Rfl") ,'Refill','Primary')

###############################################################################################

df_filtered4 = pd.read_excel(FileName4,'Sheet1',skiprows=IRISkiprow,dtype={'EAN' 'Size':str})
#df_filtered4 = df4[df4['Sum 4 Periods'] != 0.0]
df_filtered4 = df_filtered4.drop(['Market', 'Groups Total', 'Level', 
                                  'Total', 'Gst', 'Client','Woolworths Commodity'
                                  ,'Coles Commodity','Woolworths Reference',
                                  'Metcash Reference','Progressive NZ Reference'
                                  ,'Standard Launched In','Standard Totals' 
                                  ,'Whitening','Brush Price','Brush Head','Brush Indicator',
                                  'Woolworths Assortment Code','Fac_vol','Product.1'], axis=1) ## Droping unessesary columns

df_filtered4.rename(columns={'Category' : 'Sub Category' , 'Segment' : 'Product Category','Minor Segment':'Segment',
                             'Packsize':'Size Range','Subsegment' : 'Sub Segment','Flavour' : 'Variant','Subbrand':'Sub Brand',
                             'Sum 4 Periods': 'Units','Sum 4 Periods.1': '$ASP','Sum 4 Periods.2':'Base Price'}, inplace=True)

df_filtered4['Category']         = 'Oral Care'
df_filtered4['Uom']              = 'Still to be added'
df_filtered4['Uom']              = np.where(df_filtered4['Size Range'].str.contains("pk") ,'pk',df_filtered4['Uom'] )
df_filtered4['Uom']              = np.where(df_filtered4['Size Range'].str.contains("g") ,'gm',df_filtered4['Uom'] )
df_filtered4['Uom']              = np.where(df_filtered4['Size Range'].str.contains("m") ,'mt',df_filtered4['Uom'] )
df_filtered4['Uom']              = np.where(df_filtered4['Size Range'].str.contains("ml") ,'ml',df_filtered4['Uom'] )
df_filtered4['Uom']              = np.where(df_filtered4['Size Range'].str.contains("Packsize") ,'pk',df_filtered4['Uom'] )

df_filtered4['Bonus Pack']       = 'Still to be added'
df_filtered4['Form2']            = np.where(df_filtered4['Form'] is not None, 
                                    df_filtered4['Brush Bristle'], df_filtered4['Form'])
df_filtered4['Form3']            = df_filtered4['Form' ].map(str) + df_filtered4['Form2'].map(str)
df_filtered4['Form3']            = (df_filtered4['Form3'].replace({'nan':''}, regex=True))
df_filtered4['Form']             = df_filtered4['Form3']  

df_filtered4 = df_filtered4.drop(['Brush Bristle','Form3','Form2'], axis=1)

## Appending all data together & Cleaning up UOM metric and adding Promo Bundle Metric

frames = [df_filtered1,df_filtered2,df_filtered3,df_filtered4,df_filtered5]

ConcatFrames=  pd.concat(frames)

ConcatFrames = ConcatFrames[['Category', 'Product Category','Sub Category','Segment','Sub Segment','Manufacturer','Brand',
                             'Sub Brand','Variant','Product','EAN','Azteccode','Tag','Size','Uom','Size Range','Bonus Pack',
                             'Private Label','Packtype','Pack Intention','New Item','Include','Multi Pack','Form','Units','$ASP','Base Price']]


ConcatFrames['Uom'] =  np.where(ConcatFrames['Uom'].str.contains("Millilitre") ,'ml',ConcatFrames['Uom'])
ConcatFrames['Uom'] =  np.where(ConcatFrames['Uom'].str.contains("Litre") ,'ml',ConcatFrames['Uom'])
ConcatFrames['Uom'] =  np.where(ConcatFrames['Uom'].str.contains("Kilogram") ,'gm',ConcatFrames['Uom'])
ConcatFrames['Uom'] =  np.where(ConcatFrames['Uom'].str.contains("Pack") ,'pk',ConcatFrames['Uom'])
ConcatFrames['Uom'] =  np.where(ConcatFrames['Uom'].str.contains("Misc") ,'pk',ConcatFrames['Uom'])
ConcatFrames['Uom'] =  np.where(ConcatFrames['Uom'].str.contains("Gram") ,'gm',ConcatFrames['Uom'])


ConcatFrames['Promo Bundle'] = 'Still to be Added'
ConcatFrames['Promo Bundle'] = ConcatFrames['Sub Brand']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom']

ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Product Category'].str.contains("Fabric Conditioner") ,ConcatFrames['Sub Brand']+' '+ConcatFrames['Packtype']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])

ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Product Category'].str.contains("Cleaners") ,ConcatFrames['Sub Brand']+' '+ConcatFrames['Form']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])

ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Product Category'].str.contains("Dish") ,ConcatFrames['Sub Brand']+' '+ConcatFrames['Segment']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])

ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Sub Brand'].str.contains("Andrew Collinge") ,ConcatFrames['Brand']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])
ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Sub Brand'].str.contains("Edward Beale Smooth Control") ,ConcatFrames['Brand']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])
ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Sub Brand'].str.contains("Edward Beale Hydra Lock") ,ConcatFrames['Brand']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])
ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Sub Brand'].str.contains("Edward Beale Intense Repair") ,ConcatFrames['Brand']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])
ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Sub Brand'].str.contains("Edward Beale Smooth Control") ,ConcatFrames['Brand']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])
ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Sub Brand'].str.contains("Head & Shoulders") ,ConcatFrames['Brand']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])
ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Sub Brand'].str.contains("Pantene") ,ConcatFrames['Brand']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])
ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Sub Brand'].str.contains("Tresemme") ,ConcatFrames['Brand']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])
ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Segment'].str.contains("Liq Foam") ,ConcatFrames['Sub Brand']+' '+ConcatFrames['Segment']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])
ConcatFrames['Promo Bundle'] =  np.where(ConcatFrames['Category'].str.contains("Oral Care") ,ConcatFrames['Sub Brand']+" "+ConcatFrames['Size'].map(str)+ConcatFrames['Uom'],ConcatFrames['Promo Bundle'])


### Re-coding IRI data to Product Category & Sub-Cat definitions ###

ConcatFrames['Sub Category'] = np.where((ConcatFrames['Product Category'].str.contains('Cleaners') & (ConcatFrames['Product'].str.contains('Wipes'))),'Cleaners Scourer',ConcatFrames['Sub Category'])
ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Segment'].str.contains('Glass') ,'Cleaners Glass',ConcatFrames['Sub Category'])
#
ConcatFrames['Sub Category'] = np.where((ConcatFrames['Product Category'].str.contains('Cleaners') & (ConcatFrames['Product'].str.contains('Cream'))),'Cleaners Scourer',ConcatFrames['Sub Category'])
#
ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Segment'].str.contains('Conditioner') ,'Conditioner',ConcatFrames['Sub Category'])
ConcatFrames['Sub Category'] = np.where((ConcatFrames['Segment'].str.contains('Styling Aids') & (ConcatFrames['Product Category'].str.contains('Hair Care'))),'Hair Care Styling Ai',ConcatFrames['Sub Category'])
ConcatFrames['Sub Category'] = np.where((ConcatFrames['Segment'].str.contains('Treatment') & (ConcatFrames['Product Category'].str.contains('Hair Care'))),'Hair Care Styling Ai',ConcatFrames['Sub Category'])
ConcatFrames['Product Category'] =  np.where(ConcatFrames['Product Category'].str.contains('M/W ') ,'Mouthwash',ConcatFrames['Product Category'])
ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Product Category'].str.contains('Mouthwash') ,'Mouthwash',ConcatFrames['Sub Category'])
#
ConcatFrames['Product Category'] =  np.where(ConcatFrames['Product Category'].str.contains('T/B Manual') ,'Manual TB',ConcatFrames['Product Category'])
#
ConcatFrames['Product Category'] =  np.where(ConcatFrames['Product Category'].str.contains('T/B Powered') ,'Powered TB',ConcatFrames['Product Category'])
#
ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Segment'].str.contains('T/B Battery') ,'Battery TB',ConcatFrames['Sub Category'])
#
ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Segment'].str.contains('T/B Hybrid') ,'Hybrid TB',ConcatFrames['Sub Category'])
#
ConcatFrames['Product Category'] =  np.where(ConcatFrames['Product Category'].str.contains('T/B Other') ,'Manual TB',ConcatFrames['Product Category'])

ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Sub Category'].str.contains('Toothbrush') ,'Manual TB',ConcatFrames['Sub Category'])
#
ConcatFrames['Product Category'] =  np.where(ConcatFrames['Product Category'].str.contains('Floss ') ,'Adjacencies TB',ConcatFrames['Product Category'])
#
ConcatFrames['Product Category'] =  np.where(ConcatFrames['Product Category'].str.contains('Denture ') ,'Adjacencies TB',ConcatFrames['Product Category'])

ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Product Category'].str.contains('Adjacencies TB') ,'Adjacencies TB',ConcatFrames['Sub Category'])
#
ConcatFrames['Product Category'] =  np.where(ConcatFrames['Product Category'].str.contains('Body Cleaning') ,'Body Cleansing',ConcatFrames['Product Category'])
#
ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Sub Category'].str.contains('Shower Gels') ,'Shower Gel',ConcatFrames['Sub Category'])
#
ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Sub Category'].str.contains('Liquid Soaps') ,'Liquid Hand Wash',ConcatFrames['Sub Category'])
#
ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Sub Category'].str.contains('Shp') ,'Shampoo',ConcatFrames['Sub Category'])

ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Sub Category'].str.contains('Bar Soaps') ,'Bar Soap',ConcatFrames['Sub Category'])
#
ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Sub Category'].str.contains('Sanitiser') ,'Hand Sanitiser',ConcatFrames['Sub Category'])

ConcatFrames['Product Category'] =  np.where(ConcatFrames['Product Category'].str.contains('T/P ') ,'Toothpaste',ConcatFrames['Product Category'])

ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Product Category'].str.contains('Toothpaste') ,'Toothpaste',ConcatFrames['Sub Category'])

ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Segment'].str.contains('T/B Electric') ,'Electric TB',ConcatFrames['Sub Category'])

ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Product Category'].str.contains('Toothpaste') ,'Toothpaste',ConcatFrames['Sub Category'])

ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Product Category'].str.contains('Adjacencies TB') ,'Adjacencies TB',ConcatFrames['Sub Category'])

ConcatFrames['Sub Category'] =  np.where(ConcatFrames['Product Category'].str.contains('Ahw') ,'Ahw',ConcatFrames['Sub Category'])

ConcatFrames['Product Category'] =  np.where(ConcatFrames['Sub Category'].str.contains('Ahw') ,'Toothpaste',ConcatFrames['Product Category'])

ConcatFrames['Include'] =  np.where(ConcatFrames['Include'] is None ,'Yes',ConcatFrames['Include'])


ConcatFrames=ConcatFrames.round(2)
ConcatFrames = ConcatFrames.sort_values(['Sub Category','Brand','Size','Base Price','Promo Bundle'], 
                                      ascending= True, kind ='quicksort',na_position = 'last')

ConcatFrames.to_csv('OUTPUT IRI Product Master (EAN Level).csv',index= False)

