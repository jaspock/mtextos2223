import csv
import os
import sys


def load_dataset(path_csv):
    use_python3 = sys.version_info[0] >= 3
    with (open(path_csv, encoding="windows-1252") if use_python3 else open(path_csv)) as f:
        csv_file = csv.reader(f, delimiter=',')
        dataset = []
        words, tags = [], []

        for idx, row in enumerate(csv_file):
            if idx == 0: continue
            sentence, word, pos, tag = row
            if len(sentence) != 0:
                if len(words) > 0:
                    assert len(words) == len(tags)
                    dataset.append((words, tags))
                    words, tags = [], []
            try:
                word, tag = str(word), str(tag)
                words.append(word)
                tags.append(tag)
            except UnicodeDecodeError as e:
                print("An exception was raised, skipping a word: {}".format(e))
                pass

    return dataset


def save_dataset(dataset, save_dir):
    
    print("Saving in {}...".format(save_dir))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    with open(os.path.join(save_dir, 'sentences.txt'), 'w') as file_sentences:
        with open(os.path.join(save_dir, 'labels.txt'), 'w') as file_labels:
            for words, tags in dataset:
                file_sentences.write("{}\n".format(" ".join(words)))
                file_labels.write("{}\n".format(" ".join(tags)))
    print("- done.")


if __name__ == "__main__":
    
    path_dataset = 'data/kaggle/ner_dataset.csv'
    msg = "{} file not found. Make sure you have downloaded the right dataset".format(path_dataset)
    assert os.path.isfile(path_dataset), msg

    print("Loading Kaggle dataset into memory...")
    dataset = load_dataset(path_dataset)
    print("- done.")

    train_dataset = dataset[:int(0.7*len(dataset))]
    val_dataset = dataset[int(0.7*len(dataset)) : int(0.85*len(dataset))]
    test_dataset = dataset[int(0.85*len(dataset)):]

    save_dataset(train_dataset, 'data/kaggle/train')
    save_dataset(val_dataset, 'data/kaggle/val')
    save_dataset(test_dataset, 'data/kaggle/test')