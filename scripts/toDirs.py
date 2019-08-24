import shutil
import os

source = '/home/ksr/Downloads/2007_2010 LERs'
dest1 = '/home/ksr/Downloads/2007_2010 LERs/Arkansas'
dest2 = '/home/ksr/Downloads/2007_2010 LERs/Beaver Valley'
dest3 = '/home/ksr/Downloads/2007_2010 LERs/Braidwood'
dest4 = '/home/ksr/Downloads/2007_2010 LERs/Browns Ferry'
dest5 = '/home/ksr/Downloads/2007_2010 LERs/Brunswick'
dest6 = '/home/ksr/Downloads/2007_2010 LERs/Byron'
dest7 = '/home/ksr/Downloads/2007_2010 LERs/Callaway'
dest8 = '/home/ksr/Downloads/2007_2010 LERs/Calvert Cliffs'
dest9 = '/home/ksr/Downloads/2007_2010 LERs/Catawba'
dest10 = '/home/ksr/Downloads/2007_2010 LERs/Clinton'
dest11 = '/home/ksr/Downloads/2007_2010 LERs/Columbia Generating Station'
dest12 = '/home/ksr/Downloads/2007_2010 LERs/Comanche Peak'
dest13 = '/home/ksr/Downloads/2007_2010 LERs/Cooper'
dest14 = '/home/ksr/Downloads/2007_2010 LERs/D.C. Cook'
dest15 = '/home/ksr/Downloads/2007_2010 LERs/Davis-Besse'
dest16 = '/home/ksr/Downloads/2007_2010 LERs/Diablo Canyon'
dest17 = '/home/ksr/Downloads/2007_2010 LERs/Dresden'
dest18 = '/home/ksr/Downloads/2007_2010 LERs/Duane Arnold'
Farley = '/home/ksr/Downloads/2007_2010 LERs/Farley'
Fermi = '/home/ksr/Downloads/2007_2010 LERs/Fermi'
FitzPatrick = '/home/ksr/Downloads/2007_2010 LERs/FitzPatrick'
Ginna = '/home/ksr/Downloads/2007_2010 LERs/Ginna'
dest23 = '/home/ksr/Downloads/2007_2010 LERs/Grand Gulf'
Haddam = '/home/ksr/Downloads/2007_2010 LERs/Haddam Neck'
Harris = '/home/ksr/Downloads/2007_2010 LERs/Harris'
Hatch = '/home/ksr/Downloads/2007_2010 LERs/Hatch'
Hope = '/home/ksr/Downloads/2007_2010 LERs/Hope Creek'
Humboldt = '/home/ksr/Downloads/2007_2010 LERs/Humboldt Bay'
Indian = '/home/ksr/Downloads/2007_2010 LERs/Indian Point'
Kewaunee = '/home/ksr/Downloads/2007_2010 LERs/Kewaunee'
La = '/home/ksr/Downloads/2007_2010 LERs/La Crosse'
LaSalle = '/home/ksr/Downloads/2007_2010 LERs/LaSalle'
Limerick = '/home/ksr/Downloads/2007_2010 LERs/Limerick'
Maine = '/home/ksr/Downloads/2007_2010 LERs/Maine Yankee'
McGuire = '/home/ksr/Downloads/2007_2010 LERs/McGuire'
Millstone = '/home/ksr/Downloads/2007_2010 LERs/Millstone'
Monticello = '/home/ksr/Downloads/2007_2010 LERs/Monticello'
Nine = '/home/ksr/Downloads/2007_2010 LERs/Nine Mile Point'
North = '/home/ksr/Downloads/2007_2010 LERs/North Anna'
Oconee = '/home/ksr/Downloads/2007_2010 LERs/Oconee'
Oyster = '/home/ksr/Downloads/2007_2010 LERs/Oyster Creek'
Palisades = '/home/ksr/Downloads/2007_2010 LERs/Palisades'
Palo = '/home/ksr/Downloads/2007_2010 LERs/Palo Verde'
Peach = '/home/ksr/Downloads/2007_2010 LERs/Peach Bottom'
Perry = '/home/ksr/Downloads/2007_2010 LERs/Perry'
Pilgrim = '/home/ksr/Downloads/2007_2010 LERs/Pilgrim'
Point = '/home/ksr/Downloads/2007_2010 LERs/Point Beach'
Prairie = '/home/ksr/Downloads/2007_2010 LERs/Prairie Island'
Quad = '/home/ksr/Downloads/2007_2010 LERs/Quad Cities'
Rancho = '/home/ksr/Downloads/2007_2010 LERs/Rancho Seco'
River = '/home/ksr/Downloads/2007_2010 LERs/River Bend'
Robinson = '/home/ksr/Downloads/2007_2010 LERs/Robinson'
Saint = '/home/ksr/Downloads/2007_2010 LERs/Saint Lucie'
Salem = '/home/ksr/Downloads/2007_2010 LERs/Salem'
San = '/home/ksr/Downloads/2007_2010 LERs/San Onofre'
Seabrook = '/home/ksr/Downloads/2007_2010 LERs/Seabrook'
Sequoyah = '/home/ksr/Downloads/2007_2010 LERs/Sequoyah'
Shoreham = '/home/ksr/Downloads/2007_2010 LERs/Shoreham'
South = '/home/ksr/Downloads/2007_2010 LERs/South Texas'
Summer = '/home/ksr/Downloads/2007_2010 LERs/Summer'
Surry = '/home/ksr/Downloads/2007_2010 LERs/Surry'
Susquehanna = '/home/ksr/Downloads/2007_2010 LERs/Susquehanna'
Three = '/home/ksr/Downloads/2007_2010 LERs/Three Mile Island'
Trojan = '/home/ksr/Downloads/2007_2010 LERs/Trojan'
Turkey = '/home/ksr/Downloads/2007_2010 LERs/Turkey Point'
Vermont = '/home/ksr/Downloads/2007_2010 LERs/Vermont Yankee'
Vogtle = '/home/ksr/Downloads/2007_2010 LERs/Vogtle'
Waterford = '/home/ksr/Downloads/2007_2010 LERs/Waterford'
Watts = '/home/ksr/Downloads/2007_2010 LERs/Watts Bar'
Wolf = '/home/ksr/Downloads/2007_2010 LERs/Wolf Creek'
Yankee_Rowe = '/home/ksr/Downloads/2007_2010 LERs/Yankee_Rowe'
Zion = '/home/ksr/Downloads/2007_2010 LERs/Zion'
dest62 = '/home/ksr/Downloads/2007_2010 LERs/Big Rock Point'
dest63 = '/home/ksr/Downloads/2007_2010 LERs/Crystal River'
dest64 = '/home/ksr/Downloads/2007_2010 LERs/Fort Calhoun'
dest65 = '/home/ksr/Downloads/2007_2010 LERs/Fort St. Vrain'

