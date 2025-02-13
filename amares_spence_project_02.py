def main():
    stop_loop = "no"
    while stop_loop != "yes":
       print("we want to know eveyting about you")
       anime = input("what is your favorite anime?:")
       print("anime is" + anime )
       loction = input("where are you from?:")
       print("loction is" + loction)
       season = input("do you like winter or fall?:")
       print("season is" + season)
       stop_loop = input("Type 'yes' to exit program: ").lower().strip()
        print("Thank you for anwersing the qustion?")
if __name__ == "__main__":
    main()
