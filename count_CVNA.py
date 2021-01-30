import math
import re
import time
import random
import numpy as np
from urllib.request import Request, urlopen
from  CVNA_cars import  CVNA_cars
class count_CVNA:

    def count(brands):
        array = np.zeros([4, 14])
        pending_index = 0
        incoming_index = 1
        available_index = 2
        total_result = 0

        brands_to_search = []
        pending_count = 0
        incoming_count = 0
        available_count = 0
        total_count = -1
        cars = []
        while len(brands_to_search) < 7:
            r = random.randint(1, len(brands)-1)
            if r not in brands_to_search:
                brands_to_search.append(r)
        for b in brands_to_search:
            print(brands[b])
            url = "https://www.carvana.com/cars/" + brands[b]
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read().decode("utf-8")

            for s in webpage.split():
                if "totalMatchedPages\":" in s:
                    s = s[s.rfind("totalMatchedPages"): s.rfind("totalMatchedPages")+30]
                    numeric_string = re.sub("[^0-9]", "", s)
                    total_result = int(numeric_string)
            pages_to_search =[]
            print(total_result)
            while len(pages_to_search) < math.ceil(total_result/20) and len(pages_to_search)<5:
                r = random.randint(1,total_result)
                if r not in pages_to_search:
                    pages_to_search.append(r)


            time.sleep(1)
            for num in pages_to_search:
                url = "https://www.carvana.com/cars/" + brands[b]+"?page=" + str(num)
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                time.sleep(1)
                webpage = urlopen(req).read().decode("utf-8")

                index = webpage.split()
                for s in index:
                    if "isPurchasePending" in s:
                        total_count += 1
                        car = CVNA_cars()
                        cars.append(car)
                        year_index = s.rfind("\"year\":")
                        year_strand =s[year_index: year_index+11]
                        year = int(year_strand[year_strand.rfind(":")+1: year_strand.rfind(":")+5])
                        car.set_year(year2= year)
                        car.set_brand(brand2=brands[b].strip())

                        incoming = s.rfind("vehicleInventoryType")
                        incoming_strand = s[incoming: incoming + 25]
                        if "\"vin\":" in s:
                            vin = s[s.rfind("\"vin\":" )+7: s.rfind("\"vin\":" )+24]
                            car.set_vin(vin.strip())




                        if "\"isPurchasePending\":true" in s :
                            pending_count += 1
                            array[pending_index][year - 2008] +=1
                            car.set_isPurchasePending(True)
                            car.set_status("Pending")
                        if " \"isOnDemand\":true" in s:
                            if  car.status != "Pending":
                                pending_count += 1
                                array[pending_index][year - 2008] += 1
                                car.set_status("Pending")
                            car.set_isOnDemand(isOnDemand2= True)
                        if "\"vehicleLockType\":3" in s:
                            if car.status != "Pending":
                                pending_count += 1
                                array[pending_index][year - 2008] += 1
                                car.set_status("Pending")
                            car.set_vehicleLockType(vehicleLockType2= 3)

                        if any(char.isdigit() for char in incoming_strand) :

                            for x in range(len(incoming_strand)):
                                if incoming_strand[x].isdigit():
                                        if int(incoming_strand[x]) ==2:
                                          incoming_count += 1
                                          array[incoming_index][year - 2008] += 1
                                          car.set_vehicleInventoryType(vehicleInventoryType2=2)
                                          car.set_status("Incoming")
                                        else:
                                            if car.status != "Pending" and car.status!= "Incoming":
                                                available_count +=1
                                                array[available_index][year - 2008] += 1
                                                car.set_status("Available")


                #print("There are total of " + str(pending_count) + " cars pending.")
                #print("There are total of " + str(incoming_count) + " cars incoming.")
                #print("There are total of " + str(available_count) + " cars available.")

                url = "https://www.carvana.com/cars?page=" + str(num)
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                webpage = urlopen(req).read().decode("utf-8")


        print("There are total of " + str(total_count) + " cars on the site.")
        print("There are total of " + str(pending_count) + " cars pending.")
        print("There are total of " + str(incoming_count) + " cars incoming.")
        print("There are total of " + str(available_count) + " cars available.")

        print(array)
        return array,cars
    def open_data(file_path):
        car_list = []

        file = open(file_path,"r")
        for line in file:
            if line is not None:
                car = CVNA_cars()
                temp = line.split("\t")
                car.set_vin(temp[0].strip())
                car.set_brand(temp[1].strip())
                if  temp[2] =="True":
                    car.set_isPurchasePending(True)
                else:
                    car.set_isPurchasePending(False)

                if  temp[3] =="True":
                    car.set_isOnDemand(True)
                else:
                    car.set_isOnDemand(False)
                car.set_vehicleInventoryType(int(temp[4]))
                car.set_year(int(temp[5]))
                car.set_vehicleLockType(int(temp[6]))
                car.set_status(temp[7].strip())
                car_list.append(car)
        file.close()
        return car_list
    def check_data(car_list):
        array = np.zeros([8, 15])
        pending_index = 0
        incoming_index = 1
        available_index = 2
        sold_index = 3


        pending_to_sold =0
        available_to_pending =0
        pending_to_available = 0
        incoming_to_availble = 0
        for car in car_list :
            if car.status.lower().strip() != "sold":

                url = "https://www.carvana.com/cars/" + car.vin
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                time.sleep(random.uniform(5, 7))
                webpage = urlopen(req).read().decode("utf-8")
                index = webpage.split()
                car_temp = CVNA_cars()
                if "isPurchasePending" in webpage:
                    for s in index:
                        if "isPurchasePending" in s:


                            incoming = s.rfind("vehicleInventoryType")
                            incoming_strand = s[incoming: incoming + 25]
                            if "\"isPurchasePending\":true" in s:
                                car_temp.set_status("Pending")
                                if not car.isPurchasePending:
                                    car.set_isPurchasePending(True)
                            if " \"isOnDemand\":true" in s:
                                if not car_temp.isPurchasePending:
                                    car_temp.set_status("Pending")
                                    car.set_isOnDemand(True)
                            if "\"vehicleLockType\":3" in s:
                                if not car_temp.isPurchasePending and not car_temp.isOnDemand:
                                    car.set_vehicleLockType(3)
                                    car_temp.set_status("Pending")
                            if any(char.isdigit() for char in incoming_strand):

                                for x in range(len(incoming_strand)):
                                    if incoming_strand[x].isdigit():
                                        if int(incoming_strand[x]) == 2:

                                                car.set_vehicleInventoryType(2)
                                                car_temp.set_status("Incoming")

                                        else:
                                            if car_temp.status != "Pending" and car_temp.status != "Incoming":
                                             car_temp.set_status("Available")

                else:
                    car_temp.set_status("Sold")
                if car_temp.status.strip() != car.status.strip():
                    print("Was: "+car.status)
                    print("Changed to: "+car_temp.status)
                    if car_temp.status.strip() == "Available" and car.status.strip() == "Incoming":
                        incoming_to_availble +=1
                    if car_temp.status.strip() == "Pending":
                        available_to_pending +=1
                    if car_temp.status.strip() == "Available" and car.status.strip() == "Pending":
                        pending_to_available +=1
                    if car_temp.status.strip() =="Sold":
                        pending_to_sold +=1
                car.set_status(car_temp.status.strip("\n"))
                print(car.toString())

            if car.status == "Pending":
                array[pending_index][car.year - 2008] += 1
            if car.status == "Incoming":
                array[incoming_index][car.year - 2008] += 1
            if car.status == "Available":
                array[available_index][car.year - 2008] += 1
            if car.status == "Sold":
                array[sold_index][car.year - 2008] +=1

        array[4][1] =  (available_to_pending)
        array[5][1] =  (pending_to_available)
        array[6][1] = (incoming_to_availble)
        array[7][1]= (pending_to_sold)
        return array, car_list