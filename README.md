
Version 3.0: Exception-Safe & Optimized Engine

Now the script is crash-resilient and optimized for resource efficiency. It handles potential system errors gracefully and cuts execution times during successful simulations.
What I learned here:
*** Exception handling (try-except): I protected the tool from sudden crashes by trapping the FileNotFoundError. If the external target dictionary (data.txt) is missing, the script catches the issue and explains it gracefully instead of throwing a raw system traceback error.
*** The Flag Variable Pattern (was_found): I discovered how to use state flags to control the logic flow. Instead of messy in-loop reporting, the script updates a boolean flag and evaluates the final validation outcome strictly once at the end.
*** The Loop Optimization (break): Implemented an immediate execution halt using the break statement. Once the correct password is found, the tool instantly stops iterating through the remaining lines, saving heavy CPU resources and time.
*** Interactive Input Prompts: Improved the User Interface (UI) by adding explicit text prompts inside the input() function. This prevents confusion, ensuring the operator always knows exactly what data the script is waiting for.
*** Post-Context Evaluation: Aligned the final reporting block outside the with manager. This ensures the file stream is safely closed and memory is completely freed before the final output prints.
