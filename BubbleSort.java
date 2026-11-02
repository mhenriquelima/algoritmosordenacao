
package ed2.projeto.algoritmosordenacao;

/**
 * 
 * @author Hilario Tomaz Alves de Oliveira
 *
 */

public class BubbleSort implements IAlgoritmoOrdenacao {

  @Override
	
  public void ordenarVetor(int[] vetor) {

    boolean isTroca;

    int tamanhoVetorMenosUm = vetor.length - 1;
	
    do {
		    	
	  isTroca = false;
		
	  for(int i = 0; i < tamanhoVetorMenosUm ; i++) {
		    	  
		if( vetor[i] > vetor[i + 1] ) {
		        	
		  int aux = vetor[i];
		  
		  vetor[i] = vetor[i + 1];
		  
		  vetor[i + 1] = aux;
		  
		  isTroca = true;
		  
		}
		
	  } // FOR ELEMENTOS VETOR
		
    } while( isTroca );
	
  }
  
  @Override
	
  public String toString() {
	
    return "BubbleSort";
    
  }
	
}
