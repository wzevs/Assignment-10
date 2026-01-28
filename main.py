# ლაბირინთი 777 
def function():
    while True:
        value = input("გამოიცანი რიცხვი (გამოსართავად აკრიფეთ kaput ) : ")  
        if value.lower() == 'kaput':
            print("ნახვამდის!")
            break  
        try:    
            x = int(value)
            if x > 0 and x!=777:
                print("არის კონტაქტი")
            elif x==777:
                print("გილოცავ შენ მოიგე ჯეკპოტი !")
                y = input("აგრძელებ თამაშს? : ")
                if y == "0":
                    print("შეგერგოს")
                    return
            else:
                print("alo? aloo")    
        except ValueError:
            print("შეცდომა: გთხოვთ შეიყვანოთ მთელი რიცხვი სწორ ფორმატში")
function()