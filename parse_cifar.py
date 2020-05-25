import pickle
import glob
import numpy as np




def create_dataset(ds_name, cifar_batch_path, item_per_class, num_class):
  result = dict()

  result[b"labels"] = np.zeros(1000)

  result[b"data"] = np.zeros((1000,3072))

  with open(cifar_batch_path, "rb") as f:
    d = pickle.load(f, encoding="bytes")
    print(d.keys())
    print(d[b"data"].shape)

    #select 100 instances from every class 

    class_counts = [0] * num_class

    selected_elements_count = 0
    for row_id, row in enumerate(d[b"labels"]):
      if row < num_class and class_counts[row] < item_per_class:

        result[b"labels"][selected_elements_count] = row
        result[b"data"][selected_elements_count] = d[b"data"][row_id]
      
        selected_elements_count += 1
        class_counts[row] += 1

  assert(class_counts == [item_per_class] * num_class)
  pickle.dump(result, open(ds_name, "wb")) 


create_dataset("train_set", "cifar-10-batches-py/data_batch_1", 250, 4)
create_dataset("test_set", "cifar-10-batches-py/test_batch", 50, 4)
