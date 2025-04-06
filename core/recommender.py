from sentence_transformers import SentenceTransformer, util
import json

class SHLRecommender:
    def __init__(self, product_data_path: str):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        with open(product_data_path, 'r') as f:
            self.products = json.load(f)
        self.product_embeddings = self.model.encode(
            [p["description"] for p in self.products], convert_to_tensor=True
        )

    def recommend(self, job_requirements: str, top_k: int = 1):
        job_embedding = self.model.encode(job_requirements, convert_to_tensor=True)
        similarity_scores = util.cos_sim(job_embedding, self.product_embeddings)[0]
        top_results = similarity_scores.topk(k=top_k)

        return [{
            "title": self.products[i]["title"],
            "description": self.products[i]["description"],
            "score": round(s.item(), 3)
        } for s, i in zip(top_results.values, top_results.indices)]
