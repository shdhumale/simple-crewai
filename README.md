# simple-crewai
This repo shows the integration of crewai sequential with Googlg Gemini LLm
---

````markdown
# Simple CrewAI Example 🚀

This repository demonstrates a **minimal working example** of building agents and tasks using the [CrewAI](https://github.com/CrewAI-Inc/crewai) framework. It showcases how multiple agents can collaborate on tasks using LLMs to execute a defined workflow in a structured and sequential manner.

## 📌 Overview

This project is a hands-on implementation of a simple CrewAI workflow. It defines a set of agents, each with specific roles, and coordinates them to perform tasks as a team. Ideal for developers looking to understand or prototype with CrewAI's multi-agent capabilities.

---

## 🔧 Requirements

- Python 3.10+
- [CrewAI](https://github.com/CrewAI-Inc/crewai)
- LangChain
- OpenAI or compatible LLM provider

You can install dependencies using:

```bash
pip install -r requirements.txt
````

---

## 📂 Project Structure

```bash
simple-crewai/
├── agents/
│   ├── researcher.py      # Agent responsible for research tasks
│   └── writer.py          # Agent responsible for writing tasks
├── tasks/
│   ├── research_task.py   # Task assigned to the Researcher agent
│   └── write_task.py      # Task assigned to the Writer agent
├── crew.py                # Orchestrates agents and tasks
├── main.py                # Entry point to run the crew
├── .env                   # API keys and environment configs
└── requirements.txt       # Python dependencies
```

---

## 🚀 How to Run

1. Clone the repo:

```bash
git clone https://github.com/shdhumale/simple-crewai.git
cd simple-crewai
```

2. Set your environment variables in `.env`:

```env
OPENAI_API_KEY=your_openai_key
```

3. Run the application:

```bash
python main.py
```

You’ll see the crew agents take on their roles, perform their tasks, and collaborate to complete the workflow.

---

## 👨‍💻 Agents

* **ResearcherAgent**: Gathers information or performs analysis.
* **WriterAgent**: Creates structured output (e.g., blog posts, reports) based on research.

---

## 🧠 Tasks

* **ResearchTask**: Investigates a given topic and provides detailed findings.
* **WriteTask**: Converts research findings into polished output.

---

## 📘 Example Output

```
[ResearcherAgent]: Completed research on AI trends.
[WriterAgent]: Drafted an article summarizing the findings.
```

---

## 🛠️ Customization

You can add new agents or tasks by modifying or extending the files under `agents/` and `tasks/`. Update `crew.py` to include them in the orchestration logic.

---

## 📄 License

This project is open-sourced under the MIT License.

---

## 🤝 Acknowledgements

* [CrewAI](https://github.com/CrewAI-Inc/crewai)
* [LangChain](https://github.com/langchain-ai/langchain)
* OpenAI LLMs

---

## 🌟 Star This Repo

If you found this useful, consider starring the repository to support the project!

```

---

Let me know if you'd like to add example logs, demo GIFs, or a deployment section.
```

