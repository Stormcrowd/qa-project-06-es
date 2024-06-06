Proyect 6
=================


You Will need
==================
Necesitas tener instalados los paquetes Install pytest and request packages to execute the required tests

Execute all test with the command: pytest


Explanation
=================
In this project you will find 9 test automatized to test the NAME field on the CREATION KIT TEST.

This we Will be testing 9 diferent scenarios that were requested by the client:


TEST_1, min character

TEST_2, max character

TEST_3, min character -1

TEST_4, max caracter +1

TEST_5, Special character

TEST_6, Space character

TEST_7, string number

TEST_8, Null

TEST_9, Int


Resolting in 5 successfully passed tests, 3 Failed, and 1 side scenario.

On the FAILED section we got: 3, 4 and 9 seemingly they are showing 201 code, which is WRONG, they should be error 400, by the documentation shared.

The side scenario is number 8, which is showing 500 error, more related to the server response, but it needs to be CHECK OUT and verified to share the correct output to the USER.


CONCLUSION
================

According to the test results it seems the server is currently allowing any output to be shared as a kit name, since for all test seems to be showing 201 as respond, allowing any input to be set for the kits name.

Please check out the limits put to the tool and verify they are correctly working to correct the current behavior presented.
