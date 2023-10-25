#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to check for SQL injection in a URL.
int check_for_sql_injection(const char *url) {
  // Check for common SQL injection keywords.
  const char *keywords[] = {"SELECT", "INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "CREATE"};
  for (int i = 0; i < sizeof(keywords) / sizeof(keywords[0]); i++) {
    if (strstr(url, keywords[i]) != NULL) {
      return 1;
    }
  }

  // Check for single quotes (') and double quotes (").
  if (strstr(url, "'") != NULL || strstr(url, "\"") != NULL) {
    return 1;
  }

  // Check for other suspicious characters.
  const char *suspicious_characters[] = {"%", "_", "?", "\\", "/", "&", "="};
  for (int i = 0; i < sizeof(suspicious_characters) / sizeof(suspicious_characters[0]); i++) {
    if (strstr(url, suspicious_characters[i]) != NULL) {
      return 1;
    }
  }

  // If we reach here, then the URL is likely safe from SQL injection.
  return 0;
}

int main(int argc, char *argv[]) {
  // Get the URL from the user.
  char url[1024];
  printf("Enter a URL: ");
  scanf("%s", url);

  // Check for SQL injection in the URL.
  int result = check_for_sql_injection(url);

  // Print the result to the console.
  if (result == 1) {
    printf("The URL may be vulnerable to SQL injection.\n");
  } else {
    printf("The URL is likely safe from SQL injection.\n");
  }

  return 0;
}
