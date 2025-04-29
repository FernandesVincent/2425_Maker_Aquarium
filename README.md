<header style="
      background-color: #004080;
      color: white;
      padding: 1rem;
      text-align: center;
      height: auto;">
	<div class="header-title">

		<h1>Aquarium Automatis&eacute;</h1>
	</div>
</header>
<div class="grid-2-Columns">
	<div class="h2-test">SOMMAIRE
		<div>

			<ul>
				<li><a href="#Pr%C3%A9ambule">Pr&eacute;ambule</a></li>
				<li><a href="#section2">Objectifs du projet</a></li>
				<li><a href="#section3">Meuble</a></li>
				<li><a href="#section4">Filtration</a></li>
				<li><a href="#section5">Test en gouttes</a></li>
				<li><a href="#section6">Raspberry Pi</a></li>
				<li><a href="#section7">PCB</a></li>
				<li><a href="#section8">&Eacute;crans</a></li>
				<li><a href="#section9">Code</a></li>
				<li><a href="#section10">C&acirc;blage</a></li>
				<li><a href="#section11">R&eacute;sultat et Conclusion</a></li>
				<li><a href="#section12">Futur du projet</a></li>
			</ul>
		</div></div>
	<div class="cell">
		<div id="PrÃ©ambule">

			<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">Pr&eacute;ambule</h1>

			<p>
				<br>
			</p>

			<p>Aujourd&#39;hui, lorsqu&#39;un particulier ach&egrave;te son aquarium il doit pouvoir g&eacute;rer un nombre important de facteurs comme la temp&eacute;rature du bac, la distribution de la nourriture mais &eacute;galement les diff&eacute;rents test que peux n&eacute;cessit&eacute; son Aquarium (ph, NO2, CO2, etc...). C&#39;est donc dans l&#39;id&eacute;e de soulager les personnes que cela p&egrave;se de devoir s&#39;occuper de tout &ccedil;a que l&#39;id&eacute;e du projet d&#39;aquarium automatis&eacute; et connect&eacute; m&#39;est venue &agrave; l&#39;esprit.</p>
		</div>
		<div id="section2">

			<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">Objectifs du Projet</h1>

			<p>
				<br>
			</p>Pour r&eacute;pondre &agrave; la probl&eacute;matique &eacute;nonc&eacute;e durant le pr&eacute;ambule, j&#39;ai dessin&eacute; les diff&eacute;rents axes et objectifs du projet &eacute;nonc&eacute;s ci-dessous:

			<ul>
				<li>Automatisation des changements d&#39;eau</li>
				<li>Contr&ocirc;le simple et total sur la luminosit&eacute;</li>
				<li>Automatisation de la distribution de la nourriture</li>
				<li>Automatisation des test en gouttes</li>
				<li>Contr&ocirc;le simple de la temp&eacute;rature</li>
				<li>Afficher le tout sur des &eacute;crans</li>
				<li>Bonus : Cr&eacute;er une Application mobile</li>
			</ul>Afin de r&eacute;aliser l&#39;ensemble de ces objectifs, j&#39;ai du mettre en oeuvre plusieurs comp&eacute;tences que j&#39;ai pu apprendre durant mon cursus &agrave; l&#39;ENSEA telles que:

			<ul>
				<li>D&eacute;coupe LASER</li>
				<li>Conception de PCBs</li>
				<li>Mod&eacute;lisation et impression 3D</li>
				<li>Sertissage de c&acirc;bles</li>
				<li>M&eacute;canique</li>
				<li>Soudure</li>
			</ul>Mais &eacute;galement de nouvelles comme le montage vid&eacute;o et le HTML/CSS/JS pour la cr&eacute;ation d&#39;un site. Pour expliquer chaque partie de ce projet en d&eacute;tail, nous allons partir du plus gros oeuvre vers le plus petit. Commen&ccedil;ons donc par parler du meuble qui doit supporter l&#39;aquarium.</div>
		<div id="section3">

			<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">Meuble</h1>

			<p>
				<br>
			</p>

			<p>Au vu de l&#39;ensemble des objectifs du projet, il fallait un endroit o&ugrave; ranger notamment, l&#39;&eacute;lectronique avec les PCBs et les c&acirc;bles, le bloc de filtration externe, le dispositif d&#39;analyse des test en gouttes ainsi que les bacs de changements d&#39;eau. Pour r&eacute;pondre &agrave; ce besoin j&#39;ai penser &agrave; la cr&eacute;ation d&#39;un meuble pouvant supporter le poids de l&#39;aquarium ainsi que tout ce qu&#39;il y a &agrave; l&#39;int&eacute;rieur. Pour ce faire il a &eacute;t&eacute; d&eacute;cid&eacute; que la structure du meuble se ferait &agrave; l&#39;aide de profil&eacute; aluminium 20x40mm et que les murs seront faits en MDF 3mm. Cependant quelques contraintes &eacute;taient pr&eacute;sentes:</p>

			<ul>
				<li>le meuble doit au minimum faire la largeur (30cm) et la longueur(60cm) de l&#39;aquarium.</li>
				<li>Il doit pouvoir accueillir 2 bacs ayant au minimum une capacit&eacute; de 18L.</li>
				<li>Le bac doit &ecirc;tre assez petit pour diminuer les co&ucirc;ts li&eacute;s au profil&eacute; aluminium.</li>
			</ul>Prenant tout cela en compte, j&#39;ai r&eacute;alis&eacute;s des premiers mod&egrave;les 3D pour pouvoir estimer la taille du meuble et la quantit&eacute; de profil&eacute; aluminium ainsi que de MDF n&eacute;cessaire. Vous pouvez voir les mod&egrave;les prototypes ci-dessous:&nbsp;

			<table>
				<tbody>
					<tr>
						<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%201.png?raw=true" alt="image" width="350" height="600" class="fr-fic fr-dii"></td>
						<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%202.png?raw=true" alt="Image" width="350" height="600" class="fr-fic fr-dii"></td>
						<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%203.png?raw=true" alt="Image" width="350" height="600" class="fr-fic fr-dii"></td>
					</tr>
				</tbody>
			</table>

			<table>
				<tbody>
					<tr>
						<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%204.png?raw=true" alt="image" width="350" height="600" class="fr-fic fr-dii"></td>
						<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%205.png?raw=true" alt="Image" width="350" height="600" class="fr-fic fr-dii"></td>
						<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%206.png?raw=true" alt="Image" width="350" height="600" class="fr-fic fr-dii"></td>
					</tr>
				</tbody>
			</table>

			<p>La version finale &eacute;tant la suivante :</p>
			<div style="text-align: center;"><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20final.png?raw=true" alt="Image centrée" width="300" class="fr-fic fr-dii" style="width: 417px; height: 500px;"></div>L&#39;ensemble des fichiers STL est disponible sur mon<a href="https://github.com/FernandesVincent/2425_Maker_Aquarium">GitHub</a> dans la cat&eacute;gorie &quot;onshape&quot;.

			<p>
				<br>
			</p>Ce meuble est donc sur 2 &eacute;tages, le premier &eacute;tant un &eacute;tage r&eacute;serv&eacute; aux trois bacs de changements d&#39;eau. Chacun ayant un objectif unique:
			<br>
			<br>Celui ci-dessous est d&eacute;di&eacute; &agrave; l&#39;eau us&eacute;e de l&#39;aquarium qui peut &ecirc;tre r&eacute;utilis&eacute;e pour par exemple arroser ses plantes.
			<div style="text-align: center;"><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/used%20water%20tank.png?raw=true" alt="Image centrée" width="300" class="fr-fic fr-dii" style="width: 438px; height: 292px;"></div>Le second pr&eacute;sent ci-dessous est fait pour accueillir l&#39;eau propre qui va venir remplacer l&#39;eau us&eacute;e.
			<div style="text-align: center;"><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/unused%20water%20tank.png?raw=true" alt="Image centrée" width="300" class="fr-fic fr-dii" style="width: 427px; height: 284.667px;"></div>Le troisi&egrave;me et plus petit doit est quant &agrave; lui r&eacute;serv&eacute; &agrave; l&#39;eau en sortie des test &agrave; gouttes qui doit &ecirc;tre jet&eacute;e.
			<div style="text-align: center;"><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/little%20tank.png?raw=true" alt="Image centrée" width="300" class="fr-fic fr-dii" style="width: 418px; height: 278.667px;"></div>Pour la sortie du premier bac j&#39;ai trouver un mod&egrave;le 3D de robinet qui fonctionne assez bien sur <a href="https://www.printables.com/model/278618-water-tap">Printables</a>.</div>De m&ecirc;me que pr&eacute;c&eacute;demment l&#39;ensemble des fichiers STL mais &eacute;galement les fichiers DXF sont disponibles sur mon <a href="https://github.com/FernandesVincent/2425_Maker_Aquarium">GitHub</a> dans la cat&eacute;gorie &quot;onshape&quot;.

		<p>
			<br>
		</p>
		<div id="section4">

			<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">Filtration</h1>
			<br>Attaquons le second &eacute;tage du meuble par la partie concernant le bloc de filtration. J&#39;ai souhait&eacute; faire ce bloc externe moi-m&ecirc;me car cela me permettait de cr&eacute;er un design personnalis&eacute;, notamment pour pouvoir y placer ais&eacute;ment le chauffage et la sonde ph en plus des masses filtrantes.&nbsp;
			<br>Comme pr&eacute;c&eacute;demment vous pouvez voir ci-dessous le prototype de ce bloc de filtration suivi de la version finale,&nbsp;
			<br>
			<br>prototype:&nbsp;
			<div style="text-align: center;"><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/proto%20filter.png?raw=true" alt="Image centrée" width="300" class="fr-fic fr-dii" style="width: 443px; height: 500px;"></div>
			<br>version finale:&nbsp;
			<div style="text-align: center;"><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/filter.png?raw=true" alt="Image centrée" width="300" class="fr-fic fr-dii" style="width: 468px; height:500px;"></div>
			<br>
			<br>Pour pouvoir nettoyer les masses filtrantes, j&#39;ai designer un bac de remont&eacute; (trouer pour que l&#39;eau s&#39;en &eacute;coule et ne pas tremp&eacute; le meuble en les sortant) avec sa poign&eacute;e :&nbsp;

			<table>
				<tbody>
					<tr>
						<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/tray%20tank.png?raw=true" alt="image" width="200" height="500" class="fr-fic fr-dii"></td>
						<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/tray%20tank%20handle.png?raw=true" alt="Image" width="200" height="500" class="fr-fic fr-dii"></td>
					</tr>
				</tbody>
			</table>
			<br>
			<br>Concernant les diff&eacute;rents composants de ce bloc, la sonde ph vient de <a href="https://wiki.dfrobot.com/Gravity__Analog_Spear_Tip_pH_Sensor___Meter_Kit__For_Soil_And_Food_Applications__SKU__SEN0249">DFRobot</a> tandis que le chauffage est fournis avec l&#39;aquarium qui est un aquarium de 60L de la marque CIANO disponible sur&nbsp;<a href="https://www.amazon.fr/Aquarium-Poissons-Consommables-Chauffage-Emballage/dp/B0DMZ6JCDD/?_encoding=UTF8&pd_rd_w=eTX08&content-id=amzn1.sym.46807d81-91bd-498b-9732-d523d8e7a752%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=46807d81-91bd-498b-9732-d523d8e7a752&pf_rd_r=917652W8GSPYV4HS716T&pd_rd_wg=m7z8E&pd_rd_r=916570f0-c766-4f99-b61e-7f823d6b24d8&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1">Amazon</a> .&nbsp;
			<br>De plus, concernant les masses filtrantes elles sont &eacute;galement disponibles sur Amazon: <a href="https://www.amazon.fr/Fluval-Pr%C3%A9filtre-pour-Aquariophilie-750/dp/B001CZXZEU?crid=2DO1R98ZQM2RC&dib=eyJ2IjoiMSJ9.NOtwUJAeSHLB4A1TeyF7lMZri_mYYibux8elORv2TfHT8yLHpVdMSdJHqTUiYHcFMGr334v6IEnsWWmJfPLGE1mpoogN8XoEghupyyNrigO5VS3plDP2CcTmYq2QG4MJTkvTzTTOcQFQ4Y0zzN6mUG_yH7nay19Ffslt9v3t-JCdI6s2QMdTKHUrgb4h_1CvccY8n2z9cqhy9a3K2YmWuXX8cIhYSCcO7GUgdoUt6KjcFyZBTqqU88QPV-2foIqJT7tRuESUFezL2JtSR4yoJJafDqbmSgWf8wqJXLkooE1-nc9v4LDAB3mVxILasvuHKCNPN2AHisuPH9ZROWr5dpat5z9vd5tvAiF1vmKVE2g3hL_7fAWg2CkyKnFiSWWdrk5zkhM4B4p-2tI30VVCbNROYQcaY3yV6V1a9vud8sK52BZ7lmUmHwG4r6HhVILX.sY-sm_8FTIMCC4HghsrVIvfEG4izV4uUMwokH-4gn60&dib_tag=se&keywords=ceramique%2Bfiltre%2Baquarium&qid=1740995166&sprefix=ceramique%2Bfiltre%2Baquarium%2Caps%2C81&sr=8-1&th=1">c&eacute;ramique</a> ;&nbsp;<a href="https://www.amazon.fr/cyclingcolors-d%C3%A9couper-300x210mm-Universelle-%C3%A9paisseur/dp/B0B8JQTZXK?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1GWVJFUSDAMSF&dib=eyJ2IjoiMSJ9.-Nc9EyO1uODmLOWsuEoIv2-ijdhS7vjX1hI6M1EGydp_XFS0wtrzbE2jVMFgrEHocHL6DNbcq4DOPNmEpaNBjZdWuUZP7ZPMicQLsIZ90SWD_deMd8pHQZAqzOpOAZ4D1IFHZ2X0fnkMDess7XfQdBE53jzyoQ5U7YxbRgxUxo4TxXIPRLPpCA1pShM8uPEC_14BnQmFSo0ENJEtF6zNZXzpbQdPOGYKqjRVUeZF0_ePPmf3qAuxzeko5WCX9S8S1h26QB7Ui_yH5xzVT67D3-7iV_G0tFTnQTAvHnabRmVddSMM1xzyo7R-AJKU_j0SQG36PPXQcBq1ewFXpCj_3ksSo4r8ET7GnpSYFM6XmYWrbgCw1QJ-D-15VbdYH-UsJ4eVRgI1szYcRs2AKRRBLG8D_Ecth-nHQBS7rLAzYn_QlE0Hg81ooezR5RGuDtZn.uqiGKSbLIfv1qsK1z4Wm6e5aRRmxiQVxfnGUyDTqWIk&dib_tag=se&keywords=mousse+filtration+aquarium&qid=1740746478&sprefix=mousse+filtration+aquarium%2Caps%2C86&sr=8-10">mousse</a> .&nbsp;
			<br>Les trous dans le Blocs de filtration servent &agrave; le fixer dans le plancher &agrave; mi hauteur du meuble, ils correspondent &agrave; des vis de taille M6 avec une longueur qui doit &ecirc;tre d&#39;environ 20 mm sachant que le plancher est fait en MDF 6mm. Des &eacute;crous ad&eacute;quat sont aussi &agrave; pr&eacute;voir.&nbsp;
			<br>Concernant l&#39;impression du bloc de filtration, elle peut se faire en plus ou moins de parties en fonction de la taille de l&#39;imprimantes. Par exemple, avec les imprimantes disponibles &agrave; l&#39;ENSEA :&nbsp;
			<br>
			<br>Creality K1 Max (300x300x300mm) : 2 parties&nbsp;
			<br>BambuLab X1 Carbon(250x250x250mm) : 4 parties (les 2 parties pr&eacute;c&eacute;dentes doivent &ecirc;tre coup&eacute;es &agrave; mi-hauteur)&nbsp;
			<br>
			<br>De plus, le bloc a &eacute;t&eacute; imprim&eacute; en PLA, or le PLA n&#39;est pas &eacute;tanche. Pour pallier &agrave; ce probl&egrave;me j&#39;ai pris l&#39;initiative d&#39;utiliser de la r&eacute;sine &eacute;poxy afin de vernir le bloc et de le rendre &eacute;tanche. Le seul inconv&eacute;nient de cette m&eacute;thode est la toxicit&eacute; de la r&eacute;sine notamment durant la phase de catalyse qui peut durer plusieurs heures et n&eacute;cessite le port d&#39;un <a href="https://www.amazon.fr/AirGearPro-Protection-Respiratoire-R%C3%A9utilisable-poussi%C3%A8re/dp/B08BQNKK8D/ref=sr_1_12?crid=3LH54H1JA5QNK&dib=eyJ2IjoiMSJ9.vwG9ct7oYhsXxHkosVw_DmGGbSvG-EdfTzmpbvbIy_-blRdYccvxTNdLoztSTV8tl_ikyBC3C5sx3ez7fd9GjM_BHjicTpMb-_M9EWASUwky-py3WhngzjeKjcqC1QPGVSqLLVt9dwrGpRvv8uZhM5_Re66P_tbjd75zfz0It3lw5R378O4styzF4mT2UFgELnVqo1dEaq5sjsjGSO8SU83Srj58_ZeWd_S_6tQwyARHEVkMqt6VuIe_q-BQpZhJykYvcj-rFgzkfMzgAcjRl5SiAw0cAYN1tXGGBibU2ro.akVBE5KxVIQV9yLbv8nGTHnn1ifGuOQN2ryeAmktGkY&dib_tag=se&keywords=masque%2Ba%2Bgaz&qid=1745913052&sprefix=masque%2Ba%2B%2Caps%2C88&sr=8-12&th=1">masque</a> et de&nbsp;<a href="https://www.amazon.fr/ARNOMED-jetables-pi%C3%A8ces-nitrile-disponibles/dp/B093SWH4D8/ref=sr_1_8_mod_primary_new?crid=2KVGNDRFCIO71&dib=eyJ2IjoiMSJ9.HYDeG_JqkiNaNzhkKCJYphhk3ndVM0UbqT-yoTDSnaWFA6OdHlNBi3FhoeW2ZUUI0AozoLPBT0LRJtSUa-ADjaOinG8uifUUo70TLPnk6H4vzPfIN_jZfhI2XwAXMrE8QZiC77FgNaG4N8q-fSoo0epvPihgD-rdkskBYnW7LVj1pTZO8u1pXD_ZNOCaioAR9EvJmOK1yNxrAvVQc99SmUWtKPwbwy0ztc6t6WeLP1m2mzQK-hKjnMPUpVIE1dcgy_K40Tb25gJmvBveADWoAOuMog-kQ_XCkylXwUWTjHc.5SfCoj71a8R3wwyGeR2RD5FM8fDVUkjrGQuWOm_lA1U&dib_tag=se&keywords=gants%2Bnitrile&qid=1745913117&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=gants%2Caps%2C93&sr=8-8&th=1">gants de protection</a>.&nbsp;
			<br>
			<br>Pour finir, l&#39;eau arrive du c&ocirc;t&eacute; de la sonde PH via un tuyaux avec un OD de 20mm et elle ressort de l&#39;autre c&ocirc;t&eacute; gr&acirc;ce &agrave; une pompe de remont&eacute;e connecter via un raccord &agrave; un autre tuyaux.
			<br>
			<br>
			<div id="section5">

				<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">Test en gouttes</h1>

				<p>
					<br>
				</p>Au sein du meuble et &agrave; c&ocirc;t&eacute; du bloc de filtration nous pouvons retrouver la partie test en gouttes du projet. Cette partie est surement la plus complexe du projet car elle implique la mod&eacute;lisation 3D d&#39;un dispositif permettant d&#39;ins&eacute;rer et d&#39;enlever les test en gouttes mais &eacute;galement de pouvoir faire tomber des gouttes lorsque l&#39;on le d&eacute;sire.&nbsp;
				<br>
				<br>La version actuelle a &eacute;t&eacute; r&eacute;fl&eacute;chie avec un servomoteur FS90 actionnant un engrenage qui permet &agrave; son tour de faire tourner des &quot;bras&quot; qui iront appuyer sur les test afin de faire tomber les gouttes.&nbsp;
				<div style="text-align: center;"><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/drops%20test.png?raw=true" alt="Image centrée" width="300" class="fr-fic fr-dii" style="width: 363px; height:400px;"></div>
				<br>
				<br>Ce m&eacute;canisme est malheuresement encore en phase de prototypage car la faible tension de surface au niveau de la sortie goutte &agrave; goutte des test implique qu&#39;une seule petite vibration peut faire s&#39;&eacute;couler une goutte.&nbsp;
				<br>Un autre mod&egrave;le possible serait de faire directement tourner les tests via un servomoteur afin de faire s&#39;&eacute;couler la goutte en profitant justement de la faible tension de surface.&nbsp;
				<br>
				<br>Une fois la goutte &eacute;coul&eacute;e, elle est redirig&eacute;e dans un flacon, dans lequel s&#39;&eacute;coule &eacute;galement l&#39;eau du bac a test&eacute;e, qui est bloqu&eacute; par un anneau li&eacute; &agrave; un autre servomoteur lui permettant de pivoter afin de remuer la solution et enfin de vider le flacon dans un tuyaux menant au bac associ&eacute;. Afin de d&eacute;terminer la valeur associ&eacute; au test (valeur de Ph, de NO3, etc...) il faut effectuer de la reconnaissance colorim&eacute;trique.</div>

			<p>
				<br>
			</p>
			<div id="section6">

				<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">RaspberryPi</h1>

				<p>
					<br>
				</p>Pour effectuer la reconnaissance colorim&eacute;trique je me suis servi d&#39;un raspberryPi 4 model B avec la module cam&eacute;ra associ&eacute;. Cet ensemble auquel on ajoute un code en Python, disponible sur mon <a href="https://github.com/FernandesVincent/2425_Maker_Aquarium">GitHub</a> dans la cat&eacute;gorie &quot;software&quot;, permet de r&eacute;cup&eacute;rer la vision de la cam&eacute;ra et d&#39;y d&eacute;finir un ou plusieurs points o&ugrave; l&#39;on va vouloir analyser la couleur du pixel en leur centre :
				<div style="text-align: center;"><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/software/Python/pictures/example%20point.png?raw=true" alt="Image centrée" width="300" class="fr-fic fr-dii" style="width: 393px; height: 300px;"></div>
				<br>Le code couleur que j&#39;ai utilis&eacute; est le HSV et non le RGB car cela permet d&#39;&ecirc;tre moins sensible &agrave; la diff&eacute;rence de luminosit&eacute;.&nbsp;
				<div style="text-align: center;"><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/software/Python/pictures/HSV-vs-RGB.jpg?raw=true" alt="Image centrée" width="300" class="fr-fic fr-dii" style="width: 418px; height: 350px;"></div>
				<br>
				<br>Un aspect que je n&#39;ai pas eu le temps de terminer est le fait de comparer les valeurs r&eacute;cup&eacute;r&eacute;s par la cam&eacute;ra aux valeurs de r&eacute;f&eacute;rences des couleurs des test en gouttes. Cependant, l&#39;id&eacute;e derri&egrave;re ce code serait d&#39;avoir pour chaque test un tableau contenant les couleurs r&eacute;f&eacute;rences et ainsi via un petit d&#39;algorithme de comparer la couleur HSV exp&eacute;rimental avec celle de r&eacute;f&eacute;rence afin de l&#39;assimiler &agrave; celle-ci.&nbsp;
				<br>Finalement il suffirait de faire correspondre la couleur HSV de r&eacute;f&eacute;rence avec la valeur associ&eacute;e. Une fois cela fait l&#39;objectif est de transmettre cette valeur au PCB principal qui, lui, l&#39;enverra aux &eacute;crans.</div>

			<p>
				<br>
			</p>
			<div id="section7">

				<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">PCB</h1>

				<p>
					<br>
				</p>Cela nous fait une transition parfaite pour parler plus en profondeur de la partie PCB du projet. En effet, pour mener &agrave; bien ce projet j&#39;ai du r&eacute;aliser 2 PCB : un premier PCB dit &quot;principal&quot; et un second dit &quot;d&eacute;port&eacute;&quot;. Le premier PCB et son aspect de multiprise sert &agrave; commander l&#39;ensemble du projet, c&#39;est &agrave; dire :
				<br>
				<br>

				<ul>
					<li>Les 4 ventilateurs</li>
					<li>Les 4 pompes</li>
					<li>Les LED</li>
					<li>Les servomoteurs pour le distributeur de nourriture/li&gt;</li>
					<li>Les boutons pr&eacute;sents sur le second PCB</li>
					<li>Les &eacute;crans</li>
					<li>Les servomoteurs pour les test en gouttes</li>
					<li>la raspberryPi et sa camera</li>
					<li>Les capteurs de niveau d&#39;eau</li>
					<li>Le Ph-m&egrave;tre</li>
					<li>Le chauffage</li>
					<li>Le ST-Link</li>
					<li>Le HC05</li>
				</ul>Faisons un petit apart&eacute; pour d&eacute;tailler l&#39;utilit&eacute; de chacun des modules dont nous n&#39;avons pas encore eu l&#39;occasion de discuter.
				<br>
				<br>

				<h4>Ventilateurs</h4>Le meuble et le PCB sont fait pour accueillir 4&nbsp;<a href="https://www.amazon.fr/ARCTIC-P12-Pack-Refroidisseur-Ventilateur/dp/B07HC7P3HJ/ref=sr_1_22?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3TXQLZO0PSBMV&dib=eyJ2IjoiMSJ9.zUhrIjc32H8-WvshILuE-PtJkv-mw1FkSGAgT1AOR1oDyib-dphFTw_ivU8-Os2Z3SPkMx71hmaU-qOowlMbCeCCD-m-aEquUmbZ3FlHR8_-ej5oHyh2yaVaZolCfb03zDvlUppXXPbv_NlB8bF4hvQ0kXKkbZYUaWO43Sw08Tl8NM4P3ilE9XKvfy9u-lT4zo6KmAZJ5tKS3DDawNQxlgLpxpx_1iES2Xqx_mKGXe48RHJHkL_6mCOrnpOmsJY1jxpEXj42bwhzMWrXvfzqdaw7qTj1C8cfzn7Wl4qSAVI.Drgr1JScUsXTqbsAaerU-8GdExFSoYqVR8i45yJohCs&dib_tag=se&keywords=ventilateur+pc+120mm+12V&qid=1745915029&sprefix=ventilateur+pc+120mm+12v%2Caps%2C109&sr=8-22">ventilateurs</a> 12V de 120mmx120mm. Deux (paire entr&eacute;e/sortie) &agrave; l&#39;&eacute;tage des bacs et deux ( paire entr&eacute;e/sortie) &agrave; l&#39;&eacute;tage sup&eacute;rieur.&nbsp;
				<br>Le couple de ventilateur de l&#39;&eacute;tage inf&eacute;rieur a pour but de ventil&eacute; l&#39;eau propre arrivant dans le bac associ&eacute; afin d&#39;aider &agrave; l&#39;&eacute;vaporation des &eacute;l&eacute;ments ind&eacute;sirables contenu dans cette eau (si on utilise de l&#39;eau osmos&eacute;e ces deux ventilateurs sont inutiles).&nbsp;
				<br>Le second couple de moteur, quant &agrave; lui, est l&agrave; pour a&eacute;rer la Pi, le PCB et surtout l&#39;alimentation qui ne poss&egrave;de pas de ventilateur.

				<h4>
					<br>
				</h4>

				<h4>Pompes</h4>Pour ce projet, nous avons besoins d&#39;un ensemble de 4 <a href="https://www.amazon.fr/submersibles-aquarium-poissons-fontaine-divertissement/dp/B0CDK7GQF2/ref=sr_1_21?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2CUWEXFG2PUFC&dib=eyJ2IjoiMSJ9.kt5smPhlWur0wnbrli3H4DrVLEC06_QO_JbOBYEyMijIh7_RthNJVyfAX4Ud4PPDpqdHwQ4pOWaoo6zsfZ69VyOE8kOFChswIdw_yxYq4pP-k7e8YAFBlQMr3mmeVJtgOaJd2ZKn4M9ht6t596XUTjhOngGLBwXbttb6pcsssp_XBXbosgC-o98d1DYvuCTUCOvFmy3iTxm9IGIwgRYmeEGXowZ4qxU2LAg6pIt1ekSnjvASpDlITmRQtVY1Zr23BJv-VApa7OJQNyjO6xRdQ4rEIOZGFSaqHZtZlUoIaBo.5UAUpJxV19I-vKTE8ASD2hpe8OtvqdkrKyf74I9DL3Q&dib_tag=se&keywords=pompe+12v+eau&qid=1745915095&sprefix=pompe+12v+eau%2Caps%2C86&sr=8-21">pompes</a> 12V 240L/h. Une premi&egrave;re sert pour la sortie de la filtration, une seconde &agrave; remont&eacute;e l&#39;eau du bac d&#39;eau propre &agrave; l&#39;aquarium, une troisi&egrave;me &agrave; vider l&#39;eau de l&#39;aquarium vers le bac de r&eacute;cup&eacute;ration de l&#39;eau us&eacute;e et la derni&egrave;re envoi l&#39;eau vers le filtre. Les deux pompes li&eacute;es &agrave; la filtrations fonctionnent en continu tandis que les deux autres fonctionne sur commande gr&acirc;ce &agrave; l&#39;utilisation de deux transistors NMOS pr&eacute;sents sur le PCB permettant d&#39;allumer les pompes quand le GPIO li&eacute; &agrave; leur Ground est &agrave; l&#39;&eacute;tat haut.

				<h4>
					<br>
				</h4>

				<h4>LED</h4>Les LED de ce projet sont s&eacute;par&eacute;es en deux parties mais viennent toutes de la m&ecirc;me bande <a href="https://www.amazon.fr/Jun-Saxifragelec-lumineuse-flexible-adressable-individuellement/dp/B0B8N4V9HW/ref=sr_1_7?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1CJ3DP9KGQZX7&dib=eyJ2IjoiMSJ9.jsv5HLdSZ_CqM09rG6Xk6uZZAWjjtuBx5FYoyybZ6Cq0dW9sdN0xiOcqO8t8Ln6LuHMjn9s3v2aI3iDoKG0TfEWM3Paz30Z6tmC2xSMbVQSZ50eRcyr4CrFsPwJ1RPR3CfkJwi70Efu_rKi0G0wMe0WJ2qUvEkmbGIRzA1bnyN1mzGsZ2Wg8r_ZL_B7AHo-iN01WSayc71oC5XkE90xITgpsP5gH7CkykDFgiCTTThXMaQrIhLf8PSJImtNxPoGk4S0CWjx7Hrr5ck_nuMyflQfhR7mZIpUyXcVC_EAC5UM.w_CUH-9CxgqyNuN4tKuXXqzRhF1nZa9Ggmml6dgE2r4&dib_tag=se&keywords=ruban%2Bled%2Bneopixel&qid=1745915170&sprefix=ruban%2Bled%2Bneopixel%2Caps%2C85&sr=8-7&th=1">Neopixel</a>.

				<h4>
					<br>
				</h4>

				<h5>LED internes</h5>Ce sont des LEDs coup&eacute;es du ruban et plac&eacute;es dans le meuble afin de pouvoir l&#39;&eacute;clairer en continu avec une m&ecirc;me luminosit&eacute; afin de limiter au mieux les erreurs de reconnaissances colorim&eacute;triques.

				<h4>
					<br>
				</h4>

				<h5>LED externes</h5>Ces LED sont le reste du ruban et servent directement &agrave; l&#39;&eacute;clairage de l&#39;aquarium. L&#39;utilit&eacute; d&#39;avoir pris des LED Neopxiel est ici de pouvoir totalement configurer la couleur que l&#39;on veut pour &eacute;clairer son aquarium en fonction des poissons et plantes qui l&#39;occupe.

				<h4>
					<br>
				</h4>

				<h4>Servomoteurs (nourriture)</h4>Je vais traiter directement ici la partie de la distribution automatique de la nourriture car je n&#39;ai pas eu le temps de la r&eacute;aliser et par cons&eacute;quent elle ne n&eacute;cessite pas une partie enti&egrave;re &agrave; elle seule. L&#39;objectif de cette partie &eacute;tait initialement de pouvoir automatiser la distribution de nourriture via un syst&egrave;me de courroie de transmission qui am&egrave;ne la nourriture depuis une entr&eacute;e (image ci-dessous) jusqu&#39;&agrave; une trappe qui s&#39;ouvre ou se ferme via l&#39;utilisation d&#39;un servomoteur, le tout install&eacute; &agrave; l&#39;int&eacute;rieur de la ramp LED qui &eacute;claire l&#39;aquarium.&nbsp;
				<br>
				<br>
				<br>Ce dispositif, au m&ecirc;me titre que les bacs de changement d&#39;eau, permettrait &agrave; l&#39;usager de pouvoir partir en vacances ou autre tout en sachant que les poissons seront nourris et que les changements d&#39;eau se feront. Le probl&egrave;me majeur qui a fait que je n&#39;ai pas pu r&eacute;aliser cette partie est la cr&eacute;ation de la courroie de transmission qui doit &ecirc;tre assez petite pour pouvoir faire en sorte que la rampe LED ne devienne pas trop massive autant d&#39;un point de vu visuel que du point de vu de sa masse.

				<h4>
					<br>
				</h4>

				<h4>Boutons</h4>Les boutons sont plac&eacute;s sur le PCB secondaire et sont au nombre de 6, 3 paires de 2 boutons. Chaque paire permet d&#39;ajuster un param&egrave;tre, la premi&egrave;re paire permet d&#39;ajuster la temp&eacute;rature, la deuxi&egrave;me la temp&eacute;rature et la troisi&egrave;me la fr&eacute;quence de la distribution de nourriture.

				<h4>
					<br>
				</h4>

				<h4>&Eacute;crans</h4>Le PCB secondaire est &eacute;galement connect&eacute; &agrave; 6 <a href="https://www.gotronic.fr/art-afficheur-oled-0-96-128-x-64-grove-33932.htm">&eacute;crans</a> OLED dont l&#39;objectif est d&#39;afficher les diff&eacute;rents param&egrave;tres de notre syst&egrave;me, que ce soit la temp&eacute;rature, la luminosit&eacute; ou bien els diff&eacute;rents test de l&#39;eau.

				<h4>
					<br>
				</h4>

				<h4>Capteurs de niveau d&#39;eau</h4>Ces&nbsp;<a href="https://www.adafruit.com/product/4965">capteurs</a> servent, comme leur nom l&#39;indique, &agrave; v&eacute;rifier le niveau de l&#39;eau. Je me suis procur&eacute; ceux de Adafruit car leur prix est peu &eacute;lev&eacute; et qu&#39;ils suffisent pour l&#39;utilit&eacute; que j&#39;en ai.
				<br>
				<br>Lorsque deux bandes de m&eacute;tal entrent en contact avec de l&#39;eau cela cr&eacute;e un court-circuit ce qui renvoie un signal au PCB (&eacute;tat haut : il ya la pr&eacute;sence de court circuit donc l&#39;eau &agrave; atteint le niveau que l&#39;on veut v&eacute;rifier tandis qu&#39;&agrave; l&#39;&eacute;tat bas ce n&#39;est pas le cas). J&#39;ai pr&eacute;vu d&#39;en placer un dans l&#39;aquarium, un autre dans le bac d&#39;eau us&eacute;e et un dernier dans le bac d&#39;eau propre. Tout les trois servant &agrave; indiquer que l&#39;on a atteint une hauteur limite au dessus de laquelle il se peut que l&#39;eau se d&eacute;serve des bacs.

				<h4>
					<br>
				</h4>

				<h4>Ph-m&egrave;tre</h4>Ce Ph-m&egrave;tre est fournis avec la sonde Ph et permet de rendre lisible la tension que sort la sonde Ph. Dans le futur du projet il me plairait de r&eacute;ussir &agrave; en faire un moi m&ecirc;me.

				<h4>
					<br>
				</h4>

				<h4>Chauffage</h4>Fournis avec l&#39;aquarium, l&#39;objectif serait d&#39;y connecter un servomoteur afin de pouvoir s&eacute;lectionner la temp&eacute;rature que l&#39;on souhaite avec le module externe o&ugrave; se trouve le PCB d&eacute;port&eacute; ainsi que les &eacute;crans.

				<h4>
					<br>
				</h4>

				<h4>ST-Link</h4>Simplement pr&eacute;sent pour pouvoir programmer le microprocesseur.

				<h4>
					<br>
				</h4>

				<h4>HC05</h4>J&#39;ai pr&eacute;vu un connecteur pour le module HC05 m&ecirc;me si l&#39;utilisation de celui-ci ne se fera qu&#39;&agrave; la toute fin du projet. L&#39;objectif &eacute;tant de connecter un pc ou un t&eacute;l&eacute;phone en bluetooth &agrave; ce module afin de r&eacute;cup&eacute;rer l&#39;ensemble des param&egrave;tres comme le font les &eacute;crans mais cette fois sur un pc ou un t&eacute;l&eacute;phone, l&#39;objectif ultime &eacute;tant le d&eacute;veloppement d&#39;une appilcation.&nbsp;
				<br>
				<br>
				<br>
				<br>
				<br>Revenons en aux PCBs, vous l&#39;aurez compris mais ici nous avons 2 PCB avec des r&ocirc;les bien distinct, le premier servant &agrave; contr&ocirc;ler l&#39;ensemble du projet tandis que le second ne g&egrave;re que les boutons et &agrave; se connecter aux &eacute;crans. Vous pouvez trouver ci-dessous deux photos par PCB suivies d&#39;un lien, les photos correspondent aux schemtatic et routage des PCB effectu&eacute;s sous KiCad 9.0 et le fichier quant &agrave; lui est la Bill Of Material (BOM) contenant l&#39;ensemble des composants n&eacute;cessaires &agrave; la fabrication des PCB.&nbsp;
				<br>
				<br>PCB principal:

				<table>
					<tbody>
						<tr>
							<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/pictures/main%20PCB%20sch.png?raw=true" alt="image" width="500" height="500" class="fr-fic fr-dii"></td>
							<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/pictures/main%20PCB%20.png?raw=true" alt="Image" width="500" height="500" class="fr-fic fr-dii"></td>
						</tr>
					</tbody>
				</table><a href="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/PCB_Aquarium2/BOM_PDF.pdf">BOM</a>
				<br>
				<br>PCB secondaire:

				<table>
					<tbody>
						<tr>
							<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/pictures/2nd%20PCB%20sch.png?raw=true" alt="image" width="500" height="500" class="fr-fic fr-dii"></td>
							<td><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/pictures/2nd%20PCB.png?raw=true" alt="Image" width="500" height="500" class="fr-fic fr-dii"></td>
						</tr>
					</tbody>
				</table><a href="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/PCB_secondaire/BOM_PDF.pdf">BOM</a></div>

			<p>
				<br>
			</p>
			<div id="section8">

				<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">&Eacute;crans</h1>

				<p>
					<br>
				</p>Nous avons d&#39;ores et d&eacute;j&agrave; parl&eacute; succinctement du r&ocirc;le des &eacute;crans dans le projet c&#39;est pourquoi j&#39;aimerais m&#39;attarder ici plut&ocirc;t sur la partie code associ&eacute; &agrave; ces &eacute;crans. En effet, Les &eacute;crans que j&#39;ai command&eacute; sont les suivants:&nbsp;
				<br>
				<br>Ces &eacute;crans peuvent communiquer soit en I2C (avec 2 adresses possibles : 0x7A et 0x78) soit en SPI. Or, et je pense que vous l&#39;avez compris avec la partie pr&eacute;c&eacute;dente mais nous avons beaucoup de modules diff&eacute;rents avec lesquels le microprocesseur doit communiquer. Le microprocesseur en question est le STM32G474RET6 qui poss&egrave;de 3 I2C, ce qui est parfait pour notre projet car nous pouvons commander 2 &eacute;crans avec un seul I2C. Mais &agrave; cause du nombre tr&egrave;s &eacute;lev&eacute;s du nombre de pins que le microprocesseur doit allouer au reste du projet, les pins que les 3 I2C utilisent ne sont plus disponibles.&nbsp;
				<br>Il m&#39;a donc fallu me rabattre sur le SPI qui bien que n&eacute;cessitant un nombre de pins plus &eacute;lev&eacute;s est plus pratique dans ce cas pour deux : 1 seul SPI peut g&eacute;rer les 6 &eacute;crans &agrave; conditionner de leur r&eacute;serv&eacute; un pin de s&eacute;lection (Chip Select (CS)) chacun mais &eacute;galement car la plupart des pins qu&#39;il utilise peuvent &ecirc;tre de simple GPIO (comme CS) voir m&ecirc;me non obligatoire en fonction de l&#39;utilisation.&nbsp;
				<br>Par exemple dans notre cas nous n&#39;avons pas besoin du pin MOSI (Master Out Slave In) car on attend pas de r&eacute;ponse de la part des &eacute;crans.&nbsp;
				<br>Le probl&egrave;me majeur que j&#39;avais concernant le SPI est que je n&#39;avais jamais travaill&eacute; ce protocole auparavant, j&#39;ai donc du apprendre comment il fonctionne ce qui ne fut, heureusement, pas la partie la plus compliqu&eacute;e. Cependant, l&agrave; o&ugrave; je me suis heurt&eacute; &agrave; un mur c&#39;est au moment de la recherche de librairies pour utiliser ce protocole avec le driver de mes &eacute;crans (le SSD1315) qui n&#39;est malheureusement pas le driver le plus utilis&eacute; ce qui implique donc que les librairies que j&#39;ai trouv&eacute;es n&#39;avaient pas directement de librairies pour ce driver, m&ecirc;me si il semblerait que celles du driver SSD1306 fonctionne, du moins en partie, avec le SSD1315. De plus, j&#39;ai &eacute;galement re&ccedil;u de la part de mon encadrant une library fa&icirc;te pour mon driver mais en I2C.&nbsp;
				<br>Au vu du temps qu&#39;il me restait &agrave; ce moment l&agrave; j&#39;ai pr&eacute;f&eacute;r&eacute; me concentrer sur d&#39;autres aspects du projet ce qui fait qu&#39;&agrave; l&#39;heure o&ugrave; j&#39;&eacute;cris ces lignes, les &eacute;crans ne sont pas encore fonctionnels.</div>

			<p>
				<br>
			</p>
			<div>

				<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">Code</h1>

				<p>
					<br>
				</p>Nous avons d&eacute;j&agrave; eu l&#39;occasion d&#39;aborder le sujet du code dans ce projet mais j&#39;aimerais y d&eacute;dier une partie car il y a quand m&ecirc;me des notions &agrave; ajouter et que je ne pourrais dilu&eacute;es dans aucune aitre partie. Veuillez tout d&#39;abord regarder le diagramme d&#39;architecture du code pr&eacute;sent ci-dessous:&nbsp;
				<div style="text-align: center;"><img src="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/gestion%20projet/diag%20code.png?raw=true" alt="Image centrée" width="300" class="fr-fic fr-dii" style="width: 800px; height: 300px;"></div>
				<br>Nous avons d&eacute;j&agrave; aborder la partie de la RaspberryPi except&eacute; le fait que pour effectu&eacute; la reconnaissance colorim&eacute;trique j&#39;ai du utiliser OpenCV.&nbsp;
				<br>
				<br>Concernant le code du STM32 il est, je pense, n&eacute;cessaire de recontextualiser: Pour ce projet nous devons effectu&eacute; des changements d&#39;eau &agrave; un intervalle fixe (10% de l&#39;eau de l&#39;aquarium chaque semaine), de m&ecirc;me il faut nourrir les poissons et effectuer les test en gouttes &agrave; intervalles r&eacute;guliers. Pour effectuer cela sachant que le projet n&#39;est pas connect&eacute; &agrave; Internet, il m&#39;a fallu cr&eacute;er un horloge interne qui peux fonctionner d&#39;elle m&ecirc;me apr&egrave;s avoir flasher le microprocesseur avec le code pr&eacute;sent sur mon PC. Le fichier la contenant peut &ecirc;tre trouver sur mon GitHub. Cette Horloge d&eacute;marre &agrave; partir d&#39;un date d&eacute;finit arbitrairement et permet de r&eacute;aliser des actions du type : si on est au jour X &agrave; l&#39;heure Y et &agrave; la minute Z : fait telle action.&nbsp;
				<br>De plus, comme je ne commande en moteur que des servomoteurs basiques, il me suffit de leur envoyer des PWMs pour d&eacute;finir la position d&#39;arriv&eacute; et ensuite les faire revenir &agrave; leur positions de d&eacute;part une fois leur action finie. Le seul inconv&eacute;nient de cela est que dois tester chaque mouvement de mes servomoteurs pour plusieurs valeurs de PWMs afin de pouvoir savoir quelle valeur de PWM serait la meilleure. Une m&eacute;thode plus &eacute;volu&eacute;e serait de cr&eacute;er une boucle for qui incr&eacute;mente la valeur de la PWM &agrave; chaque it&eacute;ration.&nbsp;
				<br>Finalement, Les LEDs sont command&eacute;es via DMA gr&acirc;ce &agrave; une librairie cr&eacute;e par l&#39;un des professeurs de l&#39;&eacute;cole. La seule chose est que je dois d&eacute;finir des valeurs r&eacute;f&eacute;rences pour la couleur des LEDs afin que l&#39;usager puisse par l&#39;appui des boutons, passer d&#39;une couleur &agrave; une autre. Une am&eacute;lioration serait d&#39;avoir 3 encodeur rotatif permettant &agrave; l&#39;usager d&#39;avoir la possibilit&eacute; de r&eacute;gler la couleur de la lumi&egrave;re de son pr&eacute;cision avec une pr&eacute;cision qu&#39;il n&#39;a pas actuellement.</div>

			<p>
				<br>
			</p>
			<div id="section10">

				<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">C&acirc;blage</h1>

				<p>
					<br>
				</p>Au vu du projet et du nombre de modules &agrave; connecter aux PCB vous vous doutez que le nombre de c&acirc;bles &agrave; sertir est cons&eacute;quent ! Et c&#39;est effectivement le cas.&nbsp;
				<br>Pour ce projet j&#39;ai du sertir &eacute;norm&eacute;ment de c&acirc;bles pour diff&eacute;rents types de connecteurs : JST EH, JST XH, Duponts. De plus, j&#39;ai &eacute;galement du simplement d&eacute;nuder des c&acirc;bles afin de pouvoir les souder &agrave; d&#39;autres notamment pour les pompes ou les c&acirc;bles d&#39;alimentation.&nbsp;
				<br>Mais le c&acirc;blage ne s&#39;arr&ecirc;te pas &agrave; sertir un c&acirc;ble, il faut &eacute;galement les emballer. C&#39;est &agrave; dire qu&#39;il faut entourer les c&acirc;ble de gaine tress&eacute;e pour les prot&eacute;ger m&eacute;caniquement et thermiquement mais &eacute;galement pour les organiser. Mais il faut &eacute;galement les entourer de gaine thermor&eacute;tractable pour fixer la gaine tress&eacute;e aux c&acirc;bles au niveau des extr&eacute;mit&eacute;s pour pas qu&#39;elle ne bouge mais &eacute;galement au niveau des points de soudure pour prot&eacute;ger ce point notamment si il y a un autre c&acirc;ble souder &agrave; c&ocirc;t&eacute;, ils sont ainsi isol&eacute;s l&#39;un de l&#39;autre et l&#39;on ne risque pas de mauvais contacts.</div>

			<p>
				<br>
			</p>
			<div id="section11">

				<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">R&eacute;sultat Final et Conclusion</h1>

				<p>
					<br>
				</p>Tout au long de cette pr&eacute;sentation vous avez pu voir diff&eacute;rentes parties du projet mais il est temps de montrer le r&eacute;sultat que j&#39;ai r&eacute;ussi &agrave; obtenir &agrave; la fin de ce proje ainsi que la vid&eacute;o de pr&eacute;sentation du projett: &nbsp;
				<br>
				<a href="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/gestion%20projet/final%20result.mp4">
					<br>R&eacute;sultat final</a>
				<br><a href="https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/gestion%20projet/Vid%C3%A9o%20Aquarium.mp4">vid&eacute;o de pr&eacute;sentation</a>
				<br>
				<br>Comme vous pouvez le voir je n&#39;ai pas pris de vid&eacute;os avec l&#39;aquarium remplit et le syst&egrave;me en fonctionnement et la raison &agrave; cela est simple: je n&#39;ai pas r&eacute;ussi &agrave; finir et emboiter toutes les parties du projet dans le temps impartit.&nbsp;
				<br>
				<br>Pour conclure cette pr&eacute;sentation j&#39;aimerais revenir sur ce qu&#39;&agrave; pu m&#39;apporter ce projet. En effet, ce projet malgr&eacute; le fait que je n&#39;ai pas pu le finir m&#39;a quand m&ecirc;me permis de d&eacute;velopper toutes les comp&eacute;tences que l&#39;on a pu d&eacute;velopp&eacute;es au cours de cette pr&eacute;sentation, des comp&eacute;tences que j&#39;avais d&eacute;j&agrave; mais que j&#39;ai pu grandement am&eacute;lior&eacute;es comme la cr&eacute;ation et la soudure de PCB ou bien des comp&eacute;tences que je n&#39;avais pas encore eu l&#39;occasion de d&eacute;velopper durant mon parcours comme la d&eacute;coupe LASER, la mod&eacute;lisation et l&#39;impression 3D.&nbsp;
				<br>Au vu de mon niveau, ce projet &eacute;tait sans nul doute ambitieux, surement trop d&#39;ailleurs au vu du temps impartit mais c&#39;est ce qui en fait un bon projet dans le sens o&ugrave; j&#39;ai pu apprendre comme je n&#39;ai jamais appris avec n&#39;importe quel autre projet.</div>

			<p>
				<br>
			</p>
			<div id="section12">

				<h1 style="text-align: center; text-decoration: underline; font-weight: bold;">Futur du Projet</h1>

				<p>
					<br>
				</p>Bien &eacute;videmment je ne compte pas m&#39;arr&ecirc;ter l&agrave; pour ce projet. En effet, il me reste un an pour le finir avant de finir mes &eacute;tudes et je compte bien profiter de cette ann&eacute;e pour finir le projet et y apporter toutes les am&eacute;liorations dont j&#39;ai pu parler au sein de cette pr&eacute;sentation et qui sait peut-&ecirc;tre que d&#39;autres me viendront &agrave; l&#39;esprit entre temps !</div>

			<p>
				<br>
			</p>
		</div></div></div>

<p data-f-id="pbf" style="text-align: center; font-size: 14px; margin-top: 30px; opacity: 0.65; font-family: sans-serif;">Powered by <a href="https://www.froala.com/wysiwyg-editor?pb=1" title="Froala Editor">Froala Editor</a></p>
