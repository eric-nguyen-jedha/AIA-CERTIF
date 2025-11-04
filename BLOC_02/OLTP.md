
## Modèle de Données OLTP

Le modèle OLTP conçu pour Stripe répond aux exigences critiques d’une plateforme FinTech à très haut débit, avec un accent sur la conformité, l’intégrité des données et la scalabilité.

## ✅ Respect strict de la 3ᵉ forme normale (3NF)
- Élimination des redondances (ex: `country_name` stocké une seule fois dans `COUNTRY`)
- Réduction des anomalies de mise à jour
- Cohérence maximale des données critiques (montants, statuts, devises)

## 🔗 Relations explicites au lieu de many-to-many implicites
- Toute association complexe devient une entité métier à part entière (ex: `SUBSCRIPTION`, `TRANSACTION_EVENT`, `FRAUD_SCORE`)
- Permet de capturer des attributs temporels, des métadonnées et un historique (ex: événements de statut, dates de remboursement)

## 🕵️ Traçabilité et auditabilité native
- Chaque entité comporte `created_at` / `updated_at`
- Les changements d’état sont historisés via `TRANSACTION_EVENT`
- Essentiel pour la conformité PCI-DSS, GDPR et les enquêtes de fraude

## 🧩 Extensibilité via `jsonb` sans compromis structurel
- Champs comme `metadata`, `risk_indicators`, `evidence` permettent d’ajouter des données sans modifier le schéma
- Idéal pour les intégrations rapides (nouveaux PSP, réglementations locales) tout en gardant les colonnes critiques typées (ex: `amount`, `currency_code`)

## 🔒 Séparation claire des responsabilités
- `CUSTOMER` vs `CUSTOMER_PROFILE` : les données d’identité sont séparées des agrégats analytiques
- Permet des accès différenciés (ex: support accède au client, ML accède au profil)
- Réduit la surface d’attaque (moins de données sensibles exposées)

## 🔄 Préparation native pour le CDC (Change Data Capture)
- Clés primaires UUID, versioning (`version` dans `TRANSACTION`)
- Modèle idéal pour alimenter Kafka via Debezium sans transformation complexe
- Base solide pour l’architecture Lambda (batch + streaming)

## 💼 Alignement avec les exigences métier FinTech
- Modélisation fine des concepts clés : remboursements, chargebacks, abonnements, fraude
- Chaque opération financière est traçable, annulable (logiquement) et justifiable — crucial pour les audits

## ⚡ Performance transactionnelle optimisée
- Indexation implicite via les clés étrangères
- Tables étroites (pas de colonnes inutiles dans `TRANSACTION`)
- Faible latence même sous forte charge (OLTP distribué compatible avec CockroachDB/PostgreSQL)


```mermaid

erDiagram
    MERCHANT ||--o{ TRANSACTION : processes
    CUSTOMER ||--o{ TRANSACTION : makes
    TRANSACTION ||--o{ TRANSACTION_EVENT : has
    TRANSACTION ||--|| PAYMENT_METHOD : uses
    TRANSACTION }o--|| CURRENCY : denominated_in
    TRANSACTION ||--o{ REFUND : generates
    TRANSACTION ||--o{ CHARGEBACK : may_have
    MERCHANT ||--o{ SUBSCRIPTION : offers
    CUSTOMER ||--o{ SUBSCRIPTION : subscribes_to
    SUBSCRIPTION ||--o{ SUBSCRIPTION_PAYMENT : generates
    TRANSACTION ||--o{ FRAUD_SCORE : has
    CUSTOMER ||--|| CUSTOMER_PROFILE : has
    MERCHANT ||--|| MERCHANT_PROFILE : has
    TRANSACTION }o--|| COUNTRY : originated_from
    PAYMENT_METHOD }o--|| PAYMENT_TYPE : is_of_type

    MERCHANT {
        uuid merchant_id PK
        varchar merchant_name
        varchar legal_entity_name
        varchar business_type
        varchar country_code FK
        varchar currency_code FK
        boolean is_active
        timestamp created_at
        timestamp updated_at
        jsonb settings
        varchar mcc_code
    }

    MERCHANT_PROFILE {
        uuid profile_id PK
        uuid merchant_id FK
        varchar industry
        decimal avg_transaction_amount
        integer monthly_volume
        jsonb risk_indicators
        varchar compliance_status
        timestamp last_reviewed_at
    }

    CUSTOMER {
        uuid customer_id PK
        varchar email
        varchar phone_number
        varchar country_code FK
        boolean is_verified
        timestamp created_at
        timestamp updated_at
        varchar external_id
    }

    CUSTOMER_PROFILE {
        uuid profile_id PK
        uuid customer_id FK
        integer lifetime_transactions
        decimal lifetime_value
        varchar risk_level
        jsonb preferences
        timestamp last_transaction_at
    }

    TRANSACTION {
        uuid transaction_id PK
        uuid merchant_id FK
        uuid customer_id FK
        uuid payment_method_id FK
        decimal amount
        varchar currency_code FK
        varchar status
        timestamp transaction_date
        varchar ip_address
        varchar device_type
        varchar country_code FK
        decimal fee_amount
        varchar description
        jsonb metadata
        timestamp created_at
        timestamp updated_at
        integer version
    }

    TRANSACTION_EVENT {
        uuid event_id PK
        uuid transaction_id FK
        varchar event_type
        varchar previous_status
        varchar new_status
        jsonb event_data
        timestamp event_timestamp
        varchar triggered_by
    }

    PAYMENT_METHOD {
        uuid payment_method_id PK
        uuid customer_id FK
        varchar payment_type_code FK
        varchar last_four_digits
        varchar card_brand
        varchar expiry_month
        varchar expiry_year
        boolean is_default
        varchar fingerprint
        timestamp created_at
        boolean is_active
    }

    PAYMENT_TYPE {
        varchar payment_type_code PK
        varchar payment_type_name
        varchar category
        boolean supports_refund
        jsonb processing_rules
    }

    REFUND {
        uuid refund_id PK
        uuid transaction_id FK
        decimal refund_amount
        varchar refund_reason
        varchar status
        timestamp requested_at
        timestamp processed_at
        varchar processed_by
        jsonb metadata
    }

    CHARGEBACK {
        uuid chargeback_id PK
        uuid transaction_id FK
        decimal chargeback_amount
        varchar reason_code
        varchar status
        timestamp filed_at
        timestamp resolved_at
        varchar resolution
        jsonb evidence
    }

    SUBSCRIPTION {
        uuid subscription_id PK
        uuid merchant_id FK
        uuid customer_id FK
        varchar plan_id
        varchar status
        decimal amount
        varchar currency_code FK
        varchar billing_cycle
        timestamp start_date
        timestamp end_date
        timestamp next_billing_date
        timestamp created_at
        timestamp updated_at
    }

    SUBSCRIPTION_PAYMENT {
        uuid payment_id PK
        uuid subscription_id FK
        uuid transaction_id FK
        varchar status
        timestamp billing_date
        timestamp processed_at
        integer retry_count
    }

    FRAUD_SCORE {
        uuid score_id PK
        uuid transaction_id FK
        decimal fraud_score
        varchar risk_level
        jsonb risk_indicators
        varchar model_version
        timestamp scored_at
        boolean requires_review
    }

    CURRENCY {
        varchar currency_code PK
        varchar currency_name
        integer decimal_places
        boolean is_active
    }

    COUNTRY {
        varchar country_code PK
        varchar country_name
        varchar region
        boolean high_risk
        jsonb compliance_requirements
    }
```

![Schéma ERD OLTP STRIPE](ERD-OLTP.png)
