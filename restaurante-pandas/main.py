import pandas as pd

data_food = pd.read_csv("restaurante.csv")

def only_italian_food():
    italian_food = data_food[data_food.tipo == "Italiana"]
    print(italian_food)
# only_italian_food()


def great_rating(data_food):
    good_rating = data_food[data_food.avaliacao >= 4.6]
    print(good_rating)
# great_rating(data_food)


def rating_top5(data_food):
    most_expensive_food = data_food.sort_values(by="preco",ascending=False).head(1)
    print(most_expensive_food)
# most_expensive(data_food)

def mexican_food_price_average(data_food):
    mexican_food = data_food[data_food.tipo == "Mexicana"]
    avg_mexican_plates = mexican_food.preco.mean()
    print(f"Average Mexican Food Price: {avg_mexican_plates}")
# mexican_food_price_average(data_food)

def below_50(data_food):
    below_50_reais = data_food[data_food.preco <= 50]
    print(below_50_reais)
# below_50(data_food)

def descending_rating(data_food):
    descending_rating_plates = data_food.sort_values(by="avaliacao",ascending=False)
    print(descending_rating_plates)
# descending_rating(data_food)

def each_plate_type_quantity(data_food):
    types = data_food.groupby(by="tipo")
    for type, group in types:
        print(f"{type} Quantidade: {len(type)}")
        print(group,"\n")
# each_plate_type_quantity(data_food)

def each_plate_type_price_avg(data_food):
    types = data_food.groupby(by="tipo")
    for type, group in types:
        print(f"Media de Preco Culinaria {type}: {group.preco.mean()}")
# each_plate_type_price_avg(data_food)



def rating_top5(data_food):
    top5_best_rated_plates = data_food.sort_values(by="avaliacao",ascending=False).head(5)
    print(top5_best_rated_plates)
# rating_top5(data_food)