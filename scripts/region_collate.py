import pandas as pd
import os
import os.path

def returnDataFrame(root, plant_name):
    df = pd.read_csv(os.path.join(root, 'CorpusNetwork.csv'))
    df.insert(0, 'Plant', plant_name)
    return df

dir = 'I:\Data Science Lab\LERs Data for Network Construction'
region_1 = ["Beaver Valley","Calvert Cliffs","FitzPatrick","Ginna","Hope Creek","Indian Point","Limerick","Millstone","Nine Mile Point","Peach Bottom","Pilgrim","Salem","Seabrook","Susquehanna","Three Mile Island"]
region_2 =["Browns Ferry","Brunswick","Catawba","Crystal River","Farley","Harris","Hatch","McGuire","North Anna","Oconee","Robinson","Saint Lucie","Sequoyah","Summer","Surry","Turkey Point","Vogtle","Watts Bar"]
region_3 = ["Braidwood","Byron","Clinton","Davis-Besse","D.C. Cook","Dresden","Duane Arnold","Fermi","La Salle","Monticello","Palisades","Perry","Point Beach","Prairie Island","Quad Cities"]
region_4 = ["Arkansas","Callaway","Columbia Generating Station","Comanche Peak","Cooper","Diablo Canyon","Fort Calhoun","Grand Gulf","Palo Verde","River Bend","South Texas","Waterford","Wolf Creek"]

regions = {'region 1' : region_1, 'region 2' : region_2, 'region 3' : region_3, 'region 4' : region_4}
print(regions)

r = []
r.extend(region_1)
r.extend(region_2)
r.extend(region_3)
r.extend(region_4)
#print(r)
#print(os.listdir(dir))
# for folder in os.listdir(dir):
#     for x in regions.keys():
#         os.mkdir(dir+'/'+folder+'/'+x)
region_1_data = []
region_2_data = []
region_3_data = []
region_4_data = []
region_1_data_new = []
region_2_data_new = []
region_3_data_new = []
region_4_data_new = []

for root, dirs, files in os.walk(dir):
    #print('Root :',root,' dirs : ',dirs, ' files :',files)

    if dirs and dirs[0] == 'CB-Results':
        print('Root :', root, ' dirs : ', dirs, ' files :', files)
        plant_name = root.split('\\')[-1:][0]
        year = root.split('\\')[-2]
        if plant_name in region_1:
            region_1_data.append(returnDataFrame(root, plant_name)) if year == '1998-2004 CSV plant wise' else region_1_data_new.append(returnDataFrame(root, plant_name))
            #print("Plant Name for Region 1: ", plant_name)
        elif plant_name in region_2:
            region_2_data.append(returnDataFrame(root, plant_name)) if year == '1998-2004 CSV plant wise' else region_2_data_new.append(returnDataFrame(root, plant_name))
            #print("Plant Name for Region 2: ", plant_name)
        elif plant_name in region_3:
            region_3_data.append(returnDataFrame(root, plant_name)) if year == '1998-2004 CSV plant wise' else region_3_data_new.append(returnDataFrame(root, plant_name))
            #print("Plant Name for Region 3: ", plant_name)
        else:
            region_4_data.append(returnDataFrame(root, plant_name)) if year == '1998-2004 CSV plant wise' else region_4_data_new.append(returnDataFrame(root, plant_name))
            #print("Plant Name for Region 4: ", plant_name)

region_1_file = pd.concat(region_1_data)
region_2_file = pd.concat(region_2_data)
region_3_file = pd.concat(region_3_data)
region_4_file = pd.concat(region_4_data)
region_1_file_new = pd.concat(region_1_data_new)
region_2_file_new = pd.concat(region_2_data_new)
region_3_file_new = pd.concat(region_3_data_new)
region_4_file_new = pd.concat(region_4_data_new)

region_1_file.to_csv(os.path.join(dir, "region_1_old.csv"))
region_2_file.to_csv(os.path.join(dir, "region_2_old.csv"))
region_3_file.to_csv(os.path.join(dir, "region_3_old.csv"))
region_4_file.to_csv(os.path.join(dir, "region_4_old.csv"))
region_1_file_new.to_csv(os.path.join(dir, "region_1_new.csv"))
region_2_file_new.to_csv(os.path.join(dir, "region_2_new.csv"))
region_3_file_new.to_csv(os.path.join(dir, "region_3_new.csv"))
region_4_file_new.to_csv(os.path.join(dir, "region_4_new.csv"))





