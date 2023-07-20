# peshkariki-ui-and-api

Framework with automated tests for Peshkariki.ru (b2b, b2c web App used to deliver goods, purchases, documents, etc.)

Currently includes test scenarios to check UI functionality on these pages:

 - start_page
 - my_orders_page

The project is created as a part of an educational course by QALearning School.

The Allure Report framework is added to the project. So that reports of test(s) execution can be generated automatically and in an easy-to-read format.

▶️ To run all tests at once use the command "pytest tests" in the Terminal of Pycharm. Or use a command "pytest ./tests/[test_filename.py]" to run a specific test from all.

▶️ To run test(s) with report auto-generation by Allure, firstly use the command "pytest tests --alluredir results" (for all tests) or "pytest ./tests/[test_filename.py] --alluredir results" (for a specific test) in the Terminal of Pycharm. Then in Terminal navigate to the folder of the project and run the command “allure serve results” to open the generated report.
