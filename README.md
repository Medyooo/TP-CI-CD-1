# 🚀 TP : Pipeline CI/CD et Tests en Python

**Auteur** : Mohamed Larbi EL BAIDI 
**Projet GitHub** : [https://github.com/Medyooo/TP-CI-CD-1](https://github.com/Medyooo/TP-CI-CD-1)

---

## 🧠 Objectif du TP

Mettre en place un pipeline CI/CD simple avec GitHub Actions, intégrer des tests unitaires en Python, et automatiser la vérification du code source à chaque modification.

---

## 🗂️ Structure du projet

```
TP-CI-CD-1/
├── app/
│   └── math_functions.py         # Fichier contenant les fonctions à tester
├── tests/
│   └── test_math_functions.py    # Fichier de tests unitaires (pytest)
├── requirements.txt              # Dépendances du projet
├── .github/
│   └── workflows/
│       └── python-ci.yml         # Fichier de configuration GitHub Actions
├── .gitignore
└── README.md                     # Rapport de présentation
```

---

## 🔬 Fonctionnalité testée

Fichier `app/math_functions.py` :

```python
def addition(a, b):
    return a + b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro interdite.")
    return a / b
```

---

## ✅ Tests unitaires (`pytest`)

Fichier `tests/test_math_functions.py` :

- `test_addition()` : valeurs positives et négatives
- `test_division()` : division normale et négative
- `test_division_by_zero()` : gestion d'erreur

### Couverture testée avec `pytest-cov`

```bash
pytest --cov=app --cov-report=term-missing tests/
```

---

## 🔄 Pipeline CI/CD avec GitHub Actions

Fichier `.github/workflows/python-ci.yml` :

- Lance les tests à chaque `push` ou `pull_request` sur `main` ou `master`
- Installe les dépendances
- Exécute les tests avec couverture de code
- Affiche les lignes non couvertes

Extrait de configuration :

```yaml
- name: Lancer les tests avec couverture
  run: |
    PYTHONPATH=. pytest --cov=app --cov-report=term-missing tests/
```

---

## ❌ Erreurs rencontrées et résolues

| Problème                             | Solution apportée                                   |
|-------------------------------------|-----------------------------------------------------|
| `ModuleNotFoundError: No module named 'app'` | Ajout de `PYTHONPATH=.` avant les commandes `pytest` |
| Syntax error dans `.yml`            | Suppression d’une ligne invalide `git add .`        |
| Tests non trouvés                   | Correction des noms et chemins des fichiers         |

---

## 💡 Réponses aux questions de réflexion

1. **Pourquoi est-il important d’exécuter des tests dans un pipeline CI/CD ?**  
   Pour détecter automatiquement les erreurs dès qu’on modifie le code. Cela évite les bugs en production et garantit que les fonctionnalités restent stables.

2. **Quels avantages offre l’automatisation des tests ?**  
   Gain de temps, exécution fiable et constante, retour immédiat sur les erreurs, amélioration continue de la qualité du code.

3. **Comment améliorer la couverture des tests ?**  
   - Tester les cas limites et erreurs.
   - Ajouter des tests pour toutes les branches conditionnelles (`if`, `except`, etc.).
   - Utiliser des outils de rapport comme `pytest-cov` et HTMLCov.

4. **Quels outils CI/CD sont les plus adaptés à ton projet ?**  
   GitHub Actions est idéal : gratuit, intégré à GitHub, simple à configurer et très utilisé en entreprise. Pour des projets plus complexes, GitLab CI ou Jenkins peuvent être pertinents.

---

## ✅ Résultat attendu

- ✔️ Pipeline fonctionnel
- ✔️ Tests automatisés
- ✔️ Couverture de code visible
- ✔️ Rapport structuré

---

## 🏆 Challenge bonus

- Couverture de code avec `pytest-cov`
- Génération de rapport détaillé
- Gestion des erreurs dans le pipeline

---

> _"Ce projet m'a permis de comprendre concrètement les avantages de l'intégration continue et des tests automatisés dans un workflow de développement professionnel."_
