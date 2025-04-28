#include <stdio.h>
#include <unistd.h>  // Pour sleep()

int main() {
    // Initialisation de l'horloge interne (exemple : 12:59:50, un mercredi)
    int heures = 12, minutes = 59, secondes = 50;
    int jour = 3;  // 0 = Dimanche, 1 = Lundi, ..., 6 = Samedi

    char* jours[] = {"Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"};

    // Référence (quand afficher "Hello")
    int JOUR_REF = 3;      // Mercredi
    int HEURE_REF = 13;    // 13h (1 PM)
    int MINUTE_REF = 0;
    int SECONDE_REF = 0;    // 00 minutes

    while (1) {
        // Affichage de l'heure actuelle
        printf("\r%02d:%02d:%02d - %s", heures, minutes, secondes, jours[jour]);
        fflush(stdout);  // Rafraîchir immédiatement l'affichage

        // Mise à jour de l'heure interne
        secondes++;
        if (secondes >= 60) {
            secondes = 0;
            minutes++;
        }
        if (minutes >= 60) {
            minutes = 0;
            heures++;
        }
        if (heures >= 24) {
            heures = 0;
            jour = (jour + 1) % 7;  // Passer au jour suivant
        }

        // Vérification si on atteint le moment cible
        if (jour == JOUR_REF && heures == HEURE_REF && minutes == MINUTE_REF && secondes == SECONDE_REF) {
            printf("\nHello !\n");
        }

        sleep(1);  // Attendre 1 seconde
    }

    return 0;
}

