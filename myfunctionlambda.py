import json

def lambda_handler(event, context):
    # Récupérer les données de la requête
  
    
    # Extraire le nom et le post-nom de la personne
    nom ="Nziengi"
    post_nom = "kamuina"
    
    # Créer la réponse JSON avec le nom et le post-nom
    response = {
        'nom': nom,
        'post_nom': post_nom
    }
    
    # Retourner la réponse HTTP
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }