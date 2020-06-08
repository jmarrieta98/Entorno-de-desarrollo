import junit.framework.TestCase;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static fizzbuzz.FizzBuzz.ObtenerResultadoMultiple;
import static fizzbuzz.FizzBuzz.ObtenerResultadoSimple;

class FizzBuzzTest extends TestCase {

    private final String[] lista = {"1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11",
            "fizz", "fizz", "14", "fizzbuzz", "16", "17", "fizz", "19", "buzz", "fizz", "22", "fizz", "fizz", "buzz", "26", "fizz", "28", "29",
            "fizzbuzz", "fizz", "fizz", "fizz", "fizz", "fizzbuzz", "fizz", "fizz", "fizz", "fizz", "buzz", "41", "fizz", "fizz", "44", "fizzbuzz",
            "46", "47", "fizz", "49", "buzz"};

    private List<String> ListaFizzBuzz;

    @Test
    public void FizzSielnumeroesDivisibleEntre3() {
        assertEquals("fizz", ObtenerResultadoSimple(3));
    }

    @Test
    public void BuzzSielnumeroesDivisibleEntre5() {
        assertEquals("buzz", ObtenerResultadoSimple(5));

        assertEquals("buzz", ObtenerResultadoSimple(10));
    }

    @Test
    public void FizzBuzzSielnumeroesDivisibleEntre3y5() {
        assertEquals("fizzbuzz", ObtenerResultadoSimple(15));
        assertEquals("fizzbuzz", ObtenerResultadoSimple(30));
    }

    @Test
    public void FizzSielNumeroContiene3() {
        assertEquals("fizz", ObtenerResultadoSimple(32));
    }

    @Test
    public void BuzzSielNumeroContiene5() {
        assertEquals("buzz", ObtenerResultadoSimple(58));
    }

    @Test
    public void FizzBuzzSielNumeroContiene3y5() {
        assertEquals("fizzbuzz", ObtenerResultadoSimple(35));
        assertEquals("fizzbuzz", ObtenerResultadoSimple(53));

    }

    @Test
    public void ElmismoNumeroSinoSeCumpleOtraCondicion() {
        assertEquals("1", ObtenerResultadoSimple(1));
        assertEquals("2", ObtenerResultadoSimple(2));
        assertEquals("4", ObtenerResultadoSimple(4));
    }

    @Test
    public void ListaDeNumerosFizzBuzz() {
        ListaFizzBuzz = new ArrayList<>();
        ListaFizzBuzz.addAll(Arrays.asList(lista));

        assertEquals(ListaFizzBuzz, ObtenerResultadoMultiple(50));
    }
}