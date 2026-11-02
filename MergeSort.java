
package ed2.projeto.algoritmosordenacao;

/**
 * 
 * @author Hilario Tomaz Alves de Oliveira
 *
 */

public class MergeSort implements IAlgoritmoOrdenacao {

  @Override
	
  public void ordenarVetor(int[] vetor) {
	
    this.mergeSort( vetor, 0, ( vetor.length - 1 ) );
  }

  public void mergeSort(int[] vetor, int inicio, int fim) {
	  
    int meio;
	    
    if( inicio < fim ) {
	    	
      meio = ( inicio + fim ) / 2;
      
      this.mergeSort( vetor, inicio, meio );
      this.mergeSort( vetor, meio + 1, fim );
	      
      this.intercala( vetor, inicio, fim, meio );
	      
    }
	    
  }
	  
  private void intercala(int[] vetor, int inicio, int fim, int meio) {
		
    int posLivre, inicioVetor1, inicioVetor2;
	    
    int aux[] = new int[vetor.length];
	    
    inicioVetor1 = inicio;
    inicioVetor2 = meio + 1;
	    
    posLivre = inicio;
	    
    while( ( inicioVetor1 <= meio ) && ( inicioVetor2 <= fim ) ) {
	    	
      if( vetor[inicioVetor1] <= vetor[inicioVetor2] ) {
	    	  
        aux[posLivre] = vetor[inicioVetor1];
	        
        inicioVetor1++; 
	        
      } else {
	    	  
        aux[posLivre] = vetor[inicioVetor2];
	        
        inicioVetor2++;
	        
      }
	     
      posLivre++;
	      
    } // WHILE
	    
    for(int i = inicioVetor1; i <= meio; i++) {
	    
      aux[posLivre] = vetor[i];
	      
      posLivre++;
	      
    } // FOR VETOR 1
	    
    for(int i = inicioVetor2; i <= fim; i++) {
	    	
      aux[posLivre] = vetor[i];
	      
      posLivre++;
	      
    } // FOR VETOR 2
	    
    for(int i = inicio; i <= fim; i++) {
	    	
      vetor[i] = aux[i];
	      
    } // FOR VETOR COMPLETO
	    	
  }

  @Override
	
  public String toString() {
	
	return "MergeSort";
	
  }
  
}
