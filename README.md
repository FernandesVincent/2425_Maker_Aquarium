<header style="
      background-color: #004080;
      color: white;
      padding: 1rem;
      text-align: center;
      height: auto;">
	<div class="header-title">

		<h1>Maker Aquarium</h1>
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
				<li><a href="#section11">Lumi&egrave;re &amp; nourriture</a></li>
				<li><a href="#section12">R&eacute;sultat Final</a></li>
				<li><a href="#section13">Conclusion</a></li>
				<li><a href="#section14">Futur du projet</a></li>
			</ul>
		</div></div>
	<div class="cell">
		<div id="Préambule">

			<h2>Pr&eacute;ambule</h2>

			<p>Aujourd&#39;hui, lorsqu&#39;un particulier ach&egrave;te son aquarium il doit pouvoir g&eacute;rer un nombre important de facteurs comme la temp&eacute;rature du bac, la distribution de la nourriture mais &eacute;galement les diff&eacute;rents test que peux n&eacute;cessit&eacute; son Aquarium (ph, NO2, CO2, etc...). C&#39;est donc dans l&#39;id&eacute;e de soulager les personnes que cela p&egrave;se de devoir s&#39;occuper de tout &ccedil;a que l&#39;id&eacute;e du projet d&#39;aquarium automatis&eacute; et connect&eacute; m&#39;est venue &agrave; l&#39;esprit.</p>
		</div>
		<div id="section2">

			<h2>Objectifs du Projet</h2>Pour r&eacute;pondre &agrave; la probl&eacute;matique &eacute;nonc&eacute;e durant le pr&eacute;ambule, j&#39;ai dessin&eacute; les diff&eacute;rents axes et objectifs du projet &eacute;nonc&eacute;s ci-dessous:

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
				<li>D&eacute;coupe LASER/li&gt;</li>
				<li>Conception de PCBs</li>
				<li>Mod&eacute;lisation et impression 3D</li>
				<li>Sertissage de c&acirc;bles</li>
				<li>M&eacute;canique/li&gt;</li>
				<li>Soudure</li>
				<li>/li&gt;</li>
			</ul>Mais &eacute;galement de nouvelles comme le montage vid&eacute;o et le HTML/CSS/JS pour la cr&eacute;ation d&#39;un site. Pour expliquer chaque partie de ce projet en d&eacute;tail, nous allons partir du plus gros oeuvre vers le plus petit. Commen&ccedil;ons donc par parler du meuble qui doit supporter l&#39;aquarium.</div>
		<div id="section3">

			<h2>Meuble</h2>

			<p>Au vu de l&#39;ensemble des objectifs du projet, il fallait un endroit o&ugrave; ranger notamment, l&#39;&eacute;lectronique avec les PCBs et les c&acirc;bles, le bloc de filtration externe, le dispositif d&#39;analyse des test en gouttes ainsi que les bacs de changements d&#39;eau. Pour r&eacute;pondre &agrave; ce besoin j&#39;ai penser &agrave; la cr&eacute;ation d&#39;un meuble pouvant supporter le poids de l&#39;aquarium ainsi que tout ce qu&#39;il y a &agrave; l&#39;int&eacute;rieur. Pour ce faire il a &eacute;t&eacute; d&eacute;cid&eacute; que la structure du meuble se ferait &agrave; l&#39;aide de profil&eacute; aluminium 20x40mm et que les murs seront faits en MDF 3mm. Cependant quelques contraintes &eacute;taient pr&eacute;sentes:</p>

			<ul>
				<li>le meuble doit au minimum faire la largeur (30cm) et la longueur(60cm) de l&#39;aquarium /li&gt;</li>
				<li>Il doit pouvoir accueillir 2 bacs ayant au minimum une capacit&eacute; de 18L</li>
				<li>Le bac doit &ecirc;tre assez petit pour diminuer les co&ucirc;ts li&eacute;s au profil&eacute; aluminium</li>
			</ul>Prenant tout cela en compte, j&#39;ai r&eacute;alis&eacute;s des premiers mod&egrave;les 3D pour pouvoir estimer la taille du meuble et la quantit&eacute; de profil&eacute; aluminium ainsi que de MDF n&eacute;cessaire. Vous pouvez voir les mod&egrave;les ci-dessous:&nbsp;

			<p>La version finale &eacute;tant la suivante :</p>Ce meuble est donc sur 2 &eacute;tages, le premier &eacute;tant un &eacute;tage r&eacute;serv&eacute; aux trois bacs de changements d&#39;eau. Chacun ayant un objectif unique:

			<ul>
				<li>Celui avec un trou dans l&#39;un de ses murs est d&eacute;di&eacute; &agrave; l&#39;eau us&eacute;e de l&#39;aquarium qui peut &ecirc;tre r&eacute;utilis&eacute;e pour par exemple arroser ses plantes.</li>
				<li>Celui identique au premier mais sans le trou est fait pour accueillir l&#39;eau non us&eacute;e qui va venir remplacer l&#39;eau us&eacute;e.</li>
				<li>Le troisi&egrave;me et plus petit doit est quant &agrave; lui r&eacute;serv&eacute; &agrave; l&#39;eau en sortie des test &agrave; gouttes qui doit &ecirc;tre jet&eacute;e.</li>
			</ul>Pour la sortie du premier bac j&#39;ai trouver un mod&egrave;le 3D de robinet qui fonctionne assez bien sur Printables: https://www.printables.com/model/278618-water-tap .</div>
		<div id="section4">

			<h2>Filtration</h2>Attaquons le second &eacute;tage du meuble par la partie concernant le bloc de filtration, j&#39;ai souhait&eacute; faire ce bloc externe moi-m&ecirc;me car cela me permettait de cr&eacute;er un design personnalis&eacute;, notamment pour pouvoir y placer ais&eacute;ment le chauffage et la sonde ph en plus des masses filtrantes. Comme pr&eacute;c&eacute;demment vous pouvez voir ci-dessous les prototypes de ce bloc de filtration suivi de la version finale prototypes: version finale: Pour pouvoir nettoyer les masses filtrantes, j&#39;ai designer un bac de remont&eacute; (trouer pour que l&#39;eau s&#39;en &eacute;coule et ne pas tremp&eacute; le meuble en les sortant) avec sa poign&eacute;e : Concernant les diff&eacute;rents composants de ce bloc, la sonde ph vient de <a href="https://wiki.dfrobot.com/Gravity__Analog_Spear_Tip_pH_Sensor___Meter_Kit__For_Soil_And_Food_Applications__SKU__SEN0249">DFRobot</a> tandis que le chauffae est fournis avec l&#39;aquarium qui est un aquarium de 60L de la marque CIANO disponible sur <a href="https://www.amazon.fr/Aquarium-Poissons-Consommables-Chauffage-Emballage/dp/B0DMZ6JCDD/?_encoding=UTF8&pd_rd_w=eTX08&content-id=amzn1.sym.46807d81-91bd-498b-9732-d523d8e7a752%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=46807d81-91bd-498b-9732-d523d8e7a752&pf_rd_r=917652W8GSPYV4HS716T&pd_rd_wg=m7z8E&pd_rd_r=916570f0-c766-4f99-b61e-7f823d6b24d8&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1">Amazon</a> . De plus, concernant les masses filtrantes elles sont disponibles via les suivants : <a href="https://www.amazon.fr/Fluval-Pr%C3%A9filtre-pour-Aquariophilie-750/dp/B001CZXZEU?crid=2DO1R98ZQM2RC&dib=eyJ2IjoiMSJ9.NOtwUJAeSHLB4A1TeyF7lMZri_mYYibux8elORv2TfHT8yLHpVdMSdJHqTUiYHcFMGr334v6IEnsWWmJfPLGE1mpoogN8XoEghupyyNrigO5VS3plDP2CcTmYq2QG4MJTkvTzTTOcQFQ4Y0zzN6mUG_yH7nay19Ffslt9v3t-JCdI6s2QMdTKHUrgb4h_1CvccY8n2z9cqhy9a3K2YmWuXX8cIhYSCcO7GUgdoUt6KjcFyZBTqqU88QPV-2foIqJT7tRuESUFezL2JtSR4yoJJafDqbmSgWf8wqJXLkooE1-nc9v4LDAB3mVxILasvuHKCNPN2AHisuPH9ZROWr5dpat5z9vd5tvAiF1vmKVE2g3hL_7fAWg2CkyKnFiSWWdrk5zkhM4B4p-2tI30VVCbNROYQcaY3yV6V1a9vud8sK52BZ7lmUmHwG4r6HhVILX.sY-sm_8FTIMCC4HghsrVIvfEG4izV4uUMwokH-4gn60&dib_tag=se&keywords=ceramique%2Bfiltre%2Baquarium&qid=1740995166&sprefix=ceramique%2Bfiltre%2Baquarium%2Caps%2C81&sr=8-1&th=1">c&eacute;ramique</a> <a href="https://www.amazon.fr/cyclingcolors-d%C3%A9couper-300x210mm-Universelle-%C3%A9paisseur/dp/B0B8JQTZXK?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1GWVJFUSDAMSF&dib=eyJ2IjoiMSJ9.-Nc9EyO1uODmLOWsuEoIv2-ijdhS7vjX1hI6M1EGydp_XFS0wtrzbE2jVMFgrEHocHL6DNbcq4DOPNmEpaNBjZdWuUZP7ZPMicQLsIZ90SWD_deMd8pHQZAqzOpOAZ4D1IFHZ2X0fnkMDess7XfQdBE53jzyoQ5U7YxbRgxUxo4TxXIPRLPpCA1pShM8uPEC_14BnQmFSo0ENJEtF6zNZXzpbQdPOGYKqjRVUeZF0_ePPmf3qAuxzeko5WCX9S8S1h26QB7Ui_yH5xzVT67D3-7iV_G0tFTnQTAvHnabRmVddSMM1xzyo7R-AJKU_j0SQG36PPXQcBq1ewFXpCj_3ksSo4r8ET7GnpSYFM6XmYWrbgCw1QJ-D-15VbdYH-UsJ4eVRgI1szYcRs2AKRRBLG8D_Ecth-nHQBS7rLAzYn_QlE0Hg81ooezR5RGuDtZn.uqiGKSbLIfv1qsK1z4Wm6e5aRRmxiQVxfnGUyDTqWIk&dib_tag=se&keywords=mousse+filtration+aquarium&qid=1740746478&sprefix=mousse+filtration+aquarium%2Caps%2C86&sr=8-10">mousse</a> Les trous dans le Blocs de filtration servent &agrave; le fixer dans le sol &agrave; mi hauteur du meuble, ils correspond &agrave; des vis de taille M6 avec une longueur qui doit &ecirc;tre d&#39;environ 20 mm sachant que le sol est fait en MDF 6mm. Des &eacute;crous ad&eacute;quat sont aussi &agrave; pr&eacute;voir. Concernant l&#39;impression du bloc de filtration, elle peut se faire en plus ou moins de parties en fonction de la taille de l&#39;imprimantes. Par exemple, avec les imprimantes disponibles &agrave; l&#39;ENSEA : Creality K1 Max (300x300x300mm) : 2 parties BambuLab X1 Carbon(250x250x250mm) : 4 parties (les 2 parties pr&eacute;c&eacute;dentes doivent &ecirc;tre coup&eacute;es &agrave; mi-hauteur) De plus, le bloc a &eacute;t&eacute; imprim&eacute; en PLA, or la PLA n&#39;est pas &eacute;tanche. Pour pallier &agrave; ce probl&egrave;me j&#39;ai pris l&#39;initiative d&#39;utiliser de la r&eacute;sine &eacute;poxy afin de vernir le bloc et de le rendre &eacute;tanche. Le seul inconv&eacute;nient de cette m&eacute;thode est la toxicit&eacute; de la r&eacute;sine notamment durant la phase de catalyse qui peut durer plusieurs heures et n&eacute;cessite le port d&#39;un masque et de gants de protection. L&#39;eau arrive du c&ocirc;t&eacute; de la sonde PH via un tuyaux avec un OD de 20mm et elle ressort de l&#39;autre c&ocirc;t&eacute; gr&acirc;ce &agrave; une pompe de remont&eacute;e connecter via un raccord &agrave; un autre tuyaux.
			<div id="section5">

				<h2>Test en gouttes</h2>Au sein du meuble et &agrave; c&ocirc;t&eacute; du bloc de filtration nous pouvons retrouver la partie test en gouttes du projet. Cette partie est surement la plus complexe du projet car elle implique la mod&eacute;lisation 3D d&#39;un dispositif permettant d&#39;ins&eacute;rer et d&#39;enlever les test en gouttes mais &eacute;galement de pouvoir faire tomber des gouttes lorsque l&#39;on le d&eacute;sire. La version actuelle a &eacute;t&eacute; r&eacute;fl&eacute;chie avec un servomoteur FS90 actionnant un engrenage qui permet &agrave; son tour de faire tourner des &quot;bras&quot; qui iront appuyer sur les test afin de faire tomber les gouttes. Ce m&eacute;canisme est malheuresement encore en phase de prototypage car la faible tension de surface au niveau de la sortie goutte &agrave; goutte des test implique qu&#39;une seule petite vibration peut faire s&#39;&eacute;couler une goutte. Un autre mod&egrave;le possible serait de faire directement tourner les tests via un servomoteur afin de faire s&#39;&eacute;couler la goutte en profitant justement de la faible tension de surface. Une fois la goutte &eacute;coul&eacute;e, elle est redirig&eacute;e dans un flacon, dans lequel s&#39;&eacute;coule &eacute;galement l&#39;eau du bac a test&eacute;e, qui est bloqu&eacute; par un anneau li&eacute; &agrave; un autre servomoteur lui permettant de pivoter afin de remuer la solution et enfin de vider le flacon dans un tuyaux menant au bac associ&eacute;. Afin de d&eacute;terminer la valeur associ&eacute; au test (valeur de Ph, de NO3, etc...) il faut effectuer de la reconnaissance colorim&eacute;trique.</div>
			<div id="section6">

				<h2>RaspberryPi</h2>Pour effectuer la reconnaissance colorim&eacute;trique je me suis servi d&#39;un raspberryPi 4 model B avec la module cam&eacute;ra associ&eacute;. Cet ensemble auquel on ajoute un code en Python disponible sur mon GitHub permet de r&eacute;cup&eacute;rer la vision de la cam&eacute;ra et d&#39;y d&eacute;finir un ou plusieurs points o&ugrave; l&#39;on va vouloir analyser la couleur du pixel en leur centre. Le code couleur que j&#39;ai utilis&eacute; est le HSV et non le RGB car cela permet d&#39;&ecirc;tre moins sensible &agrave; la diff&eacute;rence de luminosit&eacute;. Un aspect que je n&#39;ai pas eu le temps de terminer est le fait de comparer les valeurs r&eacute;cup&eacute;r&eacute;s par la cam&eacute;ra aux valeurs de r&eacute;f&eacute;rences des couleurs des test en gouttes. Cependant, l&#39;id&eacute;e derri&egrave;re ce code serait d&#39;avoir pour chaque test un tableau contenant les couleurs r&eacute;f&eacute;rences et ainsi via un petit d&#39;algorithme de comparer la couleur HSV exp&eacute;rimental avec celle de r&eacute;f&eacute;rence afin de l&#39;assimiler &agrave; celle-ci. Finalement il suffirait de faire correspondre la couleur HSV de r&eacute;f&eacute;rence avec la valeur associ&eacute;e. Une fois cela fait l&#39;objectif est de transmettre cette valeur au PCB principal qui, lui, l&#39;enverra aux &eacute;crans.</div>
			<div id="section7">Cela nous fait une transition parfait pour parler plus en profondeur de la partie PCB du projet. En effet, pour mener &agrave; bien ce projet j&#39;ai du r&eacute;aliser 2 PCBs : un premier PCB dit &quot;principal&quot; et un second dit &quot;d&eacute;port&eacute;&quot;. Le premier PCB et son aspect de multiprise sert &agrave; commander l&#39;ensemble du projet, c&#39;est &agrave; dire :

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
				</ul>Faisons un petit apart&eacute; pour d&eacute;taill&eacute; l&#39;utilit&eacute; de chacun des modules dont nous n&#39;avons pas encore eu l&#39;occasion de discuter.

				<h4>Ventilateurs</h4>Le meuble et le PCB sont fait pour accueillir 4 ventilateur 12V de 120mmx120mm. Deux (entr&eacute;e/sortie) &agrave; l&#39;&eacute;tage des bacs et deux (entr&eacute;e/sortie) &agrave; l&#39;&eacute;tage sup&eacute;rieur. Le couple de moteur de l&#39;&eacute;tage inf&eacute;rieur a pour but de ventil&eacute; l&#39;eau non us&eacute;e arrivant dans le bac associ&eacute; afin d&#39;aider &agrave; l&#39;&eacute;vaporation des &eacute;l&eacute;ments ind&eacute;sirables contenu dans cette eau (seulement si ce n&#39;est pas de l&#39;eau osmos&eacute;e, si on utilise de l&#39;eau osmos&eacute;e ces deux ventilateurs sont inutiles). Le second couple de moteur, quant &agrave; lui, est l&agrave; pour a&eacute;rer la Pi, le PCB et surtout l&#39;alimentation qui ne poss&egrave;de pas de ventilateur.

				<h4>Pompes</h4>Pour ce projet, nous avons besoins d&#39;un ensemble de 4 pompes 12V 240L/h. Une premi&egrave;re sert pour la filtration, une seconde &agrave; remont&eacute;e l&#39;eau du bac d&#39;eau propre &agrave; l&#39;aquarium, une troisi&egrave;me &agrave; vider l&#39;eau de l&#39;aquarium vers le bac de r&eacute;cup&eacute;ration de l&#39;eau us&eacute;e et la derni&egrave;re envoi l&#39;eau vers le filtre pour qu&#39;elle soit filtr&eacute;e. Les deux pompes li&eacute;es &agrave; la filtrations fonctionnent en continu tandis que les deux autres fonctionne &quot;sur commande&quot;; deux transistors NMOS pr&eacute;sents sur le PCB permettent d&#39;allumer les pompes quand le GPIO li&eacute; &agrave; leur Ground est &agrave; l&#39;&eacute;tat haut.

				<h4>LED</h4>Les LED de ce projet sont s&eacute;par&eacute;es en deux parties mais viennent toutes de la m&ecirc;me bande neopixel.

				<h4>LED internes</h4>Ce sont des LEDs coup&eacute;es du ruban et plac&eacute;es dans le meuble afin de pouvoir l&#39;&eacute;clairer en continu avec une m&ecirc;me luminosit&eacute; afin de limiter au mieux les erreurs de reconnaissances colorim&eacute;triques.

				<h4>LED externes</h4>Ces LED sont le reste du ruban et servent directement &agrave; l&#39;&eacute;clairage de l&#39;aquarium. L&#39;utilit&eacute; d&#39;avoir pris des LED Neopxiel est ici de pouvoir totalement configurer la couleur que l&#39;on veut pour &eacute;clairer son aquarium en fonction des poissons et plantes qui l&#39;occupent.

				<h4>Servomoteurs (nourriture)</h4>Je vais traiter directement ici la partie de la distribution automatique de la nourriture car je n&#39;ai pas eu le temps de la r&eacute;aliser et que par cons&eacute;quent elle ne n&eacute;cessite pas une partie enti&egrave;re &agrave; elle seule. L&#39;objectif de cette partie &eacute;tait initialement de pouvoir automatiser la distribution de nourriture via un syst&egrave;me de courroie de transmission qui am&egrave;ne la nourriture depuis une entr&eacute;e (image ci-dessous) jusqu&#39;&agrave; une trappe qui s&#39;ouvre ou se ferme via l&#39;utilisation d&#39;un servomoteur, le tout install&eacute; &agrave; l&#39;int&eacute;rieur de la ramp LED qui &eacute;claire l&#39;aquarium. Ce dispositif, au m&ecirc;me titre que les bacs de changement d&#39;eau, permettrait &agrave; l&#39;usager de pouvoir partir en vacances ou autre tout en sachant que les poissons seront nourris et que les changements d&#39;eau se feront. Le probl&egrave;me majeur qui a fait que je n&#39;ai pas pu r&eacute;aliser cette partie est la cr&eacute;ation de la courroie de transmission qui doit &ecirc;tre assez petite pour pouvoir faire en sorte que la rampe LED ne devienne pas trop massive autant d&#39;un point de vu visuel que du point de vu de sa masse.

				<h4>Boutons</h4>Les boutons sont plac&eacute;s sur le PCB secondaire et sont au nombre de 6, 3 paires de 2 boutons. Chaque paire permet d&#39;ajuster un param&egrave;tre, la premi&egrave;re paire permet d&#39;ajuster la temp&eacute;rature, la deuxi&egrave;me la temp&eacute;rature et la troisi&egrave;me la fr&eacute;quence de la distribution de nourriture.

				<h4>&Eacute;crans</h4>Le PCB secondaire est &eacute;galement connect&eacute; &agrave; 6 &eacute;crans OLED dont l&#39;objectif est d&#39;afficher les diff&eacute;rents param&egrave;tres de notre syst&egrave;me, que ce soit la temp&eacute;rature, la luminosit&eacute; ou bien els diff&eacute;rents test de l&#39;eau.

				<h4>Capteurs de niveau d&#39;eau</h4>Ces capteurs servent, comme leur nom l&#39;indique, &agrave; v&eacute;rifier le niveau de l&#39;eau. Lorsque deux bandes de m&eacute;tal entrent en contact avec de l&#39;eau cela cr&eacute;e un court-circuit ce qui renvoie un signal au PCB (&eacute;tat haut : il ya la pr&eacute;sence de court circuit donc l&#39;eau &agrave; atteint le niveau que l&#39;on veut v&eacute;rifier tandis qu&#39;&agrave; l&#39;&eacute;tat bas ce n&#39;est pas le cas). J&#39;ai pr&eacute;vu d&#39;en placer un dans l&#39;aquarium, un autre dans le bac d&#39;eau us&eacute;e et un dernier dans le bac d&#39;eau propre. Tout les trois servant &agrave; indiquer que l&#39;on a atteint une hauteur limite au dessus de laquelle il se peut que l&#39;eau se d&eacute;serve des bacs.

				<h4>Ph-m&egrave;tre</h4>Ce Ph-m&egrave;tre est fournis avec la sonde Ph et permet de rendre lisible la tension que sort la sonde Ph. Dans la suite du projet il me plairait de r&eacute;ussir &agrave; en faire un moi m&ecirc;me.

				<h4>Chauffage</h4>Fournis avec l&#39;aquarium, l&#39;objectif serait d&#39;y connecter un servomoteur afin de pouvoir s&eacute;lectionner la temp&eacute;rature que l&#39;on souhaite avec le module externe o&ugrave; se trouve le PCB d&eacute;port&eacute; ainsi que les &eacute;crans.

				<h4>ST-Link</h4>Simplement pr&eacute;sent pour pouvoir programmer le microprocesseur.

				<h4>HC05</h4>J&#39;ai pr&eacute;vu un connecteur pour le module HC05 m&ecirc;me si l&#39;utilisation de celui-ci ne se fera qu&#39;&agrave; la toute fin du projet. L&#39;objectif &eacute;tant de connecter un pc ou un t&eacute;l&eacute;phone en bluetooth &agrave; ce module afin de r&eacute;cup&eacute;rer l&#39;ensemble des param&egrave;tres comme le font les &eacute;crans mais cette fois sur un pc ou un t&eacute;l&eacute;phone, l&#39;objectif ultime &eacute;tant le d&eacute;veloppement d&#39;une appilcation. Revenons en aux PCBs, vous l&#39;aurez compris mais ici nous avons 2 PCBs avec des r&ocirc;les bien distinct, le premier servant &agrave; contr&ocirc;ler l&#39;ensemble du projet tandis que le second ne g&egrave;re que les boutons et &agrave; se connecter aux &eacute;crans. Vous pouvez trouver ci-dessous deux photos par PCB suivies d&#39;un lien, les photos correspondent aux schemtatic et routage des PCB effectu&eacute;s sous KiCad 9.0 et le fichier quant &agrave; lui est l&agrave; Bill Of Material (BOM) contenant l&#39;ensemble des composants n&eacute;cessaires &agrave; la fabrication des PCBs.</div>

			<p>
				<br>
			</p>
		</div></div></div>

<p data-f-id="pbf" style="text-align: center; font-size: 14px; margin-top: 30px; opacity: 0.65; font-family: sans-serif;">Powered by <a href="https://www.froala.com/wysiwyg-editor?pb=1" title="Froala Editor">Froala Editor</a></p>
