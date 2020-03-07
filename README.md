# Analisador Sintáctico para Língua Portuguesa em Python

## Introdução
Este analisador sintáctico para língua portuguesa utiliza a biblioteca Python **NLTK**, para fazer a análise sintáctica de uma frase escrita em língua portuguesa retornando a sua árvore sintáctica, isto é, está implementado de forma a identificar num determinado texto:

-   Frase
-   Oração Relativa
-   Sintagma nominal
-   Sintagma verbal
-   Sintagma proposicional 


## Processo de Análise Sintáctica

A primeira parte passa por identificar a classe da palavra, para perceber se é um nome, verbo ou adjectivo por exemplo E assim chamamos isto de dar um *tag* a cada palavra num determinado texto. Para isso utilizei o sub-módulo floresta, que contém uma base de dados de palavras já associadas a um tag. Utilizei então esta base de dados, e os taggers [1] que já existem na biblioteca **NLTK** para treinar o modelo que faz o tagging das palavras do meu input de texto. 

> Nota: Segundo os Documento do NLTK, o tagger2 desta função tem uma precisão de 87,02% aproximadamente. Ou seja, existe uma percentagem de cerca de 13% de esta atribuir mal a tag à palavra.

Após ter as palavras já associadas a tags, defini um conjunto de regras de análise sintáctica que são utilizadas pelo parser do **NLTK** que antes transforma as seguintes regras em gramática: 

Regras: 
>F -> SN | SN SV | SN OR SV

>OR -> SP V

>SV -> V | V SN SP | V SN | V adj | V adj SP | V SP | V V | V V SN

>SP -> prp SN | pron-indp SN

>V -> v-pcp | v-inf | v-ger | v-fin | v-pcp

>SN -> art n | n

Após ter estas regras, implementei outras funções auxiliares que adicionam então as palavras do input de texto, as quais anteriormente tínhamos atribuído a tag e adiciona estas palavras à sua respectiva regra. Por exemplo, na frase: 
   
- O João gosta de Python. 

O programa irá adicionar as classes __art__, __n__, e __prp__ ás regras, e adicionar também as respectivas palavras:

- prp-> "de"

será adicionada às regras, bem como todas as palavras contidas no input. Por fim, o programa retornará então a árvore sintáctica da frase.

> Nota: Para ver mais exemplos executar o Python Notebook: `syntax-parser-notebook.ipynb`


Para executar: 
- `%run app.py` (via Jupyter Notebook)
- `parse_text("o João gosta de Python")`

output:
> Tree: 
   (F
  (SN (art o) (n João))
  (SV (V (v-fin gosta)) (SP (prp de) (SN (n Python)))))


## Resumo e trabalho futuro

Foi bastante desafiante fazer este trabalho e gratificante terminar os objectivos que desenhei inicialmente, pois a informação disponível online para Processamento de Língua Natural e __NLTK__ está essencialmente escrita em inglês daí tive que fazer uma adaptação à língua Portuguesa.
Escolhi seguir um caminho diferente e fazer a população automática da gramática para tornar o programa mais interactivo, ou seja, adicionando estas palavras programaticamente, o analisador permite a análise de milhares de frases diferentes, de todas aquelas em que as palavras estejam inseridas no módulo floresta do NLTK e não só daquelas que eu adicionasse num dicionário. Como ponto negativo, o analisador pode não ser totalmente fidigno uma vez que o tagger que utilizei tem uma precisão de 87,02% aproximadamente, ou seja, pode atribuir uma classe errada a uma determinada palavra numa frase.

Penso que o trabalho está muito bom, tendo em conta os objectivos deste trabalho e haverá sempre um grande campo a explorar no que toca a refinar estes algoritmos do analisador sintáctico pois como se sabe no processamento de língua natural, a ambiguidade é ainda um problema por resolver.


## Bibliografia

 1 - Treinar o modelo tagger e tokenize das palavras -> http://www.nltk.org/howto/portuguese_en.html
 
 2 - Regras de Gramática, Capitulo 3 -> https://www.nltk.org/book/ch08.html
