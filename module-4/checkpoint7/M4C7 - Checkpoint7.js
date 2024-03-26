function operation(num1, num2, num3, num4) {
	// Suma los dos primeros argumentos
	var sum1 = num1 + num2;
	// Suma los dos segundos argumentos
	var sum2 = num3 + num4;
	// Compara el resultado de la multiplicación con 50
	if ((sum1 * sum2) >= 50) {
	  console.log("¡El número es mayor que 50!");
	} else {
	  console.log("¡El número es menor que 50!");
	}
  }
  
  // Ejemplo de uso
  operation(10, 20, 5, 2); // Salida: ¡El número es mayor que 50!
  operation(1, 2, 3, 4); // Salida: ¡El número es menor que 50!