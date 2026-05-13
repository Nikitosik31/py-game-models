import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race = player["race"]
        race_obj, created = Race.objects.get_or_create(
            name=race["name"],
            defaults={
                "description": race["description"]
            }
        )
        for skill in race["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race_obj
                }
            )
        guild = player["guild"]
        if guild:
            guild_obj, created = Guild.objects.get_or_create(
                name=guild["name"],
                defaults={
                    "description": guild["description"]
                }
            )
        else:
            guild_obj = None
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race_obj,
                "guild": guild_obj})


if __name__ == "__main__":
    main()
