
import java.util.*;

public class NFA {
    public Set<String> states = new HashSet<>();
    public Set<String> symbols = new HashSet<>();
    public Map<String, Map<String, Set<String>>> transitions = new HashMap<>();
    public String initialState;
    public Set<String> finalStates = new HashSet<>();

    public NFA() {
        // Initialize transitions map
        transitions = new HashMap<>();
    }
}
