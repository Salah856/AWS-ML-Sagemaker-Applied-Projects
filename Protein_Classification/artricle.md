
# Fine-tune and deploy the ProtBERT model for protein classification using Amazon SageMaker

Proteins, the key fundamental macromolecules governing in biological bodies, are composed of amino acids. These 20 essential amino acids, each represented by a capital letter, combine to form a protein sequence, which can be used to predict the subcellular localization (the location of protein in a cell) and structure of proteins.

The study of protein localization is important to comprehend the function of protein, which is essentially to structure, function, and regulate the body’s tissues and organs. Protein localization has great importance for drug design and other applications. For example, we can investigate methods to disrupt the binding of the spiky S1 protein of the SARS-Cov-2 virus. The binding of the S1 protein to the human receptor ACE2 is the mechanism which led to the COVID-19 pandemic. It also plays an important role in characterizing the cellular function of hypothetical and newly discovered proteins

In this article, we use NLP techniques for protein sequence classification. The idea is to interpret protein sequences as sentences and their constituent—amino acids—as single words. More specifically, we fine-tune the PyTorch ProtBERT model from the Hugging Face library using Amazon SageMaker.

## What is ProtBERT?
ProtBERT is a pretrained model on protein sequences using a masked language modeling objective. It’s based on the BERT model, which is pretrained on a large corpus of protein sequences in a self-supervised fashion. This means it was pretrained on the raw protein sequences only, with no humans labeling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those protein sequences [8]. For more information about ProtBERT

