def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.title()
    match unit:
        case "packets":
            print(f"{seed} seeds: {quantity} packets available")
            return
        case "grams":
            print(f"{seed} seeds: {quantity} grams total")
            return
        case "area":
            print(f"{seed} seeds: covers {quantity} square meters")
            return
        case _:
            print("Unknown unit type")
            return
