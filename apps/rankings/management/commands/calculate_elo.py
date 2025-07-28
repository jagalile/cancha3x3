from django.core.management.base import BaseCommand
from apps.competitions.models import Match
from apps.rankings.models import PlayerRanking


K_PROVISIONAL = 40
K_NORMAL = 20
K_ELITE = 10

PROVISIONAL_GAMES = 20
ELO_ELITE = 2400


class Command(BaseCommand):
    help = 'Calculate ELO rankings for players based on recent matches'

    def add_arguments(self, parser):
        parser.add_argument('match_id', type=int, help='El ID del partido a procesar')

    def handle(self, *args, **kwargs):
        match_id = kwargs['match_id']
        try:
            match = Match.objects.get(id=match_id)
        except Match.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Partido con ID {match_id} no encontrado.'))
            return

        elo_winner_team = self.get_average_elo(match.winner_team)
        elo_loser_team = self.get_average_elo(match.loser_team)

        mov_multiplier = self.get_margin_of_victory_multiplier(match.score_winner_team, match.score_loser_team)

        expected_winner = self.calculate_expected_result(elo_winner_team, elo_loser_team)
        expected_loser = 1 - expected_winner

        for player in match.winner_team.members.all():
            k = self.get_k_factor(player)
            elo_update = k * (1 - expected_winner) * mov_multiplier
            self.update_player_elo(player, elo_update)

        for player in match.loser_team.members.all():
            k = self.get_k_factor(player)
            elo_update = k * (0 - expected_loser) * mov_multiplier
            self.update_player_elo(player, elo_update)

        self.stdout.write(self.style.SUCCESS(f'ELO rankings updated for match {match_id}'))

    def get_average_elo(self, team):
        team_members = team.members.all()

        total_elo = sum(PlayerRanking.objects.filter(player=team_member.player).order_by('-date').values_list('elo', flat=True).first() for team_member in team_members)

        return total_elo / len(team_members) if team_members else 0

    def get_margin_of_victory_multiplier(self, winner_score, loser_score):
        margin = abs(winner_score - loser_score)

        # Puedes ajustar estos umbrales y multiplicadores según tus preferencias
        if margin <= 4:
            return 1.0  # Sin modificador para victorias ajustadas
        elif margin <= 9:
            return 1.2  # Modificador moderado
        else:  # margin >= 10
            return 1.5  # Modificador alto para victorias contundentes

    def calculate_expected_result(self, elo_winner, elo_loser):
        return 1 / (1 + 10 ** ((elo_loser - elo_winner) / 400))
    
    def update_player_elo(self, player, elo_update):
        player_ranking = PlayerRanking.objects.filter(player=player.player).order_by('-date').first()
        player_ranking.elo += elo_update
        player_ranking.save()
        self.stdout.write(self.style.SUCCESS(f'ELO rankings updated for player {player.player.username} to {player_ranking.elo}'))

    def get_k_factor(self, team_member) -> int:
        player_elo = PlayerRanking.objects.filter(player=team_member.player).order_by('-date').values_list('elo', flat=True).first()
        #if player.partidos_jugados < self.PROVISIONAL_GAMES:
        #    return self.K_PROVISIONAL
        if player_elo >= ELO_ELITE:
            return K_ELITE
        return K_NORMAL