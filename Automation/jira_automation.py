from selenium import webdriver
import jira.client

class JiraAutomation:
    def _init_(self, host, username, password):
        self.jira = jira.client.JIRA(options={'server': host}, basic_auth=(username, password))

    def create_card(self, summary, description, priority):
        new_issue = {
            'project': {'key': 'PROJECT_KEY'},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Task'},
            'priority': {'name': priority}
        }
        return self.jira.create_issue(fields=new_issue)

    def delete_card(self, card_id):
        self.jira.delete_issue(card_id)

    def prioritize_cards(self, priority):
        cards = self.jira.search_issues('priority=' + priority)
        return [card.key for card in cards]

if _name_ == '_main_':
    jira_automation = JiraAutomation(host='https://jira.example.com',
                                     username='user',
                                     password='password')
    new_card = jira_automation.create_card(summary='Card summary',
                                            description='Card description',
                                            priority='High')
    jira_automation.delete_card(new_card.key)
    high_priority_cards = jira_automation.prioritize_cards('High')
    print(high_priority_cards)
