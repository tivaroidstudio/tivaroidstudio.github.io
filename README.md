# Hangman: Rivals — publiczne strony prawne

Ten katalog jest samodzielną, statyczną stroną bez cookies, analityki i zewnętrznego JavaScriptu.

Docelowe adresy wpisane w aplikacji:

- polityka: `https://tivaroidstudio.github.io/hangman-rivals-privacy/index.html`
- usuwanie konta: `https://tivaroidstudio.github.io/hangman-rivals-privacy/delete-account.html`
- informacja o najnowszej wersji: `https://tivaroidstudio.github.io/hangman-rivals-privacy/app-version.json`
- autoryzowani sprzedawcy reklam: plik `app-ads.txt` (musi być opublikowany w katalogu głównym hosta wskazanego jako witryna dewelopera w Google Play)

Przy każdym wydaniu zmień `latestVersion` w `app-version.json` dopiero po udostępnieniu wersji testerom/produkcji. Klient sprawdza manifest przy starcie oraz przed pierwszym wejściem do multiplayera. Nowsza wartość `latestVersion` blokuje multiplayer do czasu aktualizacji, ale brak pliku lub sieci nie blokuje gry offline.

## Darmowe wdrożenie przez Cloudflare Pages

1. Zaloguj się na `https://dash.cloudflare.com/`.
2. Otwórz **Workers & Pages → Create → Pages → Upload assets**.
3. Jako nazwę projektu wpisz dokładnie `hangman-rivals-privacy`.
4. Przeciągnij cały katalog `PrivacySite` albo archiwum ZIP zawierające jego pliki.
5. Kliknij **Deploy site**.
6. Sprawdź w trybie incognito oba adresy podane powyżej.
7. Jeśli nazwa jest zajęta i Cloudflare nada inny adres, zmień oba adresy w `Assets/Hangman/Scripts/LegalLinks.cs` przed kolejnym buildem.
8. Po każdej zmianie użyj w projekcie Pages opcji **Create deployment / Upload assets**, wgraj ponownie zawartość katalogu i sprawdź datę wdrożenia.

## AdMob `app-ads.txt`

Plik zawiera wpis wydawcy Hangman: Rivals:

```text
google.com, pub-5931050261951076, DIRECT, f08c47fec0942fa0
```

AdMob ignoruje ścieżkę witryny dewelopera i sprawdza plik w katalogu głównym jej hosta. Dlatego obecny adres projektu GitHub Pages:

```text
https://tivaroidstudio.github.io/hangman-rivals-privacy/
```

powoduje sprawdzanie:

```text
https://tivaroidstudio.github.io/app-ads.txt
```

a nie `/hangman-rivals-privacy/app-ads.txt`. Wybierz jeden z dwóch poprawnych wariantów:

1. **Cloudflare Pages (najprostszy):** wgraj zawartość `PrivacySite` jako osobny projekt. Jeżeli otrzymasz adres `https://hangman-rivals-privacy.pages.dev`, wpisz dokładnie ten adres jako **Witryna dewelopera** w Google Play. Sprawdź publicznie `https://hangman-rivals-privacy.pages.dev/app-ads.txt`.
2. **GitHub Pages:** opublikuj ten plik w repozytorium witryny użytkownika `tivaroidstudio.github.io`, tak aby działał dokładnie adres `https://tivaroidstudio.github.io/app-ads.txt`. Samo umieszczenie pliku w repozytorium `hangman-rivals-privacy` nie wystarcza.

Po zmianie witryny dewelopera Google Play może potrzebować do 24 godzin, żeby przekazać ją do AdMob. Następnie w AdMob otwórz **Aplikacje → Hangman: Rivals → app-ads.txt → Sprawdź aktualizacje**. Nie wpisuj w Google Play pełnego adresu pliku — wpisz adres witryny dewelopera.

W Google Play Console wpisz:

- **Polityka prywatności:** adres strony głównej;
- **Usuwanie konta / Data deletion URL:** adres `delete-account.html`.

Publiczna strona nie ma dostępu do Unity i nie usuwa danych automatycznie. Bezpieczne zgłoszenie tworzy zalogowana gra przez Cloud Code. Dla osoby bez aplikacji pozostaje ręczna ścieżka e-mail z weryfikacją zgodnie z `Docs/ACCOUNT_DELETION_RUNBOOK.md`.

Plik `_headers` dodaje CSP, HSTS i blokady niepotrzebnych funkcji przeglądarki. Po wdrożeniu zweryfikuj nagłówki np. przez `https://securityheaders.com/`.
