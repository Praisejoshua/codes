/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package assignment;

import java.util.Scanner;

/**
 *
 * @author HP
 */
public class Assignment {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner xy = new Scanner (System.in);
        int a = 8;
        int n; 
        int d = 5;
        int Tn;
        System.out.println("Enter the value for n ");
        n= xy.nextInt();
        Tn = a+(n-1)*d;
        
        if (Tn < 1000){
        System.out.println("this is the "+ Tn + "value ");
        
        }else {
        System.out.println("the "+ n+ " th value is greater than 1000");
        }
        
        
        }
    }
    

