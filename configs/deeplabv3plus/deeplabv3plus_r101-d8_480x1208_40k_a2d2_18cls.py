_base_ = './deeplabv3plus_r50-d8_480x1208_40k_a2d2_18cls.py'
model = dict(
    pretrained='open-mmlab://resnet101_v1c',
    backbone=dict(depth=101),
    decode_head=dict(num_classes=18),
    auxiliary_head=dict(num_classes=18))
