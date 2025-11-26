---
title: Real Time Fraud Detection
emoji: 🐠
colorFrom: red
colorTo: gray
sdk: docker
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

##  Customisation de l'API Jedha

# Jedha - Real-time Payments API 💵

Une API simple pour simuler des transactions en temps réel, avec une limite de 5 transactions par minute.

---

## 📌 Description

Cette API permet de récupérer des transactions aléatoires depuis un fichier CSV (`fraud_api.csv`). Chaque transaction inclut des informations comme l'heure, la date, et un indicateur de fraude.
🚨 Attention : masquer l'indicateur de Fraude avant de passer l'information dans votre modèle de Machine Learning.


---

## 🚀 Installation et Exécution

### Étapes

```
#### 1. Cloner le dépôt
Clone le dépôt ou télécharge les fichiers du projet sur ta machine locale.

#### 2. Exécution avec Docker
L'image Docker `jedha/real-time-payments-api-lead-program` contient déjà toutes les dépendances nécessaires. Il suffit de construire et lancer le conteneur :

```

L'API sera accessible à l'adresse : [http://0.0.0.0:4000](http://0.0.0.0:4000).

Sur Hugging Face Space : [https://ericjedha-real-time-fraud-detection.hf.space](https://ericjedha-real-time-fraud-detection.hf.space)

---

## 📂 Structure du Projet

| Fichier/Dossier       | Description                                  |
|-----------------------|----------------------------------------------|
| `app.py`              | Code principal de l'API FastAPI.             |
| `fraud_api.csv`       | Fichier CSV contenant les données de transaction. |
| `static/`             | Dossier pour les fichiers statiques (CSS, JS, etc.). |
| `templates/index.html`| Page HTML de base pour l'API.                |
| `Dockerfile`          | Configuration pour conteneuriser l'application. |
| `README.md`           | Ce fichier.                                  |

---

## 🔧 Endpoints Disponibles

| Endpoint                | Méthode | Description                                      | Limite          |
|-------------------------|---------|--------------------------------------------------|-----------------|
| `/`                     | GET     | Affiche la page d'accueil.                       | Aucune          |
| `/current-transactions`| GET     | Retourne une transaction aléatoire au format JSON. | 5/minute/IP     |

---

## 🛠️ Limitation de Débit

L'API utilise [`slowapi`](https://pypi.org/project/slowapi/) pour limiter le nombre de requêtes :
- **5 requêtes par minute** pour `/current-transactions`.
- Une réponse `429 Too Many Requests` est retournée si la limite est dépassée.

---

## 📦 Utilisation avec Docker

1. Construire l'image Docker :
   ```bash
   docker build -t jedha-payments-api .
   ```
2. Lancer le conteneur :
   ```bash
   docker run -d -p 4000:4000 jedha-payments-api
   ```

---

## 📝 Exemple de Réponse

```json
{
  "columns": ["col1", "col2", ...],
  "data": [[val1, val2, ...], ...],
  "index": [0]
}
```

---

## 🤝 Contribution

Pour contribuer, ouvre une *issue* ou soumets une *pull request*.
