/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.jmsa.eratostenes;

import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author jmsa
 */
public class GeneradorDePrimosTest
{
    
    public GeneradorDePrimosTest()
    {
    }

    @org.junit.jupiter.api.BeforeAll
    public static void setUpClass() throws Exception
    {
    }

    @org.junit.jupiter.api.AfterAll
    public static void tearDownClass() throws Exception
    {
    }

    @org.junit.jupiter.api.BeforeEach
    public void setUp() throws Exception
    {
    }

    @org.junit.jupiter.api.AfterEach
    public void tearDown() throws Exception
    {
    }
    


    /**
     * Test of generarPrimos method, of class GeneradorDePrimos.
     */
    @org.junit.jupiter.api.Test
    public void testGenerarPrimosCero()
    {
        System.out.println("generarPrimos");
        int max = 0;
        int  expResult = 0;
        int[] result = GeneradorDePrimos.generarPrimos(max);
        assertEquals(expResult, result.length);
        //assertArrayEquals(expected, actual);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }

    @org.junit.jupiter.api.Test
    public void testGenerarPrimosMin()
    {
        System.out.println("generarPrimos");
        int max = 2;
        int expResult = 1;
        int[] result = GeneradorDePrimos.generarPrimos(max);
        assertEquals(expResult, result.length);
        assertEquals(result[0], 2);
        //assertArrayEquals(expResult, result.length);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    @org.junit.jupiter.api.Test
    public void testGenerarPrimosTres()
    {
        System.out.println("generarPrimos");
        int max = 3;
        int expResult = 2;
        int[] result = GeneradorDePrimos.generarPrimos(max);
        assertEquals(expResult, result.length);
        assertEquals(result[0], 2);
        assertEquals(result[1], 3);
        //assertArrayEquals(expResult, result.length);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    @org.junit.jupiter.api.Test
    public void testGenerarPrimos100()
    {
        System.out.println("generarPrimos");
        int max = 100;
        int expResult = 25;
        int[] result = GeneradorDePrimos.generarPrimos(max);
        assertEquals(expResult, result.length);
        assertEquals(result[24], 97);
        //assertArrayEquals(expResult, result.length);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }    
}
