import java.util.function.Predicate;
class MenuAction {
    private final String prompt;
    private final Predicate<String> trigger;
    private final Runnable action;

    public MenuAction(String prompt, Predicate<String> trigger, Runnable action) {
        this.prompt = prompt;
        this.trigger = trigger;
        this.action = action;
    }

    public boolean matches(String userInput) {
        return trigger.test(userInput);
    }

    public void run() {
        action.run();
    }

    public String getPrompt() {
        return prompt;
    }
}