from city import City
from hospital import Hospital
import random

def random_hospitals(meanNumHospitals, meanHospitalRange, city, numHospitalsStandardDeviation, hospitalRangeStandardDeviation):
    numHospitals = random.randint(meanNumHospitals-hospitalRangeStandardDeviation, meanNumHospitals+hospitalRangeStandardDeviation)
    random_hospitals = []
    while len(random_hospitals) < numHospitals:
        x = random.randint(0, city.width-1)
        y = random.randint(0, city.height-1)
        d = random.randint(max(meanHospitalRange-hospitalRangeStandardDeviation, 0), meanHospitalRange+hospitalRangeStandardDeviation)
        random_hospitals.append(Hospital(x, y, d, city))

    return random_hospitals
    
def random_population(populationSize, meanNumHospitals, meanHospitalRange, city, numHospitalsStandardDeviation, hospitalRangeStandardDeviation):
    random_population = []
    while len(random_population) < populationSize:
        random_population.append(random_hospitals(meanNumHospitals, meanHospitalRange, city, numHospitalsStandardDeviation, hospitalRangeStandardDeviation))

    return random_population