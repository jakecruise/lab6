# Jake Cruise and ...


def weight_converter():
    for weight_kg in range(30,101,10):
        weight_lb = (weight_kg * 2.2)
        print(f'Weight in Kilos: {weight_kg:5d} is {weight_lb:6.2f} in Pounds')


def main():
    weight_converter()


if  __name__ == "__main__":
    main()
