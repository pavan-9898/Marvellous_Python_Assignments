try:
    import times


    start_time=time.time()
    print(start_time)
except ModuleNotFoundError as i:
    print("You have imported wrong module:",i)

finally:
    print("finally block executed")

def main():

    pass

if __name__ == "__main__":
    main()