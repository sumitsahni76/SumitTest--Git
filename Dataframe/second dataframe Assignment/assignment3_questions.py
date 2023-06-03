# -*- coding: utf-8 -*-
"""Assignment3_Questions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mOb1jaAvCwaOrDSeIFXkPhDl_5gPIkGk

# Your Name:
..................................

# Assignment 3 (Olympics Data Analysis)

> Indented block

> Indented block




In this assignment you will analysis an Olympics dataset using PySpark.

# Olympics Dataset 
This data is a publicly available. The ***olympix_data.csv*** file is in the Blackboard.

# Dataset Description

This data set consists of the following fields:

***Athlete [0]***: Name of the athlete

***Age [1]***: Age of the athlete

***Country [2]***: The name of the country participating in Olympics

***Year [3]***: The year in which Olympics is conducted

***Closing Date [4]***: Closing date of Olympics

***Sport [5]***: Sports name

***Gold Medals [6]***: No. of gold medals

***Silver Medals [7]***: No. of silver medals

***Bronze Medals [8]***: No. of bronze medals

***Total Medals [9]***: Total no. of medals
"""

import findspark
findspark.init()

# create entry points to spark

"""## Q1: Write PySpark code to read olympix_data.csv file"""

var new1 = spark.read.format("csv").option("header","true").option("inferSchema","true").load("C://Users//xx//Desktop//project//Dataframe//second dataframe Assignment//olympix_data_organized_with_header.csv")
new1.show()

#read the data

"""## Q2: Write PySpark code to print the Olympic Sports/games in the dataset."""


var new1 = spark.read.format("csv").option("header","true").option("inferSchema","true").load("C://Users//xx//Desktop//project//Dataframe//second dataframe Assignment//olympix_data_organized_with_header.csv")
new1.show()
var distinct1 = new1.select(new1("sports")).distinct.show()



"""##Q3: Write PySpark code to plot the total number of medals in  each Olympic Sport/game. Sort the result based on the the total number of medals."""

var new1 = spark.read.format("csv").option("header","true").option("inferSchema","true").load("C://Users//xx//Desktop//project//Dataframe//second dataframe Assignment//olympix_data_organized_with_header.csv")
new1.show()
val result = new1.groupBy("country").agg(sum("total_medal")


//Q4: Find the total number of medals won by each country in swimming.

var new1 = spark.read.format("csv").option("header","true").option("inferSchema","true").load("C://Users//xx//Desktop//project//Dataframe//second dataframe Assignment//olympix_data_organized_with_header.csv")
new1.show()

val swim = new1.filter($"sports" === "Swimming")
 var result = swim.groupBy("country").agg(sum("total_medal")),show()

"""### Q5: Find the total number of medals won by each country in Skeleton."""

var skeleton = new1.filter($"sports" === "Skeleton")
var result = skeleton.groupBy("country").agg(sum("total_medal")).show()


"""### Q6 Find the number of medals that the US won yearly."""

 var US = new1.filter($"country" === "United States").groupBy("year").agg(sum("total_medal")).show()


"""### Q7 Find the total number of medals won by each country."""

var result1 = new1.groupBy("country").agg(sum("total_medal")).show()



"""### Q8 Who was the oldest athletic in the olympics? whcih country was he/she from?"""

var r1 = new1.agg(max("age")).show()


var filter1 = new1.filter($"age" === "61").toshow()




