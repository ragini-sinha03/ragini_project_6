"""
ragini_visual_consumer.py - Ragini's Visual Consumer with Matplotlib Animation

A consumer that creates real-time animated visualizations of streaming data.
Shows dynamic insights including message counts, timing patterns, and data trends.
Created by Ragini for demonstrating streaming analytics with visual dashboards.
"""

import json
import time
from pathlib import Path
import sys
import os
from datetime import datetime, timedelta
from collections import deque
import threading

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib
try:
    matplotlib.use('TkAgg')  # Try TkAgg first
except:
    try:
        matplotlib.use('Qt5Agg')  # Try Qt5Agg
    except:
        matplotlib.use('Agg')  # Fallback to non-GUI backend
        print("⚠️  No GUI backend available. Try running in Windows PowerShell instead.")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.dates import DateFormatter
import pandas as pd

import utils.utils_config as config
from utils.utils_logger import logger

# Global data storage for visualization
message_times = deque(maxlen=50)  # Store last 50 message timestamps
message_counts = deque(maxlen=50)  # Store cumulative message counts
authors = {}  # Track messages by author
sentiment_data = deque(maxlen=30)  # Store sentiment values
message_lengths = deque(maxlen=30)  # Store message lengths

class StreamingDataVisualizer:
    def __init__(self):
        self.fig, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        self.fig.suptitle('Ragini\'s Real-Time Streaming Data Dashboard', fontsize=16, fontweight='bold')
        
        # Configure subplots
        self.setup_plots()
        
        # Data reading thread
        self.running = True
        self.data_thread = threading.Thread(target=self.read_data_continuously)
        self.data_thread.daemon = True
        
    def setup_plots(self):
        """Configure all subplot layouts and labels"""
        
        # Plot 1: Message Flow Over Time
        self.ax1.set_title('Message Flow Over Time', fontweight='bold', pad=20)
        self.ax1.set_xlabel('Time')
        self.ax1.set_ylabel('Cumulative Messages')
        self.ax1.grid(True, alpha=0.3)
        
        # Plot 2: Messages by Author
        self.ax2.set_title('Messages by Author', fontweight='bold', pad=20)
        self.ax2.set_xlabel('Author')
        self.ax2.set_ylabel('Message Count')
        
        # Plot 3: Sentiment Analysis
        self.ax3.set_title('Sentiment Trends', fontweight='bold', pad=20)
        self.ax3.set_xlabel('Message Sequence')
        self.ax3.set_ylabel('Sentiment Score')
        self.ax3.set_ylim(0, 1)
        self.ax3.grid(True, alpha=0.3)
        
        # Plot 4: Message Length Distribution
        self.ax4.set_title('Message Length Analysis', fontweight='bold', pad=20)
        self.ax4.set_xlabel('Message Length (characters)')
        self.ax4.set_ylabel('Frequency')
        
        plt.tight_layout()
        
    def read_data_continuously(self):
        """Background thread to continuously read new data"""
        data_dir = Path("data")
        file_sources = [
            data_dir / "simple_messages.jsonl",
            data_dir / "project_live.json",
            data_dir / "demo.jsonl"
        ]
        
        processed_lines = {str(f): 0 for f in file_sources}
        
        while self.running:
            try:
                for file_path in file_sources:
                    if file_path.exists():
                        self.read_new_messages(file_path, processed_lines)
                time.sleep(2)  # Check for new data every 2 seconds
            except Exception as e:
                logger.error(f"Error reading data: {e}")
                time.sleep(5)
    
    def read_new_messages(self, file_path, processed_lines):
        """Read only new messages from file"""
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
                
            # Process only new lines
            start_line = processed_lines[str(file_path)]
            new_lines = lines[start_line:]
            
            for line in new_lines:
                if line.strip():
                    try:
                        message = json.loads(line.strip())
                        self.process_message(message)
                    except json.JSONDecodeError:
                        continue
            
            # Update processed line count
            processed_lines[str(file_path)] = len(lines)
            
        except Exception as e:
            logger.error(f"Error reading {file_path}: {e}")
    
    def process_message(self, message):
        """Process a new message and update data structures"""
        current_time = datetime.now()
        
        # Update message flow data
        message_times.append(current_time)
        message_counts.append(len(message_times))
        
        # Update author statistics
        author = message.get('author', 'Unknown')
        authors[author] = authors.get(author, 0) + 1
        
        # Update sentiment data
        sentiment = float(message.get('sentiment', 0.5))
        sentiment_data.append(sentiment)
        
        # Update message length data
        msg_length = int(message.get('message_length', len(str(message.get('message', '')))))
        message_lengths.append(msg_length)
        
        logger.info(f"📊 Processed message from {author}, sentiment: {sentiment:.2f}")
    
    def animate(self, frame):
        """Animation function called by matplotlib"""
        # Clear all axes
        for ax in [self.ax1, self.ax2, self.ax3, self.ax4]:
            ax.clear()
        
        # Reconfigure plots
        self.setup_plots()
        
        if not message_times:
            # Show "waiting for data" message
            self.ax1.text(0.5, 0.5, '⏳ Waiting for streaming data...\nRun ragini_producer.py first!', 
                         ha='center', va='center', transform=self.ax1.transAxes, fontsize=12)
            return
        
        # Plot 1: Message Flow Over Time
        if len(message_times) > 1:
            self.ax1.plot(list(message_times), list(message_counts), 
                         'b-o', linewidth=2, markersize=4, alpha=0.8)
            self.ax1.set_title(f'📈 Message Flow Over Time (Total: {len(message_times)})', 
                              fontweight='bold', pad=20)
        
        # Plot 2: Messages by Author
        if authors:
            author_names = list(authors.keys())
            author_counts = list(authors.values())
            bars = self.ax2.bar(author_names, author_counts, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
            self.ax2.set_title(f'👥 Messages by Author ({sum(author_counts)} total)', 
                              fontweight='bold', pad=20)
            
            # Add value labels on bars
            for bar, count in zip(bars, author_counts):
                self.ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                             str(count), ha='center', va='bottom', fontweight='bold')
        
        # Plot 3: Sentiment Trends
        if sentiment_data:
            sentiment_list = list(sentiment_data)
            x_range = range(len(sentiment_list))
            self.ax3.plot(x_range, sentiment_list, 'g-o', linewidth=2, markersize=4, alpha=0.8)
            
            # Add average line
            avg_sentiment = sum(sentiment_list) / len(sentiment_list)
            self.ax3.axhline(y=avg_sentiment, color='red', linestyle='--', alpha=0.7, 
                            label=f'Average: {avg_sentiment:.2f}')
            self.ax3.legend()
            
            # Color code sentiment zones
            self.ax3.axhspan(0.7, 1.0, alpha=0.2, color='green', label='Positive')
            self.ax3.axhspan(0.3, 0.7, alpha=0.2, color='yellow', label='Neutral')
            self.ax3.axhspan(0.0, 0.3, alpha=0.2, color='red', label='Negative')
            
            self.ax3.set_title(f'😊 Sentiment Trends (Avg: {avg_sentiment:.2f})', 
                              fontweight='bold', pad=20)
        
        # Plot 4: Message Length Distribution
        if message_lengths:
            lengths = list(message_lengths)
            self.ax4.hist(lengths, bins=10, color='purple', alpha=0.7, edgecolor='black')
            avg_length = sum(lengths) / len(lengths)
            self.ax4.axvline(x=avg_length, color='red', linestyle='--', linewidth=2, 
                            label=f'Average: {avg_length:.1f} chars')
            self.ax4.legend()
            self.ax4.set_title(f'📝 Message Length Analysis (Avg: {avg_length:.1f} chars)', 
                              fontweight='bold', pad=20)
        
        # Update timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fig.suptitle(f'🚀 Ragini\'s Real-Time Streaming Data Dashboard - Updated: {current_time}', 
                         fontsize=16, fontweight='bold')
    
    def start_visualization(self):
        """Start the visualization with animation"""
        logger.info("🎨 Starting Ragini's Visual Consumer Dashboard")
        logger.info("📊 Dashboard will update every 2 seconds")
        logger.info("🛑 Close the window or press Ctrl+C to stop")
        
        # Start data reading thread
        self.data_thread.start()
        
        # Start animation and keep reference
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=2000, cache_frame_data=False)
        
        try:
            plt.show(block=True)
        except KeyboardInterrupt:
            logger.info("🛑 Visualization stopped by user")
        except Exception as e:
            logger.error(f"Display error: {e}")
            logger.info("💡 Try running in Windows PowerShell instead of WSL")
        finally:
            self.running = False

def main():
    """Main function to run the visual consumer"""
    try:
        visualizer = StreamingDataVisualizer()
        visualizer.start_visualization()
    except Exception as e:
        logger.error(f"Error in visual consumer: {e}")
    finally:
        logger.info("👋 Ragini's Visual Consumer shut down")

if __name__ == "__main__":
    main()