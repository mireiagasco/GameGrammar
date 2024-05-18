import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class NFAInterpreter {
    private Set<String> states;
    private Set<String> alphabet;
    private Map<String, Set<String>> transitions;
    private String initialState;
    private Set<String> finalStates;

    public void interpret(String nodes, String transitions, String initial, String accept) {
        // Parsear los nodos
        nodes = nodes.replaceAll("[{}]", "");
        this.states = new HashSet<>(Arrays.asList(nodes.split(",")));

        // Parsear las transiciones
        this.transitions = new HashMap<>();
        transitions = transitions.replaceAll("[{( )}]", "");
        String[] transitionArray = transitions.split(";");
        for (String transition : transitionArray) {
            String[] parts = transition.split(",");
            String fromState = parts[0];
            String symbol = parts[1];
            String toState = parts[2];
            this.transitions.computeIfAbsent(fromState, k -> new HashSet<>()).add(symbol + "->" + toState);
        }
        // Establecer el estado inicial
        this.initialState = initial;

        // Establecer el estado final
        this.finalStates = new HashSet<>(Arrays.asList(accept.split(",")));

        // Construir el alfabeto
        this.alphabet = new HashSet<>();
        for (Set<String> symbols : this.transitions.values()) {
            for (String symbol : symbols) {
                this.alphabet.add(symbol.split("->")[0]);
            }
        }
    }

    public String generateLatex() {
        StringBuilder latex = new StringBuilder();

        // Encabezado del documento LaTeX
        latex.append("\\documentclass{article}\n")
                .append("\\usepackage{tikz}\n")
                .append("\\begin{document}\n")
                .append("\\begin{tikzpicture}[->, >=stealth, shorten >=1pt, auto, node distance=2.5cm, semithick]\n")
                .append("\\tikzstyle{every state}=[fill=blue!30,draw=none,text=white]\n");

        // Definir los estados
        for (String state : states) {
            String stateOptions = "";
            if (state.equals(initialState)) {
                stateOptions += ", initial";
            }
            if (finalStates.contains(state)) {
                stateOptions += ", accepting";
            }
            latex.append("\\node[state").append(stateOptions).append("] (").append(state).append(") {").append(state).append("};\n");
        }

        // Definir las transiciones
        for (Map.Entry<String, Set<String>> entry : transitions.entrySet()) {
            String fromState = entry.getKey();
            for (String transition : entry.getValue()) {
                String[] parts = transition.split("->");
                String symbol = parts[0];
                String toState = parts[1];
                latex.append("\\path (").append(fromState).append(") edge node {").append(symbol).append("} (").append(toState).append(");\n");
            }
        }

        // Pie del documento LaTeX
        latex.append("\\end{tikzpicture}\n")
                .append("\\end{document}\n");

        return latex.toString();
    }

    public static void main(String[] args) {

        String[] listAll = leerTEST("NFAs_TEST.txt");
        NFAInterpreter interpreter = new NFAInterpreter();
        interpreter.interpret(listAll[0], listAll[1], listAll[2], listAll[3]);

        String latexCode = interpreter.generateLatex();
        // generaLatex();
        try {
            Files.write(Paths.get("dfa_diagram.txt"), latexCode.getBytes());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private static String[] leerTEST(String filename) {
        FileReader fileReader = null;
        BufferedReader reader = null;
        StringBuilder all = new StringBuilder();
        String line;
        try {
            fileReader = new FileReader(filename);
            reader = new BufferedReader(fileReader);
            while ((line = reader.readLine()) != null) {
                all.append(line).append("\n");
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        String[] listAll = all.toString().split(" ");
        return listAll;
    }



}
