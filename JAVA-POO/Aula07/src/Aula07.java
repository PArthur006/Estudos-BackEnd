import java.util.ArrayList;

public class Aula07 {
    public static void main(String[] args) {
        ArrayList<Lutador> lutadores = new ArrayList<>();

        // DEFININDO LUTADORES
        lutadores.add(new Lutador("Pretty Boy", "França", 31, 1.75, 68.9, 11, 2, 4));
        lutadores.add(new Lutador("Putscript", "Brasil", 29, 1.68, 57.8, 14, 2, 3));
        lutadores.add(new Lutador("Snapshadow", "EUA", 35, 1.65, 80.9, 12, 2, 1));
        lutadores.add(new Lutador("Dead Code", "Austrália", 28, 1.93, 81.6, 13, 0, 2));
        lutadores.add(new Lutador("UFOCobol", "Brasil", 37, 1.70, 119.3, 5, 4, 3));
        lutadores.add(new Lutador("Nerdaart","EUA", 30, 1.81, 105.5, 12, 2, 4));

        for(int i=0; i<lutadores.size(); i++){
            lutadores.get(i).apresentar();
        }
    }
}
