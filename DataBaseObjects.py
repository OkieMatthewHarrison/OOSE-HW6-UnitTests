'''
Matthew Harrison
April 26 2025

This file contains the Classes for objects that are in my ERD/ database
'''
class Document:
    def __init__(self, documentID, accountNumber, docName, docType, docCreationDate):
        self.documentID = documentID
        self.accountNumber = accountNumber
        self.docName = docName
        self.docType = docType
        self.docCreationDate = docCreationDate

class Account:
    def __init__(self, acountNumber, userID, acountType, balance, deliveryFrequency, deliveryPreference, customerName):
        self.acountNumber = acountNumber
        self.userID = userID
        self.acountType = acountType
        self.balance = balance
        self.deliveryFrequency = deliveryFrequency
        self.deliveryPreference = deliveryPreference
        self.customerName = customerName

class User:
    def __init__(self, userID, userName, password, last4SSN, customerName):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.last4SSN = last4SSN
        self.customerName = customerName

class UserEngagement:
    def __init__(self, userID, adminID, loginFrequency, favoriteDocumentType, optedIntoPaperless):
        self.userID = userID
        self.adminID = adminID
        self.loginFrequency = loginFrequency
        self.favoriteDocumentType = favoriteDocumentType
        self.optedIntoPaperless = optedIntoPaperless

class Admin:
    def __init__(self, adminID, userName, password, role):
        self.adminID = adminID
        self.userName = userName
        self.password = password
        self.role = role

class Log:
    def __init__(self, logID, userEngagementID, createdAt, actionType, description):
        self.logID = logID
        self.userEngagementID = userEngagementID
        self.createdAt = createdAt
        self.actionType = actionType
        self.description = description