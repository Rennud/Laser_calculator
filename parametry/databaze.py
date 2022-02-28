# Ocel
ocel_1mm = [4200, float(0.5)]
ocel_1_5mm = [3100, float(0.5)]
ocel_2mm = [3000, float(0.5)]
ocel_3mm = [1650, float(1)]
ocel_4mm = [1500, float(6)]
ocel_5mm = [1200, float(7)]
ocel_6mm = [1000, float(6.7)]
ocel_8mm = [700, float(10.5)]
ocel_10mm = [500, float(10)]
# Nerez
nerez_vzduch_0_5mm = [8000, float(0.2)]
nerez_dusik_1mm = [4200, float(0.5)]
nerez_vzduch_1mm = [3400, float(0.5)]
nerez_dusik_1_5mm = [2500, float(0.4)]
nerez_vzduch_1_5mm = [3200, float(1)]
nerez_dusik_2mm = [1800, float(0.5)]
nerez_vzduch_2mm = [3000, float(1)]
nerez_dusik_3mm = [1200, float(2.3)]
nerez_vzduch_3mm = [1600, float(2)]
nerez_dusik_4mm = [800, float(0.5)]
nerez_vzduch_4mm = [550, float(2)]
nerez_dusik_5mm = [1500, float(1)]
nerez_vzduch_5mm = [300, float(1.5)]
# Pozink
pozink_dusik_1mm = [5000, float(0.5)]
pozink_vzduch_1mm = [4300, float(1)]
pozink_dusik_1_5mm = [4000, float(0.5)]
pozink_vzduch_1_5mm = [4600, float(1)]
pozink_vzduch_2mm = [2000, float(1)]
# Hliník
hlinik_1mm = [4800, float(0.6)]
hlinik_1_5mm = [1400, float(3.3)]
hlinik_2mm = [1400, float(3.3)]
hlinik_3mm = [250, float(3.3)]

seznam_druhu = [ocel_1mm, ocel_1_5mm, ocel_2mm, ocel_3mm, ocel_4mm, ocel_5mm, ocel_6mm, ocel_8mm, ocel_10mm, nerez_dusik_1mm, nerez_dusik_1_5mm, nerez_dusik_2mm, nerez_dusik_3mm, nerez_dusik_4mm, nerez_dusik_5mm, nerez_vzduch_0_5mm, nerez_vzduch_1mm,
                nerez_vzduch_1_5mm, nerez_vzduch_2mm, nerez_vzduch_3mm, nerez_vzduch_4mm, nerez_vzduch_5mm, pozink_dusik_1mm, pozink_dusik_1_5mm, pozink_vzduch_1mm, pozink_vzduch_1_5mm, pozink_vzduch_2mm, hlinik_1mm, hlinik_1_5mm, hlinik_2mm, hlinik_3mm]
nazvy_druhu = ["1mm ocel pálená kyslíkem", "1,5mm ocel pálená kyslíkem ", "2mm ocel pálená kyslíkem", "3mm ocel pálená kyslíkem", "4mm ocel pálená kyslíkem", "5mm ocel pálená kyslíkem", "6mm ocel pálená kyslíkem", "8mm ocel pálená kyslíkem", "10mm ocel pálená kyslíkem", "1mm nerez pálená dusíkem", "1,5mm nerez pálená dusíkem", "2mm nerez pálená dusíkem", "3mm nerez pálená dusíkem", "4mm nerez pálená dusíkem", "5mm nerez pálená dusíkem", "0,5mm nerez pálená vzduchem",
               "1mm nerez pálená vzduchem", "1,5mm nerez pálená vzduchem", "2mm nerez pálená vzduchem", "3mm nerez pálená vzduchem", "4mm nerez pálená vzduchem", "5mm nerez pálená vzduchem", "1mm pozink pálený dusíkem", "1,5mm pozink pálený dusíkem", "1mm pozink pálený vzduchem", "1,5mm pozink pálený vzduchem", "2mm pozink pálený vzduchem", "1mm hliník pálený vzduchem", "1,5mm hliník pálený vzduchem", "2mm hliník pálený vzduchem", "3mm hliník pálený vzduchem"]
seznam_uvod = """Vítejte v naší kalkulačce. Zde je seznam palicích možností:
        OCEL            NEREZ - PÁLENÍ DUSÍKEM      NEREZ - PÁLENÍ VZDUCHEM      POZINK - PÁLENÍ DUSÍKEM      POZINK - PÁLENÍ VZDUCHEM      HLINÍK - PÁLENÍ VZDUCHEM
        1 -  1mm        10 -  1mm                   16 -  0,5mm                  23 - 1mm                     25 -  1mm                     28 -  1mm
        2 -  1,5mm      11 -  1,5mm                 17 -  1mm                    24 - 1,5mm                   26 -  1,5mm                   29 -  1,5mm
        3 -  2mm        12 -  2mm                   18 -  1,5mm                                               27 -  2mm                     30 -  2mm
        4 -  3mm        13 -  3mm                   19 -  2mm                                                                               31 -  3mm
        5 -  4mm        14 -  4mm                   20 -  3mm
        6 -  5mm        15 -  5mm                   21 -  4mm
        7 -  6mm                                    22 -  5mm
        8 -  8mm                             
        9 -  10mm
        """
