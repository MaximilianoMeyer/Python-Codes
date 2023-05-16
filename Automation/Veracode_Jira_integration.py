#for this code your need veracode-api-py
#https://github.com/veracode/veracode-api-py
#configure your api_key app_secret in veracode and Jira.
#for veracode, just follow the indications in the veracode-api-py repo
import sys
import argparse
import logging
import datetime
import os
import json
from uuid import UUID
import anticrlf
from jira import JIRA
from time import sleep

from veracode_api_py import VeracodeAPI as vapi, Applications, Findings


def prompt_for_app(prompt_text):
    appguid = ""
    app_candidates = vapi().get_app_by_name(prompt_text)
    if len(app_candidates) == 0:
        print("No matches were found!")
    else:
        appguid = app_candidates[0].get('guid')
        #appname = app_candidates[0].get('profile')['name']
        #print(appname)
    return appguid


def get_findings(guid, rparameters):
    findings = vapi().get_findings(guid, rparameters)
    return findings



def list_all_apps():
    app_list = vapi().get_apps()
    for app in app_list:
        print(app['profile']['name'])

#list_all_apps()
#list_applications.append(list_all_apps())
#print(list_applications)


jiraOptions = {'server': 'https://yourName-projects.atlassian.net'}
jira = JIRA(options=jiraOptions, basic_auth=('email_of_your_account', 'your_token'))


Apps = ["create_list_of_your_apps_in_veracode"]

Link_Veracode = 'veracode_link'

# get informations of your app list
for app in Apps:
    #print(app)
    appguid = prompt_for_app(app)
    app_candidates = vapi().get_app_by_name(app)
    appname = app_candidates[0].get('profile')['name']
    #print(appname)
    flaws = get_findings(appguid, f"violates_policy=true")
    #print(f"Violates Policy for {appname}:", flaws)
    for finding in flaws:
        details = finding['finding_details']
        #print(details)
        severity = details['severity']
        #print(severity)
        cwe = details['cwe']
        #print(cwe)
        cwe_link = cwe['href']
        cwe_name = cwe['name']
        cwe_id = cwe['id']
        #print(cwe_id, cwe_name)
        #print(cwe_link)
        file_path = details['file_path']
        file_name = details['file_name']
        category = details['finding_category']['name']
        exploitability = details['exploitability']
        vector = details['attack_vector']
        module = details['module']
        file_line_number = details['file_line_number']
        #print(file_line_number)
        #print(module)

    summary = appname

    last_severity = None

    if severity == 0 and last_severity != 0:
        summary = appname
        description = f"Severidade: Informativo\nCWE: {cwe_id} {cwe_name}\nModulo: {module}\nCaminho do arquivo: {file_path}\nNome do arquivo: {file_name}\nCategoria: {category}\nExploitabilidade: {exploitability}\nVetor de ataque: {vector}\nLink da vulnerabilidade no veracode: {cwe_link}\nLinha de código da falha: {file_line_number}\nLink de acesso ao veracode: {Link_Veracode}"

        issue_dict = {
            'project': {'key': 'TV'},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Erro'},
        }
        new_issue = jira.create_issue(fields=issue_dict)
        last_severity = 0



    if severity == 1 and last_severity != 1:
        summary = appname
        description = f"Severidade: Muito Baixa\nCWE: {cwe_id} {cwe_name}\nModulo: {module}\nCaminho do arquivo: {file_path}\nNome do arquivo: {file_name}\nCategoria: {category}\nExploitabilidade: {exploitability}\nVetor de ataque: {vector}\nLink da vulnerabilidade no veracode: {cwe_link}\nLinha de código da falha: {file_line_number}\nLink de acesso ao veracode: {Link_Veracode}"

        issue_dict = {
            'project': {'key': 'TV'},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Erro'},
        }
        new_issue = jira.create_issue(fields=issue_dict)
        last_severity = 1



    if severity == 2 and last_severity != 2:
        summary = appname
        description = f"Severidade: Baixa\nCWE: {cwe_id} {cwe_name}\nModulo: {module}\nCaminho do arquivo: {file_path}\nNome do arquivo: {file_name}\nCategoria: {category}\nExploitabilidade: {exploitability}\nVetor de ataque: {vector}\nLink da vulnerabilidade no veracode: {cwe_link}\nLinha de código da falha: {file_line_number}\nLink de acesso ao veracode: {Link_Veracode}"

        issue_dict = {
            'project': {'key': 'TV'},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Erro'},
        }
        new_issue = jira.create_issue(fields=issue_dict)
        last_severity = 2


    if severity == 3 and last_severity != 3:
        summary = appname
        description = f"Severidade: Baixa\nCWE: {cwe_id} {cwe_name}\nModulo: {module}\nCaminho do arquivo: {file_path}\nNome do arquivo: {file_name}\nCategoria: {category}\nExploitabilidade: {exploitability}\nVetor de ataque: {vector}\nLink da vulnerabilidade no veracode: {cwe_link}\nLinha de código da falha: {file_line_number}\nLink de acesso ao veracode: {Link_Veracode}"

        issue_dict = {
            'project': {'key': 'TV'},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Erro'},
        }
        new_issue = jira.create_issue(fields=issue_dict)
        last_severity = 3


    if severity == 4 and last_severity != 4:
        summary = appname
        description = f"Severidade: Alta\nCWE: {cwe_id} {cwe_name}\nModulo: {module}\nCaminho do arquivo: {file_path}\nNome do arquivo: {file_name}\nCategoria: {category}\nExploitabilidade: {exploitability}\nVetor de ataque: {vector}\nLink da vulnerabilidade no veracode: {cwe_link}\nLinha de código da falha: {file_line_number}\nLink de acesso ao veracode: {Link_Veracode}"

        issue_dict = {
            'project': {'key': 'TV'},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Erro'},
        }
        new_issue = jira.create_issue(fields=issue_dict)
        last_severity = 4


    if severity == 5 and last_severity != 5:
        summary = appname
        description = f"Severidade: Muito Alta\nCWE: {cwe_id} {cwe_name}\nModulo: {module}\nCaminho do arquivo: {file_path}\nNome do arquivo: {file_name}\nCategoria: {category}\nExploitabilidade: {exploitability}\nVetor de ataque: {vector}\nLink da vulnerabilidade no veracode: {cwe_link}\nLinha de código da falha: {file_line_number}\nLink de acesso ao veracode: {Link_Veracode}"

        issue_dict = {
            'project': {'key': 'TV'},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Erro'},
        }
        new_issue = jira.create_issue(fields=issue_dict)
        last_severity = 5
