'''
Matthew Harrison
April 26 2025
'''
from datetime import datetime
from DataBaseObjects import *

from datetime import datetime
from unittest.mock import Mock

# Test for Account
def test_account_constructor_sets_fields_correctly():
    account = Account(
        accountNumber=1001,
        userID=1,
        accountType="Checking",
        balance=5358.32,
        deliveryFrequency=1,
        deliveryPreference="Paperless",
        customerName="John Doe",
        creationDate=datetime(2022, 1, 1)
    )

    assert account.accountNumber == 1001
    assert account.userID == 1
    assert account.accountType == "Checking"
    assert account.balance == 5358.32
    assert account.deliveryFrequency == 1
    assert account.deliveryPreference == "Paperless"
    assert account.customerName == "John Doe"
    assert isinstance(account.balance, float)
    assert (account.balance * 100).is_integer() #check to make sure there aren't any cents in the thousands place
    assert account.creationDate == datetime(2022, 1, 1)

def test_user_constructor_sets_fields_correctly():
    user = User(
        userID=1,
        userName="mock_user",
        password="mock_password",
        last4SSN=1234,
        cusomerName="John Doe",
        role="Customer",
        optedIntoPaperless=True,
        birthdate=datetime(1995, 5, 15)
    )

    assert user.userID == 1
    assert user.userName == "mock_user"
    assert user.password == "mock_password"
    assert user.last4SSN == 1234
    assert user.cusomerName == "John Doe"
    assert user.role == "Customer"
    assert user.optedIntoPaperless is True
    assert user.birthdate == datetime(1995, 5, 15)

# Test for Document
def test_document_constructor_sets_fields_correctly():
    document = Document(
        documentID=501,
        accountNumber=1001,
        documentType="Statement",
        docName="January Statement",
        docCreationDate=datetime(2022, 1, 2),
        creationDate=datetime(2022, 1, 3)
    )

    assert document.documentID == 501
    assert document.accountNumber == 1001
    assert document.documentType == "Statement"
    assert document.docName == "January Statement"
    
    assert document.docCreationDate == datetime(2022, 1, 2)
    assert not (document.docCreationDate > datetime.now()) #document.docCreationDate is not in the future
    assert document.docCreationDate > datetime(1920, 1, 1) #document.docCreationDate is not created before computers
    assert isinstance(document.docCreationDate, datetime)
    
    assert document.creationDate == datetime(2022, 1, 3)
    assert not (document.creationDate > datetime.now()) #document.creationDate is not in the future
    assert document.creationDate > datetime(1920, 1, 1) #document.creationDate is not created before computers
    assert isinstance(document.creationDate, datetime)

def test_profile_details_constructor_sets_fields_correctly():
    profile = ProfileDetails(
        profileDetailsID=200,
        userID=1,
        favoriteDocumentType="Statement",
        loginFrequency=15
    )

    assert profile.profileDetailsID == 200
    assert profile.userID == 1
    assert profile.favoriteDocumentType == "Statement"
    assert profile.loginFrequency == 15


def test_log_constructor_sets_fields_correctly():
    log = Log(
        logID=300,
        accountNumber=1001,
        documentID=500,
        createdAt=datetime(2024, 4, 25, 12, 0),
        actionType=1,
        description="User downloaded statement",
        creationDate=datetime(2024, 4, 25, 12, 1)
    )

    assert log.logID == 300
    assert log.accountNumber == 1001
    assert log.documentID == 500
    assert log.createdAt == datetime(2024, 4, 25, 12, 0)
    assert log.actionType == 1
    assert log.description == "User downloaded statement"
    assert log.creationDate == datetime(2024, 4, 25, 12, 1)
    assert not (log.createdAt > datetime.now()) #log.createAt is not in the future
    assert log.createdAt > datetime(1920, 1, 1) #log.createAt is not created before computers
    assert isinstance(log.createdAt, datetime)
    


# Unit Tests with mocks
def test_account_mock():
    mock_account = Mock()
    mock_account.accountNumber = 1001
    mock_account.userID = 1
    mock_account.accountType = "Checking"
    mock_account.balance = 2500
    mock_account.deliveryFrequency = 2
    mock_account.deliveryPreference = "Paperless"
    mock_account.customerName = "Jane Doe"
    mock_account.creationDate = datetime(2022, 1, 1)

    assert mock_account.accountNumber == 1001
    assert mock_account.userID == 1
    assert mock_account.accountType == "Checking"
    assert mock_account.balance == 2500
    assert mock_account.deliveryFrequency == 2
    assert mock_account.deliveryPreference == "Paperless"
    assert mock_account.customerName == "Jane Doe"
    assert mock_account.creationDate == datetime(2022, 1, 1)
    
def test_user_mock():
    mock_user = Mock()
    mock_user.userID = 1
    mock_user.userName = "mocked_user"
    mock_user.password = "mocked_password"
    mock_user.last4SSN = 1234
    mock_user.cusomerName = "John Doe"
    mock_user.role = "Customer"
    mock_user.optedIntoPaperless = True
    mock_user.birthdate = datetime(1995, 5, 15)

    assert mock_user.userID == 1
    assert mock_user.userName == "mocked_user"
    assert mock_user.password == "mocked_password"
    assert mock_user.last4SSN == 1234
    assert mock_user.cusomerName == "John Doe"
    assert mock_user.role == "Customer"
    assert mock_user.optedIntoPaperless is True
    assert mock_user.birthdate == datetime(1995, 5, 15)