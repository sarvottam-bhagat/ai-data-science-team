# Text-to-SQL Database Agent

A powerful AI-powered application that allows users to query SQL databases using natural language. This project leverages OpenAI's language models and LangChain to convert natural language questions into SQL queries and provide interactive data exploration capabilities.

## 🌟 Features

- Natural language to SQL query conversion
- Interactive chat interface using Streamlit
- Support for multiple database connections
- Built-in example questions for quick start
- Interactive data visualization and exploration
- Downloadable query results
- Support for multiple OpenAI models

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: SQLAlchemy (with SQLite support)
- **AI/ML**: 
  - OpenAI GPT models
  - LangChain
  - LangGraph
- **Data Processing**: Pandas

## 📋 Prerequisites

- Python 3.11
- OpenAI API key
- SQLite database (Northwind database included)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/sarvottam-bhagat/text-to-sql.git
cd text-to-sql
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Install the AI Data Science Team package:
```bash
pip install git+https://github.com/sarvottam-bhagat/ai-data-science-team.git --upgrade
```

## 💻 Usage

1. Set up your OpenAI API key in your environment variables.

2. Run the Streamlit application:
```bash
streamlit run app2.py
```

3. Access the application through your web browser (typically at `http://localhost:8501`).

4. Select your database from the sidebar options.

5. Start asking questions in natural language about your database!

## 📊 Example Questions

- "What tables exist in the database?"
- "What are the first 10 rows in the territory table?"
- "Aggregate sales for each territory."
- "Aggregate sales by month for each territory."

## 📁 Project Structure

```
text-to-sql/
├── app.py              # Main application file (original version)
├── app2.py             # Enhanced application file (current version)
├── setup.py            # Package setup configuration
├── requirements.txt    # Project dependencies
├── data/              # Database files directory
└── ai_data_science_team/ # Core AI/ML functionality package
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License

This project is licensed under the terms of the MIT license.

## 👥 Authors

- Sarvottam Bhagat

## 🙏 Acknowledgments

- OpenAI for providing the GPT models
- LangChain community for the excellent tools and frameworks
- Northwind database for sample data 