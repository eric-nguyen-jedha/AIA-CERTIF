# 🏦 Stripe Data Architecture – Bloc 02 : Security & Governance

> **Architecture data moderne, sécurisée et conforme pour une plateforme FinTech mondiale**

Ce dépôt contient l’ensemble des documents techniques et de conformité pour l’architecture data de Stripe, alignée sur les réglementations **GDPR, CCPA et PCI-DSS**.

---

## 📁 Arborescence du dépôt

```

└── BLOC_02/
    ├── AIA_BLOC_02_STRIPE_SECURITE_GOUVERNANCE.pdf ← Document central de conformité
    ├── AIA_BLOC_02_STRIPE_ARCHITECTURE_OLTP.pdf ← Modèle transactionnel (PostgreSQL)
    ├── AIA_BLOC_02_STRIPE_ARCHITECTURE_OLAP.pdf ← Modèle analytique (Snowflake)
    ├── AIA_BLOC_02_STRIPE_ARCHITECTURE_NoSQL.pdf ← Modèle documentaire (MongoDB)
    ├── AIA_BLOC_02_STRIPE_ARCHITECTURE_PIPELINES.pdf ← Architecture des pipelines (Kafka, Airflow, Flink)
    ├── AIA_BLOC_02_STRIPE_ARCHITECTURE_MACHINE_LEARNING.pdf ← Architecture ML (Feast, MLflow, Monitoring)
    ├── AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLTP.pdf ← Schéma ERD OLTP (entités, relations, cardinalités)
    ├── AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLAP.pdf ← Schéma OLAP (star schema, dimensions, faits)
    ├── AIA_BLOC_02_STRIPE_DIAGRAMME_noSQL_STRIPE.pdf ← Schéma NoSQL (collections, champs, flux)
    ├── AIA_BLOC_02_STRIPE_DOCUMENTATION_OLA_DIAGRAMME_SQL.pdf ← Requêtes SQL OLAP (revenus, fraude, segmentation)
    ├── AIA_BLOC_02_STRIPE_DOCUMENTATION_OLTP_DIAGRAMME_SQL.pdf ← Requêtes SQL OLTP (transactions, logs, statistiques)
    ├── AIA_BLOC_02_STRIPE_SQL_NoSQL_QUERIES.pdf ← Exemples de requêtes NoSQL (MongoDB) et SQL combinées

```


---

## 🎯 Objectif du projet

Construire une **architecture data unifiée, évolutive et sécurisée** pour Stripe, couvrant :

- **OLTP** : transactions à haute fréquence, ACID, disponible en continu.
- **OLAP** : analyses complexes, agrégations, reporting temps réel.
- **NoSQL** : données non structurées (logs, interactions, features ML).
- **Sécurité & Conformité** : GDPR, CCPA, PCI-DSS intégrés dès la conception.
- **Machine Learning** : modèles en production avec monitoring, retraining et explication.

---

## 📄 Documents clés

### 1. **Sécurité & Gouvernance**
📄 [`AIA_BLOC_02_STRIPE_SECURITE_GOUVERNANCE.pdf`](AIA_BLOC_02_STRIPE_SECURITE_GOUVERNANCE.pdf)  
→ **Document central** : cadre réglementaire, principes, recommandations par couche.

### 2. **Architecture Technique**

| Domaine | Document |
|--------|----------|
| **OLTP** | [`AIA_BLOC_02_STRIPE_ARCHITECTURE_OLTP.pdf`](AIA_BLOC_02_STRIPE_ARCHITECTURE_OLTP.pdf) |
| **OLAP** | [`AIA_BLOC_02_STRIPE_ARCHITECTURE_OLAP.pdf`](AIA_BLOC_02_STRIPE_ARCHITECTURE_OLAP.pdf) |
| **NoSQL** | [`AIA_BLOC_02_STRIPE_ARCHITECTURE_NoSQL.pdf`](AIA_BLOC_02_STRIPE_ARCHITECTURE_NoSQL.pdf) |
| **Pipelines** | [`AIA_BLOC_02_STRIPE_ARCHITECTURE_PIPELINES.pdf`](AIA_BLOC_02_STRIPE_ARCHITECTURE_PIPELINES.pdf) |
| **Machine Learning** | [`AIA_BLOC_02_STRIPE_ARCHITECTURE_MACHINE_LEARNING.pdf`](AIA_BLOC_02_STRIPE_ARCHITECTURE_MACHINE_LEARNING.pdf) |

### 3. **Diagrammes**

| Type | Document |
|------|----------|
| **ERD OLTP** | [`AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLTP.pdf`](AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLTP.pdf) |
| **ERD OLAP** | [`AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLAP.pdf`](AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLAP.pdf) |
| **NoSQL Schema** | [`AIA_BLOC_02_STRIPE_DIAGRAMME_noSQL_STRIPE.pdf`](AIA_BLOC_02_STRIPE_DIAGRAMME_noSQL_STRIPE.pdf) |

### 4. **Documentation & Requêtes**

| Contenu | Document |
|---------|----------|
| **Requêtes SQL OLAP** | [`AIA_BLOC_02_STRIPE_DOCUMENTATION_OLA_DIAGRAMME_SQL.pdf`](AIA_BLOC_02_STRIPE_DOCUMENTATION_OLA_DIAGRAMME_SQL.pdf) |
| **Requêtes SQL OLTP** | [`AIA_BLOC_02_STRIPE_DOCUMENTATION_OLTP_DIAGRAMME_SQL.pdf`](AIA_BLOC_02_STRIPE_DOCUMENTATION_OLTP_DIAGRAMME_SQL.pdf) |
| **Requêtes NoSQL + SQL** | [`AIA_BLOC_02_STRIPE_SQL_NoSQL_QUERIES.pdf`](AIA_BLOC_02_STRIPE_SQL_NoSQL_QUERIES.pdf) |

---

## 🔐 Conformité & Sécurité

Tous les composants respectent les exigences de :
- **GDPR** (UE) : droit d’accès, effacement, portabilité, consentement.
- **CCPA** (Californie) : opt-out, transparence.
- **PCI-DSS** (paiements) : tokenisation, segmentation réseau, chiffrement.

> ✅ **Privacy & Security by Design** : la conformité est **intégrée dans l’architecture**, pas ajoutée après coup.

---

## 🚀 Prochaines étapes

1. **Déploiement des pipelines** (Airflow, Kafka, Flink)
2. **Mise en place du Feature Store** (Feast) et du modèle ML
3. **Validation de conformité** par DPO et auditeurs
4. **Monitoring continu** (Evidently, MLflow, Prometheus)

---

## 📞 Contact

Pour toute question ou clarification :

> **Équipe Data Engineering**  
> Email : enguyen.fr@gmail.com  
> Slack : #data-architecture

---

