# 摸鱼专区cookieClicker自动点击鹿和饼干

利用opencv截图，yolox动态识别鹿和饼干，pyautogui控制鼠标点击，无自动升级

```bash
# 下载依赖包，并安装yolox 此处不能使用代理，否则会连接异常
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -v -e .

# 测试yolox是否安装成功 根据选型使用对应的数据集及权重
python tools/demo.py image -f exps/default/yolox_tiny.py -c ./weights/yolox_tiny.pth --path assets/dog.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device gpu
```
