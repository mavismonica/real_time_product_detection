import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2 
from sklearn.model_selection import train_test_split
from tqdm import tqdm


DATA_DIR = "C:/Users/mavis/thesis/real_time_product_detection/images/"
CATEGORIES = ['BEANS','CAKE','CANDY','CEREAL','CHIPS','CHOCOLATE','COFFEE','CORN','FISH','FLOUR','HONEY',
                    'JAM','JUICE','MILK','NUTS','OIL','PASTA','RICE','SODA','SPICES','SUGAR','TEA','TOMATO_SAUCE',
                    'VINEGAR','WATER']

# for category in CATEGORIES:
#     path = os.path.join(DATA_DIR,category)
#     for img in os.listdir(path):
#         img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
#         plt.imshow(img_array,cmap="gray")
#         plt.show()
#         break
#     break

# print(img_array.shape)

IMG_SIZE = 160

# new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
# plt.imshow(new_array, cmap='gray')
# plt.show()

training_data = []
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATA_DIR,category)
        class_num = CATEGORIES.index(category)
        for img in tqdm(os.listdir(path)):
            try:

                img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array,class_num])

            except Exception as e:  # in the interest in keeping the output clean...
                print("OSErrroBad img most likely", e, os.path.join(path,img))

create_training_data()
print(len(training_data))

import random
random.shuffle(training_data)
# for sample in training_data:
#     print([sample[1]])

X = []
y = []

for features,label in training_data:
    X.append(features)
    y.append(label)

print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
# X = np.array(X).reshape(-1, 256,256,1)

import pickle

pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()



