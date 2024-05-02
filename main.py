import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set_theme(style="darkgrid")


fig = plt.figure(figsize=(10, 5))
tips = sns.load_dataset("tips")
sns.relplot(data=tips, x="total_bill", y="tip", hue="smoker")
