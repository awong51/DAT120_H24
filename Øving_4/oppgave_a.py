while True:
    høyde = input("hvor høy er du?")
    try:
        høyde = int(høyde)
        break
    except:
        print("skriv et lovlig tall")
        
if høyde >= 120:
   print("Ja, du kan!")
else:
    print("Nei, du kan ikke!")
