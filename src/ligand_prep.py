"""Fonctions de préparation de ligands avec RDKit."""
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, rdMolDescriptors

SEED = 42


def load_mol(smiles: str) -> Chem.Mol:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"SMILES invalide : {smiles}")
    return mol


def describe(mol: Chem.Mol) -> dict:
    centers = Chem.FindMolChiralCenters(mol, includeUnassigned=True, useLegacyImplementation=False)
    return {
        "formule": rdMolDescriptors.CalcMolFormula(mol),
        "masse_molaire": round(Descriptors.MolWt(mol), 2),
        "logP": round(Descriptors.MolLogP(mol), 2),
        "HBD": rdMolDescriptors.CalcNumHBD(mol),
        "HBA": rdMolDescriptors.CalcNumHBA(mol),
        "liaisons_rotatives": rdMolDescriptors.CalcNumRotatableBonds(mol),
        "centres_chiraux": len(centers),
    }


def embed_conformers(mol: Chem.Mol, n_confs: int = 50, seed: int = SEED):
    """Génère des conformères 3D, les optimise (MMFF) et renvoie (mol_H, énergies)."""
    molh = Chem.AddHs(mol)
    ids = AllChem.EmbedMultipleConfs(molh, numConfs=n_confs, randomSeed=seed)
    res = AllChem.MMFFOptimizeMoleculeConfs(molh, maxIters=2000)
    energies = [e for _, e in res]
    return molh, list(ids), energies


def write_best_conformer(molh: Chem.Mol, energies, path: str) -> int:
    best = min(range(len(energies)), key=energies.__getitem__)
    Chem.MolToMolFile(molh, path, confId=best)
    return best
