// Interfejs Logger
interface Logger {
    log(message: string): void;
  }
  
  // Prawdziwy Logger - loguje do konsoli
  class ConsoleLogger implements Logger {
    log(message: string): void {
      console.log(`[INFO]: ${message}`);
    }
  }
  
  // Null Logger - "pusty" logger, który nic nie robi
  class NullLogger implements Logger {
    log(message: string): void {
      // Brak akcji - implementacja jest celowo pusta
    }
  }
  
  // Klasa używająca Loggera
  class Application {
    private logger: Logger;
  
    constructor(logger: Logger) {
      this.logger = logger;
    }
  
    run(): void {
      this.logger.log("Application is running");
      // Inne operacje...
      this.logger.log("Application has finished running");
    }
  }
  
  // Przykład użycia
  const realLogger = new ConsoleLogger();
  const nullLogger = new NullLogger();
  
  // Aplikacja z prawdziwym loggerem
  const appWithLogging = new Application(realLogger);
  appWithLogging.run(); // Logi zostaną wyświetlone w konsoli
  
  // Aplikacja z NullLoggerem
  const appWithoutLogging = new Application(nullLogger);
  appWithoutLogging.run(); // Żadne logi nie zostaną wyświetlone
  