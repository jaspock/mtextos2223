import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self, params):

        super(Net, self).__init__()

        self.embedding = nn.Embedding(params.vocab_size, params.embedding_dim)

        self.lstm = nn.LSTM(params.embedding_dim,
                            params.lstm_hidden_dim, batch_first=True)

        self.fc = nn.Linear(params.lstm_hidden_dim, params.number_of_tags)

    def forward(self, s):

        s = self.embedding(s)

        s, _ = self.lstm(s)

        s = s.contiguous()

        s = s.view(-1, s.shape[2])

        s = self.fc(s)

        return F.log_softmax(s, dim=1)


def loss_fn(outputs, labels):

    labels = labels.view(-1)

    mask = (labels >= 0).float()

    labels = labels % outputs.shape[1]

    num_tokens = int(torch.sum(mask))

    return -torch.sum(outputs[range(outputs.shape[0]), labels]*mask)/num_tokens


def accuracy(outputs, labels):

    labels = labels.ravel()

    mask = (labels >= 0)

    outputs = np.argmax(outputs, axis=1)

    return np.sum(outputs == labels)/float(np.sum(mask))


metrics = {
    'accuracy': accuracy,
}
