from transformers import BertTokenizer, BertModel
import torch

from transformers import BertTokenizer, BertModel
import torch
import numpy as np

def Modified_Weighted_BERT(texts):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')

    inputs = tokenizer(
        texts,
        padding=True,
        truncation=True,
        max_length=128,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)

    token_embeddings = outputs.last_hidden_state
    attention_mask = inputs['attention_mask']

    mask = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()

    weighted_sum = torch.sum(token_embeddings * mask, dim=1)
    summed_mask = torch.clamp(mask.sum(dim=1), min=1e-9)

    embeddings = weighted_sum / summed_mask

    # rating-based weighting
    # weights = np.array(ratings) / max(ratings)

    return embeddings.numpy()

te = "I love you"
output = Modified_Weighted_BERT(te)
