# exception-handling

Types of Errors in Python
=================================================
=>The purpose of Exception Handling is that " To Develop OR Bulid Robust (Strong) Applications ".
=>In real time to develop any project, we choose a lang. By using that lang we develop, compile and execute Various Programs. During this Process, we get 3 types of Errors. They are

			1. Compile Time Error
			2. Logical Error
			3. Runtime Error
--------------------------------------------------------------------------------------
Compile Time Error
--------------------------------------------------------------------------------------
=>These Errors occurs during Compilation Time (.py------>.pyc)
=>These errors occurs due to Syntaxes are not followed during Program Development.
=>These errors are solved by Programmers During Development Time

------------------------------------------------------------------------------------------------------------------------------
Logical Error
------------------------------------------------------------------------------------------------------------------------------
=>These Errors occurs during Runtime OR Execution Time
=>These errors occurs due to Wrong Representation of Logic 
=>Logical Error always gives Wrong Result
=>These errors are solved by Programmers During Development Time

------------------------------------------------------------------------------------------------------------------------------
Runtime Error ( Implementation Error )
------------------------------------------------------------------------------------------------------------------------------
=>These Errors occurs during Runtime OR Execution Time
=>These errors occurs due to WRONG INPUT / INVALID INPUT Entered by End Users OR Application Users.
=>When Runtime Errors occurs  By Default all the Languages gives Technical Error Messages, which are 
    understandable by Programmers but not by End-Users. This is not a Recommended Process in Real Time.
=>According to Industry Standards, It recommends to display always User-Friendly Error Messages for making the 
    Application Robust by using Exception Handling.
    
----------------------
NOTE:
----------------------
=>When the End User enters Valid Input  to the Project then the Project gives Successful Result.
=>When the End User enters InValid Input  to the Project then the Project Must display User-Friendly Error Messages 
    by using Exception Handling.





=======================================================
						**Types of Exceptions in Python**
				=======================================================
=>In Python Programming, we have 2 Types of Exceptions. They are

			1. Pre-Defined OR Built-In Exceptions
			2. Programmer OR User OR Custom Defined Exceptions
-------------------------------------------------------------------------------------------------------------------------------------------------------
Pre-Defined OR Built-In Exceptions
-------------------------------------------------------------------------------------------------------------------------------------------------------
=>Pre-Defined OR Built-In Exceptions are those which are already developed by Python Language Developers and available in Python Software and They are used by Python Lang Programmers for Dealing with Universal Problems.
=>Some of the Universal Problems are
			i) Invalid Index ( IndexError )
			ii) Invalid Conversions ( ValueError)
			iii) Invalid Number of Arguments OR Operations (TypeError )
			iv) Passing Invalid Key (KeyError)
			v) Division by zero problems (ZeroDivisionError:) .........etc
=>All Previous Error Names are called Runtime Errors  and They are called Pre-Defined Exception Class Names.

-------------------------------------------------------------------------------------------------------------------------------------------------------
Programmer OR User OR Custom Defined Exceptions
-------------------------------------------------------------------------------------------------------------------------------------------------------
=>Programmer OR User OR Custom Defined Exceptions are those which are developed by Python Programmers and they are available in Python Project and They are used by  Other Team Members of Same Project and They are always deals with Common Problems occuring in the project.
=>Some of the Common Problems are
			i) Attempting to enter Invalid User Name and Password 
			ii) Attempting to enter Invalid PIN in ATM Applications
			iii) Attempting to Withdraw More Amount than Existing Bal of Account
			iv) Attempting to enter Invalid Names for People, Places , Product..etc
   
-----------------------------------------------------------------------------------------------------------------






===================================================
					Handling the Exception
