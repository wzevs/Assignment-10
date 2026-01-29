# თავიდან თამაშს ერქვა კონტაქტი(პირველი commit საც ამიტომ ქვია contact)  ახლა ლაბირინთი 777 ზე გადაკეთდა კოდიდან გამომდინარე
def function():
    while True:
        value = input("გამოიცანი რიცხვი (გამოსართავად აკრიფეთ exit ) : ")  
        if value.lower() == 'exit':
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