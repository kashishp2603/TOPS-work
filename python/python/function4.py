def check_prime(num):
     (print("Not Prime" if num<=1 or not all(num%i!=0 for i in range(2,num)) else "Prime"))
check_prime(int(input("Enter number: ")))