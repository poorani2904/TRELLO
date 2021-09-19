from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from Features.Pages.Trellopage import TrelloPageLocators

@given('launch chrome browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")
    context.driver.maximize_window()

@when('open Trello URL')
def OpenTrelloURL(context):
    context.driver.get(TrelloPageLocators.Trello_URL)
    print("Trello is launched successfully")

@then('Login into Trello')
def Login(context):
    context.driver.find_element_by_xpath(TrelloPageLocators.Login_Link).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.Username_Textbox).send_keys(TrelloPageLocators.Login_Username)
    context.driver.find_element_by_xpath(TrelloPageLocators.Login_Atlassian_Button).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.Password_Textbox).send_keys(TrelloPageLocators.Login_Password)
    context.driver.find_element_by_xpath(TrelloPageLocators.Login_Button).click()
    context.driver.implicitly_wait(5)
    print("Login into Trello is successfull")

@then('Create a new board')
def CreateBoard(context):
    context.driver.find_element_by_xpath(TrelloPageLocators.Create_Board_Tile).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.BoardTitle_Textbox).send_keys(TrelloPageLocators.BoardName)
    context.driver.find_element_by_xpath(TrelloPageLocators.CreateBoard_Submit_Button).click()
    print("New Board is created successfully")

@then('Create four Lists as Not Started, In Progress, QA, Done')
def CreateLists(context):
    context.driver.find_element_by_xpath(TrelloPageLocators.ListName_Textbox).send_keys(TrelloPageLocators.List1_Name)
    context.driver.find_element_by_xpath(TrelloPageLocators.Add_List).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.ListName_Textbox).send_keys(TrelloPageLocators.List2_Name)
    context.driver.find_element_by_xpath(TrelloPageLocators.Add_List).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.List_Textbox_Input).send_keys(TrelloPageLocators.List3_Name)
    context.driver.find_element_by_xpath(TrelloPageLocators.Add_List).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.List_Textbox_Input).send_keys(TrelloPageLocators.List4_Name)
    context.driver.find_element_by_xpath(TrelloPageLocators.Add_List).click()
    print("Four lists - Lists as Not Started, In Progress, QA, Done are created")

@then('Create four Cards.Card 1, Card 2, Card 3, Card 4 under the list Not Started')
def CreateCards(context):
    context.driver.find_element_by_xpath(TrelloPageLocators.Add_Card_NotStarted).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.CardTitle_Textbox_Input).send_keys(TrelloPageLocators.Card1_Name)
    context.driver.find_element_by_xpath(TrelloPageLocators.Add_Card).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.CardTitle_Textbox_Input).send_keys(TrelloPageLocators.Card2_Name)
    context.driver.find_element_by_xpath(TrelloPageLocators.Add_Card).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.CardTitle_Textbox_Input).send_keys(TrelloPageLocators.Card3_Name)
    context.driver.find_element_by_xpath(TrelloPageLocators.Add_Card).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.CardTitle_Textbox_Input).send_keys(TrelloPageLocators.Card4_Name)
    context.driver.find_element_by_xpath(TrelloPageLocators.Add_Card).click()
    print("Four Cards - Card 1, Card 2, Card 3, Card 4 under the list Not Started are created")

@then('Move Card 2 to In Progress')
def MoveCard2ToInProgress(context):
    EditIcon2 = context.driver.find_element_by_xpath(TrelloPageLocators.EditIcon_Card2)
    ActionChains(context.driver).move_to_element(EditIcon2).click(EditIcon2).perform()
    context.driver.find_element_by_xpath(TrelloPageLocators.Movelink).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.Inprogress_Dropdown).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.Move_Button).click()
    print("Card 2 is moved to In Progress")

@then('Move Card 3 to QA')
def MoveCard3ToQA(context):
    EditIcon3 = context.driver.find_element_by_xpath(TrelloPageLocators.EditIcon_Card3)
    ActionChains(context.driver).move_to_element(EditIcon3).click(EditIcon3).perform()
    context.driver.find_element_by_xpath(TrelloPageLocators.Movelink).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.QA_Dropdown).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.Move_Button).click()
    print("Card 3 is moved to QA")

@then('Move Card 2 under QA')
def MoveCard2ToQA(context):
    EditIcon = context.driver.find_element_by_xpath(TrelloPageLocators.EditIcon_Card2)
    ActionChains(context.driver).move_to_element(EditIcon).click(EditIcon).perform()
    context.driver.find_element_by_xpath(TrelloPageLocators.Movelink).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.QA_Dropdown).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.Move_Button).click()
    print("Card 2 is moved to QA")

@then('Open Card 1 and Assign it to the current logged in user and then leave a comment on Card 1 saying “I am done”')
def OpenCard1(context):
    context.driver.find_element_by_xpath(TrelloPageLocators.Card1).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.CardMembers_Link).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.CurrentMember).click()
    context.driver.find_element_by_xpath(TrelloPageLocators.Comment_Textbox).send_keys(TrelloPageLocators.CommentText)
    context.driver.find_element_by_xpath(TrelloPageLocators.Save_Button).click()
    print("Card 1 is opened and assigned it to the current logged in user and provided a comment on Card 1 saying I am done")

@then('close the chrome browser')
def CloseBrowser(context):
    context.driver.close()











