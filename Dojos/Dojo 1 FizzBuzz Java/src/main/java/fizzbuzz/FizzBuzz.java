package fizzbuzz;

import java.util.ArrayList;
import java.util.List;


/**
 * Esta clase define los metodos tan simple como multiple para efectuar el fizzbuzz
 *
 * @author Jose Manuel Arrieta Soto
 */
public class FizzBuzz {

    /**
     * @param numero entero que vamos aplicar el fizzbuzz
     * @return fizzbuzz si numero es divisible entre 3 y 5 o contiene 3 y 5
     * fizz si numero es divisible entre 3 o contiene 3
     * buzz si numero es divisible entre 5 o contiene 5
     */
    public static String ObtenerResultadoSimple(int numero) {

        if (numero % 3 == 0 && numero % 5 == 0 || Integer.toString(numero).contains("3") && Integer.toString(numero).contains("5")) {
            return "fizzbuzz";
        }
        if (numero % 3 == 0 || Integer.toString(numero).contains("3")) {
            return "fizz";
        } else if (numero % 5 == 0 || Integer.toString(numero).contains("5")) {
            return "buzz";
        } else {
            return Integer.toString(numero);
        }
    }

    /**
     * @param numero numero para recorrer un bucle
     * @return una lista con todos los numeros de 1 al numero y aplicando el criterio fizzbuzz
     */
    public static List<String> ObtenerResultadoMultiple(int numero) {
        ArrayList<String> ListaFizzBuzz = new ArrayList<>();

        for (int i = 1; i <= numero; i++) {
            if (i % 3 == 0 && i % 5 == 0 || Integer.toString(i).contains("3") && Integer.toString(i).contains("5")) {
                ListaFizzBuzz.add("fizzbuzz");
            } else if (i % 3 == 0 || Integer.toString(i).contains("3")) {
                ListaFizzBuzz.add("fizz");
            } else if (i % 5 == 0 || Integer.toString(i).contains("5")) {
                ListaFizzBuzz.add("buzz");
            } else {
                ListaFizzBuzz.add(Integer.toString(i));
            }
        }
        return ListaFizzBuzz;
    }
}