from rest_framework import serializers
from team.models import Section, Memeber, Skill


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class MemeberSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True, read_only=True)
    belongs_to = SectionSerializer(many=False, read_only=True)

    class Meta:
        model = Memeber
        fields = "__all__"
