
import java.util.Random;

/**
 * 
 * @author Hilario Tomaz Alves de Oliveira
 *
 */

public class Utils {

  private Utils() {

  }
  
  // M�todos

  public static void imprimirVetor(int[] vetor, int limite) {
	
	System.out.print( "  Vetor = {" );
	  
    int tamanhoImpressao = Math.min(vetor.length, limite);
    for(int i = 0; i < tamanhoImpressao; i++) {
    	
      System.out.print( vetor[i] );
      
      if( i < ( tamanhoImpressao - 1 ) ) {
    	  
        System.out.print( ", " );
    	  
      }
      
    }
    
    System.out.print( "}" );
    
  }

  public static int[] gerarVetor(int tamanhoVetor, int limiteSuperior) {
	
	Random random = new Random();
	
	int[] vetor = new int[tamanhoVetor];
	
    for(int i = 0; i < tamanhoVetor; i++) {
	    	
	  int numero = random.nextInt( limiteSuperior );
	 
	  vetor[i] = numero;
	  
    } // FOR VETOR
	    
    return vetor;
    
  }

}
