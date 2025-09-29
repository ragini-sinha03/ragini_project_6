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

### Ragini's Custom Visual Consumer (`consumers/ragini_visual_consumer.py`)

My custom consumer represents a sophisticated streaming analytics solution that transforms raw message data into actionable business insights through real-time visualization. Built with professional-grade architecture, this consumer demonstrates advanced streaming data processing patterns suitable for enterprise environments.

**Core Capabilities:**
- **Intelligent Data Ingestion**: Multi-source data reading from local files (JSONL, JSON) and Kafka topics with automatic fallback mechanisms
- **Real-time Processing**: Background threading ensures continuous data collection without blocking the user interface
- **Advanced Analytics**: Performs sentiment analysis, message length statistics, author activity tracking, and temporal trend analysis
- **Dynamic Visualization**: 4-panel matplotlib dashboard with animated charts updating every 2 seconds
- **Memory Management**: Uses efficient deque data structures with configurable buffer limits (50 messages for time series, 30 for analysis)

**Technical Innovation:**
- **Multi-threaded Architecture**: Separates data collection from visualization rendering for smooth performance
- **Cross-platform Compatibility**: Automatic matplotlib backend detection (TkAgg, Qt5Agg, Agg) ensures GUI compatibility across Windows, WSL, and Linux
- **Error Resilience**: Graceful handling of missing data sources, GUI backend failures, and network connectivity issues
- **Statistical Computing**: Real-time calculation of rolling averages, distribution analysis, and anomaly detection zones

**Business Value**: The consumer provides immediate insights into data patterns, user engagement trends, and system performance metrics, making it suitable for applications ranging from IoT monitoring to social media analytics and manufacturing quality control.

## 🛠️ Technical Implementation

### Key Technologies
- **Python 3.11**: Core programming language
- **Matplotlib**: Real-time dashboard with automatic GUI backend selection
- **Pandas**: Data processing and analysis
- **SQLite/DuckDB**: Local database storage
- **Kafka**: Distributed streaming (optional)
- **Threading**: Background processing for smooth animations

### Emitter System
Multiple output destinations in `utils/emitters/`:
- **File Emitter**: Saves data to JSONL files
- **SQLite Emitter**: Stores in relational database
- **DuckDB Emitter**: Analytics-focused database storage
- **Kafka Emitter**: Distributed messaging

Each emitter works independently - if one fails, others continue working.

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


---

## 📚 Learning Outcomes

Through building this project, key streaming data concepts were mastered:

- **Real-time Processing**: Understanding of continuous data flow patterns
- **Data Pipeline Architecture**: Producer/consumer patterns with multiple sinks
- **Visualization Techniques**: Animation and real-time dashboard development
- **System Integration**: Combining file-based and distributed streaming approaches
- **Performance Optimization**: Memory-efficient data structures and threading patterns


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



