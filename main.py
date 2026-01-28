def function():
    while True:
        value = input("გამოიცანი რიცხვი (გამოსართავად აკრიფეთ kaput ) : ")  
        if value.lower() == 'kaput':
            print("ნახვამდის!")
            break  
        try:    
            x = int(value)
            if x > 0:
                print("არის კონტაქტი")
            else:
                print("alo? aloo")    
        except ValueError:
            print("შეცდომა: გთხოვთ შეიყვანოთ მთელი რიცხვი სწორ ფორმატში")
function()