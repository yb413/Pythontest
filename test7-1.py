from PIL import Image
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = "SimHei"

img = Image.open("lena.tiff")
img_r,img_g,img_b = img.split()
plt.figure(figsize=(10,10))

plt.subplot(221)
plt.axis("off")
plt.imshow(img_r.resize((50,50)),cmap="gray")
plt.title("R-缩放",fontsize=14)

plt.subplot(222)
plt.imshow(img_g.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270),cmap="gray")
plt.title("G-镜像+旋转",fontsize=14)

plt.subplot(223)
plt.axis("off")
plt.imshow(img_b.crop((0,0,150,150)),cmap="gray")
plt.title("B-裁剪",fontsize=14)

plt.subplot(224)
plt.axis("off")
img_rgb = Image.merge("RGB",[img_r,img_g,img_b])
plt.imshow(img_rgb)
plt.title("RGB",fontsize=14)

plt.suptitle("图画基本操作",fontsize=20,color="b")
plt.tight_layout(rect=(0,0,1,0.9))
plt.show()
img_rgb.save("test.png")