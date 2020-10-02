# Databricks notebook source
import random

for i in range(10):
  try:
    if i == 0:
      r_number = "42"
    elif random.random() > 0.5:
      r_number = "not a number!"
    else:
      r_number = str(random.randint(0, 100))
      
    retValue = dbutils.notebook.run("./Data Functions", 60, {"r_number": r_number})
    print(f"At step {i} for value '{r_number}' we've got: {retValue}")
  except Exception as e:
    print(f"We've got the error: {e}")