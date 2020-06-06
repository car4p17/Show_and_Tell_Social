### Preface
This is based on the repo: (https://github.com/nikhilmaram/Show_and_Tell) with slight modifications.

### Prerequisites
* **Tensorflow Version 1.15.0** ([instructions](https://www.tensorflow.org/install/)) 
* **NumPy Version 1.17.3** ([instructions](https://scipy.org/install.html))
* **OpenCV-Python Version 4.2.0.34** ([instructions](https://pypi.python.org/pypi/opencv-python))
* **Natural Language Toolkit (NLTK) Version 3.4.5** ([instructions](http://www.nltk.org/install.html))
* **Pandas Version 0.25.3** ([instructions](https://scipy.org/install.html))
* **Matplotlib Version 3.1.1** ([instructions](https://scipy.org/install.html))
* **tqdm Version 4.36.1** ([instructions](https://pypi.python.org/pypi/tqdm))

### Usage
* **Preparation For COCO:** Download the COCO train2017 and val2017 data [here](http://cocodataset.org/#download). Put the COCO train2017 images in the folder `train/images`, and put the file `captions_train2017.json` in the folder `train`. Similarly, put the COCO val2017 images in the folder `val/images`, and put the file `captions_val2017.json` in the folder `val`. Furthermore, download the pretrained VGG16 net [here](https://ucsb.box.com/s/pj4gg3vpei57cf9xewttoqn01qqa3uj4)  if you want to use it to initialize the CNN part.

* **Preperation For Google Conceptual Captions:** Download the train dataset [here](https://ai.google.com/research/ConceptualCaptions). Place the tsv file "Train_GCC-training.tsv" in the root directory and then run prepGoogleData.py to generate the train/googleanns.csv file

* **Preperation For Instagram Dataset:** Download the dataset from this [repo](https://github.com/cesc-park/attend2u). Then run the prepInstaData.py script to generate the train/instagramanns.csv caption cache file.

* **Training:**
First setup various parameters in the file `config.py` to point to the appropriate dataset and then run a command like this:
```shell
python3 main.py --phase=train \
    --load_cnn \
    --cnn_model_file='./vgg16_weights.npz'\
    [--train_cnn]
```
Turn on `--train_cnn` if you want to jointly train the CNN and RNN parts. Otherwise, only the RNN part is trained. The checkpoints will be saved in the folder `models`. If you want to resume the training from a checkpoint, run a command like this:
```shell
python3 main.py --phase=train \
    --load \
    --model_file='./models/xxxxxx.npy'\
    [--train_cnn]
```
To monitor the progress of training, run the following command:
```shell
tensorboard --logdir='./summary/'
```

* **Evaluation:**
To evaluate a trained model using the COCO val2017 data, run a command like this:
```shell
python3 main.py --phase=eval \
    --model_file='./models/xxxxxx.npy'
```
The result will be shown in stdout. Furthermore, the generated captions will be saved in the file `val/results.json`.

* **Inference:**
You can use the trained model to generate captions for any JPEG images! Put such images in the folder `test/images`, and run a command like this:
```shell
python3 main.py --phase=test \
    --model_file='./models/xxxxxx.npy'
```
The generated captions will be saved in the folder `test/results`.

### References
* [Show and Tell: A Neural Image Caption Generator](https://arxiv.org/pdf/1411.4555.pdf).By Oriol Vinyals, Alexander Toshev, Samy Bengio, Dumitru Erhan ICML 2015.
* [Adapted from earlier implementation in Tensorflow](https://github.com/DeepRNN/image_captioning)
* [Microsoft COCO dataset](http://mscoco.org/)