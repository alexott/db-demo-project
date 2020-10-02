# Databricks notebook source
dbutils.widgets.text("r_number", "42", "Random number")

# COMMAND ----------

r_number = int(dbutils.widgets.get("r_number"))

if r_number == 42:
  returnValue = "Answer to the Ultimate Question of Life, the Universe, and Everything"
elif r_number > 50:
  returnValue = "Quite big value"
else:
  returnValue = "Some other value"

dbutils.notebook.exit(returnValue)

# COMMAND ----------

