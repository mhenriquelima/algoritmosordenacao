
package ed2.projeto.algoritmosordenacao;

/**
 * 
 * @author Hilario Tomaz Alves de Oliveira
 *
 */

public class QuickSort implements IAlgoritmoOrdenacao {

  public QuickSort() {

  }
  
  // Métodos
  
  @Override
	
  public void ordenarVetor(int[] vetor) {
	
    this.quickSort( vetor, 0, ( vetor.length - 1 ) );
    
  }

  public void quickSort(int[] vetor, int p, int r) {
	  
    int q;
	    
    if( p < r ) {
	    	
      q = this.particao( vetor, p, r );
	      
      this.quickSort( vetor, p, q );
      this.quickSort( vetor, q + 1, r );
	      
    }
	    
  }
	  
  private int particao(int vetor[], int p, int r) {
		  
    int pivo, i, j;
	    
    pivo = vetor[ ( p + r ) / 2 ];
	    
    i = p - 1;
    j = r + 1;
	    
    while( i < j ) {
	    	
      do {
	    	  
        j--;
	        
      } while( vetor[j] > pivo );

      do {
	    	  
        i++;
	        
      } while( vetor[i] < pivo );

      if( i < j ) {
	    	  
        this.troca( vetor, i, j );
	        
      }
	      
    } // WHILE
	    
    return j;
	    
  }
	  
  private void troca(int vetor[], int i, int j) {
		  
    int aux = vetor[i];
	    
    vetor[i] = vetor[j];
	    
    vetor[j] = aux;
	    
  }

  @Override
	
  public String toString() {
	
    return "QuickSort";
    
  }

}
