
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) throws IOException {
        String input = "nfa {\n" +
                "    state q0 {initial}\n" +
                "    state q1 {}\n" +
                "    state q2 {}\n" +
                "    state q4 {final}\n" +
                "    state q5 {}\n" +
                "    state q6 {}\n" +
                "    transition q0 -> q1 : a;\n" +
                "    transition q1 -> q2 : E;\n" +
                "    transition q0 -> q4 : a;\n" +
                "    transition q0 -> q5 : E;\n" +
                "    transition q5 -> q6 : a;\n" +
                "}";

        CharStream inputStream = CharStreams.fromString(input);
        NFALexer lexer = new NFALexer(inputStream);
        CommonTokenStream tokenStream = new CommonTokenStream(lexer);
        NFAParser parser = new NFAParser(tokenStream);
        ParseTree tree = parser.automaton();

        ParseTreeWalker walker = new ParseTreeWalker();
        NFAToDFALatexListener listener = new NFAToDFALatexListener();
        walker.walk(listener, tree);

        NFA dfa = listener.convertToDFA();
        String latexCode = listener.generateLatex(dfa);

        // Write the LaTeX code to a file
        Files.write(Paths.get("dfa_diagram.tex"), latexCode.getBytes());
        System.out.println("LaTeX code has been generated and saved to dfa_diagram.tex");
    }
}
