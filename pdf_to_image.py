#pip install pdf2image

import os
from pdf2image import convert_from_path
rootdir = '/home/cso/Downloads/customer_pdfs'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        full_path = os.path.join(subdir, file)
        if full_path.endswith('.pdf'):
			converted_name = os.path.join(subdir, '%s_conv.jpg' % (file.replace('.pdf', '')))
			converted_name_2 = os.path.join(subdir, '%s_conv_2.jpg' % (file.replace('.pdf', '')))
			images = convert_from_path(full_path,500,output_folder=subdir,fmt='jpg', first_page=7, last_page=7)
			images2 = convert_from_path(full_path,500,output_folder=subdir,fmt='jpg', first_page=9, last_page=9)
			os.rename(images[0].filename, converted_name)
			os.rename(images2[0].filename, converted_name_2)
