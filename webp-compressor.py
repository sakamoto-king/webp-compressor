import os
from PIL import Image

# 处理单张照片压缩并转换为webp
def compress_image(input_path, output_path, quality=80):
    file_form = "webp"
    try:
        image = Image.open(input_path)
        output_path = os.path.splitext(output_path)[0] + "." + file_form  # 修改输出文件的文件扩展名为 .webp
        image.save(output_path, file_form , quality=quality)
        print(f"Image compressed: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Failed to compress image: {input_path}")
        print(str(e))

# 封装单照片压制为文件夹照片压制
def compress_images_in_directory(input_dir, output_dir, quality=80):
    # 检查并创建目标路径
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Output directory created: {output_dir}")

    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            input_path = os.path.join(root, filename)
            output_path = os.path.join(output_dir, os.path.relpath(input_path, input_dir))
            output_dirname = os.path.dirname(output_path)

            if not os.path.exists(output_dirname):
                os.makedirs(output_dirname)

            compress_image(input_path, output_path, quality=quality)

# 设置输入和输出的文件夹
input_directory = r"D:\学习\编程\前端学习\aizaswim-banner"
output_directory = r"D:\学习\编程\前端学习\aizaswim-banner\output"

# 运行函数
compress_images_in_directory(input_directory, output_directory, quality=80)
