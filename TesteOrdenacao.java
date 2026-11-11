
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Random;

public class TesteOrdenacao {

  private static final long SEMENTE = 42L;

  private static int totalTestes = 0;
  private static int totalFalhas = 0;

  public static void main(String[] args) {

    IAlgoritmoOrdenacao[] algoritmos = {
      new BubbleSort(),
      new InsertionSort(),
      new SelectionSort(),
      new MergeSort(),
      new QuickSort()
    };

    Map<String, int[]> casos = criarCasosDeTeste();

    for (IAlgoritmoOrdenacao algoritmo : algoritmos) {

      int falhasAntes = totalFalhas;

      for (Map.Entry<String, int[]> caso : casos.entrySet()) {
        testar(algoritmo, caso.getKey(), caso.getValue());
      }

      testarVetoresAleatorios(algoritmo);

      String status = (totalFalhas == falhasAntes) ? "OK" : "FALHOU";
      System.out.printf("%-15s %s%n", algoritmo, status);

    }

    System.out.println();
    System.out.printf("%d testes executados, %d falha(s).%n", totalTestes, totalFalhas);

    if (totalFalhas > 0) {
      System.exit(1);
    }

  }


  private static Map<String, int[]> criarCasosDeTeste() {

    Map<String, int[]> casos = new LinkedHashMap<>();

    casos.put("vetor vazio",                new int[] {});
    casos.put("um elemento",                new int[] { 7 });
    casos.put("dois elementos ordenados",   new int[] { 1, 2 });
    casos.put("dois elementos invertidos",  new int[] { 2, 1 });
    casos.put("dois elementos iguais",      new int[] { 5, 5 });
    casos.put("já ordenado",                new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 });
    casos.put("ordem decrescente",          new int[] { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 });
    casos.put("todos iguais",               new int[] { 4, 4, 4, 4, 4, 4, 4 });
    casos.put("com repetidos",              new int[] { 3, 1, 3, 2, 1, 3, 2, 1 });
    casos.put("com negativos",              new int[] { -3, 5, 0, -10, 8, -1, 2 });
    casos.put("valores extremos",           new int[] { Integer.MAX_VALUE, 0, Integer.MIN_VALUE, -1, 1 });
    casos.put("tamanho ímpar",              new int[] { 9, 2, 7, 4, 5 });
    casos.put("tamanho par",                new int[] { 8, 3, 6, 1, 4, 2 });
    casos.put("menor no fim",               new int[] { 2, 3, 4, 5, 6, 1 });
    casos.put("maior no início",            new int[] { 6, 1, 2, 3, 4, 5 });
    casos.put("zigue-zague",                new int[] { 1, 9, 2, 8, 3, 7, 4, 6, 5 });

    int[] grandeDecrescente = new int[2000];
    for (int i = 0; i < grandeDecrescente.length; i++) {
      grandeDecrescente[i] = grandeDecrescente.length - i;
    }
    casos.put("2000 elementos decrescentes", grandeDecrescente);

    return casos;

  }


  private static void testarVetoresAleatorios(IAlgoritmoOrdenacao algoritmo) {

    Random random = new Random(SEMENTE);

    for (int tamanho = 0; tamanho <= 100; tamanho++) {
      testar(algoritmo, "aleatório (repetidos) tam=" + tamanho, gerar(random, tamanho, 10));
    }

    int[] tamanhos = { 50, 128, 500, 1000, 5000 };
    for (int tamanho : tamanhos) {
      testar(algoritmo, "aleatório (amplo) tam=" + tamanho, gerarAmplo(random, tamanho));
    }

    testar(algoritmo, "Utils.gerarVetor(1000, 100)", Utils.gerarVetor(1000, 100));

  }

  private static int[] gerar(Random random, int tamanho, int limite) {
    int[] vetor = new int[tamanho];
    for (int i = 0; i < tamanho; i++) {
      vetor[i] = random.nextInt(limite);
    }
    return vetor;
  }

  private static int[] gerarAmplo(Random random, int tamanho) {
    int[] vetor = new int[tamanho];
    for (int i = 0; i < tamanho; i++) {
      vetor[i] = random.nextInt();
    }
    return vetor;
  }


  private static void testar(IAlgoritmoOrdenacao algoritmo, String descricao, int[] original) {

    totalTestes++;

    int[] esperado = original.clone();
    Arrays.sort(esperado);

    int[] obtido = original.clone();

    try {
      algoritmo.ordenarVetor(obtido);
    } catch (RuntimeException e) {
      falha(algoritmo, descricao, original, "lançou " + e);
      return;
    }

    if (!Arrays.equals(esperado, obtido)) {
      falha(algoritmo, descricao, original,
            "esperado " + resumo(esperado) + " mas obteve " + resumo(obtido));
    }

  }

  private static void falha(IAlgoritmoOrdenacao algoritmo, String descricao, int[] entrada, String detalhe) {
    totalFalhas++;
    System.out.printf("  [FALHA] %s - %s%n    entrada: %s%n    %s%n",
                      algoritmo, descricao, resumo(entrada), detalhe);
  }

  private static String resumo(int[] vetor) {
    if (vetor.length <= 20) {
      return Arrays.toString(vetor);
    }
    return Arrays.toString(Arrays.copyOf(vetor, 20)).replace("]", ", ...] (" + vetor.length + " elementos)");
  }

}
