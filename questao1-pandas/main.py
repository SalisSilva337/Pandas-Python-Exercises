import pandas as pd


data_cars = pd.read_csv("seminovos.csv")

def only_toyotas(data_cars):
    toyota = data_cars[data_cars.marca == "Toyota"]

    print(toyota)

# only_toyotas(data_cars)


def newer_than_2019(data_cars):
    new = data_cars[data_cars.ano >= 2019]
    print(new)
# newer_than_2019(data_cars)


def cheapest_car(data_cars):
    cheapest = data_cars[data_cars.preco == data_cars.preco.min()]
    print(cheapest)
# cheapest_car(data_cars)

def honda_avg(data_cars):
    honda = data_cars[data_cars.marca == "Honda"]

    avg = sum(honda.preco)/len(honda)

    # pandas "way"
    # avg = honda.preco.mean()

    print(avg)
# honda_avg(data_cars)


def lower_milage(data_cars):
    mileage = data_cars[data_cars.quilometragem <= 30000]
    print(mileage)
# lower_milage(data_cars)


def sortby_decreasing_price(data_cars):
    decreasing_price = data_cars.sort_values(by="preco",ascending=False)
    print(decreasing_price)
# sortby_decreasing_price(data_cars)


def each_brand(data_cars):
    brands = data_cars.groupby(by="marca")

    for brand, group in brands:
        print(f"Brand: {brand} has {len(group)} vehicles")
        print(group, "\n")
# each_brand(data_cars)


def avg_price_per_year(data_cars):
    years = data_cars.groupby(by="ano")

    for year, car in years:
        avg_price = car.preco.mean()

        print(f"Year: {year}")
        print(f"Avg. Price: {avg_price.__round__(2)}")
        print(car, "\n")
# avg_price_per_year(data_cars)


def top3_most_expensive_vehicles(data_cars):
    top3 = data_cars.sort_values(by="preco", ascending=False).head(3)
    print(top3)

top3_most_expensive_vehicles(data_cars)

