from glob import glob

saved_path = "datasets/VOCdevkit/VOC2012/"
txtsavepath = saved_path + "ImageSets/Main/"


ftest = open(txtsavepath + '/test.txt', 'w')
ftrain = open(txtsavepath + '/train.txt', 'w')
fval = open(txtsavepath + '/val.txt', 'w')


test_files = glob("./datasets/VOCdevkit/VOC2012/test/*.jpg")
test_files = [i.replace("\\", "/").split("/")[-1].split(".jpg")[0] for i in test_files]
train_files = glob("./datasets/VOCdevkit/VOC2012/train/*.jpg")
train_files = [i.replace("\\", "/").split("/")[-1].split(".jpg")[0] for i in train_files]
val_files = glob("./datasets/VOCdevkit/VOC2012/valid/*.jpg")
val_files = [i.replace("\\", "/").split("/")[-1].split(".jpg")[0] for i in val_files]
for file in test_files:
  print(file)
  ftest.write(file + "\n")
for file in train_files:
  print(file)
  ftrain.write(file + "\n")
for file in val_files:
  print(file)
  fval.write(file + "\n")