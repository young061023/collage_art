from PIL import Image

def generate_image_grid(input_image_path, output_image_path):

    original_image = Image.open(input_image_path)

    width, height = original_image.size

    mirrored_lr = original_image.transpose(Image.FLIP_LEFT_RIGHT)
    mirrored_ud = original_image.transpose(Image.FLIP_TOP_BOTTOM)
    mirrored_both = original_image.transpose(Image.ROTATE_180)

    result_image = Image.new('RGB', (2*width, 2*height))

    result_image.paste(original_image, (0, 0))
    result_image.paste(mirrored_lr, (width, 0))
    result_image.paste(mirrored_ud, (0, height))
    result_image.paste(mirrored_both, (width, height))
    
    result_image.save(output_image_path)

input_image_path = 'crow1.png'
output_image_path = 'level1.jpg'

def cut_and_stack_images(level1_image_path, num_slices, level2_image_path):

    step1_image = Image.open(level1_image_path)
    width1, height1 = step1_image.size
    slice_height = height1 // num_slices

    new_image = Image.new('RGB', (width1, height1)) 
    for i in range(num_slices):
        y_start = i * slice_height
        y_end = (i + 1) * slice_height

        slice_image = step1_image.crop((0, y_start, width1, y_end))
        y_reverse_offset = new_image.height - y_end - slice_image.height

        if i % 2 == 0:
            new_image.paste(slice_image, (0, y_start)) 
        else:
            new_image.paste(slice_image, (0, y_reverse_offset))

    new_image.save(level2_image_path)

def cut_and_stack_images2(level2_image_path, num_slices, level3_image_path):

    step2_image = Image.open(level2_image_path)
    width2, height2 = step2_image.size
    slice_width = width2 // num_slices

    new_image2 = Image.new('RGB', (width2, height2))
    for j in range(num_slices):
        x_start = j * slice_width
        x_end = (j + 1) * slice_width

        slice_image = step2_image.crop((x_start, 0, x_end, height2))
        x_reverse_offset = new_image2.width - x_end - slice_image.width

        if j % 2 == 0:
            new_image2.paste(slice_image, (x_start, 0))
        else:
            new_image2.paste(slice_image, (x_reverse_offset, 0))

        new_image2.save(level3_image_path)

def crop_image(level3_image_path, final_image_path):

    step3_image = Image.open(level3_image_path)
    width3, height3 = step3_image.size
    wid = width3//2
    hei = height3//2

    final_img = step3_image.crop((0,0,wid,hei))

    final_img.save(final_image_path)

level1_image_path = 'level1.jpg'
level2_image_path = 'level2.jpg'
level3_image_path = 'level3.jpg'
final_image_path = 'final.jpg'
num_slices = 90

generate_image_grid(input_image_path, output_image_path)
print("이미지 그리드 생성 완료!")
cut_and_stack_images(level1_image_path, num_slices, level2_image_path)
print("이미지 자르기 및 조각 쌓기 완료!")
cut_and_stack_images2(level2_image_path, num_slices, level3_image_path)
print("최종 모자이크 완료!")
crop_image(level3_image_path, final_image_path)
print("이미지 크롭 완료!")

