dataset_paths = {
	'ffhq': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/data/head2/images/train',
	'celeba_test': './data_test',

	'cars_train': '',
	'cars_test': '',

	'church_train': '',
	'church_test': '',

	'horse_train': '',
	'horse_test': '',

	'afhq_wild_train': '',
	'afhq_wild_test': ''
}

model_paths = {
	'ir_se50': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/model_ir_se50.pth',
	'resnet34': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/resnet34-333f7ec4.pth',
	'stylegan_ffhq': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/stylegan2-ffhq-config-f.pt',
	'stylegan_cars': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/stylegan2-car-config-f.pt',
	'stylegan_church': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/stylegan2-church-config-f.pt',
	'stylegan_horse': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/stylegan2-horse-config-f.pt',
	'stylegan_ada_wild': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/afhqwild.pt',
	'stylegan_toonify': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/ffhq_cartoon_blended.pt',
	'shape_predictor': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/shape_predictor_68_face_landmarks.dat',
	'circular_face': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/CurricularFace_Backbone.pth',
	'mtcnn_pnet': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/mtcnn/pnet.npy',
	'mtcnn_rnet': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/mtcnn/rnet.npy',
	'mtcnn_onet': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/mtcnn/onet.npy',
	'moco': '/kaggle/input/zhoudualstyleganencode/DualStyleGAN/checkpoint/moco_v2_800ep_pretrain.pt'
}
