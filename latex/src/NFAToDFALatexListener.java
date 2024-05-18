
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

public class NFAToDFALatexListener extends NFABaseListener {
    private NFA nfa;
    private NFA dfa;

    public NFAToDFALatexListener() {
        nfa = new NFA();
    }

    @Override
    public void enterState(NFAParser.StateContext ctx) {
        String stateName = ctx.IDENTIFIER().getText();
        nfa.states.add(stateName);
        if (ctx.stateProperty() != null) {
            for (NFAParser.StatePropertyContext propCtx : ctx.stateProperty()) {
                if (propCtx.getText().equals("initial")) {
                    nfa.initialState = stateName;
                }
                if (propCtx.getText().equals("final")) {
                    nfa.finalStates.add(stateName);
                }
            }
        }
    }

    @Override
    public void enterTransition(NFAParser.TransitionContext ctx) {
        String fromState = ctx.IDENTIFIER(0).getText();
        String toState = ctx.IDENTIFIER(1).getText();
        String symbol = ctx.SYMBOL().getText();

        nfa.symbols.add(symbol);

        nfa.transitions
                .computeIfAbsent(fromState, k -> new HashMap<>())
                .computeIfAbsent(symbol, k -> new HashSet<>())
                .add(toState);
    }

    public NFA convertToDFA() {
        dfa = new NFA();
        dfa.symbols = nfa.symbols;

        Set<String> initialSet = new HashSet<>();
        initialSet.add(nfa.initialState);
        Set<Set<String>> unprocessedStates = new HashSet<>();
        unprocessedStates.add(initialSet);
        Map<Set<String>, String> dfaStateNames = new HashMap<>();
        AtomicInteger stateCounter = new AtomicInteger();

        while (!unprocessedStates.isEmpty()) {
            Set<String> currentStateSet = unprocessedStates.iterator().next();
            unprocessedStates.remove(currentStateSet);

            String dfaStateName = dfaStateNames.computeIfAbsent(currentStateSet, k -> "q" + stateCounter.getAndIncrement());
            dfa.states.add(dfaStateName);

            if (currentStateSet.contains(nfa.initialState)) {
                dfa.initialState = dfaStateName;
            }
            if (!Collections.disjoint(currentStateSet, nfa.finalStates)) {
                dfa.finalStates.add(dfaStateName);
            }

            for (String symbol : nfa.symbols) {
                Set<String> nextStateSet = new HashSet<>();
                for (String state : currentStateSet) {
                    nextStateSet.addAll(nfa.transitions.getOrDefault(state, Collections.emptyMap()).getOrDefault(symbol, Collections.emptySet()));
                }

                if (!nextStateSet.isEmpty()) {
                    String nextDfaStateName = dfaStateNames.computeIfAbsent(nextStateSet, k -> "q" + stateCounter.getAndIncrement());
                    dfa.transitions
                            .computeIfAbsent(dfaStateName, k -> new HashMap<>())
                            .computeIfAbsent(symbol, k -> new HashSet<>())
                            .add(nextDfaStateName);

                    if (!dfa.states.contains(nextDfaStateName)) {
                        unprocessedStates.add(nextStateSet);
                    }
                }
            }
        }

        return dfa;
    }

    public String generateLatex(NFA dfa) {
        StringBuilder latex = new StringBuilder();

        latex.append("\\documentclass{article}\n")
                .append("\\usepackage{tikz}\n")
                .append("\\\\usetikzlibrary{automata, positioning, arrows}\n")
                .append("\\begin{document}\n")
                .append("\\begin{tikzpicture}[->, >=stealth, shorten >=1pt, auto, node distance=3cm, semithick]\n")
                .append("\\tikzstyle{every state}=[fill=red,draw=none,text=white]\n");

        for (String state : dfa.states) {
            String stateFormat = "\\node[state";
            if (state.equals(dfa.initialState)) {
                stateFormat += ", initial";
            }
            if (dfa.finalStates.contains(state)) {
                stateFormat += ", accepting";
            }
            stateFormat += "] (" + state + ") {" + state + "};\n";
            latex.append(stateFormat);
        }

        for (String fromState : dfa.transitions.keySet()) {
            for (String symbol : dfa.transitions.get(fromState).keySet()) {
                for (String toState : dfa.transitions.get(fromState).get(symbol)) {
                    latex.append("\\path (")
                            .append(fromState)
                            .append(") edge node {")
                            .append(symbol)
                            .append("} (")
                            .append(toState)
                            .append(");\n");
                }
            }
        }

        latex.append("\\end{tikzpicture}\n")
                .append("\\end{document}\n");

        return latex.toString();
    }
}
