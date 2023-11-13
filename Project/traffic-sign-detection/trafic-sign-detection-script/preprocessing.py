# import os
# import xml.etree.ElementTree as ET

# def convert_voc_to_yolo():
#     for anno in os.listdir('./data/labels'):
#         if anno.split('.')[1] == 'xml':
#             file_name = anno.split('.')[0]
#             out_file = open(f'./data/labels/{file_name}.txt', 'w')

#             tree = ET.parse(os.path.join('data', 'labels', anno))
#             root = tree.getroot()
#             size = root.find('size')
#             w = int(size.find('width').text)
#             h = int(size.find('height').text)

#             names = ['trafficlight', 'speedlimit', 'crosswalk', 'stop']

#             for obj in root.iter('object'):
#                 cls = obj.find('name').text
#                 if cls in names and int(obj.find('difficult').text) != 1:
#                     xmlbox = obj.find('bndbox')
#                     x_min = float(xmlbox.find('xmin').text)
#                     x_max = float(xmlbox.find('xmax').text)
#                     y_min = float(xmlbox.find('ymin').text)
#                     y_max = float(xmlbox.find('ymax').text)

#                     # Convert bounding box to YOLO format
#                     x_center = (x_min + x_max) / (2.0 * w)
#                     y_center = (y_min + y_max) / (2.0 * h)
#                     box_width = (x_max - x_min) / w
#                     box_height = (y_max - y_min) / h

#                     cls_id = names.index(cls)  # class id
#                     out_file.write(" ".join([str(a) for a in (cls_id, x_center, y_center, box_width, box_height)]) + '\n')




# FIRST
# import os 
# import xml.etree.ElementTree as ET

# def convert_box(size, box):
#     dw, dh = 1. / size[0], 1. / size[1]
#     x, y, w, h = (box[0] + box[1]) / 2.0 - 1, (box[2] + box[3]) / 2.0 - 1, box[1] - box[0], box[3] - box[2]
#     return x * dw, y * dh, w * dw, h * dh

# def convert_voc_to_yolo():
#     for anno in os.listdir('./data/labels'):
#         if anno.split('.')[1] == 'xml':
#             file_name = anno.split('.')[0]
#             out_file = open(f'./data/labels/{file_name}.txt', 'w')

#             tree = ET.parse(os.path.join('data','labels', anno))
#             root = tree.getroot()
#             size = root.find('size')        
#             w = int(size.find('width').text)
#             h = int(size.find('height').text)

#             names = ['trafficlight', 'speedlimit', 'crosswalk', 'stop']

#             for obj in root.iter('object'):
#                 cls = obj.find('name').text
#                 if cls in names and int(obj.find('difficult').text) != 1:
#                     xmlbox = obj.find('bndbox')
#                     bb = convert_box((w, h), [float(xmlbox.find(x).text) for x in ('xmin', 'xmax', 'ymin', 'ymax')])
#                     cls_id = names.index(cls)  # class id
#                     out_file.write(" ".join([str(a) for a in (cls_id, *bb)]) + '\n')


#somewhat worked
# import os 
# import xml.etree.ElementTree as ET

# def convert_box(size, box):
#     dw, dh = 1. / size[0], 1. / size[1]
#     x, y, w, h = (box[0] + box[1]) / 2.0 - 1, (box[2] + box[3]) / 2.0 - 1, box[1] - box[0], box[3] - box[2]
#     return x * dw, y * dh, w * dw, h * dh

# def convert_voc_to_yolo():
#     bounding_boxes = {}  # Dictionary to store ground truth bounding boxes for each image
#     names = ['trafficlight', 'speedlimit', 'crosswalk', 'stop']

#     for anno in os.listdir('./data/labels'):
#         if anno.split('.')[1] == 'xml':
#             file_name = anno.split('.')[0]
#             bounding_boxes[file_name] = {}  # Dictionary to store bounding boxes for each class in the image

#             tree = ET.parse(os.path.join('data', 'labels', anno))
#             root = tree.getroot()
#             size = root.find('size')        
#             w = int(size.find('width').text)
#             h = int(size.find('height').text)

#             for obj in root.iter('object'):
#                 cls = obj.find('name').text
#                 if cls in names and int(obj.find('difficult').text) != 1:
#                     xmlbox = obj.find('bndbox')
#                     bb = convert_box((w, h), [float(xmlbox.find(x).text) for x in ('xmin', 'xmax', 'ymin', 'ymax')])
#                     cls_id = names.index(cls)  # class id

#                     bounding_boxes[file_name][cls] = bb  # Store bounding box for the class

#     return bounding_boxes

#another
import os 
import xml.etree.ElementTree as ET

def convert_box(size, box):
    dw, dh = 1. / size[0], 1. / size[1]
    x, y, w, h = box[0], box[2], box[1] - box[0], box[3] - box[2]
    return x * dw, y * dh, w * dw, h * dh

def convert_voc_to_yolo():
    bounding_boxes = {}  # Dictionary to store ground truth bounding boxes for each image
    names = ['trafficlight', 'speedlimit', 'crosswalk', 'stop']

    for anno in os.listdir('./data/labels'):
        if anno.split('.')[1] == 'xml':
            file_name = anno.split('.')[0]
            bounding_boxes[file_name] = {}  # Dictionary to store bounding boxes for each class in the image

            tree = ET.parse(os.path.join('data', 'labels', anno))
            root = tree.getroot()
            size = root.find('size')        
            w = int(size.find('width').text)
            h = int(size.find('height').text)

            for obj in root.iter('object'):
                cls = obj.find('name').text
                if cls in names and int(obj.find('difficult').text) != 1:
                    xmlbox = obj.find('bndbox')
                    bb = convert_box((w, h), [float(xmlbox.find(x).text) for x in ('xmin', 'xmax', 'ymin', 'ymax')])
                    cls_id = names.index(cls)  # class id

                    bounding_boxes[file_name][cls] = bb  # Store bounding box for the class

    return bounding_boxes