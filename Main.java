import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Main {

    public static void gerarArquivo(String nomeArquivo, int tamanhoVetor) {
        int[] vetor = Utils.gerarVetor(tamanhoVetor, tamanhoVetor * 10);
        try (BufferedWriter bf = new BufferedWriter(new FileWriter(nomeArquivo + ".txt"))) {
            for (int i = 0; i < vetor.length; i++) {
                bf.write(String.valueOf(vetor[i]));
                bf.newLine();
            }
        } catch (IOException e) {
            System.out.println("Erro ao criar o arquivo: " + e.getMessage());
        }
    }

    public static int[] lerArquivo(String nomeArquivo) {
        ArrayList<Integer> lista = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(nomeArquivo + ".txt"))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                lista.add(Integer.parseInt(linha));
            }
        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo: " + e.getMessage());
        }
        return lista.stream().mapToInt(i -> i).toArray();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        gerarArquivo("numeros", 100000);
        int[] vetor = lerArquivo("numeros");
        
        int escolha;
        String entrada;
        long tempoExecucao = 0;

        IAlgoritmoOrdenacao algoritmoOrdenacao;

        do {
            int [] vetorCopia = vetor.clone();
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

            // Ordenação
            long tempoInicial = System.currentTimeMillis();

            algoritmoOrdenacao.ordenarVetor(vetorCopia);

            long tempoFinal = System.currentTimeMillis();
            tempoExecucao = tempoFinal - tempoInicial;

            System.out.printf("Tempo de execução: %d milissegundos%n", tempoExecucao);
            System.out.println("Vetor inicial: (Caso maior de 100 elementos, apenas os 100 primeiros serão exibidos)");
            Utils.imprimirVetor(vetor, 100);
            System.out.println("\nVetor ordenado: (Caso maior de 100 elementos, apenas os 100 primeiros serão exibidos)");
            Utils.imprimirVetor(vetorCopia, 100);
            

        } while (escolha != 0);
        sc.close();
    }
}