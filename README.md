# Drug design : morphine et paclitaxel

Pipeline reproductible de préparation de ligands, docking moléculaire et génération d'analogues, appliqué à deux molécules aux propriétés structurales contrastées.

| Ligand | Cible | PDB (à vérifier sur rcsb.org) |
|---|---|---|
| Morphine | Récepteur opioïde µ | 5C1M |
| Paclitaxel | Tubuline β | 5SYF / 1JFF |

## Objectifs

1. Préparer les ligands (SMILES, stéréochimie, conformères 3D) avec RDKit.
2. Valider le protocole par **re-docking** du ligand co-cristallisé (RMSD < 2 Å).
3. Docker morphine et paclitaxel avec AutoDock Vina.
4. Générer des analogues (VAE sur SMILES ou REINVENT) puis les filtrer par docking.

## Structure

```
data/        SMILES et structures d'entrée (pas de gros fichiers)
notebooks/   01_ligand_prep, 02_docking, 03_generative
src/         fonctions réutilisables
results/     sorties (ignorées par git sauf exemples légers)
```

## Installation

```bash
conda env create -f environment.yml
conda activate drug-design
jupyter lab
```

## Avancement

- [x] 01 Préparation des ligands (RDKit)
- [ ] 02 Docking (re-docking puis docking)
- [ ] 03 Modèle génératif

## Limites

Les scores de docking sont des approximations grossières de l'affinité. Le paclitaxel, grand et très flexible, est un cas difficile : les résultats sont à interpréter avec prudence. Versions et seeds sont fixées dans les notebooks.

## Licence

MIT
