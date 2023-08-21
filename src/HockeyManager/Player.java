package HockeyManager;

public class Player
{
    public String name;
    public int age;

    public Player(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public static class Forward extends Player
    {
        public int score;
        public Forward(String name, int age, int score)
        {
            super(name, age);
            this.score = score;
        }
        public int getScore()
        {
            return score;
        }
    }

    public static class Defender extends Player
    {
        public int hits;

        public Defender(String name, int age, int hits)
        {
            super(name, age);
            this.hits = hits;
        }

        public int getHits()
        {
            return hits;
        }
    }

    public static class Goalie extends Player
    {
        public int wins;
        public Goalie(String name, int age, int wins)
        {
            super(name, age);
            this.wins = wins;
        }
        public int getWins()
        {
            return wins;
        }
    }
}