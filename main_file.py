## Farmaan
import constants as const
import body_mass as bm
import Position_Velocity_Acceleration as pva
import Video as v

output = input("Type 1 for CSV, 2 for CSV and Video:")

if output == "1":
    pva.delete_csv()
    pva.Rk4_method(pva.setup_initial_conditions(const.rf_1, const.rf_2, bm.body_mass(const.h, const.rf_1, const.p0_1)[1], bm.body_mass(const.h, const.rf_2, const.p0_2)[1], const.G), 1000/60)
    pva.Create_csv()
elif output == "2":
    pva.delete_csv()
    pva.Rk4_method(pva.setup_initial_conditions(const.rf_1, const.rf_2, bm.body_mass(const.h, const.rf_1, const.p0_1)[1], bm.body_mass(const.h, const.rf_2, const.p0_2)[1], const.G), 1000/60)
    pva.Create_csv()
    v.video("binary_star.csv")
else:
    print("Error wrong input")

print("Completed")