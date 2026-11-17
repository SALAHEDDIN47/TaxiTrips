# Guide de Contribution - Équipe E6 (TaxiTrips)

## 1. Rôles de l'équipe
* **Release Manager** : Salahadine (Gère les releases, hotfix, tags)
* **Intégrateur** : Membre 2 (Vérifie les PR, gère le conflit README)
* **Documentaliste** : Membre 3 (Gère le README, CHANGELOG et le rapport)
* **Développeur** : Membre 4 (Code les features, relit les PR)

## 2. Règles de branches
* `main` : Code en production (Protégée)
* `develop` : Branche d'intégration (Protégée)
* `feature/<nom>` : Créée depuis `develop`
* `release/<x.y.z>` : Créée depuis `develop`
* `hotfix/<x.y.z>` : Créée depuis `main`

## 3. Conventions de commits
Nous utilisons les commits conventionnels :
* `feat(module): description` (nouvelle fonctionnalité)
* `fix(module): description` (correction de bug)
* `test(module): description` (ajout de test)
* `docs: description` (documentation)
* `chore: description` (maintenance, config)

## 4. Ordre de relecture (Merge croisé)
Personne ne fusionne sa propre PR. Le relecteur qui approuve est celui qui clique sur "Merge".
* Salahadine relit la PR de Membre 2
* Membre 2 relit la PR de Membre 3
* Membre 3 relit la PR de Membre 4
* Membre 4 relit la PR de Salahadine

## 5. Règles d'or (Pénalités TP)
* ❌ Interdiction de `git push` directement sur `main` ou `develop`.
* ❌ Interdiction d'utiliser `git push --force` sur les branches protégées.
* ✅ Utiliser `git push --force-with-lease` uniquement sur sa propre branche `feature/` après un rebase.