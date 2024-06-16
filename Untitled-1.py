def fibonacci_iter(n): # def es una palabra reservada que indica la definicion una funcion fibonnaci_iter que toma un argumento n
    a=1 #inicializa una variable a con valor 1
    b=1 #inicializa una variable b con el valor 1
    if n==1: #compueba si n es igual a 1
        print("0")# imprime 0 si  n es igual a 1
    elif n==2:# si la condicion anterior no se cumple comprueba si n es igual a 2, la condicion evalua mas condiciones
        print("0","1")# si n es igual a 2 imprime 0 y 1
    else:#si ninguna de las funciones anteriores se cumple ejecuta el siguiente bloque de codigo
        #usar if elif else es una forma de conrolar flujo del programa para ejecutar bloques de codigo especifico
        print("0")#imprime 0
        print(a)#imprime el valor de a
        print(b)#imprime el valor de b
        for i in range(n-3):#inicia un bucle que itera desde 0 hasta n-3
            total=a+b#calcula la suma de a y b y la guarda en la variable total
            b=a#actualiza el de b con el valor actual de a
            a=total#actualiza el valor de a con el valor actual de total
            print(total)#imprime el total
fibonacci_iter(15)#llama a la funcion fibonacci_iter con el agumento deseado 
#para evirar ambigüedades ya que no permite argumrntos sin nombre y se hace para que los argumentos puedan ser enviados en cualquiern orden
#una funcion es un bloque con instrucciones cuya finalidad es realizar una tarea especifica 
# n es por la variable de la funcion 