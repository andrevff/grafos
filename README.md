# Algoritmos de Caminho Mínimo em Grafos
Os algoritmos de caminho mínimo são utilizados para encontrar o caminho de menor custo entre dois vértices em um grafo ponderado. Três dos algoritmos mais comuns para resolver esse tipo de problema são o algoritmo de Dijkstra, o algoritmo de Bellman-Ford e o algoritmo de Floyd-Warshall.

## Algoritmo de Dijkstra
O algoritmo de Dijkstra é usado para encontrar o caminho mais curto de um vértice de origem para todos os outros vértices em um grafo ponderado com pesos não negativos. Ele funciona da seguinte maneira:

<ol>
  <li>Inicialize uma distância mínima para todos os vértices como infinito e defina a distância mínima do vértice de origem como zero.</li>
  <li>Crie um conjunto de vértices não visitados.</li>
  <li>Enquanto houver vértices não visitados, selecione o vértice não visitado com a menor distância mínima.</li>
  <li>Atualize as distâncias mínimas dos vértices adjacentes ao vértice selecionado.</li>
  <li>Marque o vértice selecionado como visitado.</li>
  <li>Repita os passos 3 a 5 até que todos os vértices tenham sido visitados ou a distância mínima para o vértice de destino tenha sido encontrada.</li>
  <li>O algoritmo de Dijkstra garante a corretude quando todos os pesos das arestas são não negativos.</li>
</ol>

## Algoritmo de Bellman-Ford
O algoritmo de Bellman-Ford é utilizado para encontrar o caminho mais curto de um vértice de origem para todos os outros vértices em um grafo ponderado, mesmo quando existem arestas com pesos negativos. Ele opera da seguinte forma:

<ol>
  <li>Inicialize uma distância mínima para todos os vértices como infinito e defina a distância mínima do vértice de origem como zero.</li>
  <li>Repita o seguinte processo V-1 vezes, onde V é o número de vértices no grafo:</li>
  <ul>
    <li> Percorra todas as arestas do grafo e atualize as distâncias mínimas dos vértices adjacentes se um caminho mais curto for encontrado.</li>
  </ul>
  <li>Verifique se há ciclos de peso negativo no grafo. Se houver, o algoritmo não é aplicável, pois não é possível encontrar um caminho mínimo em um grafo com ciclos de peso negativo.</li>
  <li>O algoritmo de Bellman-Ford é mais lento do que o de Dijkstra, mas pode lidar com arestas de peso negativo.</li>
</ol>

## Algoritmo de Floyd-Warshall
O algoritmo de Floyd-Warshall é usado para encontrar os caminhos mínimos entre todos os pares de vértices em um grafo ponderado, mesmo quando existem arestas com pesos negativos. Ele segue os seguintes passos:

<ol>
  <li>Inicialize uma matriz de distâncias mínimas, onde a entrada (i, j) representa a distância mínima entre o vértice i e o vértice j.</li>
  <li>Inicialize a matriz de distâncias mínimas com valores infinitos, exceto para as entradas diagonais, que devem ser zero.</li>
  <li>Para cada vértice k, percorra todas as combinações de vértices i e j e atualize a matriz de distâncias mínimas se encontrar um caminho mais curto passando pelo vértice k.</li>
  <li>Após a conclusão do algoritmo, a matriz de distâncias mínimas conterá as distâncias mínimas entre todos os pares de vértices.</li>
</ol>

O algoritmo de Floyd-Warshall é mais eficiente do que o de Bellman-Ford para encontrar os caminhos mínimos entre todos os pares de vértices, mas pode ser menos eficiente que o de Dijkstra para encontrar caminhos mínimos de um único vértice de origem.
