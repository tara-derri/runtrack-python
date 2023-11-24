while True:
    try:
        N = int(input("Entrez un entier supérieur à zéro (N) : "))
        if N <= 0:
            raise ValueError("N doit être supérieur à zéro.")
        break  
    except ValueError:
        print("Veuillez entrer un entier valide.")

for i in range(1, N + 1):
    print(f"\nTable de multiplication de {i} :\n")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
