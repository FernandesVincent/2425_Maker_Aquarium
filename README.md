Aquarium Automatisé
===================

SOMMAIRE

*   [Préambule](#Pr%C3%A9ambule)
*   [Objectifs du projet](#section2)
*   [Meuble](#section3)
*   [Filtration](#section4)
*   [Test en gouttes](#section5)
*   [Raspberry Pi](#section6)
*   [PCB](#section7)
*   [Écrans](#section8)
*   [Code](#section9)
*   [Câblage](#section10)
*   [Résultat et Conclusion](#section11)
*   [Futur du projet](#section12)

Préambule
=========

  

Aujourd'hui, lorsqu'un particulier achète son aquarium il doit pouvoir gérer un nombre important de facteurs comme la température du bac, la distribution de la nourriture mais également les différents test que peux nécessité son Aquarium (ph, NO2, CO2, etc...). C'est donc dans l'idée de soulager les personnes que cela pèse de devoir s'occuper de tout ça que l'idée du projet d'aquarium automatisé et connecté m'est venue à l'esprit.

Objectifs du Projet
===================

  

Pour répondre à la problématique énoncée durant le préambule, j'ai dessiné les différents axes et objectifs du projet énoncés ci-dessous:

*   Automatisation des changements d'eau
*   Contrôle simple et total sur la luminosité
*   Automatisation de la distribution de la nourriture
*   Automatisation des test en gouttes
*   Contrôle simple de la température
*   Afficher le tout sur des écrans
*   Bonus : Créer une Application mobile

Afin de réaliser l'ensemble de ces objectifs, j'ai du mettre en oeuvre plusieurs compétences que j'ai pu apprendre durant mon cursus à l'ENSEA telles que:

*   Découpe LASER
*   Conception de PCBs
*   Modélisation et impression 3D
*   Sertissage de câbles
*   Mécanique
*   Soudure

Mais également de nouvelles comme le montage vidéo et le HTML/CSS/JS pour la création d'un site. Pour expliquer chaque partie de ce projet en détail, nous allons partir du plus gros oeuvre vers le plus petit. Commençons donc par parler du meuble qui doit supporter l'aquarium.

Meuble
======

  

Au vu de l'ensemble des objectifs du projet, il fallait un endroit où ranger notamment, l'électronique avec les PCBs et les câbles, le bloc de filtration externe, le dispositif d'analyse des test en gouttes ainsi que les bacs de changements d'eau. Pour répondre à ce besoin j'ai penser à la création d'un meuble pouvant supporter le poids de l'aquarium ainsi que tout ce qu'il y a à l'intérieur. Pour ce faire il a été décidé que la structure du meuble se ferait à l'aide de profilé aluminium 20x40mm et que les murs seront faits en MDF 3mm. Cependant quelques contraintes étaient présentes:

*   le meuble doit au minimum faire la largeur (30cm) et la longueur(60cm) de l'aquarium.
*   Il doit pouvoir accueillir 2 bacs ayant au minimum une capacité de 18L.
*   Le bac doit être assez petit pour diminuer les coûts liés au profilé aluminium.

Prenant tout cela en compte, j'ai réalisés des premiers modèles 3D pour pouvoir estimer la taille du meuble et la quantité de profilé aluminium ainsi que de MDF nécessaire. Vous pouvez voir les modèles prototypes ci-dessous: 

![image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%201.png?raw=true)

![Image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%202.png?raw=true)

![Image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%203.png?raw=true)

![image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%204.png?raw=true)

![Image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%205.png?raw=true)

![Image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20proto%206.png?raw=true)

La version finale étant la suivante :

![Image centrée](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/furniture%20final.png?raw=true)

L'ensemble des fichiers STL est disponible sur mon[GitHub](https://github.com/FernandesVincent/2425_Maker_Aquarium) dans la catégorie "onshape".

  

Ce meuble est donc sur 2 étages, le premier étant un étage réservé aux trois bacs de changements d'eau. Chacun ayant un objectif unique:  
  
Celui ci-dessous est dédié à l'eau usée de l'aquarium qui peut être réutilisée pour par exemple arroser ses plantes.

![Image centrée](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/used%20water%20tank.png?raw=true)

Le second présent ci-dessous est fait pour accueillir l'eau propre qui va venir remplacer l'eau usée.

![Image centrée](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/unused%20water%20tank.png?raw=true)

Le troisième et plus petit doit est quant à lui réservé à l'eau en sortie des test à gouttes qui doit être jetée.

![Image centrée](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/little%20tank.png?raw=true)

Pour la sortie du premier bac j'ai trouver un modèle 3D de robinet qui fonctionne assez bien sur [Printables](https://www.printables.com/model/278618-water-tap).

De même que précédemment l'ensemble des fichiers STL mais également les fichiers DXF sont disponibles sur mon [GitHub](https://github.com/FernandesVincent/2425_Maker_Aquarium) dans la catégorie "onshape".

  

Filtration
==========

  
Attaquons le second étage du meuble par la partie concernant le bloc de filtration. J'ai souhaité faire ce bloc externe moi-même car cela me permettait de créer un design personnalisé, notamment pour pouvoir y placer aisément le chauffage et la sonde ph en plus des masses filtrantes.   
Comme précédemment vous pouvez voir ci-dessous le prototype de ce bloc de filtration suivi de la version finale,   
  
prototype: 

![Image centrée](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/proto%20filter.png?raw=true)

  
version finale: 

![Image centrée](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/filter.png?raw=true)

  
  
Pour pouvoir nettoyer les masses filtrantes, j'ai designer un bac de remonté (trouer pour que l'eau s'en écoule et ne pas trempé le meuble en les sortant) avec sa poignée : 

![image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/tray%20tank.png?raw=true)

![Image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/tray%20tank%20handle.png?raw=true)

  
  
Concernant les différents composants de ce bloc, la sonde ph vient de [DFRobot](https://wiki.dfrobot.com/Gravity__Analog_Spear_Tip_pH_Sensor___Meter_Kit__For_Soil_And_Food_Applications__SKU__SEN0249) tandis que le chauffage est fournis avec l'aquarium qui est un aquarium de 60L de la marque CIANO disponible sur [Amazon](https://www.amazon.fr/Aquarium-Poissons-Consommables-Chauffage-Emballage/dp/B0DMZ6JCDD/?_encoding=UTF8&pd_rd_w=eTX08&content-id=amzn1.sym.46807d81-91bd-498b-9732-d523d8e7a752%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=46807d81-91bd-498b-9732-d523d8e7a752&pf_rd_r=917652W8GSPYV4HS716T&pd_rd_wg=m7z8E&pd_rd_r=916570f0-c766-4f99-b61e-7f823d6b24d8&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1) .   
De plus, concernant les masses filtrantes elles sont également disponibles sur Amazon: [céramique](https://www.amazon.fr/Fluval-Pr%C3%A9filtre-pour-Aquariophilie-750/dp/B001CZXZEU?crid=2DO1R98ZQM2RC&dib=eyJ2IjoiMSJ9.NOtwUJAeSHLB4A1TeyF7lMZri_mYYibux8elORv2TfHT8yLHpVdMSdJHqTUiYHcFMGr334v6IEnsWWmJfPLGE1mpoogN8XoEghupyyNrigO5VS3plDP2CcTmYq2QG4MJTkvTzTTOcQFQ4Y0zzN6mUG_yH7nay19Ffslt9v3t-JCdI6s2QMdTKHUrgb4h_1CvccY8n2z9cqhy9a3K2YmWuXX8cIhYSCcO7GUgdoUt6KjcFyZBTqqU88QPV-2foIqJT7tRuESUFezL2JtSR4yoJJafDqbmSgWf8wqJXLkooE1-nc9v4LDAB3mVxILasvuHKCNPN2AHisuPH9ZROWr5dpat5z9vd5tvAiF1vmKVE2g3hL_7fAWg2CkyKnFiSWWdrk5zkhM4B4p-2tI30VVCbNROYQcaY3yV6V1a9vud8sK52BZ7lmUmHwG4r6HhVILX.sY-sm_8FTIMCC4HghsrVIvfEG4izV4uUMwokH-4gn60&dib_tag=se&keywords=ceramique%2Bfiltre%2Baquarium&qid=1740995166&sprefix=ceramique%2Bfiltre%2Baquarium%2Caps%2C81&sr=8-1&th=1) ; [mousse](https://www.amazon.fr/cyclingcolors-d%C3%A9couper-300x210mm-Universelle-%C3%A9paisseur/dp/B0B8JQTZXK?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1GWVJFUSDAMSF&dib=eyJ2IjoiMSJ9.-Nc9EyO1uODmLOWsuEoIv2-ijdhS7vjX1hI6M1EGydp_XFS0wtrzbE2jVMFgrEHocHL6DNbcq4DOPNmEpaNBjZdWuUZP7ZPMicQLsIZ90SWD_deMd8pHQZAqzOpOAZ4D1IFHZ2X0fnkMDess7XfQdBE53jzyoQ5U7YxbRgxUxo4TxXIPRLPpCA1pShM8uPEC_14BnQmFSo0ENJEtF6zNZXzpbQdPOGYKqjRVUeZF0_ePPmf3qAuxzeko5WCX9S8S1h26QB7Ui_yH5xzVT67D3-7iV_G0tFTnQTAvHnabRmVddSMM1xzyo7R-AJKU_j0SQG36PPXQcBq1ewFXpCj_3ksSo4r8ET7GnpSYFM6XmYWrbgCw1QJ-D-15VbdYH-UsJ4eVRgI1szYcRs2AKRRBLG8D_Ecth-nHQBS7rLAzYn_QlE0Hg81ooezR5RGuDtZn.uqiGKSbLIfv1qsK1z4Wm6e5aRRmxiQVxfnGUyDTqWIk&dib_tag=se&keywords=mousse+filtration+aquarium&qid=1740746478&sprefix=mousse+filtration+aquarium%2Caps%2C86&sr=8-10) .   
Les trous dans le Blocs de filtration servent à le fixer dans le plancher à mi hauteur du meuble, ils correspondent à des vis de taille M6 avec une longueur qui doit être d'environ 20 mm sachant que le plancher est fait en MDF 6mm. Des écrous adéquat sont aussi à prévoir.   
Concernant l'impression du bloc de filtration, elle peut se faire en plus ou moins de parties en fonction de la taille de l'imprimantes. Par exemple, avec les imprimantes disponibles à l'ENSEA :   
  
Creality K1 Max (300x300x300mm) : 2 parties   
BambuLab X1 Carbon(250x250x250mm) : 4 parties (les 2 parties précédentes doivent être coupées à mi-hauteur)   
  
De plus, le bloc a été imprimé en PLA, or le PLA n'est pas étanche. Pour pallier à ce problème j'ai pris l'initiative d'utiliser de la résine époxy afin de vernir le bloc et de le rendre étanche. Le seul inconvénient de cette méthode est la toxicité de la résine notamment durant la phase de catalyse qui peut durer plusieurs heures et nécessite le port d'un [masque](https://www.amazon.fr/AirGearPro-Protection-Respiratoire-R%C3%A9utilisable-poussi%C3%A8re/dp/B08BQNKK8D/ref=sr_1_12?crid=3LH54H1JA5QNK&dib=eyJ2IjoiMSJ9.vwG9ct7oYhsXxHkosVw_DmGGbSvG-EdfTzmpbvbIy_-blRdYccvxTNdLoztSTV8tl_ikyBC3C5sx3ez7fd9GjM_BHjicTpMb-_M9EWASUwky-py3WhngzjeKjcqC1QPGVSqLLVt9dwrGpRvv8uZhM5_Re66P_tbjd75zfz0It3lw5R378O4styzF4mT2UFgELnVqo1dEaq5sjsjGSO8SU83Srj58_ZeWd_S_6tQwyARHEVkMqt6VuIe_q-BQpZhJykYvcj-rFgzkfMzgAcjRl5SiAw0cAYN1tXGGBibU2ro.akVBE5KxVIQV9yLbv8nGTHnn1ifGuOQN2ryeAmktGkY&dib_tag=se&keywords=masque%2Ba%2Bgaz&qid=1745913052&sprefix=masque%2Ba%2B%2Caps%2C88&sr=8-12&th=1) et de [gants de protection](https://www.amazon.fr/ARNOMED-jetables-pi%C3%A8ces-nitrile-disponibles/dp/B093SWH4D8/ref=sr_1_8_mod_primary_new?crid=2KVGNDRFCIO71&dib=eyJ2IjoiMSJ9.HYDeG_JqkiNaNzhkKCJYphhk3ndVM0UbqT-yoTDSnaWFA6OdHlNBi3FhoeW2ZUUI0AozoLPBT0LRJtSUa-ADjaOinG8uifUUo70TLPnk6H4vzPfIN_jZfhI2XwAXMrE8QZiC77FgNaG4N8q-fSoo0epvPihgD-rdkskBYnW7LVj1pTZO8u1pXD_ZNOCaioAR9EvJmOK1yNxrAvVQc99SmUWtKPwbwy0ztc6t6WeLP1m2mzQK-hKjnMPUpVIE1dcgy_K40Tb25gJmvBveADWoAOuMog-kQ_XCkylXwUWTjHc.5SfCoj71a8R3wwyGeR2RD5FM8fDVUkjrGQuWOm_lA1U&dib_tag=se&keywords=gants%2Bnitrile&qid=1745913117&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=gants%2Caps%2C93&sr=8-8&th=1).   
  
Pour finir, l'eau arrive du côté de la sonde PH via un tuyaux avec un OD de 20mm et elle ressort de l'autre côté grâce à une pompe de remontée connecter via un raccord à un autre tuyaux.  
  

Test en gouttes
===============

  

Au sein du meuble et à côté du bloc de filtration nous pouvons retrouver la partie test en gouttes du projet. Cette partie est surement la plus complexe du projet car elle implique la modélisation 3D d'un dispositif permettant d'insérer et d'enlever les test en gouttes mais également de pouvoir faire tomber des gouttes lorsque l'on le désire.   
  
La version actuelle a été réfléchie avec un servomoteur FS90 actionnant un engrenage qui permet à son tour de faire tourner des "bras" qui iront appuyer sur les test afin de faire tomber les gouttes. 

![Image centrée](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/onshape/stl%20files/pictures/drops%20test.png?raw=true)

  
  
Ce mécanisme est malheuresement encore en phase de prototypage car la faible tension de surface au niveau de la sortie goutte à goutte des test implique qu'une seule petite vibration peut faire s'écouler une goutte.   
Un autre modèle possible serait de faire directement tourner les tests via un servomoteur afin de faire s'écouler la goutte en profitant justement de la faible tension de surface.   
  
Une fois la goutte écoulée, elle est redirigée dans un flacon, dans lequel s'écoule également l'eau du bac a testée, qui est bloqué par un anneau lié à un autre servomoteur lui permettant de pivoter afin de remuer la solution et enfin de vider le flacon dans un tuyaux menant au bac associé. Afin de déterminer la valeur associé au test (valeur de Ph, de NO3, etc...) il faut effectuer de la reconnaissance colorimétrique.

  

RaspberryPi
===========

  

Pour effectuer la reconnaissance colorimétrique je me suis servi d'un raspberryPi 4 model B avec la module caméra associé. Cet ensemble auquel on ajoute un code en Python, disponible sur mon [GitHub](https://github.com/FernandesVincent/2425_Maker_Aquarium) dans la catégorie "software", permet de récupérer la vision de la caméra et d'y définir un ou plusieurs points où l'on va vouloir analyser la couleur du pixel en leur centre :

![Image centrée](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/software/Python/pictures/example%20point.png?raw=true)

  
Le code couleur que j'ai utilisé est le HSV et non le RGB car cela permet d'être moins sensible à la différence de luminosité. 

![Image centrée](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/software/Python/pictures/HSV-vs-RGB.jpg?raw=true)

  
  
Un aspect que je n'ai pas eu le temps de terminer est le fait de comparer les valeurs récupérés par la caméra aux valeurs de références des couleurs des test en gouttes. Cependant, l'idée derrière ce code serait d'avoir pour chaque test un tableau contenant les couleurs références et ainsi via un petit d'algorithme de comparer la couleur HSV expérimental avec celle de référence afin de l'assimiler à celle-ci.   
Finalement il suffirait de faire correspondre la couleur HSV de référence avec la valeur associée. Une fois cela fait l'objectif est de transmettre cette valeur au PCB principal qui, lui, l'enverra aux écrans.

  

PCB
===

  

Cela nous fait une transition parfaite pour parler plus en profondeur de la partie PCB du projet. En effet, pour mener à bien ce projet j'ai du réaliser 2 PCB : un premier PCB dit "principal" et un second dit "déporté". Le premier PCB et son aspect de multiprise sert à commander l'ensemble du projet, c'est à dire :  
  

*   Les 4 ventilateurs
*   Les 4 pompes
*   Les LED
*   Les servomoteurs pour le distributeur de nourriture/li>
*   Les boutons présents sur le second PCB
*   Les écrans
*   Les servomoteurs pour les test en gouttes
*   la raspberryPi et sa camera
*   Les capteurs de niveau d'eau
*   Le Ph-mètre
*   Le chauffage
*   Le ST-Link
*   Le HC05

Faisons un petit aparté pour détailler l'utilité de chacun des modules dont nous n'avons pas encore eu l'occasion de discuter.  
  

#### Ventilateurs

Le meuble et le PCB sont fait pour accueillir 4 [ventilateurs](https://www.amazon.fr/ARCTIC-P12-Pack-Refroidisseur-Ventilateur/dp/B07HC7P3HJ/ref=sr_1_22?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3TXQLZO0PSBMV&dib=eyJ2IjoiMSJ9.zUhrIjc32H8-WvshILuE-PtJkv-mw1FkSGAgT1AOR1oDyib-dphFTw_ivU8-Os2Z3SPkMx71hmaU-qOowlMbCeCCD-m-aEquUmbZ3FlHR8_-ej5oHyh2yaVaZolCfb03zDvlUppXXPbv_NlB8bF4hvQ0kXKkbZYUaWO43Sw08Tl8NM4P3ilE9XKvfy9u-lT4zo6KmAZJ5tKS3DDawNQxlgLpxpx_1iES2Xqx_mKGXe48RHJHkL_6mCOrnpOmsJY1jxpEXj42bwhzMWrXvfzqdaw7qTj1C8cfzn7Wl4qSAVI.Drgr1JScUsXTqbsAaerU-8GdExFSoYqVR8i45yJohCs&dib_tag=se&keywords=ventilateur+pc+120mm+12V&qid=1745915029&sprefix=ventilateur+pc+120mm+12v%2Caps%2C109&sr=8-22) 12V de 120mmx120mm. Deux (paire entrée/sortie) à l'étage des bacs et deux ( paire entrée/sortie) à l'étage supérieur.   
Le couple de ventilateur de l'étage inférieur a pour but de ventilé l'eau propre arrivant dans le bac associé afin d'aider à l'évaporation des éléments indésirables contenu dans cette eau (si on utilise de l'eau osmosée ces deux ventilateurs sont inutiles).   
Le second couple de moteur, quant à lui, est là pour aérer la Pi, le PCB et surtout l'alimentation qui ne possède pas de ventilateur.

####   

#### Pompes

Pour ce projet, nous avons besoins d'un ensemble de 4 [pompes](https://www.amazon.fr/submersibles-aquarium-poissons-fontaine-divertissement/dp/B0CDK7GQF2/ref=sr_1_21?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2CUWEXFG2PUFC&dib=eyJ2IjoiMSJ9.kt5smPhlWur0wnbrli3H4DrVLEC06_QO_JbOBYEyMijIh7_RthNJVyfAX4Ud4PPDpqdHwQ4pOWaoo6zsfZ69VyOE8kOFChswIdw_yxYq4pP-k7e8YAFBlQMr3mmeVJtgOaJd2ZKn4M9ht6t596XUTjhOngGLBwXbttb6pcsssp_XBXbosgC-o98d1DYvuCTUCOvFmy3iTxm9IGIwgRYmeEGXowZ4qxU2LAg6pIt1ekSnjvASpDlITmRQtVY1Zr23BJv-VApa7OJQNyjO6xRdQ4rEIOZGFSaqHZtZlUoIaBo.5UAUpJxV19I-vKTE8ASD2hpe8OtvqdkrKyf74I9DL3Q&dib_tag=se&keywords=pompe+12v+eau&qid=1745915095&sprefix=pompe+12v+eau%2Caps%2C86&sr=8-21) 12V 240L/h. Une première sert pour la sortie de la filtration, une seconde à remontée l'eau du bac d'eau propre à l'aquarium, une troisième à vider l'eau de l'aquarium vers le bac de récupération de l'eau usée et la dernière envoi l'eau vers le filtre. Les deux pompes liées à la filtrations fonctionnent en continu tandis que les deux autres fonctionne sur commande grâce à l'utilisation de deux transistors NMOS présents sur le PCB permettant d'allumer les pompes quand le GPIO lié à leur Ground est à l'état haut.

####   

#### LED

Les LED de ce projet sont séparées en deux parties mais viennent toutes de la même bande [Neopixel](https://www.amazon.fr/Jun-Saxifragelec-lumineuse-flexible-adressable-individuellement/dp/B0B8N4V9HW/ref=sr_1_7?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1CJ3DP9KGQZX7&dib=eyJ2IjoiMSJ9.jsv5HLdSZ_CqM09rG6Xk6uZZAWjjtuBx5FYoyybZ6Cq0dW9sdN0xiOcqO8t8Ln6LuHMjn9s3v2aI3iDoKG0TfEWM3Paz30Z6tmC2xSMbVQSZ50eRcyr4CrFsPwJ1RPR3CfkJwi70Efu_rKi0G0wMe0WJ2qUvEkmbGIRzA1bnyN1mzGsZ2Wg8r_ZL_B7AHo-iN01WSayc71oC5XkE90xITgpsP5gH7CkykDFgiCTTThXMaQrIhLf8PSJImtNxPoGk4S0CWjx7Hrr5ck_nuMyflQfhR7mZIpUyXcVC_EAC5UM.w_CUH-9CxgqyNuN4tKuXXqzRhF1nZa9Ggmml6dgE2r4&dib_tag=se&keywords=ruban%2Bled%2Bneopixel&qid=1745915170&sprefix=ruban%2Bled%2Bneopixel%2Caps%2C85&sr=8-7&th=1).

####   

##### LED internes

Ce sont des LEDs coupées du ruban et placées dans le meuble afin de pouvoir l'éclairer en continu avec une même luminosité afin de limiter au mieux les erreurs de reconnaissances colorimétriques.

####   

##### LED externes

Ces LED sont le reste du ruban et servent directement à l'éclairage de l'aquarium. L'utilité d'avoir pris des LED Neopxiel est ici de pouvoir totalement configurer la couleur que l'on veut pour éclairer son aquarium en fonction des poissons et plantes qui l'occupe.

####   

#### Servomoteurs (nourriture)

Je vais traiter directement ici la partie de la distribution automatique de la nourriture car je n'ai pas eu le temps de la réaliser et par conséquent elle ne nécessite pas une partie entière à elle seule. L'objectif de cette partie était initialement de pouvoir automatiser la distribution de nourriture via un système de courroie de transmission qui amène la nourriture depuis une entrée (image ci-dessous) jusqu'à une trappe qui s'ouvre ou se ferme via l'utilisation d'un servomoteur, le tout installé à l'intérieur de la ramp LED qui éclaire l'aquarium.   
  
  
Ce dispositif, au même titre que les bacs de changement d'eau, permettrait à l'usager de pouvoir partir en vacances ou autre tout en sachant que les poissons seront nourris et que les changements d'eau se feront. Le problème majeur qui a fait que je n'ai pas pu réaliser cette partie est la création de la courroie de transmission qui doit être assez petite pour pouvoir faire en sorte que la rampe LED ne devienne pas trop massive autant d'un point de vu visuel que du point de vu de sa masse.

####   

#### Boutons

Les boutons sont placés sur le PCB secondaire et sont au nombre de 6, 3 paires de 2 boutons. Chaque paire permet d'ajuster un paramètre, la première paire permet d'ajuster la température, la deuxième la température et la troisième la fréquence de la distribution de nourriture.

####   

#### Écrans

Le PCB secondaire est également connecté à 6 [écrans](https://www.gotronic.fr/art-afficheur-oled-0-96-128-x-64-grove-33932.htm) OLED dont l'objectif est d'afficher les différents paramètres de notre système, que ce soit la température, la luminosité ou bien els différents test de l'eau.

####   

#### Capteurs de niveau d'eau

Ces [capteurs](https://www.adafruit.com/product/4965) servent, comme leur nom l'indique, à vérifier le niveau de l'eau. Je me suis procuré ceux de Adafruit car leur prix est peu élevé et qu'ils suffisent pour l'utilité que j'en ai.  
  
Lorsque deux bandes de métal entrent en contact avec de l'eau cela crée un court-circuit ce qui renvoie un signal au PCB (état haut : il ya la présence de court circuit donc l'eau à atteint le niveau que l'on veut vérifier tandis qu'à l'état bas ce n'est pas le cas). J'ai prévu d'en placer un dans l'aquarium, un autre dans le bac d'eau usée et un dernier dans le bac d'eau propre. Tout les trois servant à indiquer que l'on a atteint une hauteur limite au dessus de laquelle il se peut que l'eau se déserve des bacs.

####   

#### Ph-mètre

Ce Ph-mètre est fournis avec la sonde Ph et permet de rendre lisible la tension que sort la sonde Ph. Dans le futur du projet il me plairait de réussir à en faire un moi même.

####   

#### Chauffage

Fournis avec l'aquarium, l'objectif serait d'y connecter un servomoteur afin de pouvoir sélectionner la température que l'on souhaite avec le module externe où se trouve le PCB déporté ainsi que les écrans.

####   

#### ST-Link

Simplement présent pour pouvoir programmer le microprocesseur.

####   

#### HC05

J'ai prévu un connecteur pour le module HC05 même si l'utilisation de celui-ci ne se fera qu'à la toute fin du projet. L'objectif étant de connecter un pc ou un téléphone en bluetooth à ce module afin de récupérer l'ensemble des paramètres comme le font les écrans mais cette fois sur un pc ou un téléphone, l'objectif ultime étant le développement d'une appilcation.   
  
  
  
  
Revenons en aux PCBs, vous l'aurez compris mais ici nous avons 2 PCB avec des rôles bien distinct, le premier servant à contrôler l'ensemble du projet tandis que le second ne gère que les boutons et à se connecter aux écrans. Vous pouvez trouver ci-dessous deux photos par PCB suivies d'un lien, les photos correspondent aux schemtatic et routage des PCB effectués sous KiCad 9.0 et le fichier quant à lui est la Bill Of Material (BOM) contenant l'ensemble des composants nécessaires à la fabrication des PCB.   
  
PCB principal:

![image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/pictures/main%20PCB%20sch.png?raw=true)

![Image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/pictures/main%20PCB%20.png?raw=true)

[BOM](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/PCB_Aquarium2/BOM_PDF.pdf)  
  
PCB secondaire:

![image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/pictures/2nd%20PCB%20sch.png?raw=true)

![Image](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/pictures/2nd%20PCB.png?raw=true)

[BOM](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/hardware/PCB_secondaire/BOM_PDF.pdf)

  

Écrans
======

  

Nous avons d'ores et déjà parlé succinctement du rôle des écrans dans le projet c'est pourquoi j'aimerais m'attarder ici plutôt sur la partie code associé à ces écrans. En effet, Les écrans que j'ai commandé sont les suivants:   
  
Ces écrans peuvent communiquer soit en I2C (avec 2 adresses possibles : 0x7A et 0x78) soit en SPI. Or, et je pense que vous l'avez compris avec la partie précédente mais nous avons beaucoup de modules différents avec lesquels le microprocesseur doit communiquer. Le microprocesseur en question est le STM32G474RET6 qui possède 3 I2C, ce qui est parfait pour notre projet car nous pouvons commander 2 écrans avec un seul I2C. Mais à cause du nombre très élevés du nombre de pins que le microprocesseur doit allouer au reste du projet, les pins que les 3 I2C utilisent ne sont plus disponibles.   
Il m'a donc fallu me rabattre sur le SPI qui bien que nécessitant un nombre de pins plus élevés est plus pratique dans ce cas pour deux : 1 seul SPI peut gérer les 6 écrans à conditionner de leur réservé un pin de sélection (Chip Select (CS)) chacun mais également car la plupart des pins qu'il utilise peuvent être de simple GPIO (comme CS) voir même non obligatoire en fonction de l'utilisation.   
Par exemple dans notre cas nous n'avons pas besoin du pin MOSI (Master Out Slave In) car on attend pas de réponse de la part des écrans.   
Le problème majeur que j'avais concernant le SPI est que je n'avais jamais travaillé ce protocole auparavant, j'ai donc du apprendre comment il fonctionne ce qui ne fut, heureusement, pas la partie la plus compliquée. Cependant, là où je me suis heurté à un mur c'est au moment de la recherche de librairies pour utiliser ce protocole avec le driver de mes écrans (le SSD1315) qui n'est malheureusement pas le driver le plus utilisé ce qui implique donc que les librairies que j'ai trouvées n'avaient pas directement de librairies pour ce driver, même si il semblerait que celles du driver SSD1306 fonctionne, du moins en partie, avec le SSD1315. De plus, j'ai également reçu de la part de mon encadrant une library faîte pour mon driver mais en I2C.   
Au vu du temps qu'il me restait à ce moment là j'ai préféré me concentrer sur d'autres aspects du projet ce qui fait qu'à l'heure où j'écris ces lignes, les écrans ne sont pas encore fonctionnels.

  

Code
====

  

Nous avons déjà eu l'occasion d'aborder le sujet du code dans ce projet mais j'aimerais y dédier une partie car il y a quand même des notions à ajouter et que je ne pourrais diluées dans aucune aitre partie. Veuillez tout d'abord regarder le diagramme d'architecture du code présent ci-dessous: 

![Image centrée](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/gestion%20projet/diag%20code.png?raw=true)

  
Nous avons déjà aborder la partie de la RaspberryPi excepté le fait que pour effectué la reconnaissance colorimétrique j'ai du utiliser OpenCV.   
  
Concernant le code du STM32 il est, je pense, nécessaire de recontextualiser: Pour ce projet nous devons effectué des changements d'eau à un intervalle fixe (10% de l'eau de l'aquarium chaque semaine), de même il faut nourrir les poissons et effectuer les test en gouttes à intervalles réguliers. Pour effectuer cela sachant que le projet n'est pas connecté à Internet, il m'a fallu créer un horloge interne qui peux fonctionner d'elle même après avoir flasher le microprocesseur avec le code présent sur mon PC. Le fichier la contenant peut être trouver sur mon GitHub. Cette Horloge démarre à partir d'un date définit arbitrairement et permet de réaliser des actions du type : si on est au jour X à l'heure Y et à la minute Z : fait telle action.   
De plus, comme je ne commande en moteur que des servomoteurs basiques, il me suffit de leur envoyer des PWMs pour définir la position d'arrivé et ensuite les faire revenir à leur positions de départ une fois leur action finie. Le seul inconvénient de cela est que dois tester chaque mouvement de mes servomoteurs pour plusieurs valeurs de PWMs afin de pouvoir savoir quelle valeur de PWM serait la meilleure. Une méthode plus évoluée serait de créer une boucle for qui incrémente la valeur de la PWM à chaque itération.   
Finalement, Les LEDs sont commandées via DMA grâce à une librairie crée par l'un des professeurs de l'école. La seule chose est que je dois définir des valeurs références pour la couleur des LEDs afin que l'usager puisse par l'appui des boutons, passer d'une couleur à une autre. Une amélioration serait d'avoir 3 encodeur rotatif permettant à l'usager d'avoir la possibilité de régler la couleur de la lumière de son précision avec une précision qu'il n'a pas actuellement.

  

Câblage
=======

  

Au vu du projet et du nombre de modules à connecter aux PCB vous vous doutez que le nombre de câbles à sertir est conséquent ! Et c'est effectivement le cas.   
Pour ce projet j'ai du sertir énormément de câbles pour différents types de connecteurs : JST EH, JST XH, Duponts. De plus, j'ai également du simplement dénuder des câbles afin de pouvoir les souder à d'autres notamment pour les pompes ou les câbles d'alimentation.   
Mais le câblage ne s'arrête pas à sertir un câble, il faut également les emballer. C'est à dire qu'il faut entourer les câble de gaine tressée pour les protéger mécaniquement et thermiquement mais également pour les organiser. Mais il faut également les entourer de gaine thermorétractable pour fixer la gaine tressée aux câbles au niveau des extrémités pour pas qu'elle ne bouge mais également au niveau des points de soudure pour protéger ce point notamment si il y a un autre câble souder à côté, ils sont ainsi isolés l'un de l'autre et l'on ne risque pas de mauvais contacts.

  

Résultat Final et Conclusion
============================

  

Tout au long de cette présentation vous avez pu voir différentes parties du projet mais il est temps de montrer le résultat que j'ai réussi à obtenir à la fin de ce proje ainsi que la vidéo de présentation du projett:    
[  
Résultat final](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/gestion%20projet/final%20result.mp4)  
[vidéo de présentation](https://github.com/FernandesVincent/2425_Maker_Aquarium/blob/main/gestion%20projet/Vid%C3%A9o%20Aquarium.mp4)  
  
Comme vous pouvez le voir je n'ai pas pris de vidéos avec l'aquarium remplit et le système en fonctionnement et la raison à cela est simple: je n'ai pas réussi à finir et emboiter toutes les parties du projet dans le temps impartit.   
  
Pour conclure cette présentation j'aimerais revenir sur ce qu'à pu m'apporter ce projet. En effet, ce projet malgré le fait que je n'ai pas pu le finir m'a quand même permis de développer toutes les compétences que l'on a pu développées au cours de cette présentation, des compétences que j'avais déjà mais que j'ai pu grandement améliorées comme la création et la soudure de PCB ou bien des compétences que je n'avais pas encore eu l'occasion de développer durant mon parcours comme la découpe LASER, la modélisation et l'impression 3D.   
Au vu de mon niveau, ce projet était sans nul doute ambitieux, surement trop d'ailleurs au vu du temps impartit mais c'est ce qui en fait un bon projet dans le sens où j'ai pu apprendre comme je n'ai jamais appris avec n'importe quel autre projet.

  

Futur du Projet
===============

  

Bien évidemment je ne compte pas m'arrêter là pour ce projet. En effet, il me reste un an pour le finir avant de finir mes études et je compte bien profiter de cette année pour finir le projet et y apporter toutes les améliorations dont j'ai pu parler au sein de cette présentation et qui sait peut-être que d'autres me viendront à l'esprit entre temps !


