// #include <stdio.h>
// #include <dirent.h>
// #include <string.h>
// #include <curl/curl.h>

// #define MAX_FILENAME_LENGTH 255

// int main() {
//     // directory containing the mp3 files
//     char directory[] = "/path/to/mp3/files";

//     // directory to save downloaded files
//     char download_directory[] = "/path/to/save/files";

//     DIR *dir = opendir(directory);
//     struct dirent *entry;

//     // create a list to store the file names without the extension
//     char file_names[MAX_FILENAME_LENGTH][MAX_FILENAME_LENGTH];
//     int file_count = 0;

//     // iterate through the directory
//     while((entry = readdir(dir)) != NULL) {
//         // check if the entry is a file and has the .mp3 extension
//         if(entry->d_type == DT_REG && strstr(entry->d_name, ".mp3") != NULL) {
//             // get the file name without the extension
//             char *file_name = strtok(entry->d_name, ".");

//             // store the file name in the list
//             strcpy(file_names[file_count], file_name);
//             file_count++;
//         }
//     }
//     closedir(dir);

//     // download files using libcurl
//     CURL *curl;
//     CURLcode res;

//     curl = curl_easy_init();
//     if(curl) {
//         for(int i = 0; i < file_count; i++) {
//             // create the full file path to save the downloaded file
//             char file_path[MAX_FILENAME_LENGTH];
//             sprintf(file_path, "%s/%s.mp3", download_directory, file_names[i]);

//             // set the URL to download
//             curl_easy_setopt(curl, CURLOPT_URL, "https://example.com/music/"+file_names[i]);

//             // set the file to save the downloaded data to
//             curl_easy_setopt(curl, CURLOPT_WRITEDATA, fopen(file_path, "wb"));

//             // perform the download
//             res = curl_easy_perform(curl);

//             // check for errors
//             if(res != CURLE_OK) {
//                 fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
//             }
//         }

//         // cleanup
//         curl_easy_cleanup(curl);
//     }

//     return 0;
// }