===================================================
=>Handling the Exception is nothing But Converting Technical Error Messages in User-Frinedly Error Message.
=>For Handling the Exceptions in Python, we have 5 Key words. They are

				1. try
				2. except
				3. else
				4. finally
				5. raise
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Syntax for Handling the exception
-----------------------------------------------------------------------------------------------------------------------------------------------------------
		try:
		   Block of Statements
		   generates exceptions
		except exception-class-name-1:
			Block of Statements
			generates User-Friendly Error Message
		except exception-class-name-2:
			Block of Statements
			generates User-Friendly Error Message
		-----------------------------------------------
		-----------------------------------------------
		except exception-class-name-n:
			Block of Statements
			generates User-Friendly Error Message
		else:
			Block Of Statements
			Displays Result
		finally:
			Block of Statements
			Executes Compulsorily
			for Relinquishing the Resources Like Files / Database






======================================================
					Building Points in Exception Handling
======================================================
1. When the Application User Enters Wrong OR Invalid Input then we get Runtime Error.
				( Invalid Input------->Runtime Error)
2. All Runtime Errors by default gives Technical Error Messages.
		(Invalid Input------>Runtime Error-------->Technical Error Messages)
3. Definition of Exception : Every Runtime Error is called Exception
					(Invalid Input------>Runtime Error-------->Exception)
			All invalid Inputs are considered as Exceptions
4. All Exceptions by default gives Technical Error Messages.			
5. Definition of Exception Handling:- The Process of Converting Technical Error Messages into User-Friendly 
							      Error Messages is called Exception Handling.
6. When the exception occurs in Python Program. The following Steps Takes Place Internally.
			i)   Program Execution  Abnormally Terminated
			ii)  PVM Comes out-off Program flow 
			iii) PVM by default generates Technical Error Message.
7. To do the above Step-(i),Step-(ii) and Step-(iii), PVM CREATES AN OBJECT w.r.t An EXCEPTION CLASS.
8. When an Exception occurs in Python Program then PVM creates an Object of appropriate EXCEPTION CLASS
9. Hence All Exceptions are Considered as objects of EXCEPTION CLASSES.
====================================x=======================================================






================================================
			Explanation for the keywords used in Syntax of Handling Exception
================================================
--------------------------------------------------------------------------------------------
1.try
--------------------------------------------------------------------------------------------
=>It is the block in which we write block of statements generating exceptions. In otherwords what 
    are all the statements are generating exceptions, those statements must be written within try block and hence try block is called Exception monitering block.
=>When an exception occurs in try block then PVM comes out of try block and executes  appropriate except block.
=>After executing appropriate except block, PVM never goes to try block for executing rest of the statements in try 
    block.
=>Every try block must be immediately followed by except block ( Otherwise we get   SyntaxError)
=>Every try block must contain atleast one except block . It is recommended to write multiple 
     except blocks for generating User-Friendly error messages.
     
-------------------------------------------------------------------------------------------
2.except
--------------------------------------------------------------------------------------------
=>It is the block in which we write block of statements generates User-Friendly Error Friendly  Messages. In Otherwords except block suppreses Technical error messages and generates User-Freindly Error Messages and hence except block is called Exception Processing Block.
Note: Handling exception= try block + except  block
=>except block will execute when there is an exception occurs in try block.
=>Even we write multiple except blocks , PVM executes Appropriate except block(Single Block) depends on type of exception occurs in try block.
=>The place for writing except block is that after try block and before else block.

------------------------------------------------------------------------------------------------------------------------------------------
3.else 
--------------------------------------------------------------------------------------------
=>It is the block in which we write block of statements will display results of the program and hence else block is called Result Generated Block.
=>else block will execute when there is no exception occurs in try block.
=>Writing else block is optional
=>The place of writing else block is that after except block and before finally block (if it present).

--------------------------------------------------------------------------------------------
4.finally 
--------------------------------------------------------------------------------------------
=>It is the block, in which we write block of statements will relinquish (release / close / give-up/clean-up) the resources ( Files, Database softwares) which are obtained in try block and finally block is called Resouces  relinquishing Block.
=>finally block will execute compulsorily.
=>finally block is optional to write
=>The place of writing finally block is that after else block ( if else block present)
==================================x==========================================================
