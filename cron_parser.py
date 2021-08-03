from src.main import main

if __name__ == "__main__":
    try:
        result = main()
        print(result)
    except Exception as e:
        print(e)
