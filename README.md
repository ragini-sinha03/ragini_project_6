# Ragini's Real-Time Streaming Data Analytics System

## 🚀 Project Overview

This project implements a complete **real-time streaming data analytics system** with dynamic visualization capabilities. Built on the foundation of buzzline-05-case, it demonstrates professional-grade streaming data processing with live animated dashboards.

### 🎯 Key Features

- **Real-time data streaming** with multiple producer/consumer implementations
- **Multi-sink data storage** (Files, SQLite, DuckDB, Kafka)
- **Live animated dashboard** with matplotlib animations
- **Professional data visualization** with sentiment analysis and trend monitoring
- **Scalable architecture** supporting both file-based and distributed streaming

### 📊 Dynamic Visual Dashboard

The system features a **4-panel real-time dashboard** that updates every 2 seconds:

1. **Message Flow Over Time**: Line chart showing cumulative message processing
2. **Messages by Author**: Bar chart displaying contributor activity distribution  
3. **Sentiment Trends**: Line chart with sentiment analysis and color-coded zones
4. **Message Length Analysis**: Histogram with statistical insights

![Ragini's Real-Time Streaming Dashboard](docs/dashboard-screenshot.png)
*Live dashboard showing real-time streaming analytics with 7,513 total messages processed*

## 🏗️ Architecture

### Data Pipeline Components

- **Producers**: Generate streaming data (`ragini_producer.py`, `producer_case.py`)
- **Emitters**: Single-responsibility functions for each sink type
- **Consumers**: Process and analyze streaming data (`ragini_consumer.py`, `ragini_visual_consumer.py`)
- **Sinks**: Multiple storage destinations (file, SQLite, DuckDB, Kafka)

### Streaming Flow
```
Data Sources → Producers → Emitters → [Files|SQLite|DuckDB|Kafka] → Consumers → Visualizations
```

--- 

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.11** (required for Kafka compatibility)
- **Git** for repository management
- **VS Code** (recommended IDE)

### 1. Environment Setup

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/WSL
# OR
.\.venv\Scripts\Activate.ps1  # Windows PowerShell

# Install dependencies
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt
```

### 2. Configuration Setup

```bash
# Copy environment configuration
cp .env.example .env
```

Key configuration settings:
- **Kafka Topic**: `buzzline_db`
- **Kafka Broker**: `localhost:9092`
- **Message Interval**: 5 seconds

### 3. Run Your Streaming Pipeline

#### Option A: File-Based Streaming (No Kafka Required)
```bash
# Terminal 1: Start the producer
python3 -m producers.ragini_producer

# Terminal 2: Start the visual consumer
python3 -m consumers.ragini_visual_consumer
```

#### Option B: Full Kafka Streaming
```bash
# Terminal 1: Start Kafka server (WSL/Linux)
cd ~/kafka
bin/kafka-server-start.sh config/kraft/server.properties

# Terminal 2: Run producer
python3 -m producers.producer_case

# Terminal 3: Run visual consumer
python3 -m consumers.ragini_visual_consumer
```

## 📈 Custom Components

### Ragini's Producer (`producers/ragini_producer.py`)
- Generates personalized "Hello World" messages with realistic metadata
- Writes to multiple sinks simultaneously (file, SQLite, DuckDB)
- Configurable message intervals and data patterns
- Includes sentiment analysis and message length statistics

### Ragini's Visual Consumer (`consumers/ragini_visual_consumer.py`)
- **Real-time matplotlib animations** updating every 2 seconds
- **Multi-threaded data reading** for continuous processing
- **4-panel dashboard** with professional styling and color coding
- **Dynamic statistics** including averages, totals, and trend analysis

## 🛠️ Technical Implementation

### Key Technologies
- **Python 3.11**: Core programming language
- **Matplotlib**: Real-time visualization and animation
- **Pandas**: Data processing and analysis
- **SQLite/DuckDB**: Local database storage
- **Kafka**: Distributed streaming (optional)
- **Threading**: Background data processing

### Performance Features
- **Deque-based data structures** for efficient memory management
- **Background threading** for non-blocking data collection
- **Configurable buffer sizes** (50 messages for time series, 30 for analysis)
- **Graceful error handling** with fallback mechanisms

## 📊 Dashboard Analytics

The visualization system provides real-time insights including:

- **Message Throughput**: Track processing velocity over time
- **Author Activity**: Monitor contributor engagement patterns  
- **Sentiment Analysis**: Analyze emotional trends with color-coded zones
- **Message Characteristics**: Statistical analysis of content patterns
- **System Health**: Real-time status and performance metrics

## 🔧 Advanced Features

### Multi-Backend Support
The visual consumer automatically detects and uses the best available matplotlib backend:
- **TkAgg**: Preferred for WSL/Linux environments
- **Qt5Agg**: Alternative GUI backend
- **Agg**: Fallback for headless environments

### Error Resilience
- Graceful degradation when Kafka is unavailable
- Automatic reconnection for data sources
- Comprehensive logging with sanitization
- User-friendly error messages and suggestions

## 🎯 Use Cases

This streaming system demonstrates patterns applicable to:

- **IoT Sensor Monitoring**: Real-time device data processing
- **Social Media Analytics**: Live sentiment and engagement tracking  
- **Financial Trading**: Market data streaming and analysis
- **Manufacturing**: Production line monitoring and quality control
- **Log Analysis**: System monitoring and alerting

## Task 1. Optional: Start Kafka for Full Streaming

In P2, you downloaded, installed, configured a local Kafka service.
Before starting, run a short prep script to ensure Kafka has a persistent data directory and meta.properties set up. This step works on WSL, macOS, and Linux - be sure you have the $ prompt and you are in the root project folder.

1. Make sure the script is executable.
2. Run the shell script to set up Kafka.
3. Cd (change directory) to the kafka directory.
4. Start the Kafka server in the foreground. Keep this terminal open - Kafka will run here.

```bash
chmod +x scripts/prepare_kafka.sh
scripts/prepare_kafka.sh
cd ~/kafka
bin/kafka-server-start.sh config/kraft/server.properties
```

**Keep this terminal open!** Kafka is running and needs to stay active.

For detailed instructions, see [SETUP_KAFKA](https://github.com/denisecase/buzzline-02-case/blob/main/SETUP_KAFKA.md) from Project 2. 

---

## Task 2. Manage Local Project Virtual Environment

Open your project in VS Code and use the commands for your operating system to:

1. Create a Python virtual environment.
2. Activate the virtual environment.
3. Upgrade pip and key tools. 
4. Install from requirements.txt.

### Windows

Open a new PowerShell terminal in VS Code (Terminal / New Terminal / PowerShell).
**Python 3.11** is required for Apache Kafka. 

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip wheel setuptools
py -m pip install --upgrade -r requirements.txt
```

If you get execution policy error, run this first:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Mac / Linux

Open a new terminal in VS Code (Terminal / New Terminal)

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade -r requirements.txt
```

---

## Task 3. Run Tests and Verify Emitters

In the same terminal used for Task 2, we'll run some tests to ensure that all four emitters are working fine on your machine.  All tests should pass if everything is installed and set up correctly. 

```shell
pytest -v
```

Then run the `verify_emitters.py` script as a module to check that we can emit to all four types. 
For the Kakfa sink to work, the Kafka service must be running. 

### Windows Powershell

```shell
py -m verify_emitters
```

### Mac / Linux

```shell
python3 -m verify_emitters
```

---

## Task 4. Start a New Streaming Application

This will take two terminals:

1. One to run the producer which writes messages using various emitters. 
2. Another to run each consumer. 

### Producer Terminal (Outputs to Various Sinks)

Start the producer to generate the messages. 

The existing producer writes messages to a live data file in the data folder.
If the Kafka service is running, it will try to write the messages to a Kafka topic as well.
For configuration details, see the .env file. 

In VS Code, open a NEW terminal.
Use the commands below to activate .venv, and start the producer. 

Windows:

```shell
.\.venv\Scripts\Activate.ps1
py -m producers.producer_case
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m producers.producer_case
```

NOTE: The producer will still work if the Kafka service is not available.

### Consumer Terminal (Various Options)

Start an associated consumer. 
You have options. 

1. Start the consumer that reads from the live data file.
2. Start the consumer that reads from the Kafka topic.
3. Start the consumer that reads from the SQLite relational data store. 
4. Start the consumer that reads from the DuckDB relational data store.

In VS Code, open a NEW terminal in your root project folder. 
Use the commands below to activate .venv, and start the consumer. 

Windows:
```shell
.\.venv\Scripts\Activate.ps1
py -m consumers.kafka_consumer_case
OR
py -m consumers.file_consumer_case
OR
py -m consumers.sqlite_consumer_case.py
OR
py -m consumers.duckdb_consumer_case.py
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m consumers.kafka_consumer_case
OR
python3 -m consumers.file_consumer_case
OR
python3 -m consumers.sqlite_consumer_case.py
OR
python3 -m consumers.duckdb_consumer_case.py
```

---

## Review the Project Code

Review the requirements.txt file. 
- What - if any - new requirements do we need for this project?
- Note that requirements.txt now lists both kafka-python and six. 
- What are some common dependencies as we incorporate data stores into our streaming pipelines?

Review the .env file with the environment variables.
- Why is it helpful to put some settings in a text file?
- As we add database access and passwords, we start to keep two versions: 
   - .env 
   - .env.example
 - Read the notes in those files - which one is typically NOT added to source control?
 - How do we ignore a file so it doesn't get published in GitHub (hint: .gitignore)

Review the .gitignore file.
- What new entry has been added?

Review the code for the producer and the two consumers.
 - Understand how the information is generated by the producer.
 - Understand how the different consumers read, process, and store information in a data store?

Compare the consumer that reads from a live data file and the consumer that reads from a Kafka topic.
- Which functions are the same for both?
- Which parts are different?

What files are in the utils folder? 
- Why bother breaking functions out into utility modules?
- Would similar streaming projects be likely to take advantage of any of these files?

## 🏆 Project Results

### Custom Streaming Pipeline Implementation

This project successfully implements a complete streaming data analytics system with the following achievements:

#### ✅ **Core Requirements Met**
- **Custom Producer/Consumer**: `ragini_producer.py` and `ragini_visual_consumer.py`
- **Multiple Data Sources**: JSON messages, files, SQLite, DuckDB databases
- **Dynamic Visualization**: Real-time matplotlib animations with 4-panel dashboard
- **Professional Presentation**: Well-captioned charts with statistical insights

#### 📊 **Live Dashboard Capabilities**
- **Real-time Updates**: Dashboard refreshes every 2 seconds with new data
- **Multi-dimensional Analytics**: Message flow, author distribution, sentiment trends, length analysis
- **Performance Metrics**: Processed 7,513+ messages with average sentiment of 0.65
- **Interactive Visualization**: Professional styling with color-coded zones and statistical overlays

#### 🔧 **Technical Excellence**
- **Modular Architecture**: Separate emitters for each sink type enable easy extensibility
- **Error Resilience**: Graceful handling of missing Kafka, GUI backend issues, and data source failures
- **Cross-platform Support**: Works on Windows PowerShell, WSL, and Linux environments
- **Memory Efficient**: Uses deque structures with configurable buffer limits

#### 🎯 **Business Value Demonstration**
- **Real-time Monitoring**: Live tracking of system metrics and user engagement
- **Trend Analysis**: Historical sentiment patterns and message characteristics
- **Scalable Design**: Architecture supports scaling from file-based to distributed Kafka streaming
- **Professional Quality**: Production-ready code with comprehensive logging and documentation

### Project Structure Analysis

**Producers Folder:**
- `producer_case.py`: Full-featured producer with realistic message generation
- `ragini_producer.py`: Personalized producer for learning and demonstration
- Both use the same emitter infrastructure but different message patterns

**Consumers Folder:**
- `ragini_consumer.py`: Text-based consumer for basic data reading
- `ragini_visual_consumer.py`: Advanced consumer with matplotlib animations
- Modular design allows for specialized processing while sharing core functionality

**Key Innovations:**
- **Background Threading**: Non-blocking data collection enables smooth animations
- **Multi-source Reading**: Consumers can read from files, databases, and Kafka simultaneously  
- **Dynamic Backend Selection**: Automatic matplotlib backend detection for maximum compatibility
- **Statistical Analysis**: Real-time calculation of averages, trends, and distributions

This streaming analytics system demonstrates enterprise-grade patterns suitable for IoT monitoring, social media analytics, financial trading, and manufacturing quality control applications.

---

## 📚 Learning Outcomes

Through building this project, key streaming data concepts were mastered:

- **Real-time Processing**: Understanding of continuous data flow patterns
- **Data Pipeline Architecture**: Producer/consumer patterns with multiple sinks
- **Visualization Techniques**: Animation and real-time dashboard development
- **System Integration**: Combining file-based and distributed streaming approaches
- **Performance Optimization**: Memory-efficient data structures and threading patterns

---

*Project developed by Ragini as part of streaming data analytics coursework, demonstrating professional-grade implementation of real-time data processing and visualization systems.*

---

## Explorations

- Did you run the kafka consumer or the live file consumer? Why?
- Can you use the examples to add a database to your own streaming applications? 
- What parts are most interesting to you?
- What parts are most challenging? 

---

## Verify DuckDB (Terminal Commands)

Windows PowerShell

```shell
# count rows
duckdb .\data\buzz.duckdb "SELECT COUNT(*) FROM streamed_messages;"

# peek
duckdb .\data\buzz.duckdb "SELECT * FROM streamed_messages ORDER BY id DESC LIMIT 10;"

# live analytics
duckdb .\data\buzz.duckdb "SELECT category, AVG(sentiment) FROM streamed_messages GROUP BY category ORDER BY AVG(sentiment) DESC;"
```

macOS/Linux/WSL

```shell
# count rows
duckdb data/buzz.duckdb -c "SELECT COUNT(*) FROM streamed_messages;"

# peek
duckdb data/buzz.duckdb -c "SELECT author, COUNT(*) c FROM streamed_messages GROUP BY author ORDER BY c DESC;"

# live analytics
duckdb data/buzz.duckdb -c "SELECT category, AVG(sentiment) FROM streamed_messages GROUP BY category ORDER BY AVG(sentiment) DESC;"

```

---

## How To Stop a Continuous Process

To kill the terminal, hit CTRL c (hold both CTRL key and c key down at the same time).

## Later Work Sessions

When resuming work on this project:

1. Open the project repository folder in VS Code. 
2. Start the Kafka service (use WSL if Windows) and keep the terminal running. 
3. Activate your local project virtual environment (.venv) in your OS-specific terminal.
4. Run `git pull` to get any changes made from the remote repo (on GitHub).

## After Making Useful Changes

1. Git add everything to source control (`git add .`)
2. Git commit with a -m message.
3. Git push to origin main.

```shell
git add .
git commit -m "your message in quotes"
git push -u origin main
```

## Save Space

To save disk space, you can delete the .venv folder when not actively working on this project.
You can always recreate it, activate it, and reinstall the necessary packages later.
Managing Python virtual environments is a valuable skill.

## License

This project is licensed under the MIT License as an example project.
You are encouraged to fork, copy, explore, and modify the code as you like.
See the [LICENSE](LICENSE.txt) file for more.

## Recommended VS Code Extensions

- Black Formatter by Microsoft
- Markdown All in One by Yu Zhang
- PowerShell by Microsoft (on Windows Machines)
- Python by Microsoft
- Python Debugger by Microsoft
- Ruff by Astral Software (Linter + Formatter)
- **SQLite Viewer by Florian Klampfer**
- WSL by Microsoft (on Windows Machines)
