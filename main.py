def function():
    while True:    
        try:    
            x = int(input("შეიყვანეთ რიცხვი :"))
            if x > 0:
                print("არის კონტაქტი")
            else:
                print("alo? aloo")
            break    
        except ValueError:
            print("შეცდომა: გთხოვთ შეიყვანოთ მთელი რიცხვი სწორ ფორმატში")
function()