from enum import Enum

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons


class WeaponsF1:
    AUF2_MK_82_x_2_ = {
        "clsid": "{M2KC_RAFAUT_MK82}",
        "name": "AUF2 MK-82 x 2",
        "weight": 525,
    }
    AUF2_MK_82_Snakeyes_x_2_ = {
        "clsid": "{M2KC_RAFAUT_MK82S}",
        "name": "AUF2 MK-82 Snakeyes x 2",
        "weight": 525,
    }
    Barax_ = {"clsid": "{Barax}", "name": "Barax", "weight": 1}
    Phimat_ = {"clsid": "{Phimat}", "name": "Phimat", "weight": 1}
    _2300_PTB_RAF = {"clsid": "{2300-PTB RAF}", "name": "2300-PTB RAF", "weight": 70}


class MirageF1(PlaneType):
    id = "MirageF1"
    flyable = True
    height = 5.43
    width = 9.75
    length = 16.43
    fuel_max = 4530
    max_speed = 2116.8
    chaff = 5000
    flare = 5000
    charge_total = 10000
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    class Liveries:
        class USSR(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Georgia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Venezuela(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Australia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Israel(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Combined_Joint_Task_Forces_Blue(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Sudan(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Norway(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Romania(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Iran(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Ukraine(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Libya(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Belgium(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Slovakia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Greece(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class UK(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Third_Reich(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Hungary(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Abkhazia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Morocco(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class United_Nations_Peacekeepers(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Switzerland(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class SouthOssetia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Vietnam(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class China(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Yemen(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Kuwait(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Serbia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Oman(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class India(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Egypt(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class TheNetherlands(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Poland(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Syria(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Finland(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Kazakhstan(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Denmark(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Sweden(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Croatia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class CzechRepublic(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class GDR(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Yugoslavia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Bulgaria(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class SouthKorea(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Tunisia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Combined_Joint_Task_Forces_Red(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Lebanon(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Portugal(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Cuba(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Insurgents(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class SaudiArabia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class France(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class USA(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Honduras(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Qatar(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Russia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class United_Arab_Emirates(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Italian_Social_Republi(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Austria(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Bahrain(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Italy(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Chile(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Turkey(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Philippines(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Algeria(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Pakistan(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Malaysia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Indonesia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Iraq(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Germany(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class South_Africa(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Jordan(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Mexico(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class USAFAggressors(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Brazil(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Spain(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"
            Sapanish_Air_Force_14th_Wing_LV = "Sapanish Air Force 14th Wing LV"

        class Belarus(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Canada(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class NorthKorea(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Ethiopia(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Japan(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

        class Thailand(Enum):
            F1_EQ_Sand_4014 = "F1-EQ Sand 4014"
            F1_EQ_Sand_Used = "F1-EQ Sand Used"
            F1_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_New = "F1C-100 Blue New"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"
            F1C_200_Blue_Worn = "F1C-200 Blue Worn"
            F1C_200_Vanille_Chocolat_Filthy = "F1C-200 Vanille Chocolat Filthy"
            F1C_200_Vanille_Chocolat_Very_Filthy = (
                "F1C-200 Vanille Chocolat Very Filthy"
            )
            F1CR_European_Used = "F1CR European Used"
            F1CR_Green_Grey_Used = "F1CR Green Grey Used"
            F1CR_RedFlag_New = "F1CR RedFlag New"
            F1CR_Vanille_Chocolat_Worn = "F1CR Vanille Chocolat Worn"
            F1CT_Green_Grey_Worn = "F1CT Green Grey Worn"
            F1CT_Green_Used = "F1CT Green Used"

    class Pylon1:
        R_550_Magic_2 = (1, Weapons.R_550_Magic_2)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)

    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C1}
    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C2}
    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C3}
    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C4}
    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C5}
    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C6}

    class Pylon2:
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
            2,
            Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        )
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            2,
            Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        Mk_81___250lb_GP_Bomb_LD = (2, Weapons.Mk_81___250lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        WeaponsF1.AUF2_MK_82_x_2_ = (2, WeaponsF1.AUF2_MK_82_x_2_)
        WeaponsF1.AUF2_MK_82_Snakeyes_x_2_ = (2, WeaponsF1.AUF2_MK_82_Snakeyes_x_2_)
        AUF2_BLG_66_AC_x_2 = (2, Weapons.AUF2_BLG_66_AC_x_2)
        Matra_Type_155_Rocket_Pod = (2, Weapons.Matra_Type_155_Rocket_Pod)
        BLG_66_AC_Belouga = (2, Weapons.BLG_66_AC_Belouga)
        Super_530D = (2, Weapons.Super_530D)
        Mk_83___1000lb_GP_Bomb_LD = (2, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (
            2,
            Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
        )
        MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD = (
            2,
            Weapons.MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD,
        )
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (
            2,
            Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag,
        )
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            2,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_7M_Sparrow_Semi_Active_Radar = (2, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        Barax_ = (2, WeaponsF1.Barax_)
        Phimat_ = (2, WeaponsF1.Phimat_)

    class Pylon3:
        WeaponsF1.AUF2_MK_82_x_2_ = (3, WeaponsF1.AUF2_MK_82_x_2_)
        WeaponsF1.AUF2_MK_82_Snakeyes_x_2_ = (3, WeaponsF1.AUF2_MK_82_Snakeyes_x_2_)
        AUF2_BLG_66_AC_x_2 = (3, Weapons.AUF2_BLG_66_AC_x_2)
        Matra_Type_155_Rocket_Pod = (3, Weapons.Matra_Type_155_Rocket_Pod)
        BLG_66_AC_Belouga = (3, Weapons.BLG_66_AC_Belouga)
        Super_530D = (3, Weapons.Super_530D)
        Matra_Super_530D = (3, Weapons.Matra_Super_530D)
        Mk_81___250lb_GP_Bomb_LD = (3, Weapons.Mk_81___250lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        # ERRR {B26BE7F3-3493-4fd2-AA73-8847B83A1A03}
        # ERRR {4741A78E-95AD-405c-B396-0AD3C73BBC5C}
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
            3,
            Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        )
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            3,
            Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (
            3,
            Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag,
        )
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            3,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_7M_Sparrow_Semi_Active_Radar = (3, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        Fuel_Tank_120_gallons = (3, Weapons.Fuel_Tank_120_gallons)

    class Pylon4:
        WeaponsF1.AUF2_MK_82_x_2_ = (4, WeaponsF1.AUF2_MK_82_x_2_)
        WeaponsF1.AUF2_MK_82_Snakeyes_x_2_ = (4, WeaponsF1.AUF2_MK_82_Snakeyes_x_2_)
        AUF2_BLG_66_AC_x_2 = (4, Weapons.AUF2_BLG_66_AC_x_2)
        Matra_Type_155_Rocket_Pod = (4, Weapons.Matra_Type_155_Rocket_Pod)
        BLG_66_AC_Belouga = (4, Weapons.BLG_66_AC_Belouga)
        Fuel_tank_1150L_MiG_29 = (4, Weapons.Fuel_tank_1150L_MiG_29)
        Super_530D = (4, Weapons.Super_530D)
        Mk_81___250lb_GP_Bomb_LD = (4, Weapons.Mk_81___250lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (4, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        # ERRR {B26BE7F3-3493-4fd2-AA73-8847B83A1A03}
        # ERRR {4741A78E-95AD-405c-B396-0AD3C73BBC5C}
        AIM_120B_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            4,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_7M_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        _2300_PTB_RAF = (4, WeaponsF1._2300_PTB_RAF)

    class Pylon5:
        WeaponsF1.AUF2_MK_82_x_2_ = (5, WeaponsF1.AUF2_MK_82_x_2_)
        WeaponsF1.AUF2_MK_82_Snakeyes_x_2_ = (5, WeaponsF1.AUF2_MK_82_Snakeyes_x_2_)
        AUF2_BLG_66_AC_x_2 = (5, Weapons.AUF2_BLG_66_AC_x_2)
        Matra_Type_155_Rocket_Pod = (5, Weapons.Matra_Type_155_Rocket_Pod)
        BLG_66_AC_Belouga = (5, Weapons.BLG_66_AC_Belouga)
        Super_530D = (5, Weapons.Super_530D)
        Matra_Super_530D = (5, Weapons.Matra_Super_530D)
        Mk_81___250lb_GP_Bomb_LD = (5, Weapons.Mk_81___250lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (5, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        # ERRR {B26BE7F3-3493-4fd2-AA73-8847B83A1A03}
        # ERRR {4741A78E-95AD-405c-B396-0AD3C73BBC5C}
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
            5,
            Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        )
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            5,
            Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (
            5,
            Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag,
        )
        AIM_120B_AMRAAM___Active_Rdr_AAM = (5, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            5,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_7M_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        Fuel_Tank_120_gallons = (5, Weapons.Fuel_Tank_120_gallons)

    class Pylon6:
        WeaponsF1.AUF2_MK_82_x_2_ = (6, WeaponsF1.AUF2_MK_82_x_2_)
        WeaponsF1.AUF2_MK_82_Snakeyes_x_2_ = (6, WeaponsF1.AUF2_MK_82_Snakeyes_x_2_)
        AUF2_BLG_66_AC_x_2 = (6, Weapons.AUF2_BLG_66_AC_x_2)
        Matra_Type_155_Rocket_Pod = (6, Weapons.Matra_Type_155_Rocket_Pod)
        BLG_66_AC_Belouga = (6, Weapons.BLG_66_AC_Belouga)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
            6,
            Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        )
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            6,
            Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        Mk_81___250lb_GP_Bomb_LD = (6, Weapons.Mk_81___250lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Super_530D = (6, Weapons.Super_530D)
        Mk_83___1000lb_GP_Bomb_LD = (6, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (
            6,
            Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
        )
        MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD = (
            6,
            Weapons.MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD,
        )
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (
            6,
            Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag,
        )
        AIM_120B_AMRAAM___Active_Rdr_AAM = (6, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            6,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_7M_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        Barax_ = (6, WeaponsF1.Barax_)
        Phimat_ = (6, WeaponsF1.Phimat_)

    class Pylon7:
        R_550_Magic_2 = (7, Weapons.R_550_Magic_2)
        AIM_9M_Sidewinder_IR_AAM = (7, Weapons.AIM_9M_Sidewinder_IR_AAM)

    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C1}
    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C2}
    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C3}
    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C4}
    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C5}
    # ERRR {D3F65166-1AB8-490f-AF2F-2FB6E24A61C6}

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [
        task.CAP,
        task.Escort,
        task.FighterSweep,
        task.Intercept,
        task.Reconnaissance,
        task.GroundAttack,
        task.CAS,
        task.AFAC,
        task.RunwayAttack,
        task.AntishipStrike,
    ]
    task_default = task.CAP
