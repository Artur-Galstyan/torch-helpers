import torch
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.sampler import SubsetRandomSampler
import numpy as np


class TorchDataset(Dataset):

    def __init__(self, X, y):

        self.X = X
        self.y = y
        assert len(X) == len(y), f"Features and targets have unequal shapes {len(X)} != {len(y)}"
        self.n_samples = len(X)

        # Turn into torch tensors if X and y were Numpy arrays
        if type(X) == np.ndarray:
            self.X = torch.from_numpy(X.astype(np.float32))
        if type(y) == np.ndarray:
            self.y = torch.from_numpy(y.astype(np.float32)).unsqueeze(1)

    def __getitem__(self, item):
        return self.X[item], self.y[item]

    def __len__(self):
        return self.n_samples

    def get_train_and_validation_data(self, validation_ratio, batch_size):
        dataset_size = len(self)

        indices = list(range(dataset_size))
        split = int(np.floor(validation_ratio * dataset_size))

        train_indices, val_indices = indices[split:], indices[:split]

        train_sampler = SubsetRandomSampler(train_indices)
        val_sampler = SubsetRandomSampler(val_indices)

        train_loader = DataLoader(self, batch_size=batch_size, sampler=train_sampler)
        validation_loader = DataLoader(self, batch_size=batch_size, sampler=val_sampler)

        return train_loader, validation_loader
