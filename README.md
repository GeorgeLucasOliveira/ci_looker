# ci_looker

Vantagens:<br>
-Mantém um padrão mínimo de qualidade da criação das models e views <br>
-Mitiga falhas<br>
-Garante que todas as métricas e dimensões terão description<br>
-Enriquece o dicionário da sua instância do Looker<br>

Tutorial de implementação dos testes automatizados:
1) Dentro do repositório, clique na aba superior "Actions"
2) Clique no botão "New workflow"
3) Clique em "set up a workflow yourself"
4) De um nome para o worflow, no caso desse repositório, Yruka (Naruto <3)
5) Copie o conteúdo do yml que está nesse repositório no caminho -> /.github/workflows/iruka.yml e cole no novo workflow
6) Commite o novo workflow
7) Crie uma pasta no diretório chamada "tests" e dentro dela um arquivo chamado "test_files.py" (nele conterá os testes que as views e models serão submetidas)


Quando o build falha
![alt text](https://github.com/GeorgeLucasOliveira/ci_looker/blob/production/images_readme/open%20pull%20request%20failed.jpg)

No workflow temos os detalhes do erro
![alt text](https://github.com/GeorgeLucasOliveira/ci_looker/blob/production/images_readme/test_failed.jpg)


Dica: bloqueie a abertura da pull request quando o arquivo falhar
![alt text](https://github.com/GeorgeLucasOliveira/ci_looker/blob/production/images_readme/block%20if%20not%20build.jpg)
