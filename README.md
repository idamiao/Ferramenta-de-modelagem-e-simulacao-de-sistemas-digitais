# Ferramenta-de-modelagem-e-simulacao-de-sistemas-digitais

Este projeto foi desenvolvido com o objetivo de achar uma alternativa que permite apresentar o comportamento temporal de sistemas projetados no software LogiSim, 
para isto foi desenvolvido uma ferramenta que mostra as formas de ondas dos sistemas implementados no LogiSim®,
esta ferramenta foi desenvolvida na linguagem Python por ser uma linguagem de alto nível e interpretada.


*Funcionamento*
A ferramenta de geração de gráficos é dada de forma separada ao LogiSim®, 
para o mesmo ser utilizado, deve-se primeiro construir um circuito na área principal do LogiSim®, com no mínimo uma entrada e uma saída. 
O usuário deve inserir um estado possível nas entradas do circuito, e o mesmo se encarrega em calcular os valores das saídas do circuito 
para que posteriormente seja possível desenhar gráficos que representam a forma temporal das entradas e saídas do circuito implementado.
Posto que o usuário inseriu um ou mais estados no circuito e os mesmos dados estejam contidos na tabela manual, é possível salvar essa tabela em um arquivo 
num formato que permite ser lido em um código Python, assim, é possível desenhar os gráficos conforme os dados que estão guardados no arquivo.

A ferramenta recebe o arquivo no modo de leitura e os dados que estão dentro do arquivo são desenhados por uma função, 
e são exibidas na ferramenta de geração de gráficos do Python (Tkinter). Toda vez que for adentrado um novo estado no circuito
ela deve ser gravada, e a ferramenta se incumbe de representar e acrescentar esse novo estado ao diagrama temporal já existente.

A ferramenta de geração de gráficos, pode exibir um elevado número de entradas e saídas, mas para a melhor exibição e compreensão do comportamento do circuito,
não é recomendável que se exibam mais de 9 gráficos.
