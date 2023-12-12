
**League and Group Selection:**

The program starts by asking the user which results they are interested in, allowing them to choose between UEFA and Ekstraklasa. 🌐
Next, the user is prompted to select a group in the case of the UEFA Champions League (groups A-H). 🏆

**Web Scraping Initiation:**

After receiving user input, the program initiates the web scraping mechanism using Selenium. 🚀
Depending on the user's choice, the program navigates to the appropriate Google page where match results can be found. 🌐

**Data Retrieval:**

The program automatically clicks a button to access current results (additional clicks might be required by the website). 🖱️
Subsequently, the program waits for a few seconds for the page to load. 🕒
Utilizing web scraping technology (Selenium), the program retrieves information about the clubs in the selected league and group. 🤖

**Saving to the Database:**

After gathering the data, the program saves it in a local SQLite database. 💾
Each record includes information such as the date, group, and the first, second, third, and fourth places in the group. 📝
For Ekstraklasa, the fifth place is also recorded. 🥇🥈🥉🥉🥉

**Program Termination:**

After saving the results to the database, the program concludes its operation. 🏁




**Wybór Ligi i Grupy:**

Program zaczyna od zapytania użytkownika, który zainteresowany jest wynikami. Może wybierać między UEFA a Ekstraklasą. 🌐
Następnie użytkownik zostaje poproszony o wybranie grupy w przypadku Ligi Mistrzów UEFA (grupy A-H). 🏆
**Uruchomienie Web Scraping:**

Po wprowadzeniu wyborów, program uruchamia mechanizm web scrapingu przy użyciu Selenium. 🚀
W zależności od wyboru użytkownika, program przechodzi do odpowiedniej strony Google, gdzie można znaleźć wyniki meczów. 🌐
**Pobieranie Danych:**

Program automatycznie klika na przycisk, aby uzyskać dostęp do aktualnych wyników (ewentualne kliknięcie przycisku może być wymagane przez stronę internetową). 🖱️
Następnie program oczekuje kilka sekund na załadowanie strony. 🕒
Korzystając z technologii web scrapingu (Selenium), program pobiera informacje o klubach z danej ligi i grupy. 🤖
**Zapisywanie do Bazy Danych:**

Po pobraniu danych, program zapisuje je w lokalnej bazie danych SQLite. 💾
Każdy rekord zawiera informacje takie jak data, grupa, a także pierwsze, drugie, trzecie i czwarte miejsce w danej grupie. 📝
W przypadku Ekstraklasy jest również zapisywane piąte miejsce. 🥇🥈🥉🥉🥉
**Zakończenie Programu:**

Po zapisaniu wyników do bazy danych, program kończy swoje działanie. 🏁
