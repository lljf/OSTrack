class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/kaggle/working/OStrack'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/kaggle/working/OStrack/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/kaggle/working/OStrack/pretrained_networks'
        self.lasot_dir = '/kaggle/working/OStrack/data/lasot'
        self.got10k_dir = '/kaggle/input/got10k/train'
        self.got10k_val_dir = '/kaggle/working/OStrack/data/got10k/val'
        self.lasot_lmdb_dir = '/kaggle/working/OStrack/data/lasot_lmdb'
        self.got10k_lmdb_dir = '/kaggle/working/OStrack/data/got10k_lmdb'
        self.trackingnet_dir = '/kaggle/working/OStrack/data/trackingnet'
        self.trackingnet_lmdb_dir = '/kaggle/working/OStrack/data/trackingnet_lmdb'
        self.coco_dir = '/kaggle/working/OStrack/data/coco'
        self.coco_lmdb_dir = '/kaggle/working/OStrack/data/coco_lmdb'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/kaggle/working/OStrack/data/vid'
        self.imagenet_lmdb_dir = '/kaggle/working/OStrack/data/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
