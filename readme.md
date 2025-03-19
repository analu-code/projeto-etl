# Projeto de ETL - Análise, validação e visualização

## 📌 Descrição do Projeto
Este projeto foi desenvolvido durante um workshop de ETL com Python (https://www.youtube.com/watch?v=JuOyNPjAer8) e tem como objetivo realizar uma análise exploratória de dados, validar dados e disponibilizar uma interface para visualização dos resultados.

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Excel**
- **Streamlit**
- **Pydantic**
- **Pandas**
- **Pandas Profiling**
- **Plotly**

## 🔹 Funcionalidades
O projeto original inclui as seguintes funcionalidades principais:
- **Análise Exploratória:** Utilização do Pandas Profiling para gerar um relatório detalhado dos dados.
- **Validação de Dados:** Uso do Pydantic para definir contratos de dados e garantir a integridade das informações.
- **Interfaces Interativas:** Foram criadas duas interfaces para interação, uma para validação dos dados e outra do tipo dashboard para visualização.

## 🚀 Melhorias Implementadas
Após a conclusão do workshop, realizei algumas "melhorias" no projeto:
- **Criação de um Aplicativo em Streamlit:** Unificando todas as funcionalidades em uma única aplicação.
- **Navegação via Tabs:** Ao invés de abrir múltiplos navegadores, as funcionalidades foram organizadas em abas dentro do Streamlit:
  - **Tab 1:** Validação de Dados
  - **Tab 2:** Análise Exploratória
  - **Tab 3:** Dashboard

## 📂 Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/analu-code/projeto-etl.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd projeto-etl
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

## 🚀 Sugestão de Melhoria
Implementar um botão de exportar em PDF a análise exploratória.

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizar e modificar conforme necessário.

---
📌 **Dúvidas ou sugestões?** Fique à vontade para contribuir ou entrar em contato!

