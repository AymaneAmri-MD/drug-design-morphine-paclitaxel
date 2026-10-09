# Drug design : morphine et atropine

Pipeline reproductible de préparation de ligands, docking moléculaire et génération d'analogues, appliqué à deux alcaloïdes aux cibles bien caractérisées.

| Ligand | Cible | PDB (à vérifier sur rcsb.org) |
|---|---|---|
| Morphine | Récepteur opioïde µ | 5C1M |
| Atropine (L-hyoscyamine) | Récepteur muscarinique M2 | 3UON |

## Objectifs

1. Préparer les ligands (SMILES, stéréochimie, conformères 3D) avec RDKit.
2. Valider le protocole par **re-docking** du ligand co-cristallisé (RMSD < 2 Å).
3. Docker morphine et atropine avec AutoDock Vina.
4. Générer des analogues (VAE sur SMILES ou REINVENT) puis les filtrer par docking.

## Structure

```
data/        SMILES et structures d'entrée (pas de gros fichiers)
notebooks/   01_ligand_prep, 02_docking, 03_generative
src/         fonctions réutilisables
results/     sorties (ignorées par git sauf exemples légers)
```

## Utilisation

Les notebooks sont conçus pour **Google Colab** (Fichier, puis Importer un notebook). Pour une installation locale :

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

Les scores de docking sont des approximations grossières de l'affinité. Récepteurs rigides, ligands dockés sous forme neutre, atropine représentée par son énantiomère actif (L-hyoscyamine). Versions et seeds sont fixées dans les notebooks.

*Note de parcours : le paclitaxel (cible : tubuline) avait été envisagé, puis écarté car trop flexible pour un calcul raisonnable sur Colab gratuit.*

## Licence

MIT
