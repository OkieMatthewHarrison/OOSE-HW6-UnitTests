'''
Matthew Harrison
April 26 2025

This file contains the Classes for objects that are in my ERD/ database
'''
class Document:
    def __init__(self, documentID, accountNumber, documentType, docName, docCreationDate, creationDate):
        self.documentID = documentID
        self.accountNumber = accountNumber
        self.documentType = documentType
        self.docName = docName
        self.docCreationDate = docCreationDate
        self.creationDate = creationDate

class Account:
    def __init__(self, accountNumber, userID, accountType, balance, deliveryFrequency, deliveryPreference, customerName, creationDate):
        self.accountNumber = accountNumber
        self.userID = userID
        self.accountType = accountType
        self.balance = balance
        self.deliveryFrequency = deliveryFrequency
        self.deliveryPreference = deliveryPreference
        self.customerName = customerName
        self.creationDate = creationDate

class User:
    def __init__(self, userID, userName, password, last4SSN, cusomerName, role, optedIntoPaperless, birthdate):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.last4SSN = last4SSN
        self.cusomerName = cusomerName
        self.role = role
        self.optedIntoPaperless = optedIntoPaperless
        self.birthdate = birthdate

class Log:
    def __init__(self, logID, accountNumber, documentID, createdAt, actionType, description, creationDate):
        self.logID = logID
        self.accountNumber = accountNumber
        self.documentID = documentID
        self.createdAt = createdAt
        self.actionType = actionType
        self.description = description
        self.creationDate = creationDate

        
class ProfileDetails:
    def __init__(self, profileDetailsID, userID, favoriteDocumentType, loginFrequency):
        self.profileDetailsID = profileDetailsID
        self.userID = userID
        self.favoriteDocumentType = favoriteDocumentType
        self.loginFrequency = loginFrequency
