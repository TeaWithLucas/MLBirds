import pandas as pd

analysis_fldr = 'analysis_data/'

bounding_boxes_file = analysis_fldr + 'bounding_boxes.csv'
classes_file = analysis_fldr + 'classes.csv'
image_class_labels_file = analysis_fldr + 'image_class_labels.csv'
images_file = analysis_fldr + 'images.csv'
train_test_split_file = analysis_fldr + 'train_test_split.csv'

attributes_file = analysis_fldr + 'attributes/attribute.csv'
certainties_file = analysis_fldr + 'attributes/certainties.csv'
class_attribute_labels_continuous_file = analysis_fldr + 'attributes/class_attribute_labels_continuous.csv'
image_attribute_labels_file = analysis_fldr + 'attributes/image_attribute_labels.csv'

part_click_locs_file = analysis_fldr + 'parts/part_click_locs.csv'
part_locs_file = analysis_fldr + 'parts/part_locs.csv'
parts_file = analysis_fldr + 'parts/parts.csv'

bounding_boxes = pd.read_csv(bounding_boxes_file)
classes = pd.read_csv(classes_file)
image_class_labels = pd.read_csv(image_class_labels_file)
images = pd.read_csv(images_file)
train_test_split = pd.read_csv(train_test_split_file)

attributes = pd.read_csv(attributes_file)
certainties = pd.read_csv(certainties_file)
class_attribute_labels_continuous = pd.read_csv(class_attribute_labels_continuous_file)
image_attribute_labels = pd.read_csv(image_attribute_labels_file)

part_click_locs = pd.read_csv(part_click_locs_file)
part_locs = pd.read_csv(part_locs_file)
parts = pd.read_csv(parts_file)