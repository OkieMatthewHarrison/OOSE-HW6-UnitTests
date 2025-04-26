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
        acountNumber=1001,
        userID=1,
        acountType="Checking",
        balance=5358.32,
        deliveryFrequency=1,
        deliveryPreference="Paperless",
        customerName="John Doe"
    )

    assert account.acountNumber == 1001
    assert account.userID == 1
    assert account.acountType == "Checking"
    assert account.balance == 5358.32
    assert account.deliveryFrequency == 1
    assert account.deliveryPreference == "Paperless"
    assert account.customerName == "John Doe"
    assert isinstance(account.balance, float)
    assert (account.balance * 100).is_integer() #check to make sure there aren't any cents in the thousands place


# Test for UserEngagement
def test_user_engagement_constructor_sets_fields_correctly():
    engagement = UserEngagement(
        userID=1,
        adminID=1,
        loginFrequency=5,
        favoriteDocumentType="Statement",
        optedIntoPaperless=True
    )

    assert engagement.userID == 1
    assert engagement.adminID == 1
    assert engagement.loginFrequency == 5
    assert engagement.favoriteDocumentType == "Statement"
    assert engagement.optedIntoPaperless is True
    assert not isinstance(engagement.favoriteDocumentType, int)
    

# Test for Admin
def test_admin_constructor_sets_fields_correctly():
    admin = Admin(
        adminID=1,
        userName="admin_user",
        password="securepass",
        role="SuperAdmin"
    )

    assert admin.adminID == 1
    assert admin.userName == "admin_user"
    assert admin.password == "securepass"
    assert admin.role == "SuperAdmin"

# Test for Document
def test_document_constructor_sets_fields_correctly():
    creation_date = datetime(2025, 1, 1)
    document = Document(
        documentID=501,
        accountNumber=1001,
        docType="Statement",
        docName="January Statement",
        docCreationDate=creation_date
    )

    assert document.documentID == 501
    assert document.accountNumber == 1001
    assert document.docType == "Statement"
    assert document.docName == "January Statement"
    assert document.docCreationDate == creation_date
    assert not (document.docCreationDate > datetime.now()) #document.docCreationDate is not in the future
    assert document.docCreationDate > datetime(1920, 1, 1) #document.docCreationDate is not created before computers
    assert isinstance(document.docCreationDate, datetime)


def test_log_constructor_sets_fields_correctly():
    created_time = datetime(2024, 5, 1, 12, 0, 0)
    log = Log(
        logID=1,
        userEngagementID=100,
        createdAt=created_time,
        actionType=2,
        description="User logged in."
    )

    # Assert: Check that fields are set correctly
    assert log.logID == 1
    assert log.userEngagementID == 100
    assert log.createdAt == created_time
    assert log.actionType == 2
    assert log.description == "User logged in."
    assert not (log.createdAt > datetime.now()) #log.createAt is not in the future
    assert log.createdAt > datetime(1920, 1, 1) #log.createAt is not created before computers
    assert isinstance(log.createdAt, datetime)
    
def test_user_engagement_constructor_sets_fields_correctly():
    engagement = UserEngagement(
        userID=1,
        adminID=2,
        loginFrequency=10,
        favoriteDocumentType="Statement",
        optedIntoPaperless=True
    )

    assert engagement.userID == 1
    assert engagement.adminID == 2
    assert engagement.loginFrequency == 10
    assert engagement.favoriteDocumentType == "Statement"
    assert engagement.optedIntoPaperless is True



# Unit Tests with mocks
def test_account_mock():
    mock_account = Mock()
    mock_account.acountNumber = 1001
    mock_account.userID = 1
    mock_account.acountType = "Savings"
    mock_account.balance = 2500
    mock_account.deliveryFrequency = 2
    mock_account.deliveryPreference = "Paperless"
    mock_account.customerName = "Jane Doe"

    assert mock_account.acountNumber == 1001
    assert mock_account.userID == 1
    assert mock_account.acountType == "Savings"
    assert mock_account.balance == 2500
    assert mock_account.deliveryFrequency == 2
    assert mock_account.deliveryPreference == "Paperless"
    assert mock_account.customerName == "Jane Doe"


def test_user_mock():
    mock_user = Mock()
    mock_user.userID = 1
    mock_user.userName = "mocked_user"
    mock_user.password = "mocked_password"
    mock_user.last4SSN = 1234
    mock_user.customerName = "John Doe"

    assert mock_user.userID == 1
    assert mock_user.userName == "mocked_user"
    assert mock_user.password == "mocked_password"
    assert mock_user.last4SSN == 1234
    assert mock_user.customerName == "John Doe"