import os

def data_prepartion(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        total_context_text = os.path.splitext(os.path.join(root, 'keras_data_output'))[0] + ".gt.txt"
        output_file = open(total_context_text, 'a')
        for name in files:
            print("file name", name)
            print(os.path.join(root, name))
            print(os.path.splitext(os.path.join(root, name))[0])
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".txt"):
                print("File exists")
                # img_text = os.path.splitext(os.path.join(root, name))[0] + ".txt"
                img_text = os.path.join(root, name)
                existing_file = open(img_text, 'r')
                lines = existing_file.readlines()
                print(lines)
                output_file.write(name[:-7] + '.png' + ',' + ' \"' + lines[0] + '\"')
                output_file.write("\n")
                existing_file.close()
    output_file.close()

if __name__ == '__main__':
    data_prepartion(r'C:\Users\user\Downloads\images')
