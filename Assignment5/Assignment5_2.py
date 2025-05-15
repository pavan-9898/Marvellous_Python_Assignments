def vowel_consonent(ch):
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        print(f"{ch} is vowel ")
    else:
        print(f"{ch} is consonent ")
        
def main():
    print("Eneter character :")
    ch=input()
    vowel_con=vowel_consonent(ch)
if __name__ == "__main__":
    main()