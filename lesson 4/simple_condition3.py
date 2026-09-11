tier = "public"

match tier:
    case "vvip":
        print("Discount 50%")
    case "vip":
        print("Discount 20%")
    case "business":
        print("Discount 10%")
    case _:
        print("No Discount")