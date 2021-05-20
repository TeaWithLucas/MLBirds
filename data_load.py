import numpy as np

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

bounding_boxes_csv = pd.read_csv(bounding_boxes_file)
classes_csv = pd.read_csv(classes_file)
image_class_labels_csv = pd.read_csv(image_class_labels_file)
images_csv = pd.read_csv(images_file)
train_test_split_csv = pd.read_csv(train_test_split_file)

attributes_csv = pd.read_csv(attributes_file)
certainties_csv = pd.read_csv(certainties_file)
class_attribute_labels_continuous_csv = pd.read_csv(class_attribute_labels_continuous_file)
image_attribute_labels_csv = pd.read_csv(image_attribute_labels_file)

part_click_locs_csv = pd.read_csv(part_click_locs_file)
part_locs_csv = pd.read_csv(part_locs_file)
parts_csv = pd.read_csv(parts_file)