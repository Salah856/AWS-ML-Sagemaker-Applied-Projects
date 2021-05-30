
# Fine-tune and deploy the ProtBERT model for protein classification using Amazon SageMaker

Proteins, the key fundamental macromolecules governing in biological bodies, are composed of amino acids. These 20 essential amino acids, each represented by a capital letter, combine to form a protein sequence, which can be used to predict the subcellular localization (the location of protein in a cell) and structure of proteins.

The study of protein localization is important to comprehend the function of protein, which is essentially to structure, function, and regulate the body’s tissues and organs. Protein localization has great importance for drug design and other applications. For example, we can investigate methods to disrupt the binding of the spiky S1 protein of the SARS-Cov-2 virus. The binding of the S1 protein to the human receptor ACE2 is the mechanism which led to the COVID-19 pandemic. It also plays an important role in characterizing the cellular function of hypothetical and newly discovered proteins

In this article, we use NLP techniques for protein sequence classification. The idea is to interpret protein sequences as sentences and their constituent—amino acids—as single words. More specifically, we fine-tune the PyTorch ProtBERT model from the Hugging Face library using Amazon SageMaker.

## What is ProtBERT?
ProtBERT is a pretrained model on protein sequences using a masked language modeling objective. It’s based on the BERT model, which is pretrained on a large corpus of protein sequences in a self-supervised fashion. This means it was pretrained on the raw protein sequences only, with no humans labeling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those protein sequences [8]. For more information about ProtBERT


Dataset
In this post, we use an open-source DeepLoc [10] public dataset of protein sequences to train the model. The dataset is a FASTA file composed of header and protein sequence. The header is composed of the accession number from Uniprot, the annotated subcellular localization, and possibly a description field indicating if the protein was part of the test set. The subcellular localization includes an additional label, where S indicates soluble, M membrane, and U unknown [9]. The following code is a sample of the data:
```
>Q9SMX3 Mitochondrion-M test
MVKGPGLYTEIGKKARDLLYRDYQGDQKFSVTTYSSTGVAITTTGTNKGSLFLGDVATQVKNNNFTADVKVST
DSSLLTTLTFDEPAPGLKVIVQAKLPDHKSGKAEVQYFHDYAGISTSVGFTATPIVNFSGVVGTNGLSLGTDV
AYNTESGNFKHFNAGFNFTKDDLTASLILNDKGEKLNASYYQIVSPSTVVGAEISHNFTTKENAITVGTQHAL>
DPLTTVKARVNNAGVANALIQHEWRPKSFFTVSGEVDSKAIDKSAKVGIALALKP"
A sequence in FASTA format begins with a single-line description, followed by lines of sequence data. The definition line (defline) is distinguished from the sequence data by a greater-than (>) symbol at the beginning. The word following the > symbol is the identifier of the sequence, and the rest of the line is the description.
```

We download the FASTA formatted dataset and read it by directly filtering out the columns that are of interest. The dataset consists of 14,000 sequences and 6 columns in total. The columns are as follows:

id – Unique identifier given each sequence in the dataset.
sequence – Protein sequence. Each character is separated by a space. This is useful for the BERT tokenizer.
sequence_length – Character length of each protein sequence.
location – Classification given each sequence. The dataset has 10 unique classes (subcellular localization).
is_train – Indicates whether the record should be used for training or test. Is also used to separate the dataset for training and validation.
When we plot the sequence lengths of each record as an histogram, we observe the following distribution.


This is an important observation because the ProtBERT model receives a fixed sentence length as input. Usually, the maximum length of a sentence depends on the data we’re working on. For sentences that are shorter than this maximum length, we have to add paddings (empty tokens) to the sentences to make up the length.

In the preceding plot, most of the sequences are under 1,500 characters in length, therefore, it’s a good idea to choose max_length = 1536, but that increases the training time for this sample notebook, therefore, we use max_length = 512.

When we’re retrieving each sequence record using the Pytorch DataLoaders during training, we must ensure that each sequence is tokenized, truncated, and the necessary padding is added to make them all the same max_length value. To encapsulate this process, we define the ProteinSequenceDataset class, which uses the encode_plus() API provided by the Hugging Face transformer library


```python

#data_prep.py

import torch
from torch import nn
import torch.utils.data
import torch.utils.data.distributed
from torch.utils.data import Dataset, DataLoader, RandomSampler, TensorDataset

class ProteinSequenceDataset(Dataset):
    def __init__(self, sequence, targets, tokenizer, max_len):
        self.sequence = sequence
        self.targets = targets
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, item):
        sequence = str(self.sequence[item])
        target = self.targets[item]
        encoding = self.tokenizer.encode_plus(
            sequence,
            truncation=True,
            add_special_tokens=True,
            max_length=self.max_len,
            return_token_type_ids=False,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt',
        )
        return {
          'protein_sequence': sequence,
          'input_ids': encoding['input_ids'].flatten(),
          'attention_mask': encoding['attention_mask'].flatten(),
          'targets': torch.tensor(target, dtype=torch.long)
        }
```
