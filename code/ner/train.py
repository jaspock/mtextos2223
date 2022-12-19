
import argparse
import logging
import os

import numpy as np
import torch
import torch.optim as optim
from tqdm import trange

import utils
import model.net as net
from model.data_loader import DataLoader
from evaluate import evaluate


parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', default='data/small',
                    help="Directory containing the dataset")
parser.add_argument('--model_dir', default='experiments/base_model',
                    help="Directory containing params.json")
parser.add_argument('--restore_file', default=None,
                    help="Optional, name of the file in --model_dir containing weights to reload before \
                    training")  # 'best' or 'train'


def train(model, optimizer, loss_fn, data_iterator, metrics, params, num_steps):
    
    model.train()

    summ = []
    loss_avg = utils.RunningAverage()

    t = trange(num_steps)
    for i in t:
        train_batch, labels_batch = next(data_iterator)

        output_batch = model(train_batch)
        loss = loss_fn(output_batch, labels_batch)

        optimizer.zero_grad()
        loss.backward()

        optimizer.step()

        if i % params.save_summary_steps == 0:
            output_batch = output_batch.data.cpu().numpy()
            labels_batch = labels_batch.data.cpu().numpy()

            summary_batch = {metric: metrics[metric](output_batch, labels_batch)
                             for metric in metrics}
            summary_batch['loss'] = loss.item()
            summ.append(summary_batch)

        loss_avg.update(loss.item())
        t.set_postfix(loss='{:05.3f}'.format(loss_avg()))

    metrics_mean = {metric: np.mean([x[metric]
                                     for x in summ]) for metric in summ[0]}
    metrics_string = " ; ".join("{}: {:05.3f}".format(k, v)
                                for k, v in metrics_mean.items())
    logging.info("- Train metrics: " + metrics_string)


def train_and_evaluate(model, train_data, val_data, optimizer, loss_fn, metrics, params, model_dir, restore_file=None):

    if restore_file is not None:
        restore_path = os.path.join(
            args.model_dir, args.restore_file + '.pth.tar')
        logging.info("Restoring parameters from {}".format(restore_path))
        utils.load_checkpoint(restore_path, model, optimizer)

    best_val_acc = 0.0

    for epoch in range(params.num_epochs):

        logging.info("Epoch {}/{}".format(epoch + 1, params.num_epochs))

        num_steps = (params.train_size + 1) // params.batch_size
        train_data_iterator = data_loader.data_iterator(
            train_data, params, shuffle=True)
        train(model, optimizer, loss_fn, train_data_iterator,
              metrics, params, num_steps)

        num_steps = (params.val_size + 1) // params.batch_size
        val_data_iterator = data_loader.data_iterator(
            val_data, params, shuffle=False)
        val_metrics = evaluate(
            model, loss_fn, val_data_iterator, metrics, params, num_steps)

        val_acc = val_metrics['accuracy']
        is_best = val_acc >= best_val_acc

        utils.save_checkpoint({'epoch': epoch + 1,
                               'state_dict': model.state_dict(),
                               'optim_dict': optimizer.state_dict()},
                              is_best=is_best,
                              checkpoint=model_dir)

        if is_best:
            logging.info("- Found new best accuracy")
            best_val_acc = val_acc

            best_json_path = os.path.join(
                model_dir, "metrics_val_best_weights.json")
            utils.save_dict_to_json(val_metrics, best_json_path)

        last_json_path = os.path.join(
            model_dir, "metrics_val_last_weights.json")
        utils.save_dict_to_json(val_metrics, last_json_path)


if __name__ == '__main__':

    args = parser.parse_args()
    json_path = os.path.join(args.model_dir, 'params.json')
    assert os.path.isfile(
        json_path), "No json configuration file found at {}".format(json_path)
    params = utils.Params(json_path)

    params.cuda = torch.cuda.is_available()

    torch.manual_seed(230)
    if params.cuda:
        torch.cuda.manual_seed(230)

    utils.set_logger(os.path.join(args.model_dir, 'train.log'))

    logging.info("Loading the datasets...")

    data_loader = DataLoader(args.data_dir, params)
    data = data_loader.load_data(['train', 'val'], args.data_dir)
    train_data = data['train']
    val_data = data['val']

    params.train_size = train_data['size']
    params.val_size = val_data['size']

    logging.info("- done.")

    model = net.Net(params).cuda() if params.cuda else net.Net(params)
    optimizer = optim.Adam(model.parameters(), lr=params.learning_rate)

    loss_fn = net.loss_fn
    metrics = net.metrics

    logging.info("Starting training for {} epoch(s)".format(params.num_epochs))
    train_and_evaluate(model, train_data, val_data, optimizer, loss_fn, metrics, params, args.model_dir,
                       args.restore_file)
