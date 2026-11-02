import allure
from playwright.sync_api import expect


@allure.feature("Todo UI")
@allure.story("Add a todo")
def test_user_can_add_a_todo(page):
    """Verify that a user can add a todo item to the demo application."""
    with allure.step("Open the TodoMVC demo"):
        page.goto("https://demo.playwright.dev/todomvc/")
        todo_title = "Prepare for automation interview"

    with allure.step("Enter a new todo and submit it"):
        todo_input = page.get_by_placeholder("What needs to be done?")
        todo_input.fill(todo_title)
        todo_input.press("Enter")

    with allure.step("Verify the todo is displayed"):
        todo_item = page.get_by_test_id("todo-title").filter(has_text=todo_title)
        expect(todo_item).to_be_visible()


    #Failure:  
    #with allure.step("Verify the todo is displayed"):
        #todo_item = page.get_by_test_id("todo-title").filter(has_text=todo_title)

    # INTENTIONAL FAILURE for practice
    #expect(todo_item).to_have_text("This is the wrong text")





