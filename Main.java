package ed2.projeto.algoritmosordenacao;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int escolha;
        String entrada;

        IAlgoritmoOrdenacao algoritmoOrdenacao;

        do {
            // Menu
            System.out.println("Escolha o algoritmo de ordenação:");
            System.out.println("1. Bubble Sort");
            System.out.println("2. Insertion Sort");
            System.out.println("3. Selection Sort");
            System.out.println("4. Merge Sort");
            System.out.println("5. Quick Sort");
            System.out.println("0. Sair");
            do {
                System.out.print("Digite sua escolha: ");
                entrada = sc.nextLine().trim();
                if (!entrada.matches("[0-5]")) {
                    System.out.println("Escolha inválida. Por favor, digite um número entre 0 e 5.");
                }
            } while (!entrada.matches("[0-5]"));
            escolha = Integer.parseInt(entrada);
            

            switch (escolha) {
                case 1:
                    algoritmoOrdenacao = new BubbleSort();
                    break;

                case 2:
                    algoritmoOrdenacao = new InsertionSort();
                    break;

                case 3:
                    algoritmoOrdenacao = new SelectionSort();
                    break;

                case 4:
                    algoritmoOrdenacao = new MergeSort();
                    break;

                case 5:
                    algoritmoOrdenacao = new QuickSort();
                    break;

                case 0:
                    System.out.println("Saindo do programa.");
                    sc.close();
                    return;
        
                default:
                    System.out.println("Escolha inválida. Quick Sort será utilizado como padrão.");
                    algoritmoOrdenacao = new QuickSort();
                    break;
            }
            
            System.out.printf("Você escolheu o algoritmo: %s%n", algoritmoOrdenacao.toString());
            sc.close();

        } while (escolha != 0);
    
    }
}