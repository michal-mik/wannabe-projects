package HockeyManager;

import HockeyManager.Player.*;
import java.util.ArrayList;
import java.util.List;

public class HockeyManager {

    public List<Player> players = new ArrayList<>();

    public HockeyManager() {
        AddNewForward("Addie Attacker", 28, 51);
        AddNewDefender("Willie Wall", 35, 69);
        AddNewGoalie("Benny Bulletproof", 32, 12);
    }

    public void AddNewForward(String name, int age, int score) {
        Forward forward = new Forward(name, age, score);
        players.add(forward);
    }

    public void AddNewDefender(String name, int age, int hits) {
        Defender defender = new Defender(name, age, hits);
        players.add(defender);
    }

    public void AddNewGoalie(String name, int age, int wins) {
        Goalie goalie = new Goalie(name, age, wins);
        players.add(goalie);
    }

    public void PrintNameAndAgeOfTheYoungestPlayer() {
        if (players.isEmpty()) {
            System.out.println("No players in list");
            return;
        }

        Player youngest = players.get(0);

        for (Player player : players) {
            if (player.getAge() < youngest.getAge()) {
                youngest = player;
            }
        }

        System.out.println("Youngest player is " + youngest.getName() + " with age " + youngest.getAge());
    }

    public static void main(String[] args) {
        HockeyManager hockeyManager = new HockeyManager();
        hockeyManager.PrintNameAndAgeOfTheYoungestPlayer();
    }
}