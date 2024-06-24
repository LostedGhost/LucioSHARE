document.getElementById('copyBtn').addEventListener('click', function() {
    var input = document.getElementById('slugToCopy');
    input.select();  // Sélectionner le texte de l'input
    input.setSelectionRange(0, 99999);  // Pour les mobiles

    try {
        var successful = document.execCommand('copy');
        var msg = successful ? 'Texte copié avec succès!' : 'Échec de la copie du texte';
        console.log(msg);
    } catch (err) {
        console.error('Erreur lors de la copie du texte', err);
    }
});
