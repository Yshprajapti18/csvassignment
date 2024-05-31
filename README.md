# Assignment: Sheet Summarizer for CSV and XLSX Files

## Overview
For this assignment at Company Selenium, the task was to create a web application capable of summarizing CSV or XLSX files uploaded by users. The summary should provide counts of occurrences where specific columns match. The approach involved utilizing Django as the web framework, along with Pandas for data manipulation. The application was deployed on Vercel.

## Approach
1. **Model Creation**: A model was defined to represent uploaded files, containing fields for the file name and the file itself.
   
2. **Form Implementation**: A form was created in Django, utilizing the previously defined model. This form was used to handle file uploads.

3. **CSV Reader Functionality**: A CSV reader function was developed within the Django app. It utilized the form to accept file uploads. Upon receiving a file, the function checked if it had a CSV or XLSX extension. If so, it proceeded to read the file using the Pandas library.

4. **Data Summarization**: Once the file was successfully read, Pandas was used to summarize the data. Specifically, the counts of occurrences where certain columns (e.g., 'cust', 'state', 'dpd') matched were computed.

5. **Conversion to Dictionary**: The summarized data was converted into a dictionary format for easy rendering on the webpage.

6. **Rendering on Webpage**: Finally, the summarized data in dictionary form was rendered on the webpage for user viewing.

## Deployment Challenge
One significant challenge encountered during deployment on Vercel was the platform's read-only filesystem. This limitation meant that the traditional approach of saving uploaded files to disk and then processing them was not feasible. Instead, the code had to be adapted to perform all operations without saving any files locally.

## Solution
To overcome the Vercel filesystem limitation, the code was modified to read and process the uploaded file directly in memory without saving it to disk. This required adjustments to the CSV reader function and the summarization process. Despite the challenge, the modified code successfully achieved the desired functionality of summarizing uploaded files without relying on local storage.

## Conclusion
In conclusion, the assignment required the development of a web application capable of summarizing CSV and XLSX files uploaded by users. By leveraging Django, Pandas, and adapting to the limitations of the Vercel platform, the task was successfully completed. The final application provides users with a convenient tool for quickly obtaining summaries of their data files.

