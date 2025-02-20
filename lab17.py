def display_menu(choose="selection"):
    menu_diet ={'1':'apples', '2':'bananas','3':'cherries','4':'grapes'
    }
    print("pick your favortie fruit")
    for items, values in menu_dict.items():
        print("\t[]. {}".formant(items,value))
    choice = input("{}".formant(choose)).upper().strip()
    choice = list(menu_dict.keys())
    if choice in choices:
      return menu_diect[choice]
    else:
        return(display_menu("invalid selection\nTry Again:"))

def main():
    fruit = dispay_menu()
    print("wow,l like {} too!".formant(fruit))

    if __name__ == "__main__":
        main()
