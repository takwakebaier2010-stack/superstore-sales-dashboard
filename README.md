\# 📊 Dashboard d'analyse des ventes — Superstore



Dashboard interactif d'analyse des ventes d'un magasin américain (2014–2017), construit avec \*\*Python, pandas, Plotly et Streamlit\*\*.



🔗 \*\*Démo en ligne :\*\* \_lien à ajouter après le déploiement\_



!\[Aperçu du dashboard](docs/screenshot.png)



\## 🎯 Objectif



Transformer un jeu de données de ventes brut en un tableau de bord clair, qui répond rapidement à des questions business :



\- Quels sont les ventes, le profit et la marge globale ?

\- Comment les ventes évoluent-elles dans le temps ?

\- Quelles catégories, régions et produits rapportent le plus (ou font perdre de l'argent) ?

\- Quels sont les meilleurs clients et segments ?



\## ✨ Fonctionnalités



\- 4 indicateurs clés (KPI) : ventes totales, profit total, nombre de commandes, marge

\- Filtres interactifs : année, région, catégorie

\- Évolution mensuelle des ventes et du profit

\- Analyse par catégorie, sous-catégorie, région et segment de clients

\- Top 10 produits et top 10 clients

\- Tableau de données et export CSV des données filtrées



\## 📁 Données



\- Source : \[Superstore Dataset (Kaggle)](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

\- 9 994 lignes et 21 colonnes, commandes de janvier 2014 à décembre 2017

\- Préparation : conversion des dates (format mois/jour/année), vérification des valeurs manquantes (aucune) et des doublons (aucun)



\## 🔎 Chiffres clés



| Indicateur | Valeur |

|---|---|

| Ventes totales | 2 297 201 $ |

| Profit total | 286 397 $ |

| Commandes | 5 009 |

| Marge | 12,5 % |



\- Les ventes annuelles passent de 484 k$ (2014) à 733 k$ (2017).

\- La catégorie Technology génère le plus de profit (145 k$). Furniture rapporte seulement 18 k$ de profit pour 742 k$ de ventes, soit environ 2,5 % de marge.



\## 🛠️ Technologies



\- Python

\- pandas (nettoyage et analyse)

\- Plotly (graphiques interactifs)

\- Streamlit (interface web du dashboard)



\## ▶️ Lancer le projet en local



```bash

git clone https://github.com/TON-PSEUDO/superstore-sales-dashboard.git

cd superstore-sales-dashboard

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

streamlit run app.py

```



Sur Mac ou Linux, remplace `venv\\Scripts\\activate` par `source venv/bin/activate`.



\## 🗂️ Structure du projet



```

superstore-sales-dashboard/

├── app.py               # le dashboard Streamlit

├── explore.py           # exploration et calcul des KPI

├── requirements.txt     # bibliothèques nécessaires

├── data/

│   └── superstore.csv   # jeu de données

├── docs/

│   └── screenshot.png   # capture d'écran

└── .streamlit/

&#x20;   └── config.toml      # thème (blanc et vert)

```



\## 👩‍💻 Auteure



\*\*Takwa Kebaier\*\* — étudiante en 3e année de Licence Business Information Systems, ISG Tunis.



\[LinkedIn](https://www.linkedin.com/in/takwa-kebaier)

