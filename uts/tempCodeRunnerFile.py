cardinal_direction = ("West", "North", "South")
islands = ("Kalimantan", "Sumatra", "Sulawesi")


def main():
    for island in islands:
        for direction in cardinal_direction:
            print(island, direction, sep=" ")


if __name__ == "__main__":
    main()