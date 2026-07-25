# Roadmap initiale d’Adaptive Deep Research Engine

Cette roadmap découpe la première version d’Adaptive Deep Research Engine en étapes testables. Une étape ne doit pas commencer tant que ses dépendances ne sont pas terminées et vérifiées.

## Règle de progression

1. Partir de `develop`.
2. Créer une branche courte liée à une seule issue.
3. Écrire un test qui échoue pour la raison attendue.
4. Ajouter le minimum de code nécessaire pour le faire passer.
5. Lancer la suite complète.
6. Pousser la branche après chaque état vert significatif.
7. Ouvrir une pull request vers `develop`.
8. Fusionner seulement après vérification des critères d'acceptation.

`main` reste réservé aux jalons démontrables. Aucun changement de fonctionnalité ne doit être poussé directement sur `main` ou `develop`.

## M0 Fondations déterministes

### Objectif

Exécuter une recherche complète à partir de fixtures locales, sans réseau et sans modèle, tout en conservant une trace explicable.

### Tickets

| Issue | Résultat testable |
|---|---|
| [#2](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/2) | Une fixture produit une trace JSON déterministe avec un claim supporté, une preuve, une lacune et une raison d'arrêt. |
| [#3](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/3) | Les limites invalides sont rejetées et une limite atteinte arrête réellement le run. |
| [#4](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/4) | Un snippet ne peut pas devenir directement une preuve. |
| [#5](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/5) | Les claims portent un type, un périmètre et un standard de preuve. |
| [#6](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/6) | Les contradictions sont classées selon leur contexte. |
| [#7](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/7) | Les duplications et reprises d'une même origine ne comptent pas comme confirmations indépendantes. |
| [#8](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/8) | Un rapport Markdown est reconstruit uniquement depuis la trace. |
| [#9](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/9) | Le run déterministe peut être lancé depuis le terminal. |

### Ce que je dois pouvoir faire à la fin

```text
lancer une fixture locale
voir les claims et leur statut
retrouver le passage exact lié à chaque conclusion
voir les lacunes et contradictions
comprendre pourquoi le run s'est arrêté
obtenir une sortie JSON et Markdown reproductible
```

### Gate de sortie

M0 est terminé lorsque la CLI déterministe fonctionne depuis une installation propre et que tous les tests passent sans réseau ni credential.

## M1 Acquisition fiable

### Objectif

Découvrir et récupérer des documents à travers des contrats neutres, sans laisser Tavily ou Exa dicter le modèle métier.

### Tickets

| Issue | Résultat testable |
|---|---|
| [#10](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/10) | Un faux fournisseur répond à un contrat de recherche neutre. |
| [#11](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/11) | Une réponse Tavily enregistrée est normalisée sans appel réel. |
| [#12](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/12) | Une réponse Exa enregistrée est normalisée et le choix du fournisseur est tracé. |
| [#13](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/13) | Une référence découverte devient un document complet avec URL canonique, date et empreinte. |

### Ce que je dois pouvoir faire à la fin

```text
soumettre une requête neutre
choisir Tavily ou Exa pour une raison explicite
normaliser leurs réponses dans la même structure
récupérer le document complet
conserver la provenance et les erreurs d'accès
```

### Gate de sortie

M1 est terminé lorsque les deux formats fournisseurs passent les mêmes tests de contrat avec des fixtures enregistrées et sans secret dans le dépôt.

## M2 Boucle adaptative

### Objectif

Choisir chaque nouvelle recherche à partir des lacunes réelles de la recherche précédente.

### Tickets

| Issue | Résultat testable |
|---|---|
| [#14](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/14) | Une vague sans nouveauté utile déclenche une saturation observable. |
| [#15](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/15) | La prochaine requête cible le gap critique le mieux justifié. |
| [#16](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/16) | Les sorties du modèle sont structurées, validées et bornées en retries. |
| [#17](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/17) | Plusieurs vagues enregistrées font évoluer le graphe jusqu'à une raison d'arrêt explicite. |

### Ce que je dois pouvoir faire à la fin

```text
voir quel gap déclenche une recherche
voir pourquoi un fournisseur est choisi
observer l'évolution du graphe après chaque vague
arrêter le run sur couverture, saturation ou limite
rejouer les décisions déterministes
```

### Gate de sortie

M2 est terminé lorsque deux scénarios opposés passent. Le premier atteint la couverture attendue. Le second atteint une limite et conserve un claim non résolu.

## M3 Validation V1

### Objectif

Vérifier sur un petit pilote réel que la boucle evidence-first apporte une valeur mesurable face à une fusion naïve.

### Tickets

| Issue | Résultat testable |
|---|---|
| [#18](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/18) | Un pilote live borné utilise Tavily et Exa sans dépasser ses limites. |
| [#19](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/19) | Adaptive Deep Research Engine est comparé à Tavily seul, Exa seul et une fusion simple. |
| [#20](https://github.com/ForgedEmir/Adaptive-Deep-Research-Engine/issues/20) | La première version démontrable est vérifiée depuis une installation propre. |

### Ce que je dois pouvoir faire à la fin

```text
lancer une question factuelle réelle
inspecter les preuves et citations
mesurer coût et latence
comparer la couverture et les contradictions
reproduire une démonstration complète
```

### Gate de sortie

La V1 est démontrable seulement si elle possède une CLI, deux fournisseurs, des tests, un benchmark contre une fusion naïve, des citations traçables et des limites de coût, de vagues et de timeout réellement exercées.

## Politique de branches

| Type de travail | Format de branche | Base | Cible de PR |
|---|---|---|---|
| Fonctionnalité | `feat/<issue>-<sujet>` | `develop` | `develop` |
| Correction | `fix/<issue>-<sujet>` | `develop` | `develop` |
| Test | `test/<issue>-<sujet>` | `develop` | `develop` |
| Documentation | `docs/<sujet>` | `develop` | `develop` |
| Jalon accepté | `release/<version>` | `develop` | `main` |

Une branche doit rester courte et liée à un objectif vérifiable. Les commits doivent rester verts. Les pushes réguliers ont lieu après un cycle test, implémentation et vérification terminé, pas au milieu d'un état volontairement cassé.
