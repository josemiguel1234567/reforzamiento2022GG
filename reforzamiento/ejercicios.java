package reforzamiento;

import java.util.Scanner;

/**
 * ejercicios
 */
public class ejercicios {

    public static void mostrarcursodia() {
        //defini varible
        int diasem;
        String mensaje;
        String primeraparteM="ese dia toca el curso de: ";
        //leer datos 
        Scanner leerT=new Scanner(System.in);
        System.out.println("ingrese un dia de la semana: \n1=dom"+"\n2=lun\n3=mar\n4=mie\n5=jue\n6=vie\n7=sab");
        diasem=leerT.nextInt();
        //proseso
        if (diasem==1) {
            mensaje="no hay clases";
        }else if (diasem==2 || diasem==4){
            mensaje=primeraparteM+"matematica";
        }else if (diasem==3 ){
            mensaje=primeraparteM+"fundamentos de programacion";
        }else if (diasem==5){
            mensaje=primeraparteM+"introduccion ala ingenieria de sistemas";
        }else if (diasem==6){
            mensaje=primeraparteM+"formacion cristiana";
        }else if (diasem==7){
            mensaje="no hay clases";}
        else{
            mensaje ="el dia que coloco no exixte";
        }

        //datos de salida
        System.out.println(mensaje);
        }    

    public static void main(String[] args) {
        mostrarcursodia();
    }

}