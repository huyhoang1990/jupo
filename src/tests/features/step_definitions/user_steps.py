#! coding: utf-8
# pylint: disable-msg=W0311, W0611, E1103, E1101
#@PydevCodeAnalysisIgnore
import web_steps
from lettuce import *
from urls import url_for


@step('a user named "(.*?)" with email "(.*?)" and password "(.*?)"')
def sign_up(step, name, email, password):
  user = {'name': name,
          'email': email,
          'password': password}
  
  step.behave_as("""
  Given I go to the sign up page
    And I fill in "name" with "%(name)s"
    And I fill in "email" with "%(email)s"
    And I fill in "password" with "%(password)s"
    And I press ENTER key
   Then I log out
  """ % user)
  


@step("(?:I am|I'm) logged in as \"(.*?)\" (email: \"(.*?)\", password: \"(.*?)\")")
def user_logged_in(step, name, email, password):
  user = {'name': name,
          'email': email,
          'password': password}
  
  step.behave_as("""
  Given a user named "%(name)s" with email "%(email)s" and password: "%(password)s"
    And I click "Sign in"
    And I fill in "email" with "%(email)s"
    And I fill in "password" with "%(password)s"
    And I press ENTER key
  """ % user)


@step('user "(.*?)" (email: "(.*?)", password: "(.*?)") exists')
def user_exists(step, name, email, password):
  user = {'name': name,
          'email': email,
          'password': password}
  
  step.behave_as("""
   When I go to the sign up page
    And I fill in "name" with "%(name)s"
    And I fill in "email" with "%(email)s"
    And I fill in "password" with "%(password)s"
    And I press ENTER key
    And I should see "%(email)s"
    And I should see "already in use"
  """ % user)

@step('user "(.*?)" (email: "(.*?)", password: "(.*?)") exists and is logged in')
def user_exists_and_is_logged_in(step, name, email, password):
  user = {'name': name,
          'email': email,
          'password': password}
  step.behave_as("""
  Given a user named "%(name)s" with email "%(email)s" and password: "%(password)s"
    And I fill in "name" with "%(name)s"
    And I fill in "email" with "%(email)s"
    And I fill in "password" with "%(password)s"
    And I press ENTER key
  """ % user)
      
      


@step('I log out')
def log_out(step):
  step.given('I click on "header nav a.user.dropdown-menu"')
  step.given('I click "Sign out"')

