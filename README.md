# How to set up

1. Download cifar 10 dataset and extract to the repo root folder.
2. Run the parse_cifar.py which will generate the test and the train sets.
3. Create a conda environment with the `conda env create -n torch environment.yml` and activate it.
4. Execute `jupyter notebook` and execute cells in the main.ipynb


# Description
0. I will use mobilenetV2 because it's light network with fast training time
and inference. Because of the 1k train set size limitation the train set is too small to
train properly so it will be very easy to overfit on the train set.

1. I will randomly select 1k images from the cifar_10 dataset for every class
I will use the same amount of training data to keep the classes in the training set balanced.
 I will use the batch_1 as the source of the training set and test_batch for the test set.
Instead of the 10 classes of the cifar 10 dataset I will only use the first 4 classes.

2. I will create a new module which returns back those 1s with the actual output of the
mobilenetv2. For the train and the inference I will only use the mobilenetv2 output.

3. I use cross entropy as loss and accuracy to check how is the model behaving. With the accuracy
 measured on the whole test set I can see how good the model can generalize on the unseen dataset.
 The accuracy and the loss on the train batches are decreasing so I can be sure that the model is 
 actually training and everything is normal. The train accuracy is converging to 1. To make the model
 more robust definitely more data would be essential 1k. Adding some  augmentation to the training set
 would be beneficial. I would use some augmentation techniques like white boxing, rotate, solarize and random noise.

4. I would select the best model based on the test accuracy and I would create a docker image around 
the model with the required dependencies. The model will wait for an image input and the model output
 would be the response. The protocol can be http, grpc or any other protocol which supports request and responses.  



