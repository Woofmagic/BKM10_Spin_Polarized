import sys

def main():
    try:
        print(f"Shut up!")
    except KeyboardInterrupt:
        print("Shutdown requested...exiting")
    sys.exit(0)
    
if __name__ == "__main__":
    main()