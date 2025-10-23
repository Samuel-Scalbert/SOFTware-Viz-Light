<p align="center">
    <h1 align="center">SOFTware-Viz</h1>
</p>
<div align="center">
  <img src="https://github.com/user-attachments/assets/43b01db2-450e-4d9d-a805-cb37f861bdb2" alt="logo_full_HUB" width="250" />
</div>

<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=default&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/github/last-commit/Samuel-Scalbert/SOFTware-Viz?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Samuel-Scalbert/SOFTware-Viz?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Samuel-Scalbert/SOFTware-Viz?style=default&color=0080ff" alt="repo-language-count">
</p>

![Capture d’écran du 2024-06-03 16-39-41](https://github.com/Samuel-Scalbert/SOFTware-Viz/assets/32683708/6be2a593-0508-4e52-a7cb-2cf28b768f00)

## Présentation du projet

🛑 Cette version de SOFTware-Viz est la version universelle qui fonctionne avec tous les fichiers PDF et sans connexion à HAL INRIA.

🛑 Si vous utilisez des fichiers de HAL, vous devez utiliser la version originale [SOFTware-Viz](https://github.com/Samuel-Scalbert/SOFTware-Viz).

### Base de données de PDF
Le processus commence avec une base de données de fichiers **PDF** académiques qui doivent être extraits et traités.

### GROBID
Les fichiers **PDF** sont envoyés à **GROBID**, un outil permettant d’extraire des données structurées (comme des informations bibliographiques) à partir de **PDF** académiques. **GROBID** génère en sortie des fichiers **XML**, rendant l’information lisible par machine.

### SOFTCITE
Après **GROBID**, les données extraites sont transmises à **SOFTCITE**, qui génère des fichiers **JSON**. **SOFTCITE** analyse les citations, les mentions de logiciels ou d’autres informations de référence présentes dans les **PDF**.

### SOFTware-Sync
Les fichiers **XML** et **JSON** extraits sont ensuite traités par **SOFTware-Sync**, un outil qui synchronise ces données dans un fichier **XML** unique.

### SOFTware-Viz
**SOFTware-Viz** est chargé de la visualisation des données traitées. Il prend les données synchronisées par **SOFTware-Sync** et les transforme en **tableaux de bord** ou autres représentations graphiques.

### ArangoDB
Les données traitées sont stockées dans **ArangoDB**, une base de données **NoSQL multi-modèle**, permettant la gestion des données structurées. Elle sert de stockage principal pour les informations et mentions extraites.

### Flask
**Flask** est un framework web utilisé pour développer des applications web. Il interagit avec **SOFTware-Viz** (pour la visualisation) et **ArangoDB** (pour la récupération des données).

---

## Installation

#### Depuis `la source`

* Clonez le dépôt :<br>
```console
git clone ../
```
* Accédez au répertoire du projet :<br>
```console
cd ./SOFTware-viz
```
* Créez un environnement virtuel :<br>
```console
python -m venv env
```
* Installez l’image **Docker** :<br>
```console
docker pull arangodb/arangodb:3.11.6
```
* Lancez un conteneur **Docker** :<br>
```console
docker run -p 8529:8529 -e ARANGO_NO_AUTH=1 arangodb/arangodb:3.11.6
```
* Activez l’environnement virtuel :<br>
```console
source env/bin/activate
```
* Installez les dépendances :<br>
```console
pip install -r requirement.txt
```
* Insérez les fichiers XML dans le dossier ./app/static/data/xml_files et les json dans app/static/data/json_files :<br>

🛑Il y a déjà des fichiers de test dans les dossiers (vous pouvez les supprimer pour essayer l'application pour votre corpus)

* Lancez l’application :    
```console
python run.py
```
---

## Utilisation

#### Depuis `la source`

Exécutez l’application avec la commande suivante (**la base de données se créera automatiquement lors du premier lancement**) :

```
python run.py
```