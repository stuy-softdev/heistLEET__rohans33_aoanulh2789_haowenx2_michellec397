# Rohan Sen, Haowen Xiao, Michelle Chen, Aoanul Hoque
# HeistLEET
# SoftDev
# P00
# 2025-10-28
# time spent: 0.67

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "code"

if __name__ == "__main__":
    app.run()
