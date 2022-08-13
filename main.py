from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import requests
import json

driver = webdriver.Chrome()
driver.get("https://0831474b.index-education.net/pronote/eleve.html")

sleep(5)

user = driver.find_element(By.XPATH, "//input[@id='id_22']")
user.clear()
user.send_keys("LSOIGNEUX")

password = driver.find_element(By.XPATH, "//input[@id='id_23']")
password.clear()
password.send_keys("Lelmc2K7")

connect = driver.find_element(By.XPATH, "//button[@id='id_11']")
connect.click()

sleep(10)

driver.execute_script('GInterface.Instances[2]._surToutVoir(7)')

sleep(4)

descriptifs = driver.find_elements(By.XPATH, "//*[@id='GInterface.Instances[2].Instances[2].Instances[0]']/div/ul/*/ul/li/div/div[3]/div[1]")

for descriptif in descriptifs:
    el = descriptif.find_element(By.XPATH, '../../div[1]/div[2]/div/div')
    
    task = "Not started"

    if el.text == "Non Fait":
        with open("components.json", "r") as f:
            matiere = json.loads(f.read())
        
        name = matiere[descriptif.find_element(By.XPATH, '../../../div[1]/div[1]/div[1]/div[1]').text]
        text = descriptif.text
        if len(text.split(' ')) <= 5:
            update = ' '.join(text.split(' ')[:5])
        else:
            update = ' '.join(text.split(' ')[:5]) + "..."

        try:
            data = {
                "parent": { "database_id": "796b3c8ad45e44a4812c424b34818566" },
                "properties": {
                    "Name": {
                        "title": [
                            {
                                "text": {
                                        "content": update
                                }
                            }
                        ]
                    },
                    "Status": {
                        "select": {
                            "name": task
                        }
                    },
                    "Matière": {
                        "select": {
                            "name": name[0]
                        }
                    }
                },
                "icon": {
                    "type": "emoji",
                        "emoji": name[3]
                },
                "cover": {
                    "type": "external",
                    "external": {
                        "url": name[1]
                    }
                },
                "children": [
                    {
                        "object": "block",
                        "type": "image",
                        "image": {
                            "type": "external",
                            "external": {
                                "url": name[2]
                            }
                        },
                    },
                    {
                        "object": "block",
                        "type": "heading_2",
                        "heading_2": {
                            "text": [
                                {
                                    "type": "text",
                                    "text": {
                                            "content": "Notes:"
                                    },
                                    "annotations": {
                                        "color": "gray"
                                    },
                                }
                            ]
                        }
                    },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "text": [
                                {
                                    "type": "text",
                                    "text": {
                                            "content": descriptif.text
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "text": [
                                {
                                    "type": "text",
                                    "text": {
                                            "content": "Pronote Document: {}".format(el.find_element(By.XPATH, '../div[2]/span[1]/a[1]/div[1]').text)
                                    },
                                    "annotations": {
                                        "color": "gray"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        except:
            data = {
                "parent": { "database_id": "796b3c8ad45e44a4812c424b34818566" },
                "properties": {
                    "Name": {
                            "title": [
                                    {
                                            "text": {
                                                    "content": update
                                            }
                                    }
                            ]
                    },
                    "Status": {
                        "select": {
                            "name": task
                        }
                    },
                    "Matière": {
                        "select": {
                            "name": name[0]
                        }
                    }
                },
                "icon": {
                    "type": "emoji",
                        "emoji": name[3]
                },
                "cover": {
                    "type": "external",
                    "external": {
                        "url": name[1]
                    }
                },
                "children": [
                    {
                        "object": "block",
                        "type": "image",
                        "image": {
                            "type": "external",
                            "external": {
                                "url": name[2]
                            }
                        },
                    },
                    {
                        "object": "block",
                        "type": "heading_2",
                        "heading_2": {
                            "text": [
                                {
                                    "type": "text",
                                    "text": {
                                            "content": "Notes:"
                                    },
                                    "annotations": {
                                        "color": "gray"
                                    },
                                }
                            ]
                        }
                    },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "text": [
                                {
                                    "type": "text",
                                    "text": {
                                            "content": descriptif.text
                                    }
                                }
                            ]
                        }
                    }
                ]
            }

        header = {
            'Authorization': 'Bearer secret_iejmaFYFqDKLyYWJRDSzOCnHzMjmImukaWhOA1IEOHL',
            'Content-Type': 'application/json',
            "Notion-Version": "2021-08-16"
        }

        response = requests.post("https://api.notion.com/v1/pages", data=json.dumps(data), headers=header)

driver.close()