# **Real-Time Data Processing with Kafka, Spark Structered Streaming, and MongoDB**

## **Project Overview**

This project demonstrates a real-time data pipeline that integrates **Confluent Kafka**, **Spark Streaming** on a **Google Cloud Platform (GCP) Hadoop Cluster**, and **MongoDB**. The goal is to process and join streaming data from multiple Kafka topics and output the results into MongoDB for further analytics.

### **Key Technologies:**
- **Kafka**: Used for real-time data streaming.
- **Apache Spark**: Runs on a GCP Hadoop Cluster for distributed data processing.
- **MongoDB**: Stores processed data for fast querying and analytics.
- **Python**: Orchestrates the pipeline, interacting with Kafka, Spark, and MongoDB.

## **Project Architecture**

1. **Kafka Streaming:**
   - Kafka topics (`orders_topic_data_v1`, `payments_topic_data_v1`) serve as the data source.
   - Kafka Producers (`orders_producer.py` and `payment_producer.py`) stream data to the Kafka topics.

2. **Spark Streaming:**
   - **Apache Spark** consumes data from Kafka using the Kafka Spark Connector.
   - The data from `orders_topic_data_v1` and `payments_topic_data_v1` is joined on a common key and transformed.
   - Spark processes the data in real-time and outputs the results.

3. **MongoDB:**
   - The processed data is written to **MongoDB** using the MongoDB Spark Connector.
   - MongoDB acts as the storage layer, allowing for fast querying and analytics of the joined data.

## **Setup Instructions**

### **Prerequisites:**
- A **GCP account** with a Hadoop cluster (Dataproc) configured.
- **Confluent Kafka** instance setup with Kafka topics created.
- **MongoDB** instance (either local or cloud) for storing the results.
- Python 3.x installed.

### **Dependencies:**
To set up the project, make sure to install the following Python packages:

```bash
pip install kafka-python
pip install pyspark
pip install pymongo
```

### **Kafka Setup:**
1. Create Kafka topics `orders_topic_data_v1` and `payments_topic_data_v1` on your **Confluent Kafka** instance.
2. Use Kafka producers (`orders_producer.py` and `payment_producer.py`) to generate and stream data into the Kafka topics.

### **Spark Setup:**
1. Launch a **GCP Dataproc** cluster with Spark.
2. Ensure the **Kafka Spark Connector** is installed in the cluster. If not, install it using the following command:

```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 your_spark_job.py
```

### **MongoDB Setup:**
1. Set up a MongoDB instance (either local or cloud, e.g., MongoDB Atlas).
2. Ensure the MongoDB Spark Connector is available for Spark to write data to MongoDB.

## **How to Run the Project**

### **1. Start Kafka Producers**
Start the Kafka producers to begin streaming data into Kafka topics:

```bash
python orders_producer.py
python payment_producer.py
```

These producers will simulate real-time data being pushed into the Kafka topics.

### **2. Start the Spark Streaming Job**
Run the Spark job that reads the streaming data from Kafka in SSH browser of GCP cluster and processes it, and writes the results to MongoDB:

```bash
python join_stream.py
```

### **3. Verify Data in MongoDB**
Once the data is processed and written to MongoDB, you can use MongoDB Atlas to check if the data is induced:

## Project Workflow
1. **Kafka Streaming**: 
   - Data is produced by Kafka producers (`orders_producer.py` and `payment_producer.py`) and streamed into `orders_topic_data_v1` and `payments_topic_data_v1`.
   
2. **Apache Spark Streaming**:
   - Spark consumes data from these Kafka topics in real-time.
   - Data is joined on a common key and transformed as required.
   
3. **MongoDB Storage**:
   - The final joined data is written to MongoDB, allowing for fast querying and further analytics.

## Screenshots

### GCP Hadoop Cluster
![GCP Hadoop Cluster](/images/hadoop_cluster.jpg)

### GCP Bucket Checkpoint
![GCP Bucket Checkpoint](/images/checkpoint.jpg)

### Kafka Topics
![Kafka Topics - Orders](/images/kafka_topic_order.jpg)
![Kafka Topics - Payments](/images/kafka_topic_payment.png)

### Spark Job Execution in GCP Dataproc Console
![GCP Console](/images/gcp_console.jpg)

### Orders Data Producer
![Orders Data Producer](/images/orders_producer.jpg)

### Payments Data Producer
![Payments Data Producer](/images/payment_producer.jpg)

### MongoDB Results Dashboard
![MongoDB Dashboard](/images/mongo_db_output.jpg)

### Note on Payment Producer
The payment producer implemented here is a single row data producer created for learning purposes. It simulates how data is being generated and combined, giving you an understanding of the data flow. This is a preliminary step to help you grasp the fundamentals before attempting to simulate a continuous data stream in a real-world use case.

The goal is to first comprehend how individual data points are generated, processed, and combined before scaling up to a more complex, continuous data production model.

## Future Enhancements
- **Error Handling & Fault Tolerance**: Implement better error handling and resilience strategies, such as retry mechanisms and better logging.
- **Scalability**: Optimize Spark job configuration to handle larger volumes of data more efficiently.
- **Real-time Analytics**: Integrate real-time dashboards for monitoring the processed data stored in MongoDB.
