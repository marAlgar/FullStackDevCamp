function operation(num1, num2, num3, num4) {
	// Suma los dos primeros argumentos
	var first_sum = num1 + num2;
	// Suma los dos segundos argumentos
	var second_sum = num3 + num4;
	// Multiplica las dos sumas
	var result = first_sum * second_sum;
  
	// Compara el resultado con 50
	if (result > 50) {
	  console.log("¡El número es mayor que 50!");
	} else {
	  console.log("¡El número es menor que 50!");
	}
  }
  
  // Ejemplo de uso
  operation(10, 20, 5, 2); // Salida: ¡El número es mayor que 50!
  operation(1, 2, 3, 4); // Salida: ¡El número es menor que 50!