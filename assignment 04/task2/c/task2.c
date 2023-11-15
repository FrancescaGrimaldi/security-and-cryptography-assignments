// In C: write a function that takes a string as input and returns a new string that is equal to the 
// input but where &, < and > are replaced by &amp;, &lt; and &gt;

# include <stdio.h>
# include <stdlib.h>
# include <string.h>

# define MAX 500

size_t new_length(char *input_string);
char* replace_char(char *input_string);

int main () {
    char input_string[MAX];

    printf("Enter your string: \n");
    fgets(input_string, sizeof(input_string), stdin);

    char *output_string = replace_char(input_string);

    if (output_string != NULL) {
        printf("Output string: \n%s", output_string);
        free(output_string);
    } else {
        printf("Error\n");
    }

    return 0;
}

size_t new_length(char *input_string) {
    size_t length = strlen(input_string);
    size_t new_length = length;

    for (size_t i = 0; i < length; i++) {
        if (input_string[i] == '<' || input_string[i] == '>') {
            new_length += 3;
        } else if (input_string[i]== '&') {
            new_length += 4;
        }
    }

    return new_length;
}

char* replace_char(char *input_string) {
    size_t newlen =  new_length(input_string);

    char *output_string = malloc(newlen + 1);

    if (output_string == NULL) {
        return NULL;
    }

    size_t j = 0;
    for (size_t i=0; i < strlen(input_string); i++) {
        if (input_string[i] == '<') {
            strcpy(&output_string[j], "&lt;");
            j += 4;
        } else if (input_string[i] == '>') {
            strcpy(&output_string[j], "&gt;");
            j += 4;
        } else if (input_string[i] == '&') {
            strcpy(&output_string[j], "&amp;");
            j += 5;
        } else {
            output_string[j] = input_string[i];
            j++;
        }
    }
    output_string[newlen] = '\0';

    return output_string;
}

