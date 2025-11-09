# 🏦 AIA - BLOC_02 : Architecture DATA chez STRIPE 🌦️ 

## Présentation en ligne de l'intégralité du projet

🚀 [Bloc_02 | STRIPE | Présentation PPT](https://docs.google.com/presentation/d/1EUjt6ZuZBRxjuxuWD4OKV9wgqbWGHm1zGtCbE3KnmMc/edit?usp=sharing) \
📁 [Bloc_02 | STRIPE | Backup sur GitHub]()

> **Architecture data moderne, sécurisée et conforme pour une plateforme FinTech mondiale**

Ce dépôt contient l’ensemble des documents techniques et de conformité pour l’architecture data de Stripe, alignée sur les réglementations **GDPR, CCPA et PCI-DSS**.

---

## 📁 Arborescence du dépôt

```

└── BLOC_02/
    ├── AIA_BLOC_02_STRIPE_SECURITE_GOUVERNANCE.pdf ← Document central de conformité
    ├── AIA_BLOC_02_STRIPE_ARCHITECTURE_DOCUMENTATION_OLTP.pdf ← Documentation OLTP (PostgreSQL)
    ├── AIA_BLOC_02_STRIPE_ARCHITECTURE_DOCUMENTATION_OLAP.pdf ← Documentation OLAP (Snowflake)
    ├── AIA_BLOC_02_STRIPE_ARCHITECTURE_DOCUMENTATION_NoSQL.pdf ← Documentation NoSQL (MongoDB)
    ├── AIA_BLOC_02_STRIPE_ARCHITECTURE_DOCUMENTATION_MACHINE_LEARNING.pdf ← Documentation ML (Feast, MLflow)
    ├── AIA_BLOC_02_STRIPE_ARCHITECTURE_DOCUMENTATION_PIPELINES.pdf ← Documentation Pipelines (Kafka, Airflow, Flink)
    ├── AIA_BLOC_02_STRIPE_SQL_NoSQL_QUERIES.pdf ← Exemples de requêtes SQL + NoSQL
    ├── AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLTP.pdf ← Schéma ERD OLTP (entités, relations)
    ├── AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLAP.pdf ← Schéma ERD OLAP (star schema)
    ├── AIA_BLOC_02_STRIPE_DIAGRAMME_noSQL_STRIPE.pdf ← Schéma NoSQL (collections, flux)
    └── README.md ← Ce document

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
📄 [`DOCUMENTATION SECURITE & GOVERNANCE`](AIA_BLOC_02_STRIPE_SECURITE_GOUVERNANCE.pdf)  
→ **Document central** : cadre réglementaire, principes, recommandations par couche.

### 2. **Architecture Technique**

| Domaine | Document |
|--------|----------|
| **OLTP** | [`DOCUMENTATION ARCHITECTURE OTLP`](AIA_BLOC_02_STRIPE_DOCUMENTATION_OLTP_DIAGRAMME_SQL.pdf) |
| **OLAP** | [`DOCUMENTATION ARCHITECTURE OLAP`](AIA_BLOC_02_STRIPE_DOCUMENTATION_OLA_DIAGRAMME_SQL.pdf) |
| **NoSQL** | [`DOCUMENTATION ARCHITECTURE NoSQL`](AIA_BLOC_02_STRIPE_ARCHITECTURE_DOCUMENTATION_NoSQL.pdf) |
| **Pipelines** | [`DOCUMENTATION ARCHITECTURE PIPELINES`](AIA_BLOC_02_STRIPE_DOCUMENTATION_ARCHITECTURE_PIPELINES.pdf) |
| **Machine Learning** | [`DOCUMENTATION ARCHITECTURE PIPELINE`](AIA_BLOC_02_STRIPE_ARCHITECTURE_MACHINE_LEARNING.pdf) |

### 3. **Diagrammes**

| Type | Document |
|------|----------|
| **ERD OLTP** | [`AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLTP.pdf`](AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLTP.pdf) |
| **ERD OLAP** | [`AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLAP.pdf`](AIA_BLOC_02_STRIPE_DIAGRAMME_ERD_OLAP.pdf) |
| **NoSQL Schema** | [`AIA_BLOC_02_STRIPE_DIAGRAMME_noSQL_STRIPE.pdf`](AIA_BLOC_02_STRIPE_DIAGRAMME_noSQL_STRIPE.pdf) |

### 4. **Documentation & Requêtes**

| Contenu | Document |
|---------|----------|
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

