import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Railway! Your Flask app is running successfully."


if __name__ == "__main__":
    # 读取 Railway 分配的 PORT 环境变量
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
