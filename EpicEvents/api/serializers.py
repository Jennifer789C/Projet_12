from rest_framework.serializers import ModelSerializer
from .models import Client, Contrat, Evenement


class ClientListeSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "societe", "statut", "nom", "prenom"]


class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "societe", "statut", "nom", "prenom", "email", "tel",
                  "port", "date_creation", "date_maj", "vendeur"]


class ClientModifSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "societe", "statut", "nom", "prenom", "email", "tel",
                  "port"]


class ContratListeSerializer(ModelSerializer):
    parent_lookup_kwargs = {"client_pk": "client__pk"}

    class Meta:
        model = Contrat
        fields = ["id", "client", "ouvert", "signe"]


class ContratCreationSerializer(ModelSerializer):
    parent_lookup_kwargs = {"client_pk": "client__pk"}

    class Meta:
        model = Contrat
        fields = ["id", "client", "montant", "echeance"]


class ContratModifSerializer(ModelSerializer):
    parent_lookup_kwargs = {"client_pk": "client__pk"}

    class Meta:
        model = Contrat
        fields = ["id", "client", "ouvert", "signe", "date_signature",
                  "montant", "echeance"]


class ContratDetailSerializer(ModelSerializer):
    parent_lookup_kwargs = {"client_pk": "client__pk"}

    class Meta:
        model = Contrat
        fields = ["id", "client", "ouvert", "signe", "date_signature",
                  "montant", "echeance", "date_creation", "date_maj"]


class EvenementListeSerializer(ModelSerializer):
    class Meta:
        model = Evenement
        fields = ["id", "ouvert", "date_evenement"]


class EvenementDetailSerializer(ModelSerializer):
    class Meta:
        model = Evenement
        fields = ["id", "ouvert", "date_evenement", "participants", "notes",
                  "date_creation", "date_maj", "contrat", "support"]
