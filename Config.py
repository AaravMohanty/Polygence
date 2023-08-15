# The new config inherits a base config to highlight the necessary modification
_base_ = '../configs/yolo/yolov3_mobilenetv2_8xb24-320-300e_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1)))

# Modify dataset related settings
data_root = 'C:/Users/15712/PycharmProjects/Polygence/Polygence/'
metainfo = {
    'classes': ('trophy', ),
    'palette': [
        (220, 20, 60),
    ]
}
train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='data.json',
        data_prefix=dict(img='train/')))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='data.json',
        data_prefix=dict(img='val/')))
test_dataloader = val_dataloader

# Modify metric related settings
val_evaluator = dict(ann_file=data_root + 'data.json')
test_evaluator = val_evaluator

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/yolo/yolov3_mobilenetv2_320_300e_coco/yolov3_mobilenetv2_320_300e_coco_20210719_215349-d18dff72.pth'
