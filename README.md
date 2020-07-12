# bolsaParser
Parser para dados extraídos do site da bolsa de valores brasileira (http://www.b3.com.br/), transformando em CSV.

Modo de uso:

bolsa_parser.py

1) Jogar o script em uma pasta contendo os arquivos com dados da bolsa com extensao .txt.
2) python bolsa_parser.py

A saída será jogada na pasta dados_csv, os dados estarão todos em um único grande arquivo.


bolsa_parser_pool.py (Utiliza todos os núcleos do processador disponíveis para parsear os dados.

1) Jogar o script em uma pasta contendo os arquivos com dados da bolsa com extensao .txt.
2) python bolsa_parser_pool.py

A saída será jogada na pasta dados_csv, os dados estarão em arquivos com o mesmo nome dos arquivos de entrada, no formato CSV.


