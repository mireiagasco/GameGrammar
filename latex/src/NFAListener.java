// Generated from C:/Users/Katty/IdeaProjects/nfaTodfa/NFA.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link NFAParser}.
 */
public interface NFAListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link NFAParser#automaton}.
	 * @param ctx the parse tree
	 */
	void enterAutomaton(NFAParser.AutomatonContext ctx);
	/**
	 * Exit a parse tree produced by {@link NFAParser#automaton}.
	 * @param ctx the parse tree
	 */
	void exitAutomaton(NFAParser.AutomatonContext ctx);
	/**
	 * Enter a parse tree produced by {@link NFAParser#state}.
	 * @param ctx the parse tree
	 */
	void enterState(NFAParser.StateContext ctx);
	/**
	 * Exit a parse tree produced by {@link NFAParser#state}.
	 * @param ctx the parse tree
	 */
	void exitState(NFAParser.StateContext ctx);
	/**
	 * Enter a parse tree produced by {@link NFAParser#stateProperty}.
	 * @param ctx the parse tree
	 */
	void enterStateProperty(NFAParser.StatePropertyContext ctx);
	/**
	 * Exit a parse tree produced by {@link NFAParser#stateProperty}.
	 * @param ctx the parse tree
	 */
	void exitStateProperty(NFAParser.StatePropertyContext ctx);
	/**
	 * Enter a parse tree produced by {@link NFAParser#transition}.
	 * @param ctx the parse tree
	 */
	void enterTransition(NFAParser.TransitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NFAParser#transition}.
	 * @param ctx the parse tree
	 */
	void exitTransition(NFAParser.TransitionContext ctx);
}