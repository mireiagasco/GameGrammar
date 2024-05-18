import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link NFAParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface NFAVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link NFAParser#automaton}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAutomaton(NFAParser.AutomatonContext ctx);
	/**
	 * Visit a parse tree produced by {@link NFAParser#state}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitState(NFAParser.StateContext ctx);
	/**
	 * Visit a parse tree produced by {@link NFAParser#stateProperty}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStateProperty(NFAParser.StatePropertyContext ctx);
	/**
	 * Visit a parse tree produced by {@link NFAParser#transition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTransition(NFAParser.TransitionContext ctx);
}