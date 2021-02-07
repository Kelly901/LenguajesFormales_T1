if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    #Es el nombre de la persona de la que se desea sacar el promedio
    query_name = raw_input()
    #Essta variable almacena la lista de las calificaciones de el diccionario 
    #studen_marks[] En el cual adentro se le coloca la llave para obtener las cantidades 
    #De ese nombre en especicifico
    datos=student_marks[query_name]
    #Se suman las cantidades de la lista datos
    suma=sum(datos)
    
    d=0
    for i in datos:
        d=d+1
        
    resultado=(suma/d) 
    #Muestra el resultado con dos decimales
    print('%.2f'%resultado)
    