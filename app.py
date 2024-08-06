from app import create_app

app = create_app()

if __name__ == '__main__':
    # debug开启调试模型，修改代码会自动重启
    app.run(debug=True)
