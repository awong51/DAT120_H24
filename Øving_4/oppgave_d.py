count = 0
value = 0
while True:
    try:
        input = int(input('hvor mye regn'))
        if input >= 0:
            value += input
            count += 1
        elif input < 0 and count == 0:
            print('total på 0 og at gjennomsnitt av 0 verdier er ugyldig.')
            break
        else: 
            
    except:
        print("skriv et lovlig tall")
    