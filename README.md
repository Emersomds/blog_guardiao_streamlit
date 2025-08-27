# 📊 Blog Guardião - Dashboard de Monitoramento

Este projeto é um **dashboard em Python com Streamlit** para monitorar os ataques detectados no sistema **Blog Guardião**.  
Ele lê os logs de segurança (`logs_ataques.txt` ou `attacks.csv`) e apresenta gráficos e métricas em tempo real.

---

## 🚀 Funcionalidades

- Leitura de logs do **Blog Guardião**
- Exibição de métricas em tempo real
- Gráficos interativos com Streamlit
- Exportação opcional para **CSV**

---

## 📂 Estrutura do Projeto

```
blog_guardiao_streamlit/
│── dashboard.py          # Arquivo principal do dashboard
│── requirements.txt      # Dependências do projeto
│── README.md             # Documentação
│── .gitignore            # Arquivos/pastas ignoradas pelo Git
```

---

## 🔧 Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/Emersomds/blog_guardiao_streamlit.git
cd blog_guardiao_streamlit
```

### 2. Crie o ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Rode o Streamlit
```bash
streamlit run dashboard.py
```

Depois, abra o navegador no endereço indicado (geralmente [http://localhost:8501](http://localhost:8501)).

---

## 🛡 Integração com Blog Guardião

O arquivo de logs do sistema **Blog Guardião** deve estar acessível (exemplo: `logs_ataques.txt`).  
O dashboard faz a leitura dos eventos registrados e exibe as métricas em tempo real.

---

## 📌 Tecnologias utilizadas

- Python 3
- Streamlit
- Pandas
- Matplotlib

---

## ✨ Autor

Desenvolvido por **Emerson Matos**  
📌 Projeto complementar ao **Blog Guardião**
