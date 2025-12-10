import whisper


def main():
    # 加载whisper模型
    model = whisper.load_model("small")  
    print("模型加载成功:", model)
    
    # 测试打印
    print('测试输出: wefwfe')
    
    # 这里可以添加其他功能模块的调用
    

if __name__ == "__main__":
    # 这里的代码只有在模块作为主程序运行时才会执行
    main()
