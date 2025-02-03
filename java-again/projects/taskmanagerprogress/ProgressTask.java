class ProgressTask implements Runnable {
    private final String taskName;
    private final int duration; // Czas trwania w ms

    public ProgressTask(String taskName, int duration) {
        this.taskName = taskName;
        this.duration = duration;
    }

    @Override
    public void run() {
        System.out.println(taskName + " rozpoczęte...");

        int steps = 10; // Ilość aktualizacji postępu
        for (int i = 1; i <= steps; i++) {
            try {
                Thread.sleep(duration / steps); // Częściowe oczekiwanie
            } catch (InterruptedException ignored) {}

            int progress = (i * 100) / steps; // Obliczanie procentów
            System.out.println(taskName + " - Postęp: " + progress + "%");
        }

        System.out.println(taskName + " zakończone!");
    }
}