files = os.listdir(source)

for f in files:
    if (f.startswith("313") or f.startswith("368")):
        shutil.move(f, dest1)
    elif (f.startswith("334") or f.startswith("412")):
        shutil.move(f, dest2)
    elif (f.startswith("155")):
        shutil.move(f, dest62)
    elif (f.startswith("456") or f.startswith("457")):
        shutil.move(f, dest3)
    elif (f.startswith("259") or f.startswith("260") or f.startswith("296")):
        shutil.move(f, dest4)
    elif (f.startswith("325") or f.startswith("324")):
        shutil.move(f, dest5)
    elif (f.startswith("454") or f.startswith("455")):
        shutil.move(f, dest6)
    elif (f.startswith("483")):
        shutil.move(f, dest7)
    elif (f.startswith("317") or f.startswith("318")):
        shutil.move(f, dest8)
    elif (f.startswith("413") or f.startswith("414")):
        shutil.move(f, dest9)
    elif (f.startswith("461")):
        shutil.move(f, dest10)
    elif (f.startswith("397")):
        shutil.move(f, dest11)
    elif (f.startswith("445") or f.startswith("446")):
        shutil.move(f, dest12)
    elif (f.startswith("298")):
        shutil.move(f, dest13)
    elif (f.startswith("315") or f.startswith("316")):
        shutil.move(f, dest14)
    elif (f.startswith("302")):
        shutil.move(f, dest63)
    elif (f.startswith("346")):
        shutil.move(f, dest15)
    elif (f.startswith("275") or f.startswith("323")):
        shutil.move(f, dest16)
    elif (f.startswith("10") or f.startswith("237") or f.startswith("249")):
        shutil.move(f, dest17)
    elif (f.startswith("331")):
        shutil.move(f, dest18)
    elif (f.startswith("348") or f.startswith("364")):
        shutil.move(f, Farley)
    elif (f.startswith("16") or f.startswith("341")):
        shutil.move(f, Fermi)
    elif (f.startswith("333")):
        shutil.move(f, FitzPatrick)
    elif (f.startswith("285")):
        shutil.move(f, dest64)
    elif (f.startswith("267")):
        shutil.move(f, dest65)
    elif (f.startswith("244")):
        shutil.move(f, Ginna)
    elif (f.startswith("416")):
        shutil.move(f, dest23)
    elif (f.startswith("213")):
        shutil.move(f, Haddam)
    elif (f.startswith("400")):
        shutil.move(f, Harris)
    elif (f.startswith("321") or f.startswith("366")):
        shutil.move(f, Hatch)
    elif (f.startswith("354")):
        shutil.move(f, Hope)
    elif (f.startswith("133")):
        shutil.move(f, Humboldt)
    elif (f.startswith("003") or f.startswith("247") or f.startswith("286")):
        shutil.move(f, Indian)
    elif (f.startswith("305")):
        shutil.move(f, Kewaunee)
    elif (f.startswith("409")):
        shutil.move(f, La)
    elif (f.startswith("373") or f.startswith("374")):
        shutil.move(f, LaSalle)
    elif (f.startswith("352") or f.startswith("353")):
        shutil.move(f, Limerick)
    elif (f.startswith("309")):
        shutil.move(f, Maine)
    elif (f.startswith("369") or f.startswith("370")):
        shutil.move(f, McGuire)
    elif (f.startswith("245") or f.startswith("336") or f.startswith("423")):
        shutil.move(f, Millstone)
    elif (f.startswith("263")):
        shutil.move(f, Monticello)
    elif (f.startswith("220") or f.startswith("410")):
        shutil.move(f, Nine)
    elif (f.startswith("338") or f.startswith("339")):
        shutil.move(f, North)
    elif (f.startswith("269") or f.startswith("270") or f.startswith("287")):
        shutil.move(f, Oconee)
    elif (f.startswith("219")):
        shutil.move(f, Oyster)
    elif (f.startswith("255")):
        shutil.move(f, Palisades)
    elif (f.startswith("528") or f.startswith("529") or f.startswith("530")):
        shutil.move(f, Palo)
    elif (f.startswith("373") or f.startswith("374")):
        shutil.move(f, LaSalle)
    elif (f.startswith("277") or f.startswith("278")):
        shutil.move(f, Peach)
    elif (f.startswith("440")):
        shutil.move(f, Perry)
    elif (f.startswith("293")):
        shutil.move(f, Pilgrim)
    elif (f.startswith("266") or f.startswith("301")):
        shutil.move(f, Point)
    elif (f.startswith("282") or f.startswith("306")):
        shutil.move(f, Prairie)
    elif (f.startswith("254") or f.startswith("265")):
        shutil.move(f, Quad)
    elif (f.startswith("312")):
        shutil.move(f, Rancho)
    elif (f.startswith("458")):
        shutil.move(f, River)
    elif (f.startswith("261")):
        shutil.move(f, Robinson)
    elif (f.startswith("272") or f.startswith("311")):
        shutil.move(f, Salem)
    elif (f.startswith("206") or f.startswith("361") or f.startswith("362")):
        shutil.move(f, San)
    elif (f.startswith("443")):
        shutil.move(f, Seabrook)
    elif (f.startswith("327") or f.startswith("328")):
        shutil.move(f, Sequoyah)
    elif (f.startswith("322")):
        shutil.move(f, Shoreham)
    elif (f.startswith("498") or f.startswith("499")):
        shutil.move(f, South)
    elif (f.startswith("335") or f.startswith("389")):
        shutil.move(f, Saint)
    elif (f.startswith("395")):
        shutil.move(f, Summer)
    elif (f.startswith("280") or f.startswith("281")):
        shutil.move(f, Surry)
    elif (f.startswith("387") or f.startswith("388")):
        shutil.move(f, Susquehanna)
    elif (f.startswith("289") or f.startswith("320")):
        shutil.move(f, Three)
    elif (f.startswith("344")):
        shutil.move(f, Trojan)
    elif (f.startswith("250") or f.startswith("251")):
        shutil.move(f, Turkey)
    elif (f.startswith("271")):
        shutil.move(f, Vermont)
    elif (f.startswith("424") or f.startswith("425")):
        shutil.move(f, Vogtle)
    elif (f.startswith("382")):
        shutil.move(f, Waterford)
    elif (f.startswith("390") or f.startswith("391")):
        shutil.move(f, Watts)
    elif (f.startswith("482")):
        shutil.move(f, Wolf)
    elif (f.startswith("029")):
        shutil.move(f, Yankee_Rowe)
    elif (f.startswith("295") or f.startswith("304")):
        shutil.move(f, Zion)
    elif (f.startswith("155")):
        shutil.move(f, dest62)
    elif (f.startswith("302")):
        shutil.move(f, dest63)
    elif (f.startswith("285")):
        shutil.move(f, dest64)
    elif (f.startswith("267")):
        shutil.move(f, dest65)

