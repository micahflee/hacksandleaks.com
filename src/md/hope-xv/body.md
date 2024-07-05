Much of what is covered in this workshop is covered in [Chapter 10](https://hacksandleaks.com/chapter-10.html), so it may be a useful resource as you follow along.

### Download the BlueLeaks data

Ideally, you will have a full copy of the [BlueLeaks dataset](https://ddosecrets.com/wiki/BlueLeaks). While not required, it would be helpful if you can download it and extract it _before_ the workshop, as it's unlikely that you'll have the time to download it and extract it _during_ the workshop.

#### Already at HOPE?

If you're already at HOPE, you should just download the BlueLeaks Explorer data (about 1GB compressed) that is necessary for the workshop. After tonight, you can spend the rest of the conference downloading the full BlueLeaks dataset.

Download the BlueLeaks Explorer data for the workshop here: [https://drive.google.com/drive/folders/1IuTYt5tZ216GUDwg54SIkZpAYIG87rZc](https://drive.google.com/drive/folders/1IuTYt5tZ216GUDwg54SIkZpAYIG87rZc)

#### The full BlueLeaks dataset

BlueLeaks is 250GB compressed. Here's where to download it:

**BitTorrent magnet link:**

```
magnet:?xt=urn:btih:8cf92b7cd3f022fa5478b84963e89c1dd0af090f&dn=BlueLeaks&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce
```

**Direct download over HTTPS:** [https://data.ddosecrets.com/BlueLeaks/](https://data.ddosecrets.com/BlueLeaks/) (download all 168 files)

Uncompressed, BlueLeaks is 269GB of data. If you download it compressed and then uncompress it, you'll need 519GB of data. I recommend that you use an external USB SSD with at least 1TB of disk space.

(If you want to learn a quick way to uncompress hundreds of zip files, check out the first exercise in [Chapter 4](https://hacksandleaks.com/chapter-4.html).

### Install Docker

Install [Docker Desktop](https://www.docker.com/products/docker-desktop/), or [Docker Engine](https://docs.docker.com/engine/install/) in Linux if you prefer.

After installing, make sure it works by opening a terminal and run:

```sh
docker run hello-world
```

### Install a text editor

If you don't already have one, install a text editor like [Visual Studio Code](https://code.visualstudio.com/). Or use vim, nano, gedit, notepad, or whatever you prefer.

### Set up your files

Make a folder called `blueleaks-explorer`.

Inside that folder, make two folders:

- `databases`
- `structures`

- **If you don't have the full BLueLeaks dataset**, extract the data you downloaded earlier into the `databases` folder. Also make a new folder called `blueleaks-data` as a placeholder for where the dataset will go. Then, inside the `blueleaks-data` folder, create empty folder for each site in BlueLeaks. You can do this by running the following commands:
```sh
# Make the blueleaks-data folder
mkdir blueleaks-data

# Change to it
cd blueleaks-data

# Make folders for each BlueLeaks site
mkdir 211sfbay cnoatraining houstonhidta miacxold northtexashidta ruralcountysummit stopeasttexasgangs acprlea cnyorca houstonhidtatraining millvalleypolice novatopolicedept sacrttac stophoustondrugs acticaz coorca hpdlineup miorca ntacnv safecityabq stoplubbockgangs akorca corca hpdretired mlrin nvhidta safecityfw stopnorthtexasgangs alabamafusioncenter counterdrugtraining icefishx mnorca nymorca sanbrunopolice stopsanantoniogangs alabamalecc crimestopperslea ilcrime morciu oaklandsheriffshield sccpca stopseattledrugs alertmidsouth cvchidta ileatraining mtorca oaktac scgcsandiego stopspokanegangs aorca dediac iowaintex mvpddoc ociac sciic stopwesttexasgangs arictexas dvicphila jerseyvillagepd mvpdtx okorca sdciaa stxhidta atlantahidta energysecuritycouncil jric ncric orcaid sdfusion sunnyvalebriefing attackwa eousa kcpers ncric-history-good orcaor sdorca swtxfusion azhidta fbicahouston kyorca ncricSteveBackup orocc sduasi terrorismtip azorca fbinaakansaswmissouri lacleartraining nctccounterdrug otewg seattleshield texasorca bostonbric fbinaamichigan lapdtraining ndslic pchidta Securitypartnership tnoa burlingamepolice fbinaatexas leapsla nehidta phillymostwanted seffc twnsg calema fcpddoc losaltospdbc neorca pleasantonpolice semacp unmpd cal-orca flinttownshippolice lupd nevadacyberexchange prvihidta sfbay-infragard usao calstas fwintex mactf nhiac pspddoc sicrime utahsiac cbaghidta gatlinburglec maorca njuasi publicsafetycadets sltew utorca ccroc graorca membersfaithbased-isao nmfisoa richlandshield snctc vlnsn chicagoheat hcsovcp memiac nmhidta rlpsaroc snorca vslea chicagolandfsg hennepincountyshield metrohoustonpolice nnorca rmhidta sogtraining wifusion ciacco hidtatraining mhidta nnric rockhillyorkcountyconnect spottinglies wsorca cnoa3 hiorca miacx northtexasfusion ruasi stopabqgangs usaeo usaoalmtraining usaoalntraining usaoaretraining usaoarwtraining usaoaztraining usaocaclea usaocactraining usaocaetraining usaocantraining usaocaslea usaocastraining usaocotraining usaocrimevictims usaoctlea usaocttraining usaodelea usaodetraining usaoflmtraining usaoflntraining usaogamtraining usaogantraining usaogastraining usaogutraining usaohitraining usaoiantraining usaoidtraining usaoilctraining usaoilntraining usaoinntraining usaokstraining usaokyelea usaokyetraining usaokywtraining usaolaetraining usaolamtraining usaolawtraining usaomatraining usaomdtraining usaometraining usaomietraining usaomiwtraining usaomnlea usaomntraining usaomoetraining usaomsstraining usaomttraining usaoncetraining usaoncmtraining usaoncwtraining usaonetraining usaonjtraining usaonmlea usaonmtraining usaonvtraining usaonyetraining usaonystraining usaoohntraining usaoohstraining usaooketraining usaookntraining usaookwtraining usaoortraining usaopaetraining usaoritraining usaosctraining usaoscvw usaosdtraining usaotnetraining usaotnmtraining usaotnwtraining usaotxetraining usaotxntraining usaotxwtraining usaouttraining usaovawtraining usaovttraining usaowaetraining usaowawtraining usaowietraining usaowitraining usaowvntraining usaowvstraining usaowytraining
```
- **If you have the full BlueLeaks dataset**, make sure it's all extracted, and you know the filesystem path of it on your computer.

Next, in your text editor, create a new file called `docker-compose.yaml` and copy and paste this:

```yaml
services:
  app:
    image: micahflee/blueleaks-explorer:latest
    ports:
      - "8000:80"
    volumes:
      - ./blueleaks-data:/data/blueleaks
      - ./databases:/data/databases
      - ./structures:/data/structures
```

Replace `./blueleaks-data` with the path to your extracted BlueLeaks folder.

### Start BlueLeaks Explorer

Open a terminal, go to your `blueleaks-explorer` folder, and run:

```sh
docker-compose pull
docker-compose up
```

Then open a web browser and go to [http://localhost:8000/](http://localhost:8000/).

You should now be able to look at the data in NCRIC.

**If you don't have the BlueLeaks dataset downloaded**, but you want to access the NCRIC files, you need to download https://data.ddosecrets.com/BlueLeaks/ncric.zip (16GB), and extract it to your `blueleaks-data/ncric` folder.

### The rest of the workshop

With the help of [Chapter 10](https://hacksandleaks.com/chapter-10.html), explore BlueLeaks...