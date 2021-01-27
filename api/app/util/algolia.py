import os
from ..model import Produit

def get_produits_from_db():
    return [produit.to_algolia_record() for produit in Produit.objects()]

def add_produits_to_algolia():
    from algoliasearch.search_client import SearchClient

    client = SearchClient.create(os.getenv("ALGOLIA_APPLICATION_ID"), os.getenv("ALGOLIA_ADMIN_API_KEY"))
    index = client.init_index(os.getenv("ALGOLIA_INDEX_NAME"))
    index.set_settings({"searchableAttributes": ["location","categorie", "description"],
                        "customRanking": ["desc(created)"],
                        "attributesForFaceting": ["categorie"]})

    res = index.save_objects(get_produits_from_db())

    print(res)

if __name__ == '__main__':
    add_produits_to_algolia()
