import os
import tkinter
import tkinter.messagebox
from time import time
from write_Excel import write_Data
from count_CVNA import count_CVNA
from datetime import  datetime
import tkinter as tk
from tkinter.filedialog import askdirectory
import glob
global root
def request_location():

    root.withdraw()
    path = askdirectory(title='Select Folder')  # shows dialog box and return the path
    if "/" in path:
        path += "/"
    elif "\\" in path:
        path += "\\"

    root.update()
    root.withdraw()
    return  path
if __name__ == '__main__':
    root = tk.Tk()
    print("Hello world")
    brands="Acura AlfaRomeo Audi BMW Buick Cadillac Chevrolet Chrysler Dodge FIAT Ford Genesis GMC Honda Hyundai INFINITI Jaguar Jeep Kia LandRover Lexus Lincoln Maserati Mazda Mercedes-Benz Mercury MINI Mitsubishi Nissan Pontiac Porsche Ram Scion smart Subaru Suzuki Tesla Toyota Volkswagen Volvo"
    brands = brands.lower()
    brand_list = brands.split(" ")

    write = write_Data()
    location = request_location()

    write.set_location(location)
    date = datetime.now().strftime("%d-%b-%Y")

    time1 = time()

    dir = os.listdir(location)
    if len(dir) == 0 :
        CVNA_count, cars_list = count_CVNA.count(brand_list)
        write.write_xlsx(CVNA_count, "Carvana")
        write.write_txt(cars_list, "Carvana")
    else:
        files = dir
        paths = [os.path.join(location, basename) for basename in files]
        temp_paths = paths
        for x in range(len(paths)):
            if ".txt" not in paths[x]:
                temp_paths.remove(paths[x])



        location = max(temp_paths, key=os.path.getctime)
        print(location)





        CVNA_count, cars_list = count_CVNA.check_data(count_CVNA.open_data(location))
        write.write_xlsx(CVNA_count, "Carvana")
        write.write_txt(cars_list, "Carvana" + str(date))

    tkinter.messagebox.showinfo(title="Program has finished running", message="The result will be in " + location +"\n The program took: %s seconds " % str(time()-time1) )
    root.update()
    root.destroy()





