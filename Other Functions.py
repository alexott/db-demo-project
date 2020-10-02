# Databricks notebook source
import random

dbutils.notebook.exit("ERROR" if random.random() < 0.1 else "SUCCESS")