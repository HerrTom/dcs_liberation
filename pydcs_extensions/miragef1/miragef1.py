from enum import Enum

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

class MirageF1_Weapons:
    _2300_PTB_RAF = {"clsid": "{2300-PTB RAF}", "name": "2300-PTB RAF", "weight": 70}


class MirageF1(PlaneType):
    id = "MirageF1"
    flyable = True
    height = 5.43
    width = 9.75
    length = 16.43
    fuel_max = 4530
    max_speed = 2001.996
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Liveries:
        class USSR(Enum):
            F1C_100_Vanille_Chocolat_Worn = "F1C-100 Vanille Chocolat Worn"

        class France(Enum):
            F1C_EQ5_Marine = "F1-EQ5 Marine"
            F1C_100_Blue_Used = "F1C-100 Blue Used"
    
    class Pylon1:
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        R_550_Magic_2 = (1, Weapons.R_550_Magic_2)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)

    class Pylon2:
        LAU_10___4_ZUNI_MK_71  = (2, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        Mk_81 = (2, Weapons.Mk_81)
        Mk_82 = (2, Weapons.Mk_82)
        AUF2_MK_82_x_2 = (2, Weapons.AUF2_MK_82_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (2, Weapons.AUF2_MK_82_Snakeyes_x_2)
        AUF2_BLG_66_AC_x_2 = (2, Weapons.AUF2_BLG_66_AC_x_2)
        BLG_66_AC_Belouga_ = (2, Weapons.BLG_66_AC_Belouga_)
        Matra_Type_155_Rocket_Pod = (2, Weapons.Matra_Type_155_Rocket_Pod)

        Super_530D = (2, Weapons.Super_530D)
        Mk_83 = (2, Weapons.Mk_83)
        MER_2_MK_82 = (2, Weapons.MER_2_MK_82)
        MER_2_MK_83 = (2, Weapons.MER_2_MK_83)
        UB_32A___32_S_5KO = (2, Weapons.UB_32A___32_S_5KO)
        AIM_120B = (2, Weapons.AIM_120B)
        AIM_120C = (2, Weapons.AIM_120C)
        AIM_7M = (2, Weapons.AIM_7M)
    
    class Pylon3:
        AUF2_MK_82_x_2 = (3, Weapons.AUF2_MK_82_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (3, Weapons.AUF2_MK_82_Snakeyes_x_2)
        AUF2_BLG_66_AC_x_2 = (3, Weapons.AUF2_BLG_66_AC_x_2)
        Matra_Type_155_Rocket_Pod = (3, Weapons.Matra_Type_155_Rocket_Pod)
        BLG_66_AC_Belouga_ = (3, Weapons.BLG_66_AC_Belouga_)
        Super_530D = (3, Weapons.Super_530D)
        Matra_Super_530D = (3, Weapons.Matra_Super_530D)
        Mk_81 = (3, Weapons.Mk_81)
        Mk_82 = (3, Weapons.Mk_82)
        Mk_83 = (3, Weapons.Mk_83)
        MER_2_MK_82 = (3, Weapons.MER_2_MK_82)
        MER_2_MK_83 = (3, Weapons.MER_2_MK_83)
        LAU_10___4_ZUNI_MK_71 = (3, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        UB_32A___32_S_5KO = (3, Weapons.UB_32A___32_S_5KO)
        AIM_120B = (3, Weapons.AIM_120B)
        AIM_120C = (3, Weapons.AIM_120C)
        AIM_7M = (3, Weapons.AIM_7M)
        Fuel_Tank_120_gallons = (3, Weapons.Fuel_Tank_120_gallons)

    class Pylon4:
        AUF2_MK_82_x_2 = (4, Weapons.AUF2_MK_82_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (4, Weapons.AUF2_MK_82_Snakeyes_x_2)
        AUF2_BLG_66_AC_x_2 = (4, Weapons.AUF2_BLG_66_AC_x_2)
        Matra_Type_155_Rocket_Pod = (4, Weapons.Matra_Type_155_Rocket_Pod)
        BLG_66_AC_Belouga_ = (4, Weapons.BLG_66_AC_Belouga_)
        Fuel_tank_1150L_MiG_29 = (4, Weapons.Fuel_tank_1150L_MiG_29)
        Super_530D = (4, Weapons.Super_530D)
        Mk_81 = (4, Weapons.Mk_81)
        Mk_82 = (4, Weapons.Mk_82)
        Mk_83 = (4, Weapons.Mk_83)
        MER_2_MK_82 = (4, Weapons.MER_2_MK_82)
        MER_2_MK_83 = (4, Weapons.MER_2_MK_83)
        AIM_120B = (4, Weapons.AIM_120B)
        AIM_120C = (4, Weapons.AIM_120C)
        AIM_7M = (4, Weapons.AIM_7M)
        _2300_PTB_RAF = (4, MirageF1_Weapons._2300_PTB_RAF)

    class Pylon5:
        AUF2_MK_82_x_2 = (5, Weapons.AUF2_MK_82_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (5, Weapons.AUF2_MK_82_Snakeyes_x_2)
        AUF2_BLG_66_AC_x_2 = (5, Weapons.AUF2_BLG_66_AC_x_2)
        Matra_Type_155_Rocket_Pod = (5, Weapons.Matra_Type_155_Rocket_Pod)
        BLG_66_AC_Belouga_ = (5, Weapons.BLG_66_AC_Belouga_)
        Super_530D = (5, Weapons.Super_530D)
        Matra_Super_530D = (5, Weapons.Matra_Super_530D)
        Mk_81 = (5, Weapons.Mk_81)
        Mk_82 = (5, Weapons.Mk_82)
        Mk_83 = (5, Weapons.Mk_83)
        MER_2_MK_82 = (5, Weapons.MER_2_MK_82)
        MER_2_MK_83 = (5, Weapons.MER_2_MK_83)
        LAU_10___4_ZUNI_MK_71 = (5, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61___19_2_75__rockets_MK151_HE = (5, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        UB_32A___32_S_5KO = (5, Weapons.UB_32A___32_S_5KO)
        AIM_120B = (5, Weapons.AIM_120B)
        AIM_120C = (5, Weapons.AIM_120C)
        AIM_7M = (5, Weapons.AIM_7M)
        Fuel_Tank_120_gallons = (5, Weapons.Fuel_Tank_120_gallons)

    class Pylon6:
        LAU_10___4_ZUNI_MK_71  = (6, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61___19_2_75__rockets_MK151_HE = (6, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        Mk_81 = (6, Weapons.Mk_81)
        Mk_82 = (6, Weapons.Mk_82)
        AUF2_MK_82_x_2 = (6, Weapons.AUF2_MK_82_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (6, Weapons.AUF2_MK_82_Snakeyes_x_2)
        AUF2_BLG_66_AC_x_2 = (6, Weapons.AUF2_BLG_66_AC_x_2)
        BLG_66_AC_Belouga_ = (6, Weapons.BLG_66_AC_Belouga_)
        Matra_Type_155_Rocket_Pod = (6, Weapons.Matra_Type_155_Rocket_Pod)

        Super_530D = (6, Weapons.Super_530D)
        Mk_83 = (6, Weapons.Mk_83)
        MER_2_MK_82 = (6, Weapons.MER_2_MK_82)
        MER_2_MK_83 = (6, Weapons.MER_2_MK_83)
        UB_32A___32_S_5KO = (6, Weapons.UB_32A___32_S_5KO)
        AIM_120B = (6, Weapons.AIM_120B)
        AIM_120C = (6, Weapons.AIM_120C)
        AIM_7M = (6, Weapons.AIM_7M)

    class Pylon7:
        Smokewinder___red = (7, Weapons.Smokewinder___red)
        Smokewinder___green = (7, Weapons.Smokewinder___green)
        Smokewinder___blue = (7, Weapons.Smokewinder___blue)
        Smokewinder___white = (7, Weapons.Smokewinder___white)
        Smokewinder___yellow = (7, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (7, Weapons.Smokewinder___orange)
        R_550_Magic_2 = (7, Weapons.R_550_Magic_2)
        AIM_9M_Sidewinder_IR_AAM = (7, Weapons.AIM_9M_Sidewinder_IR_AAM)


    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAP, task.CAS, task.GroundAttack]
    task_default = task.CAS